# Spec: Integração de Dados Climáticos (NASA POWER)

## Propósito

Fornecer funções para buscar dados climáticos históricos da API NASA POWER para a área e período selecionados, incluindo precipitação e temperatura.

## Interface

```python
def fetch_climate_data(
    geometry: ee.Geometry,
    start_date: str,
    end_date: str,
    parameters: list[str] = None
) -> pd.DataFrame
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `geometry` | `ee.Geometry` | Área de interesse (para extrair coordenadas centrais) |
| `start_date` | `str` | Data inicial "YYYY-MM-DD" |
| `end_date` | `str` | Data final "YYYY-MM-DD" |
| `parameters` | `list[str]` ou `None` | Parâmetros POWER. Default: `["PRECTOTCORR", "T2M"]` |

**Retorno**: `pd.DataFrame` — colunas: `date`, `precipitation`, `temperature`.

## Regras de Negócio

- API: `https://power.larc.nasa.gov/api/temporal/daily/point`
- Extrair coordenada central da geometry: `geometry.centroid().coordinates()`
- Formato da request: GET com parâmetros `parameters`, `start`, `end`, `latitude`, `longitude`, `format=JSON`
- Parâmetros POWER:
  - `PRECTOTCORR`: precipitação diária corrigida (mm/dia)
  - `T2M`: temperatura média diária a 2m (°C)
  - `T2M_MAX`: temperatura máxima diária (°C)
  - `T2M_MIN`: temperatura mínima diária (°C)
- Converter resposta JSON para DataFrame com colunas padronizadas
- Valores nulos na API (código -999) devem ser convertidos para `None`
- Se API retornar erro, lançar exceção descritiva

```python
def plot_climate_data(climate_df: pd.DataFrame) -> plotly.graph_objects.Figure
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `climate_df` | `pd.DataFrame` | Dados climáticos com `date`, `precipitation`, `temperature` |

**Retorno**: `plotly.graph_objects.Figure` — gráfico de barras + linha.

## Regras de Negócio (Plotagem)

- Usar Plotly
- Eixo X: datas
- Eixo Y esquerdo: precipitação (barras, azul)
- Eixo Y direito: temperatura (linha, vermelha)
- Título: "Dados Climáticos - Precipitação e Temperatura"
- Grid visível

## Critérios de Aceitação

1. Dado geometry com coordenadas válidas, quando buscar clima, então retorna DataFrame não vazio
2. DataFrame contém colunas "date", "precipitation", "temperature"
3. Dado geometry sem coordenadas, quando buscar, então lança ValueError
4. Dado parâmetros personalizados, quando buscar, então retorna colunas adicionais
5. Dado climate_df não vazio, quando plotar, então retorna Figure com barras e linha

## Tasks Relacionadas

- TASK-039 — API NASA
- TASK-040 — Chuva
- TASK-041 — Temperatura
- TASK-042 — Gráfico clima

## Dependências

- `06-series-temporais/spec-serie-temporal.md`
