# Spec: Série Temporal

## Propósito

Fornecer funções para calcular a evolução temporal de um índice (NDVI/NDWI) ao longo do período selecionado, gerando dados para plotagem de gráficos.

## Interface

```python
def compute_time_series(
    collection: ee.ImageCollection,
    geometry: ee.Geometry,
    index_name: str,
    scale: int = 10
) -> list[dict]
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `collection` | `ee.ImageCollection` | Coleção com imagens que já contêm a banda do índice |
| `geometry` | `ee.Geometry` | Área de interesse para reduzir a região |
| `index_name` | `str` | Nome da banda do índice ("NDVI" ou "NDWI") |
| `scale` | `int` | Escala em metros para redução (default 10) |

**Retorno**: `list[dict]` — lista de dicionários com `{"date": "YYYY-MM-DD", "value": float}`.

## Regras de Negócio

- Para cada imagem na coleção, reduzir a região com `image.reduceRegion(reducer=ee.Reducer.mean(), geometry=geometry, scale=scale)`
- Extrair a data da imagem com `image.date().format("YYYY-MM-dd")`
- Ordenar resultados por data (crescente)
- Remover entradas onde o valor do índice é `None` (não há dados válidos na área)
- Retornar lista vazia se coleção estiver vazia
- Não modificar a coleção original

## Critérios de Aceitação

1. Dado collection com imagens, quando computar série, então retorna lista ordenada por data
2. Dado collection vazia, quando computar, então retorna lista vazia
3. Dado image sem dados na região, quando reduzir, então valor é None e removido da lista
4. Cada entrada contém "date" (string ISO) e "value" (float)

## Plotagem

```python
def plot_time_series(data: list[dict], index_name: str) -> plotly.graph_objects.Figure
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `data` | `list[dict]` | Lista de pontos `{"date": ..., "value": ...}` |
| `index_name` | `str` | Nome do índice para título/eixo Y |

**Retorno**: `plotly.graph_objects.Figure` — figura do Plotly.

## Regras de Negócio (Plotagem)

- Usar Plotly (`plotly.graph_objects.Figure`)
- Eixo X: datas
- Eixo Y: valor do índice (-1 a 1)
- Título: "Evolução Temporal de {index_name}"
- Linha com marcadores (scatter + line)
- Grid visível
- Layout responsivo para caber no Streamlit

## Critérios de Aceitação (Plotagem)

1. Dado data não vazio, quando plotar, então retorna Figure do Plotly
2. Gráfico tem título "Evolução Temporal de NDVI" ou "Evolução Temporal de NDWI"
3. Eixo Y varia de -1 a 1
4. Dado data vazio, quando plotar, então retorna None

## Tasks Relacionadas

- TASK-031 — Loop
- TASK-032 — NDVI time
- TASK-033 — Plot
- TASK-034 — UI

## Dependências

- `03-indices/spec-ndvi.md` ou `03-indices/spec-ndwi.md`
- `02-earth-engine/spec-filtro-data-area.md`
