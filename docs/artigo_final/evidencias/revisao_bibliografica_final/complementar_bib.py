from auditar_bib import fetch, dump, CACHE
from concurrent.futures import ThreadPoolExecutor
tasks=[
    ("QGIS_roadmap","https://qgis.org/resources/roadmap/"),
    ("QGIS_blog","https://blog.qgis.org/2026/10/03/release-schedule-changes-for-next-qgis-ltr/"),
]
for version in ["3.44","4.2"]:
    for chapter in ["vector_data","raster_data","map_production"]:
        tasks.append((f"QGIS_{version}_{chapter}",f"https://docs.qgis.org/{version}/en/docs/gentle_gis_introduction/{chapter}.html"))
with ThreadPoolExecutor(max_workers=5) as p:
    result=list(p.map(fetch,tasks))
dump(CACHE/"complementares.json",result)
for r in result: print(r["id"],r.get("http",r.get("error")),r.get("title",""))
