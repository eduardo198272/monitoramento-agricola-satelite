"""Preserva capturas do autor e prepara recortes editoriais sem alterar valores."""

import hashlib
import json
from pathlib import Path
import shutil

from PIL import Image


ARTICLE = Path(__file__).resolve().parents[1]
ROOT = ARTICLE.parents[1]
SOURCE = ROOT / "Imagens Artigo"
OUTPUT = ARTICLE / "fig/capturas_autor"
AUDIT = ARTICLE / "evidencias/capturas_autor"
FILES = [
    ("inicial.png", "Imagem1-Página Inicial.png"),
    ("configuracao.png", "Imagem1.2-Barra de configuração.png"),
    ("busca.png", "Imagem1.3-Barra de pesquisa de localizações.png"),
    ("busca_resultado.png", "Imagem1.4-Ao clicar em pesquisa no mapa fica centralizada a localização pesquisada.png"),
    ("mapa_indice.png", "Imagem2.1-Mapa da área selecioada com gradiente do índice selecionado.png"),
    ("painel_series.png", "Imagem2.2-Relatório dos Indices da série temporal.png"),
    ("anomalias_clima.png", "Imagem2.3-Relatório de Anomalias do Indicador selecioado e de clima.png"),
    ("relatorio_pdf_pendente.png", "Imagem3.1-Relatório gerado em pdf.png"),
    ("geojson_upload.png", "Imagem4.1-Barra de upload no geoJson.png"),
    ("geojson_arquivo.png", "Imagem4.2-arquivo geojson aberto.png"),
    ("geojson_importado.png", "imagem4.3-arquivo importado e opções aparecendo.png"),
    ("desenho.png", "Imagem4.4-Desenhada figura no mapa.png"),
    ("salvar.png", "Imagem4.5-Salvamento da localização.png"),
    ("salva.png", "Imagem4.6-Localização salva.png"),
    ("restaurar.png", "Imagem4.7-Restauração de localização no mapa, após clicar na localização.png"),
    ("mobile_mapa.jpeg", "Imagem5.1-responsividade mapa celular.jpeg"),
    ("mobile_painel.jpeg", "Imagem5.2-Responsividade celular relatório.jpeg"),
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    AUDIT.mkdir(parents=True, exist_ok=True)
    records = []
    for name, original in FILES:
        source = SOURCE / original
        # A captura de PDF não entra nos assets finais nem na compilação.
        pending = name == "relatorio_pdf_pendente.png"
        target = (AUDIT if pending else OUTPUT) / name
        shutil.copy2(source, target)
        assert digest(source) == digest(target)
        with Image.open(source) as image:
            size = list(image.size)
        records.append({
            "source": str(source.relative_to(ROOT)),
            "copy": str(target.relative_to(ROOT)),
            "sha256": digest(source),
            "size_px": size,
            "included": not pending,
            "status": "Aguardar nova captura após atualização e conferência da radiação"
            if pending else "Ilustração da interface fornecida pelo autor",
        })
    crops = []
    # Recortes da barra lateral; não se redesenham controles, textos ou dados.
    for name in ["geojson_upload", "geojson_arquivo", "geojson_importado"]:
        source = OUTPUT / f"{name}.png"
        target = OUTPUT / f"{name}_barra.png"
        box = (0, 0, 264, 871 if name == "geojson_importado" else 783)
        with Image.open(source) as image:
            image.crop(box).save(target)
        crops.append({
            "source": str(source.relative_to(ROOT)),
            "output": str(target.relative_to(ROOT)),
            "box_px": list(box),
            "sha256": digest(target),
        })
    manifest = {
        "source_context": "Capturas declaradas reais e fornecidas pelo autor nesta revisão",
        "capture_date": None,
        "desktop_commit": None,
        "mobile_device_and_browser_version": None,
        "limits": [
            "Não substituem a demonstração instrumentada anterior nem seus resultados.",
            "Capturas não comprovam equivalência com o código corrigido.",
            "A série na imagem fornecida tem eixo temporal fora do enquadramento.",
            "Mobile mostra outra área; não é continuação da análise desktop.",
        ],
        "originals": records,
        "editorial_crops": crops,
    }
    (AUDIT / "manifesto.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    )
    print("17 originais preservados; 16 usados no artigo, 1 PDF pendente; 3 recortes de barra.")


if __name__ == "__main__":
    main()
