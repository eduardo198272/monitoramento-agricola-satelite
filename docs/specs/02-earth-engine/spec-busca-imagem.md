# Spec: Buscar Imagem Sentinel-2

## Propósito

Fornecer função que busca imagens Sentinel-2 do Google Earth Engine para uma área geográfica e período específicos, retornando a coleção filtrada pronta para processamento.

## Interface

```python
def get_image_collection(
    geometry: ee.Geometry,
    start_date: str,
    end_date: str,
    cloud_cover_max: int = 20
) -> ee.ImageCollection
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `geometry` | `ee.Geometry` | Polígono ou retângulo da área de interesse |
| `start_date` | `str` | Data inicial no formato "YYYY-MM-DD" |
| `end_date` | `str` | Data final no formato "YYYY-MM-DD" |
| `cloud_cover_max` | `int` | Percentual máximo de cobertura de nuvens (0-100, default 20) |

**Retorno**: `ee.ImageCollection` — coleção filtrada de imagens Sentinel-2.

## Regras de Negócio

- Usar coleção `COPERNICUS/S2_SR_HARMONIZED` (Surface Reflectance)
- Filtrar por data com `ee.Filter.date(start_date, end_date)`
- Filtrar por bounds com `ee.Filter.bounds(geometry)`
- Filtrar por cobertura de nuvens com `ee.Filter.lt("CLOUD_COVERAGE_ASSESSMENT", cloud_cover_max)`
- Se `cloud_cover_max` for 0, retornar imagens com cobertura mínima
- Se nenhuma imagem encontrada, retornar `ee.ImageCollection([])` vazia (não lançar erro)
- A coleção retornada deve incluir as bandas: `B2`, `B3`, `B4`, `B8`, `QA60`

## Critérios de Aceitação

1. Dado geometry, start_date e end_date válidos, quando chamar `get_image_collection`, então retorna um `ee.ImageCollection` não nulo
2. Dado período sem imagens disponíveis, quando chamar `get_image_collection`, então retorna coleção vazia
3. Dado `cloud_cover_max=0`, quando filtrar, então retorna apenas imagens sem nuvens
4. Dado `cloud_cover_max=100`, quando filtrar, então retorna todas as imagens disponíveis

## Tasks Relacionadas

- TASK-012 — Buscar imagem
- TASK-013 — Função get_image

## Dependências

- `01-visao-geral/spec-visao-geral.md`
