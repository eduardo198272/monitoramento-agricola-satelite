"""Capture a real local session. Never submits forms or supplies analytical results.

Requires Playwright and a locally running, authorized Streamlit instance.
Coordinates are an illustrative spatial input, without crop/ownership claims.
"""

import argparse
import json
from pathlib import Path
from playwright.sync_api import sync_playwright


parser = argparse.ArgumentParser()
parser.add_argument("--url", default="http://localhost:8502")
parser.add_argument("--output", type=Path, default=Path("/tmp/opencode/tcc03-demo"))
args = parser.parse_args()
args.output.mkdir(parents=True, exist_ok=True)
manifest = {
    "scenario": "Demonstração computacional, sem identificação de cultura",
    "url": args.url, "period": ["2026-09-01", "2026-10-31"],
    "indices": ["NDVI", "NDWI", "NDMI"],
    "polygon": [[-52.332, -28.229], [-52.330, -28.229],
                [-52.330, -28.227], [-52.332, -28.227]],
    "captures": [], "downloads": [], "completed": False,
}

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        executable_path="/usr/bin/google-chrome", headless=True,
        args=["--no-sandbox"],
    )
    page = browser.new_page(viewport={"width": 1680, "height": 1100}, accept_downloads=True, has_touch=True)

    def capture(name, full=False):
        page.screenshot(path=str(args.output / f"{name}.png"), full_page=full)
        manifest["captures"].append(name)

    try:
        page.goto(args.url)
        page.get_by_text("Área de interesse", exact=True).wait_for(timeout=60000)
        frame = page.frame_locator('iframe[title="streamlit_folium.st_folium"]')
        # Wait for cartography instead of recording the initial blank iframe.
        frame.locator(".leaflet-tile-loaded").first.wait_for(timeout=60000)
        capture("cap01_interface")
        page.get_by_label("Localidade", exact=True).fill("Passo Fundo")
        page.get_by_role("button", name="🔍", exact=True).click()
        page.get_by_text("Localidade encontrada:", exact=False).wait_for(timeout=45000)
        capture("cap02_busca")
        # Drawing automation supplies a geometry through the real Leaflet event.
        selected_frame = next(f for f in page.frames if "streamlit_folium" in f.url)
        selected_frame.wait_for_function(
            "() => Object.keys(window).some(k => k.startsWith('map_') && window[k]?.fire)"
        )
        selected_frame.evaluate("""(ring) => {
          const key = Object.keys(window).find(k => k.startsWith('map_') && window[k]?.fire);
          const map = window[key];
          const layer = L.polygon(ring.map(([lon,lat]) => [lat,lon]));
          map.fitBounds(layer.getBounds());
          map.fire('draw:created', {layer, layerType:'polygon'});
        }""", manifest["polygon"])
        page.get_by_role("button", name="Salvar localização", exact=True).wait_for(timeout=60000)
        capture("cap03_poligono")
        page.get_by_role("button", name="Salvar localização", exact=True).click()
        page.get_by_label("Nome da localização", exact=True).fill("Recorte demonstrativo")
        capture("cap04_salvar")
        page.get_by_role("button", name="Confirmar", exact=True).click()
        page.get_by_text('foi salva.', exact=False).wait_for(timeout=30000)
        page.wait_for_timeout(1000)
        page.keyboard.press("Escape")
        page.get_by_role("dialog").wait_for(state="hidden", timeout=10000)
        page.get_by_role("button", name="📍 Localizações salvas", exact=True).click()
        page.get_by_role("button", name="Recorte demonstrativo", exact=True).click()
        page.get_by_role("button", name="Salvar localização", exact=True).wait_for(timeout=60000)
        capture("cap05_restaurar")
        date_inputs = page.locator('[data-testid="stDateInput"] input')
        date_inputs.nth(0).fill("01/09/2026")
        date_inputs.nth(0).press("Enter")
        date_inputs.nth(1).fill("31/10/2026")
        date_inputs.nth(1).press("Enter")
        page.keyboard.press("Escape")
        page.get_by_text("Monitoramento Agrícola", exact=True).click()
        page.get_by_text("Todos", exact=True).click()
        page.wait_for_timeout(2500)
        capture("cap07_parametros")
        page.get_by_role("button", name="Analisar área", exact=True).click()
        page.get_by_text("Visão geral multiíndice", exact=True).wait_for(timeout=240000)
        capture("cap08_painel")
        for index, name in (("NDVI", "cap09_ndvi"), ("NDWI", "cap10_ndwi"), ("NDMI", "cap11_ndmi")):
            page.locator('[data-testid="stRadio"]').last.get_by_text(index, exact=True).click()
            component = page.frame_locator('iframe[title="src.app.map_interaction.index_pixel_hover"]')
            component.locator("#map-status").wait_for(state="hidden", timeout=90000)
            analytical_frame = page.locator('iframe[title="src.app.map_interaction.index_pixel_hover"]').element_handle().content_frame()
            analytical_frame.evaluate("(ring) => map.fitBounds(ring.map(([lon,lat])=>[lat,lon]))", manifest["polygon"])
            page.wait_for_timeout(2000)
            page.locator('iframe[title="src.app.map_interaction.index_pixel_hover"]').screenshot(path=str(args.output / f"{name}.png"))
            manifest["captures"].append(name)
        point = analytical_frame.evaluate("map.latLngToContainerPoint(L.latLng(-28.228,-52.331))")
        box = page.locator('iframe[title="src.app.map_interaction.index_pixel_hover"]').bounding_box()
        page.mouse.move(box["x"] + point["x"], box["y"] + point["y"])
        page.wait_for_timeout(300)
        manifest["cursor_read"] = analytical_frame.locator("#pixel-tooltip").inner_text()
        page.locator('iframe[title="src.app.map_interaction.index_pixel_hover"]').screenshot(path=str(args.output / "cap12_cursor.png"))
        manifest["captures"].append("cap12_cursor")
        page.get_by_text("Série Temporal de NDMI", exact=True).scroll_into_view_if_needed()
        page.locator('[data-testid="stPlotlyChart"]').nth(0).screenshot(path=str(args.output / "cap13_series.png"))
        manifest["captures"].append("cap13_series")
        capture("cap14_anomalias")
        page.get_by_text("Dados Climáticos (NASA POWER)", exact=True).scroll_into_view_if_needed()
        page.locator('[data-testid="stPlotlyChart"]').nth(1).screenshot(path=str(args.output / "cap15_clima.png"))
        manifest["captures"].append("cap15_clima")
        for label, filename in (("PDF", "demonstracao.pdf"), ("Excel", "demonstracao.xlsx"),
                                ("CSV (ZIP)", "demonstracao.zip")):
            page.get_by_role("button", name=f"Gerar {label}", exact=True).click()
            download_button = page.get_by_role("button", name=f"Baixar {label}", exact=True)
            download_button.wait_for(timeout=180000)
            with page.expect_download() as event:
                download_button.click()
            event.value.save_as(args.output / filename)
            manifest["downloads"].append(filename)
        capture("cap16_exportacao", full=True)
        page.get_by_text("Importar / exportar localizações", exact=True).click()
        page.get_by_role("button", name="Preparar GeoJSON para download", exact=True).click()
        with page.expect_download() as event:
            page.get_by_role("button", name="Baixar minhas localizações", exact=True).click()
        event.value.save_as(args.output / "localizacoes.geojson")
        manifest["downloads"].append("localizacoes.geojson")
        capture("cap06_geojson")
        page.get_by_text("Importar / exportar localizações", exact=True).click()
        imported = browser.new_page(viewport={"width":1440,"height":1000})
        imported.goto(args.url)
        imported.get_by_text("Área de interesse", exact=True).wait_for(timeout=60000)
        imported.get_by_text("Importar / exportar localizações", exact=True).click()
        imported.locator('input[type="file"]').set_input_files(str(args.output / "localizacoes.geojson"))
        imported.get_by_role("button", name="Importar localizações", exact=True).click()
        imported.get_by_text("1 localização(ões) importada(s). Abra Localizações salvas.", exact=True).wait_for(timeout=30000)
        imported.screenshot(path=str(args.output / "geojson_importacao.png"))
        manifest["geojson_imported_in_new_session"] = True
        imported.close()
        page.set_viewport_size({"width":390,"height":844})
        page.get_by_text("Mapa do índice", exact=True).scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        point = analytical_frame.evaluate("map.latLngToContainerPoint(L.latLng(-28.228,-52.331))")
        box = page.locator('iframe[title="src.app.map_interaction.index_pixel_hover"]').bounding_box()
        page.touchscreen.tap(box["x"] + point["x"], box["y"] + point["y"])
        manifest["touch_read"] = analytical_frame.locator("#pixel-tooltip").inner_text()
        capture("mobile_resultados", full=True)
        manifest["completed"] = True
    except Exception as error:
        # Record type and controlled context, not remote exception credentials.
        manifest["failure_type"] = type(error).__name__
        (args.output / "interface.txt").write_text(page.locator("body").inner_text(), encoding="utf-8")
        capture("estado_interrupcao", full=True)
    finally:
        (args.output / "manifesto.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        print(json.dumps({"completed": manifest["completed"], "captures": manifest["captures"],
                          "failure_type": manifest.get("failure_type")}))
        browser.close()
