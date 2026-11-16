"""Registra consultas públicas; sucesso HTTP não implica validação de conteúdo."""

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess

import requests

BASE = Path(__file__).resolve().parent
CACHE = Path("/tmp/opencode/auditoria-cientifica/fontes")
ARTICLE = BASE.parent
URLS = {
    "rouse_pdf": "https://ntrs.nasa.gov/api/citations/19740022614/downloads/19740022614.pdf",
    "gao_pdf": "https://cpb-us-w2.wpmucdn.com/sites.udel.edu/dist/d/1835/files/2014/06/NDWI-A-Normalized-Difference-Water-Index-for-Remote-Sensing-of-Vegetation-Liquid-Water-From-Space-1ko95nn.pdf",
    "patricio_pdf": "https://www.alice.cnptia.embrapa.br/bitstream/doc/1099103/1/ID444052008CompElectroAgricv153p69.pdf",
    "weiss_pdf": "https://hal.inrae.fr/hal-02627117v1/document",
    "amani_pdf": "https://ieeexplore.ieee.org/iel7/4609443/8994817/09184118.pdf",
    "gorelick": "https://www.sciencedirect.com/science/article/pii/S0034425717302900",
    "mcfeeters": "https://www.tandfonline.com/doi/abs/10.1080/01431169608948714",
    "slaiffer2023": "https://repositorio.ufsm.br/handle/1/29995",
    "slaiffer2025": "https://periodicoscientificos.ufmt.br/ojs/index.php/nativa/article/view/18592",
    "izquierdo2026": "https://redivia.gva.es/handle/20.500.11939/9107",
    "pohjankukka2025": "https://jukuri.luke.fi/items/212cdbb5-9248-4b46-8922-3b2dc96deaca",
    "qgis_raster": "https://docs.qgis.org/3.40/en/docs/gentle_gis_introduction/raster_data.html",
    "qgis_vector": "https://docs.qgis.org/3.40/en/docs/gentle_gis_introduction/vector_data.html",
    "qgis_crs": "https://docs.qgis.org/3.40/en/docs/gentle_gis_introduction/coordinate_reference_systems.html",
    "qgis_map": "https://docs.qgis.org/3.40/en/docs/gentle_gis_introduction/map_production.html",
    "ee_weight": "https://developers.google.com/earth-engine/guides/reducers_reduce_region",
    "ee_resample": "https://developers.google.com/earth-engine/guides/resample",
    "ee_s2": "https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED",
    "sentinel_ndmi": "https://custom-scripts.sentinel-hub.com/custom-scripts/sentinel-2/ndmi/",
    "numpy_std": "https://numpy.org/doc/stable/reference/generated/numpy.std.html",
    "numpy_polyfit": "https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html",
    "numpy_percentile": "https://numpy.org/doc/stable/reference/generated/numpy.percentile.html",
    "nist_location": "https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm",
    "nist_scale": "https://www.itl.nist.gov/div898/handbook/eda/section3/eda356.htm",
    "nist_outliers": "https://www.itl.nist.gov/div898/handbook/eda/section3/eda35h.htm",
    "fpp_ma": "https://otexts.com/fpp3/moving-averages.html",
    "fpp_regression": "https://otexts.com/fpp3/least-squares.html",
    "swebok": "https://www.computer.org/education/bodies-of-knowledge/software-engineering",
    "sommerville": "https://software-engineering-book.com/web/intro/",
    "parnas": "https://www.cs.umd.edu/class/spring2003/cmsc838p/Design/criteria.pdf",
    "fowler": "https://martinfowler.com/eaaCatalog/repository.html",
    "oecd": "https://doi.org/10.1787/9789264239012-en",
    "aapor": "https://aapor.org/wp-content/uploads/2022/11/NPS_TF_Report_Final_7_revised_FNL_6_22_13.pdf",
    "si": "https://www.bipm.org/documents/20126/41483022/SI-Brochure-9.pdf",
    "power_daily": "https://power.larc.nasa.gov/docs/services/api/temporal/daily/",
    "power_sources": "https://power.larc.nasa.gov/docs/methodology/",
    "power_parameters": "https://power.larc.nasa.gov/api/system/manager/parameters?community=AG&temporal=DAILY",
    "eosda": "https://eos.com/products/crop-monitoring/",
    "onesoil": "https://onesoil.ai/en/platform",
    "eobrowser": "https://www.sentinel-hub.com/explore/education/eo_browser/",
    "braun": "https://uwe-repository.worktribe.com/output/1043068",
    "davis": "https://www.jstor.org/stable/249008",
    "sullivan": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3886444/",
    "iso": "https://www.iso.org/standard/63500.html",
    "upf_collection": "https://repositorio.upf.br/handle/123456789/8754",
    "streamlit_state": "https://docs.streamlit.io/develop/concepts/architecture/session-state",
    "google_testing": "https://abseil.io/resources/swe-book/html/ch11.html",
    "slaiffer2025_pdf": "https://periodicoscientificos.ufmt.br/ojs/index.php/nativa/article/download/18592/14926",
    "izquierdo2026_pdf": "https://redivia.gva.es/bitstream/20.500.11939/9107/5/2026_Izquierdo-Sanz_Hybrid.pdf",
}


def fetch(item):
    key, url = item
    try:
        response = requests.get(url, timeout=35, headers={"User-Agent": "TCC-scientific-audit/1.0"})
        content = response.content
        pdf = content.startswith(b"%PDF")
        path = CACHE / (key + (".pdf" if pdf else ".html"))
        path.write_bytes(content)
        if pdf:
            subprocess.run(["pdftotext", "-layout", str(path), str(CACHE/f"{key}.txt")],
                           check=False, capture_output=True)
        return {"id": key, "url": url, "final_url": response.url,
                "status": response.status_code, "pdf": pdf,
                "sha256": hashlib.sha256(content).hexdigest(),
                "bytes": len(content), "cache": str(path),
                "scope": "Consulta técnica registrada; leitura e pertinência na auditoria de referências"}
    except Exception as error:
        return {"id": key, "url": url, "error": str(error)}


def main():
    CACHE.mkdir(parents=True, exist_ok=True)
    # Registrar separadamente metadados DOI e conteúdo das fontes.
    bib = (ARTICLE/"referencias.bib").read_text()
    for _, key, body in re.findall(r"^@(\w+)\{([^,]+),(.*?)(?=^@|\Z)", bib, re.M | re.S):
        urls = re.findall(r"\\url\{([^}]+)\}", body)
        if urls and "doi.org/" not in urls[0] and urls[0] not in URLS.values():
            URLS["bib_"+key] = urls[0]
    dois = sorted(set(re.findall(r"https://doi.org/([^}\s]+)", bib)) | {
        "10.1016/j.geoderma.2025.117216", "10.3390/agronomy16050541",
        "10.31413/nat.v13i3.18592", "10.1145/361598.361623",
    })
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(fetch, URLS.items()))
    metadata = []
    for doi in dois:
        try:
            response = requests.get("https://api.crossref.org/works/"+doi, timeout=25)
            row = {"doi": doi, "status": response.status_code}
            if response.ok:
                row["message"] = response.json()["message"]
            metadata.append(row)
        except Exception as error:
            metadata.append({"doi": doi, "error": str(error)})
    (BASE/"CONSULTAS_FONTES.json").write_text(json.dumps({
        "consulted_at": datetime.now(timezone.utc).isoformat(),
        "warning": "Metadados e HTTP não comprovam suporte de afirmações; ver AUDITORIA_REFERENCIAS.md.",
        "sources": results, "crossref": metadata,
    }, ensure_ascii=False, indent=2)+"\n")
    for row in results:
        print(row["id"], row.get("status", row.get("error")), row.get("bytes"), "PDF" if row.get("pdf") else "")
    for row in metadata:
        m = row.get("message", {})
        print(row["doi"], row.get("status"), m.get("title"),
              [(a.get("given"), a.get("family")) for a in m.get("author", [])])


if __name__ == "__main__":
    main()
