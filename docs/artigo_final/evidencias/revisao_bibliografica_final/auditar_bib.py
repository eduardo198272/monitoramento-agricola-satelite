"""Coleta rastreável; HTTP 200 não equivale a validação bibliográfica."""
from pathlib import Path
import concurrent.futures as cf
import hashlib
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
import requests
from bs4 import BeautifulSoup
from pybtex.database import parse_file

ROOT = Path.cwd()
BASE = ROOT / "docs/artigo_final"
CACHE = Path("/tmp/opencode/auditoria-bibliografica")
OUT = BASE / "evidencias/revisao_bibliografica_final"
CACHE.mkdir(exist_ok=True)

def dump(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")

def snapshot():
    files = subprocess.check_output(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"]
    ).decode().split("\0")
    hashes = {s: hashlib.sha256((ROOT/s).read_bytes()).hexdigest()
              for s in files if s and (ROOT/s).is_file()}
    dump(CACHE/"baseline.json", hashes)
    (CACHE/"status_antes.txt").write_bytes(subprocess.check_output(["git","status","--short"]))
    for name in ["Relatorio_Final.pdf","referencias_normalizadas.bib","referencias_institucionais.bib"]:
        shutil.copy2(BASE/name, CACHE/("antes_"+name))

def fetch(task):
    key, url = task
    record = {"id":key,"url":url,"consulta":datetime.now(timezone.utc).isoformat()}
    try:
        r = requests.get(url, timeout=(15,55), headers={"User-Agent":"TCC-Bibliographic-Audit/1.0"})
        content = r.content
        record.update(http=r.status_code, final_url=r.url,
                      redirects=[{"http":x.status_code,"url":x.url} for x in r.history],
                      content_type=r.headers.get("Content-Type",""),
                      sha256=hashlib.sha256(content).hexdigest(), bytes=len(content))
        (CACHE/(key+".body")).write_bytes(content)
        text = r.text
        if content.startswith(b"%PDF"):
            record["pdf"] = True
            subprocess.run(["pdftotext",str(CACHE/(key+".body")),str(CACHE/(key+".txt"))],check=True)
        else:
            soup = BeautifulSoup(text,"html.parser")
            record["title"] = soup.title.get_text(" ",strip=True) if soup.title else ""
            for tag in soup(["script","style","nav","footer"]):
                tag.decompose()
            plain=soup.get_text(" ",strip=True)
            (CACHE/(key+".txt")).write_text(plain)
            record["challenge"] = any(s in plain.lower() for s in
                ["verify you are human","checking your browser","making sure you're not a bot","just a moment...","access denied"])
        try:
            data=r.json()
            record["valid_json"]=True
            if key.startswith("crossref_"):
                m=data.get("message",{})
                record["metadata"]={k:m[k] for k in
                    ["title","author","published","published-print","published-online","container-title","volume","issue","page","article-number","publisher","type","DOI","ISBN"]
                    if k in m}
        except ValueError:
            record["valid_json"]=False
    except Exception as e:
        record["error"]=str(e)
    return record

def collect():
    data=parse_file(BASE/"referencias_normalizadas.bib")
    tasks=[]
    for key,e in data.entries.items():
        if e.fields.get("url"):
            tasks.append((key,e.fields["url"]))
        if e.fields.get("doi"):
            tasks.append(("crossref_"+key,"https://api.crossref.org/works/"+e.fields["doi"]))
    tasks += [
        ("EOSDA_especifico","https://eos.com/user-guide/crop-monitoring/"),
        ("UPF_direto","https://www.upf.br//_uploads/Conteudo/IN%20n%C2%BA%2003_2026%20Uso%20de%20Intelig%C3%AAncia%20Artificial%20%28IA%29%20nas%20atividades%20acad%C3%AAmicas%20da%20UPF_docx%281%29.pdf"),
        ("NASA_manager","https://power.larc.nasa.gov/docs/services/api/system/manager/"),
        ("BIPM_citacao","https://www.bipm.org/en/si-brochure-9"),
        ("QGIS_download","https://qgis.org/download/"),
        ("QGIS_versions","https://docs.qgis.org/"),
        ("NASA_point","https://power.larc.nasa.gov/api/temporal/daily/point?parameters=PRECTOTCORR,T2M,ALLSKY_SFC_SW_DWN&community=AG&longitude=-52.4&latitude=-28.2&start=20250101&end=20250102&format=JSON"),
        ("ROUSE_api","https://ntrs.nasa.gov/api/citations/19740022614"),
        ("ROUSE_pdf","https://ntrs.nasa.gov/api/citations/19740022614/downloads/19740022614.pdf"),
    ]
    with cf.ThreadPoolExecutor(max_workers=8) as pool:
        results=list(pool.map(fetch,tasks))
    dump(CACHE/"consultas.json",results)
    for r in results:
        print(r["id"],r.get("http",r.get("error")),r.get("title","")[:100])

if __name__=="__main__":
    if "snapshot" in sys.argv: snapshot()
    if "collect" in sys.argv: collect()
