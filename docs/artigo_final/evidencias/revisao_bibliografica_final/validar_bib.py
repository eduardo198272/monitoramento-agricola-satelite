"""Inventário e verificações desta rodada, sem alterar texto científico."""
from pathlib import Path
import difflib, hashlib, json, re, shutil
import pymupdf
from pybtex.database import parse_file
from auditar_bib import BASE, ROOT, CACHE, OUT, dump

OUT.mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
build=CACHE/"build_entrega"
before=json.loads((CACHE/"baseline.json").read_text())
data=parse_file(BASE/"referencias_normalizadas.bib")
old=parse_file(CACHE/"antes_referencias_normalizadas.bib")
manifest=json.loads((ROOT/"docs/envio_professor/projeto_latex/MANIFESTO_SHA256.json").read_text())
usage={}
for name in manifest:
    if not name.endswith(".tex"): continue
    text=(BASE/name).read_text()
    for m in re.finditer(r"\\(?:cite[a-zA-Z]*|fonteTCC)\*?(?:\[[^\]]*\]){0,2}\{([^{}]+)\}",text):
        # fonteTCC containing prose does not produce bibliography keys.
        for key in m[1].split(","):
            key=key.strip()
            if key in data.entries:
                usage.setdefault(key,[]).append({"arquivo":name,"linha":text[:m.start()].count("\n")+1})

aux=(build/"Relatorio_Final.aux").read_text()
bbl=(build/"Relatorio_Final.bbl").read_text()
blg=(build/"Relatorio_Final.blg").read_text()
log=(build/"Relatorio_Final.log").read_text()
cited=set(k for s in re.findall(r"\\citation\{([^}]+)\}",aux) for k in s.split(","))
published=re.findall(r"\\harvarditem(?:\[[^\]]*\])?\{[^\n]*",bbl)
bibkeys=re.findall(r"\\bibcite\{([^}]+)\}",aux)
assert len(data.entries)==63 and len(cited)==54 and set(usage)==cited
assert len(bibkeys)==54 and len(set(bibkeys))==54 and set(bibkeys)==cited
assert "\\bibstyle{dcu}" in aux
assert not re.search(r"undefined|Overfull|^! ",log,re.M)
assert "Warning--" not in blg
doi=[data.entries[k].fields["doi"].lower() for k in cited if data.entries[k].fields.get("doi")]
assert len(doi)==len(set(doi))
changed=[]
entries=[]
records=[]
for name in ["consultas.json","complementares.json","adicionais.json"]:
    records+=json.loads((CACHE/name).read_text())
# Receipts omit affiliations and other irrelevant personal metadata.
for r in records:
    for a in r.get("metadata",{}).get("author",[]):
        for field in list(a):
            if field not in ["given","family","sequence"]: del a[field]
dump(OUT/"consultas.json",records)
by_id={r["id"]:r for r in records}
overrides={"EOSDA_GUIDE":"EOSDA_especifico","UPF_IA2026":"UPF_direto",
           "QGIS_VECTOR":"QGIS_3.44_vector_data","QGIS_RASTER":"QGIS_3.44_raster_data",
           "QGIS_MAP":"QGIS_3.44_map_production"}
for key,e in data.entries.items():
    delta={k:{"antes":old.entries[key].fields.get(k),"depois":e.fields.get(k)}
           for k in set(e.fields)|set(old.entries[key].fields)
           if e.fields.get(k)!=old.entries[key].fields.get(k)}
    if delta: changed.append(key)
    entries.append({"chave":key,"citada":key in cited,"tipo":e.type,
                    "autores_ordenados":[str(x) for x in e.persons.get("author",[])],
                    "editores_ordenados":[str(x) for x in e.persons.get("editor",[])],
                    "campos":dict(e.fields),"citacoes":usage.get(key,[]),
                    "consulta_url":by_id.get(overrides.get(key,key)),
                    "consulta_crossref":by_id.get("crossref_"+key),
                    "consulta_doi_adicional":by_id.get("doi_"+key),
                    "alteracoes":delta})
assert set(changed)=={"EOSDA_GUIDE","UPF_IA2026","NASA_POWER_PARAMETERS",
                     "BIPM_SI","QGIS_VECTOR","QGIS_RASTER","QGIS_MAP","ROUSE1974_NTRS"}
dump(OUT/"referencias.json",entries)
dump(OUT/"baseline_sha256.json",before)
shutil.copy2(CACHE/"status_antes.txt",OUT/"status_antes.txt")

quotes={
    "BIPM_citacao":["Citation","Published in May 2019","4.01"],
    "EOSDA_especifico":["When you hover the cursor","Upload fields","Account And Pricing"],
    "NASA_manager":["Manager microservice API","only response format"],
    "QGIS_roadmap":["Currently available binaries","Long Term Release"],
    "QGIS_3.44_vector_data":["Vector data provide","enclosed polygon feature"],
    "QGIS_3.44_raster_data":["Rasters are made up"],
    "QGIS_3.44_map_production":["legend relates map symbols","a map legend is used"],
    "UPF_direto":["INSTRUÇÃO NORMATIVA Nº 03/2026/PROACAD",
                  "Dispõe sobre o uso","Art. 4º","Art. 6º","Art. 8º","Passo Fundo, 28 de outubro de 2026."],
    "GOTEL_pdf":["Orlena","Anthony"],
}
excerpts={}
for key,terms in quotes.items():
    text=(CACHE/(key+".txt")).read_text()
    # UPF excerpts explicitly exclude signature and personal identifier.
    rows=[]
    for term in terms:
        m=re.search(re.escape(term),text,re.I)
        if m:
            excerpt=text[m.start():m.start()+450]
            if key=="UPF_direto" and term.startswith("Passo Fundo"): excerpt=term
            rows.append(excerpt)
    excerpts[key]={"url":by_id[key]["url"],"sha256":by_id[key]["sha256"],"trechos":rows}
params=json.loads((CACHE/"NASA_POWER_PARAMETERS.body").read_text())
point=json.loads((CACHE/"NASA_point.body").read_text())
excerpts["NASA_unidades"]={
    "dicionario":{k:params[k] for k in ["PRECTOTCORR","T2M","ALLSKY_SFC_SW_DWN"]},
    "resposta":point["parameters"],"consulta":by_id["NASA_point"]["url"],
    "time_standard":point["header"]["time_standard"],
    "observacao":"Sondagem documental; não é resultado novo do TCC."}
dump(OUT/"trechos_fontes.json",excerpts)

oldpdf=pymupdf.open(CACHE/"antes_Relatorio_Final.pdf")
newpdf=pymupdf.open(build/"Relatorio_Final.pdf")
assert len(oldpdf)==len(newpdf)==32
text_changes=[]
visual_changes=[]
for i in range(32):
    if oldpdf[i].get_text()!=newpdf[i].get_text(): text_changes.append(i+1)
    if oldpdf[i].get_pixmap().samples!=newpdf[i].get_pixmap().samples: visual_changes.append(i+1)
assert text_changes==visual_changes==[10,30,31,32]
assert oldpdf[9].get_text().replace("2019","2026")==newpdf[9].get_text()
links=[{"pagina":i+1,"uri":l["uri"]} for i,p in enumerate(newpdf)
       for l in p.get_links() if l.get("uri")]
uris={l["uri"] for l in links}
for key in changed:
    assert data.entries[key].fields["url"] in uris,key
assert "https://power.larc.nasa.gov/docs/services/api/system/manager/" in uris
assert not any("\\%" in x for x in uris)
dump(OUT/"hyperlinks.json",links)
for i in [9,29,30,31]:
    newpdf[i].get_pixmap(matrix=pymupdf.Matrix(1.6,1.6)).save(OUT/f"pagina_{i+1:02d}.png")
shutil.copy2(build/"Relatorio_Final.pdf",BASE/"Relatorio_Final.pdf")
for name in ["Relatorio_Final.log","Relatorio_Final.blg","Relatorio_Final.bbl","Relatorio_Final.aux","console.txt"]:
    shutil.copy2(build/name,OUT/name)
shutil.copy2(CACHE/"build/console.txt",OUT/"primeira_tentativa_percentuais.log")
diff="".join(difflib.unified_diff(
    (CACHE/"antes_referencias_normalizadas.bib").read_text().splitlines(True),
    (BASE/"referencias_normalizadas.bib").read_text().splitlines(True),
    fromfile="antes/referencias_normalizadas.bib",tofile="depois/referencias_normalizadas.bib"))
(OUT/"alteracoes_bibliograficas.diff").write_text(diff)
for src in ["auditar_bib.py","complementar_bib.py","fontes_adicionais_bib.py","compilar_bib.py","validar_bib.py"]:
    shutil.copy2(Path("/tmp/opencode")/src,OUT/src)
allowed={
 "docs/artigo_final/referencias_normalizadas.bib",
 "docs/artigo_final/referencias_institucionais.bib",
 "docs/artigo_final/scripts/preparar_bib_dcu.py",
 "docs/artigo_final/Relatorio_Final.pdf",
 "docs/artigo_final/AUDITORIA_ABNT.md",
 "docs/artigo_final/auditoria_cientifica/AUDITORIA_REFERENCIAS.md"}
modified=[name for name,h in before.items() if not (ROOT/name).is_file() or sha(ROOT/name)!=h]
assert set(modified)==allowed,modified
scientific=[name for name in before if name.startswith("docs/artigo_final/") and name.endswith(".tex")]
assert all(sha(ROOT/name)==before[name] for name in scientific)
assert sha(BASE/"CC-EC_TF-TC.cls")==before["docs/artigo_final/CC-EC_TF-TC.cls"]
validation={
    "aprovado_checagens_automaticas":True,"compilador":"Tectonic 0.17.0 (XeTeX), BibTeX/dcu",
    "compilacao_limpa":True,"paginas":32,"entradas_base":63,"citadas":54,"entradas_alteradas":changed,
    "figuras":len(re.findall(r"\\contentsline \{figure\}",aux)),
    "tabelas":len(re.findall(r"\\contentsline \{table\}",aux)),
    "equacoes_com_rotulo_explicito":sorted(set(re.findall(r"\\newlabel\{eq:[^}]*\}\{\{(\d+)\}",aux)),key=int),
    "citações_indefinidas":False,"overfull":False,"avisos_bibtex":False,
    "dois_duplicados_na_lista":False,
    "paginas_texto_modificado":text_changes,"paginas_render_modificado":visual_changes,
    "pagina_10_unica_mudanca_textual":"2019 → 2026, citação BIPM",
    "hyperlinks_corrigidos_conferidos":True,
    "pdf_antes_sha256":sha(CACHE/"antes_Relatorio_Final.pdf"),
    "pdf_depois_sha256":sha(BASE/"Relatorio_Final.pdf"),
    "arquivos_baseline":len(before),"arquivos_baseline_modificados":modified,
    "arquivos_baseline_preservados":len(before)-len(modified),
    "tex_cientificos_preservados":len(scientific),
    "classe_preservada":True,"snapshot_envio_professor_preservado":True,
    "aprovacao_humana":False,"commit_push":False,
    "limitacoes":"Ver AUDITORIA_REFERENCIAS.md; acesso integral/metadados não são certificados por HTTP 200."}
assert validation["figuras"]==22 and validation["tabelas"]==5
# Equations in align without explicit labels also count; source bytes and PDF
# numbering are compared to the preserved baseline rather than inferred here.
validation["expressoes_numeradas_preservadas"]=14
validation["numeros_equacoes_no_pdf"]=sorted({
    int(m) for pg in newpdf for m in re.findall(r"^\((\d+)\)$",pg.get_text(),re.M)})
assert validation["numeros_equacoes_no_pdf"]==list(range(1,15))
dump(OUT/"validacao.json",validation)
print(json.dumps(validation,ensure_ascii=False,indent=2))
