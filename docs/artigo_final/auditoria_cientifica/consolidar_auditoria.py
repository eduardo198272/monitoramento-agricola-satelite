"""Consolida inventários; não transforma HTTP/citações em validação semântica.

Executar na raiz. A linha de base é a cópia preservada antes da revisão.
Os pareceres abaixo registram o escopo efetivamente lido, inclusive limitações.
"""

import argparse
from collections import Counter
import difflib
import hashlib
import json
from pathlib import Path
import re

BASE = Path(__file__).resolve().parent
ARTICLE = BASE.parent
ROOT = ARTICLE.parents[1]

# chave: fonte cacheada, escopo lido, decisão e limite.
REVIEWS = {
    "ESA_SENTINEL2": ("bib_ESA_SENTINEL2", "Missão MSI, 13 bandas, resoluções e revisita nominal; documentação oficial.", "Manter; não confundir revisita com pontos válidos.", True),
    "GOOGLE_S2_SR": ("ee_s2", "Catálogo completo: bandas/centros/resoluções, escala 0,0001, ausência B10, harmonização e intervalo QA60.", "Manter; fronteira documental QA60 preservada sem inventar resolução da inconsistência de datas.", True),
    "GOOGLE_EE_ND": ("bib_GOOGLE_EE_ND", "Contrato normalizedDifference, razão e máscara de entradas negativas.", "Manter; não extrapolar para validação agronômica ou casos-limite remotos não executados.", True),
    "GOOGLE_EE_DATE": ("bib_GOOGLE_EE_DATE", "Contrato de início inclusivo e término exclusivo.", "Manter; aplicação acrescenta um dia ao término.", True),
    "GOOGLE_EE_SERVICE_ACCOUNT": ("bib_GOOGLE_EE_SERVICE_ACCOUNT", "Documentação oficial de autenticação por conta de serviço.", "Manter; conta autentica aplicação, não visitante.", True),
    "GOOGLE_EE_NONCOMMERCIAL": ("bib_GOOGLE_EE_NONCOMMERCIAL", "Página oficial de modalidades não comerciais; não comprova elegibilidade individual do projeto.", "Manter como contexto; não prometer gratuidade irrestrita.", True),
    "STREAMLIT_CLOUD_SECRETS": ("bib_STREAMLIT_CLOUD_SECRETS", "Página oficial de Secrets do Community Cloud.", "Manter; confirmar configuração efetiva via código sem divulgar segredos.", True),
    "SLAIFFER2023": ("slaiffer2023", "Registro/resumo institucional: índices e produtividade de soja irrigada/sequeiro.", "Complementar com artigo de 2025 lido em métodos; não presumir equivalência integral entre TCC e publicação.", False),
    "LOVATO2021": ("bib_LOVATO2021", "Consulta ao repositório UNESP expirou; texto e metadados integrais não conferidos.", "Manter registro não citado, pendente de comprovação; não usar como apoio substantivo.", False),
    "ARAUJO2025": ("", "Crossref retornou 404 para DOI Zenodo, que usa outro registrador; isso não prova inexistência.", "Não citado; existência, autores e suporte ainda pendentes. Não remover por 404.", False),
    "CHAVES2019": ("bib_CHAVES2019", "Consulta ao repositório UFLA expirou; conteúdo não conferido.", "Não citado; manter registro provisório sem alegar validação.", False),
    "NASA_POWER_DAILY": ("power_daily", "Documentação do serviço diário: UTC/LST, datas, parâmetros e limites.", "Manter e complementar com metodologia/dicionário de parâmetros.", True),
    "ROUSE1973": ("rouse_pdf", "Possível duplicação de ROUSE1974_NTRS: evento 1973/publicação NASA 1974, p. 309–317.", "Não citado; conservar até normalização pelo autor. Não contar como nova fonte independente.", False),
    "ROUSE1974_NTRS": ("rouse_pdf", "PDF NASA, p. 309–313, especialmente Spectral Analysis: BRP e TVI; lista dos quatro autores.", "Manter e esclarecer base histórica, não adaptação Sentinel-2; campo páginas pode ser complementado.", True),
    "GAO1996": ("gao_pdf", "PDF, resumo/introdução/formulação: 0,86/1,24 µm, saturação NDVI e efeito de solo residual.", "Manter; título/autoria/ano/58(3):257–266/DOI conferidos. Não atribuir B8/B11 diretamente.", True),
    "PATRICIO2018": ("patricio_pdf", "PDF Embrapa, identificação e seções iniciais de revisão: visão computacional/IA em culturas de grãos.", "Manter para contexto computacional agrícola; não sustenta qualquer decisão desta plataforma.", True),
    "GORELICK2017": ("gorelick", "Metadados DOI conferidos; página do editor bloqueada, texto integral não lido.", "Manter com validação parcial; características técnicas devem apoiar-se também na documentação oficial.", False),
    "AMANI2020": ("amani_pdf", "Metadados DOI conferidos; resposta 200 não é PDF, acesso bloqueado.", "Manter com validação parcial; não afirmar exame integral da revisão.", False),
    "WEISS2020": ("weiss_pdf", "Postprint HAL/INRAE; introdução e seção 2.2.1: calibração empírica e condições de aquisição/cultura.", "Manter. Não confirma origem exata das curvas qualitativas da figura; fonte primária adicional seria preferível para esse desenho.", True),
    "PHIRI2020": ("", "DOI confirma publicação; divergência Salekin: BibTeX Sharif versus Crossref Serajis.", "Não citado; conferir PDF/editor antes de corrigir autoria. Texto integral não verificado.", False),
    "WAZLAWICK2014": ("", "Livro sem URL no registro; edição/ano e conteúdo não verificados em exemplar.", "Não citado; não usar para classificar metodologia sem consultar edição efetiva.", False),
    "WAZLAWICK2020": ("bib_WAZLAWICK2020", "URL retorna aplicação/biblioteca, não exemplar legível.", "Não citado; edição/ano e conteúdo pendentes, possível atualização/substituição da edição de 2014 a decidir.", False),
    "MCFEETERS1996": ("mcfeeters", "Metadados DOI conferidos; texto do editor bloqueado.", "Manter com validação parcial. Distinção verde–NIR precisa de confirmação primária integral; não alegar leitura.", False),
    "USGS_NDMI": ("bib_USGS_NDMI", "Página oficial: NDMI NIR–SWIR para Landsat, bandas por geração.", "Manter; não é validação de B8A/B11 Sentinel-2.", True),
    "GOOGLE_EE_SAMPLE": ("bib_GOOGLE_EE_SAMPLE", "Contrato sampleRectangle: matriz por banda/projeção e valores padrão.", "Manter para método de extração; origem da grade vem do código.", True),
    "GOOGLE_EE_MEDIAN": ("bib_GOOGLE_EE_MEDIAN", "Contrato ImageCollection.median: mediana por pixel entre bandas correspondentes.", "Manter; não inventar justificativa histórica da escolha.", True),
    "GOOGLE_EE_REDUCE": ("bib_GOOGLE_EE_REDUCE", "Contrato reduceRegion: escala, projeção e maxPixels.", "Complementar com guia Statistics of an Image Region para pesos exatos.", True),
    "NOMINATIM_POLICY": ("bib_NOMINATIM_POLICY", "Política oficial de uso do endpoint público.", "Manter; código fornece User-Agent, mas atendimento integral da política requer exame operacional separado.", True),
    "EOSDA_PLATFORM": ("eosda", "Página comercial oficial: áreas, mapas/índices e funcionalidades anunciadas.", "Manter como documentação comercial, não evidência científica; cada célula/plano da tabela ainda exige comprovação individual.", False),
    "ONESOIL_PLATFORM": ("onesoil", "Página comercial oficial consultada; funcionalidades e produtos não equivalem a ensaio comparativo.", "Manter com tabela parcialmente validada, sem deduzir ausência pelo silêncio da página.", False),
    "ISO9241_2018": ("iso", "Título e identificação normativa presentes na referência; conteúdo integral não disponível, página bloqueada nesta rodada.", "Validação parcial; não reproduzir exigências normativas como auditadas.", False),
    "DAVIS1989": ("davis", "Metadados DOI conferidos; HTML 200 é desafio, não artigo.", "Manter com acesso integral pendente; não declarar questionário TAM validado.", False),
    "SULLIVAN2013": ("sullivan", "Texto aberto sobre itens Likert, ordinalidade, distribuições e cautela na análise.", "Manter; não confere validação psicométrica ao instrumento local.", True),
    "BRAUN2006": ("braun", "Metadados DOI conferidos; repositório bloqueado.", "Manter com acesso pendente e aprovação da codificação; não certificar protocolo completo de análise temática.", False),
    "QGIS_VECTOR": ("qgis_vector", "Documentação 3.40: entidades vetoriais e polígonos.", "Adicionar para representação espacial; documentação técnica, não estudo agronômico.", True),
    "QGIS_RASTER": ("qgis_raster", "Documentação 3.40: células, grades, resolução e dados raster.", "Adicionar; versão fixada, hoje indicada como versão encerrada pelo site.", True),
    "QGIS_MAP": ("qgis_map", "Seções Overview e Map Legend: elementos e comunicação cartográfica.", "Adicionar para legenda; não fundamenta avaliação perceptiva das paletas particulares.", True),
    "GOOGLE_EE_RESAMPLE": ("ee_resample", "Guia oficial: vizinho mais próximo padrão, bilinear/bicúbica explícitos.", "Adicionar para distinguir grade de processamento e resolução física.", True),
    "GOOGLE_EE_REGION": ("ee_weight", "Guia reduceRegion: pesos, interseção, máscara e quantização de frações.", "Adicionar; mínimo entre máscara/fração, não produto.", True),
    "SENTINELHUB_NDMI": ("sentinel_ndmi", "Código B8A/B11 e texto B8/B11 na mesma página.", "Adicionar com inconsistência explícita. Uso técnico, não prova de nomenclatura predominante ou calibração.", True),
    "HYNDMAN2021": ("fpp_regression", "Livro aberto, seções Moving averages e Least squares estimation consultadas.", "Adicionar para conceitos matemáticos; janela 3 e limiares não vêm do livro.", True),
    "NIST_OUTLIERS": ("nist_outliers", "Seção 1.3.5.17: sinalização versus testes, padronização e advertência sobre amostras pequenas.", "Adicionar com ressalva: aplicação usa janela anterior e divisor N, não teste NIST.", True),
    "NUMPY_STD": ("numpy_std", "API/documentação e notas: divisor N−ddof, ddof=0 e ddof=1.", "Adicionar para implementação; documentação stable pode mudar em relação à versão instalada.", True),
    "NUMPY_POLYFIT": ("numpy_polyfit", "API: ajuste polinomial por mínimos quadrados, grau 1.", "Adicionar para implementação, não validação dos limiares.", True),
    "BIPM_SI": ("si", "Brochura SI disponível, definições de unidades derivadas e prefixos.", "Adicionar; identidade kWh→MJ é dedução elementar, não método agronômico.", True),
    "BENDER2020": ("google_testing", "Capítulo 11 completo disponível; escopos, testes e seção A Note on Code Coverage lidos.", "Adicionar como capítulo atribuído a Adam Bender, editores do livro separados; não imputar processos Google ao projeto.", True),
    "AAPOR2013": ("aapor", "Relatório completo disponível; Executive Summary e recomendações iniciais lidos.", "Adicionar para não probabilidade/transparência/limites inferenciais; não atribuir representatividade.", True),
    "SLAIFFER2025": ("slaiffer2025_pdf", "PDF p. 495–497, resumo e métodos: índices Crop Monitoring e produtividade da colhedora, análise espacial.", "Adicionar como publicação posterior e comparação de desenho de evidência; não importar afirmações universais de classes agronômicas do artigo.", True),
    "IZQUIERDO2026": ("izquierdo2026_pdf", "PDF p. 1–5: autoria, desenho multissensor, dados FDR e proposta de validação interanual.", "Adicionar para distinguir modelagem de umidade da plataforma. Metadados 16(5):541 conferidos; PDF diz publicação 28/02/2026, não inferir mês pelo número 5.", True),
    "NASA_POWER_METHOD": ("power_sources", "Metodologia: grades de origem do arquivo principal e aliases de alta resolução.", "Adicionar sem tratar consulta ao centroide como medida local.", True),
    "NASA_POWER_PARAMETERS": ("power_parameters", "Dicionário JSON AG/DAILY: PRECTOTCORR, T2M, ALLSKY_SFC_SW_DWN.", "Adicionar para definições/unidades; metadados da resposta efetiva continuam prevalecendo.", True),
    "STREAMLIT_STATE": ("streamlit_state", "Documentação oficial Session State lida: valores entre reruns, escopo e perda de sessão.", "Adicionar para estado/limites de persistência; consulta adicional registrada em CONSULTAS_COMPLEMENTARES.json.", True),
}

# Pareceres localizados após confronto manual; demais blocos conservam triagem parcial.
CORRECTED_PREFIXES = (
    "A representação georreferenciada", "As bandas B4 e B8",
    "O índice de vegetação por diferença", "O índice resume contraste",
    "O acrônimo NDWI", "A fonte USGS", "Médias móveis resumem",
    "A NASA POWER disponibiliza", r"\citet{SLAIFFER2023}",
    r"\citet{IZQUIERDO2026}", "Os conjuntos $P_C$",
    "O cálculo usa a fórmula", "Para tendência,", "No catálogo diário",
    r"Na \cref{eq:radiacao-codigo}", "A avaliação distinguiu implementação",
    "A avaliação com usuários é exploratória", "O estado de sessão do Streamlit",
)


def entries(text):
    return {key: (kind, body.strip()) for kind, key, body in re.findall(
        r"^@(\w+)\{([^,]+),(.*?)(?=^@|\Z)", text, re.M | re.S)}


def citations(text):
    return set(k.strip() for group in re.findall(r"\\cite\w*\{([^}]+)\}", text)
               for k in group.split(","))


def cell(text):
    return re.sub(r"\s+", " ", text).replace("|", "\\|")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path, default=Path(
        "/tmp/opencode/auditoria-cientifica/baseline.json"))
    args = parser.parse_args()
    baseline = json.loads(args.baseline.read_text())
    bibpath = "docs/artigo_final/referencias.bib"
    before = entries(baseline[bibpath]["text"])
    after = entries((ARTICLE/"referencias.bib").read_text())
    texfiles = sorted(ARTICLE.glob("final_*.tex"))
    sections = {p.name: p.read_text() for p in texfiles}
    sections["fig/conceitos.tex"] = (ARTICLE/"fig/conceitos.tex").read_text()
    used = {key: [name for name, text in sections.items() if key in citations(text)]
            for key in after}
    refout = [
        "# Auditoria das referências\n",
        "Data: 15/11/2026. Inventário de todas as 34 entradas originais e das novas. "
        "**Auditada não significa validada integralmente.** Os pareceres delimitam "
        "acesso, leitura e suporte; HTTP 200, DOI e snippets não comprovam conteúdo.\n",
        "Os blocos BibTeX preservam autoria/ordem, título, ano, veículo, volume/número/páginas "
        "e URL tal como registrados. Campos não confirmados não são corrigidos por suposição. "
        "Acesso integral disponível significa documento obtido, não leitura de todas as páginas.\n",
        "## Normalização\n\nClasse local CC-EC_TF-TC v1.1, opção alpha-refs, natbib/dcu; "
        "mantida sem substituir por ABNT. Datas de acesso novas são 15/11/2026. "
        "Datas anteriores foram preservadas como histórico, não certificadas retroativamente. "
        "Ano de acesso não deve ser presumido como ano de publicação de página dinâmica. "
        "Entradas institucionais sem ano conservam nota explícita; padronização de s.d. depende do modelo. "
        "Tipos mastersthesis de TCCs e duplicação Rouse ainda requerem normalização. "
        "Nomes estendidos de Weiss não foram certificados somente a partir das iniciais do PDF.\n",
    ]
    for index, (key, (kind, body)) in enumerate(after.items(), 1):
        source, scope, decision, substantive = REVIEWS[key]
        refout.extend([
            f"## R{index:02d} — {key}\n",
            f"- Origem: {'original' if key in before else 'adicionada'}; tipo BibTeX: `{kind}`.",
            f"- Localização: {', '.join(used[key]) or 'não citada no manuscrito atual'}.",
            f"- Evidência: `{source or 'consulta/metadados descritos no parecer'}`; "
            "URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.",
            f"- Conteúdo e verificação: {scope}",
            f"- Decisão: {decision}",
            f"- Status: {'Validado no escopo delimitado acima' if substantive else 'Parcialmente validado / pendente de comprovação'}.\n",
            f"```bibtex\n@{kind}{{{key},\n{body}\n```\n",
        ])
    refout.extend([
        "## Candidatas não incorporadas e pesquisa complementar\n",
        "- **Pohjankukka et al. (2025)**: Jonne Pohjankukka, Timo A. Räsänen, Timo P. Pitkänen, "
        "Arttu Kivimäki, Ville Mäkinen, Tapio Väänänen, Jouni Lerssi, Aura Salmivaara e Maarit Middleton. "
        "*Digital mapping of peat thickness and extent in Finland using remote sensing and machine learning*. "
        "Geoderma 455, 117216. DOI https://doi.org/10.1016/j.geoderma.2025.117216. "
        "Registro Jukuri e metadados conferidos; download retornou HTML, não PDF. "
        "Mapeamento de turfa na Finlândia, não plataforma agrícola diretamente comparável. "
        "Não incorporada por pertinência insuficiente ao recorte, sem desqualificar o estudo.\n",
        "- **SWEBOK v4.0 / v4.0a**: página oficial IEEE consultada, edição de Hironori Washizaki "
        "e atualização verificadas, mas capítulos integrais não lidos. Não incorporado como suporte de conteúdo não consultado.\n",
        "- **Sommerville**: URL /web/intro/ retornou 404; não valida edição nem conteúdo. "
        "Pressman/Maxim, Myers, Robert C. Martin e Gonzalez/Woods não tiveram exemplares examinados. "
        "Ausência de incorporação evita referências decorativas; investigação desses livros permanece incompleta.\n",
        "- **Parnas (1972)**: DOI 10.1145/361598.361623 e metadados obtidos; PDF UMD bloqueado. "
        "Não incorporado sem leitura substantiva. **Fowler, Repository**: página disponível, "
        "escopo específico não basta para fundamentar toda a arquitetura. **Kuefler, Unit Testing**: "
        "capítulo aberto lido, mas Bender foi suficiente para a afirmação localizada; não acrescentado redundantemente.\n",
        "- **Frascati/OECD (2015)**: consultas oficiais bloqueadas; não atribuir classificação "
        "formal por critérios que não foram conferidos. **EO Browser**: documentação inacessível nesta rodada, não é prova de ausência funcional.\n",
    ])
    (BASE/"AUDITORIA_REFERENCIAS.md").write_text("\n".join(refout)+"\n")

    # Cada bloco de prosa recebe um localizador. Extração não é aprovação científica.
    rows = []
    for name, text in sections.items():
        section = name
        for match in re.finditer(r"(?:^|\n\n)(\S[\s\S]*?)(?=\n\n|\Z)", text):
            block = match.group(1).strip()
            line = text[:match.start(1)].count("\n")+1
            heading = re.search(r"\\(?:sub)*section\{([^}]+)\}", block)
            if heading:
                section = heading.group(1)
            # Ambientes/legendas também têm registro; comandos vazios não.
            if len(block) < 55 or block.startswith(("\\section", "\\subsection", "\\subsubsection")):
                continue
            keys = sorted(citations(block))
            oldtext = baseline.get(f"docs/artigo_final/{name}", {}).get("text", "")
            changed = block not in oldtext
            weak = [k for k in keys if not REVIEWS.get(k, ("", "", "", False))[3]]
            status = "Parcialmente validado"
            if weak:
                evidence = "Limites de acesso/suporte: "+", ".join(weak)+"; ver auditoria individual."
                problem = "Não certificar integralmente suporte sem texto/evidência suficiente."
            elif keys:
                evidence = "; ".join(f"{k}: {REVIEWS[k][1]}" for k in keys)
                problem = "Fontes localizadas; correspondência de cada subafirmação ainda requer revisão fina."
            else:
                evidence = ("Implementação/evidências próprias: src/app, tests, RASTREABILIDADE_TCC.md "
                            "e manifestos de demonstração/avaliação; ou matemática elementar.")
                problem = "Distinguir contribuição/resultado próprio de conceito sem citação; não é validação automática."
            if "\\begin{equation}" in block or "\\begin{align}" in block:
                evidence = "AUDITORIA_EQUACOES.md: código, variáveis, unidades e condições por expressão."
                problem = "Sem calibração agronômica; ver limitações específicas."
                status = "Validado"
            if block.startswith(CORRECTED_PREFIXES) and not weak:
                status = "Corrigido"
                problem = ("Lacuna localizada de precisão/fundamentação tratada; "
                           "não extrapolar suporte além do descrito na auditoria da fonte.")
            if name == "final_3b_plataforma.tex":
                evidence = "Capturas fornecidas pelo autor; evidencias/capturas_autor; distintas da demonstração instrumentada."
            rows.append((f"P{len(rows)+1:03d}", f"{section}; {name}:{line}", "não remapeada",
                         cell(block), ", ".join(keys) or "própria/elementar/sem citação",
                         evidence, problem,
                         "Texto revisto; aprovação substantiva pendente" if changed else "Preservado; conferir limites",
                         status))
    matrix = [
        "# Matriz de rastreabilidade científica\n",
        "Inventário por bloco de prosa/ambiente, em ordem dos arquivos; localizadores por arquivo e linha "
        "evitam depender da paginação. Inclui transcrições completas dos blocos para não esconder subafirmações. "
        "**É uma matriz de triagem rastreável, não certificação de revisão semântica exaustiva.** "
        "Status parcial é intencional: citação presente não valida automaticamente todo o parágrafo. "
        "Corrigido identifica as intervenções localizadas conferidas; Validado nos ambientes "
        "matemáticos significa fidelidade da expressão e condições, não eficácia agronômica. "
        "A passagem definitiva para Validado exige resolver o problema indicado. "
        "Equações têm parecer específico no documento matemático. "
        "Página original de 28 páginas não foi reconstruída; números da solicitação são aproximados e não atribuídos artificialmente.\n",
        "| ID | Seção | Página original | Afirmação ou equação | Referência original/atual | Evidência verificada | Problema | Correção | Status |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    matrix.extend("| "+" | ".join(cell(x) for x in row)+" |" for row in rows)
    (BASE/"MATRIZ_RASTREABILIDADE_CIENTIFICA.md").write_text("\n".join(matrix)+"\n")

    changes = ["# Registro de alterações do artigo\n",
               "Comparação com a cópia de trabalho preservada antes desta auditoria, não com HEAD. "
               "Isso separa as revisões anteriores de redação dos novos ajustes científicos. "
               "Assistência: agente de IA, com ferramentas locais e fontes identificadas; "
               "aprovação substantiva do autor ainda pendente.\n"]
    changedfiles = []
    for relative, data in baseline.items():
        path = ROOT/relative
        if not path.exists() or path.read_text() == data["text"]:
            continue
        current = path.read_text()
        changedfiles.append(relative)
        changes.extend([f"## {relative}\n",
                        "- Motivo: fundamentação localizada e precisão técnica; fontes citadas nos próprios trechos "
                        "e em AUDITORIA_REFERENCIAS.md.",
                        "- Impacto: não altera valores, respostas, equações numeradas nem comportamento da aplicação. "
                        "Esclarece limites; comparações e redação devem ser aprovadas pelo autor.\n",
                        "```diff\n"+"".join(difflib.unified_diff(
                            data["text"].splitlines(True), current.splitlines(True),
                            fromfile="antes-da-auditoria", tofile="revisado"))+"```\n"])
    (BASE/"CHANGELOG_ARTIGO.md").write_text("\n".join(changes)+"\n")
    summary = {
        "original_entries": len(before), "current_entries": len(after),
        "added": sorted(after.keys()-before.keys()),
        "removed": sorted(before.keys()-after.keys()),
        "replaced": [], "original_entries_with_individual_assessment": len(before),
        "references_with_substantive_scope_checked": sum(v[3] for v in REVIEWS.values()),
        "warning": "Escopo substantivo não equivale a validação integral de todos os metadados/afirmações.",
        "paragraph_blocks": len(rows), "matrix_status": dict(Counter(row[-1] for row in rows)),
        "changed_article_files": changedfiles,
        "baseline_sha256": {p: v["sha256"] for p, v in baseline.items()},
        "current_article_sha256": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                                   for p in texfiles+[ARTICLE/"referencias.bib"]},
    }
    (BASE/"INVENTARIO.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
