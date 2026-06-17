# Spec: Fluxo Completo (MVP)

## Propósito

Definir e validar o fluxo completo do MVP, integrando todos os componentes do sistema em um pipeline único que vai da seleção da área até a exibição dos resultados.

## Interface

```python
def run_analysis(
    geometry: ee.Geometry,
    start_date: str,
    end_date: str,
    index_name: str
) -> dict
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `geometry` | `ee.Geometry` | Área desenhada pelo usuário |
| `start_date` | `str` | Data inicial |
| `end_date` | `str` | Data final |
| `index_name` | `str` | "NDVI" ou "NDWI" |

**Retorno**: `dict` com as chaves:
- `index_map`: `ee.Image` — imagem do índice para exibição
- `time_series`: `list[dict]` — série temporal
- `time_series_plot`: `plotly.Figure` — gráfico da série
- `anomalies`: `list[dict]` — detecções de anomalia
- `alert`: `str | None` — alerta se houver anomalia
- `climate_data`: `pd.DataFrame` — dados climáticos
- `climate_plot`: `plotly.Figure` — gráfico climático
- `mean_value`: `float` — valor médio do índice
- `area_ha`: `float` — área em hectares

## Pipeline Completo

```
geometry, start, end, index_name
    |
    v
1. Buscar ImageCollection (spec-busca-imagem)
2. Aplicar filtro de nuvens (spec-filtro-nuvem)
3. Aplicar filtros de data/área (spec-filtro-data-area)
4. Calcular índice (spec-ndvi ou spec-ndwi) via .map()
5. Selecionar imagem mediana da coleção (collection.median())
6. Criar mapa base + adicionar camada + legenda
7. Computar série temporal (spec-serie-temporal)
8. Plotar série temporal
9. Detectar anomalias na série (spec-deteccao-anomalias)
10. Gerar alerta se necessário
11. Buscar dados climáticos (spec-nasa-power)
12. Plotar dados climáticos
13. Calcular área em hectares (geometry.area().divide(10000))
14. Calcular valor médio do índice na área
15. Retornar dict com todos os resultados
```

## Regras de Negócio

- Se qualquer etapa falhar, retornar dict parcial com erro + `success: False`
- Conversão de área: `ee.Geometry.area()` retorna m²; dividir por 10.000 para hectares
- Imagem mediana: `collection.median()` reduz coleção a uma imagem representativa
- `run_analysis` não gerencia UI; apenas processa dados

## Critérios de Aceitação

1. Dado pipeline completo com dados válidos, então retorna dict com todas as chaves
2. Dado erro em etapa intermediária, então retorna dict com `success: False` e campo `error`
3. Área calculada está em hectares (m² / 10000)
4. Valor médio do índice está entre -1 e 1

## Testes de Integração

O MVP deve ser validado com teste de integração que executa o pipeline completo:

```python
def test_full_pipeline():
    # Usar geometria de teste, datas mock
    # Verificar que todos os resultados são gerados
    # Verificar que gráficos são Plotly Figures
    # Verificar que alertas estão no formato correto
```

## Tasks Relacionadas

- TASK-043 — Fluxo completo
- TASK-044 — Corrigir bugs
- TASK-045 — Validar MVP

## Dependências

- Todas as specs anteriores (01 a 08)
