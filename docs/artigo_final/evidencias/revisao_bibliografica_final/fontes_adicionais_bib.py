from auditar_bib import fetch, dump, CACHE, BASE
from pybtex.database import parse_file
from concurrent.futures import ThreadPoolExecutor
tasks=[]
for k,e in parse_file(BASE/"referencias_normalizadas.bib").entries.items():
    f=e.fields
    if f.get("doi") and f.get("url")!="https://doi.org/"+f["doi"]:
        tasks.append(("doi_"+k,"https://doi.org/"+f["doi"]))
tasks += [
    ("GOTEL_pdf","https://discovery.ucl.ac.uk/749/1/2.2_rtprob.pdf"),
    ("GORELICK_google","https://research.google/pubs/google-earth-engine-planetary-scale-geospatial-analysis-for-everyone/"),
    ("HYNDMAN_citation","https://otexts.com/fpp3/citing.html"),
    ("WEISS_hal","https://hal.inrae.fr/hal-02624593"),
]
with ThreadPoolExecutor(max_workers=5) as p:
    result=list(p.map(fetch,tasks))
dump(CACHE/"adicionais.json",result)
for r in result: print(r["id"],r.get("http",r.get("error")),r.get("title",""))
