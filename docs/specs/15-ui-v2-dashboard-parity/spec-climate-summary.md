# Spec: SPEC-15-06 — Resumo agregado de dados climáticos NASA POWER

## Propósito

Fornecer agregadores puros que transformam o DataFrame diário retornado por
`fetch_climate_data()` em métricas resumidas para exibição na UI: precipitação
acumulada, temperatura média e radiação solar média diária. Manter a função pura
(sem efeitos colaterais, sem chamadas HTTP/EE) e testável.

## Escopo

Incluído:
- Nova função `summarize_climate_data(climate_df: pd.DataFrame) -> dict` em
  `src/app/climate.py`
- Retorno com chaves: `total_precipitation_mm`,
  `mean_temperature_c`, `mean_solar_radiation_mj_m2_day`
- Conversão de radiação: NASA POWER entrega `ALLSKY_SFC_SW_DWN` em
  kWh/m²/dia → multiplicar por 3.6 para obter MJ/m²/dia (unidade citada na
  metodologia do TCC)
- Tratamento de valores nulos/ausentes: ignorar `None` e `NaN` nos cálculos
- DataFrame vazio ou colunas ausentes → retornar dicionário com valores `None`
- Não mutar o DataFrame de entrada

Não incluído:
- Alteração em `fetch_climate_data()` ou no formato dos dados diários
- Alteração no gráfico climático existente
- Agregações por janela móvel, percentis ou outras estatísticas

## Contrato de dados

### Função

```python
def summarize_climate_data(climate_df: pd.DataFrame) -> dict:
    """
    Retorna {"total_precipitation_mm": float|None,
             "mean_temperature_c": float|None,
             "mean_solar_radiation_mj_m2_day": float|None}.
    """
```

### Regras de cálculo

| Métrica | Coluna origem | Fórmula | Unidade saída |
|---------|---------------|---------|---------------|
| Precipitação total | `precipitation` | soma de valores válidos | mm |
| Temperatura média | `temperature` | média de valores válidos | °C |
| Radiação solar média | `solar_radiation` | média de valores válidos × 3.6 | MJ/m²/dia |

Valores válidos = não nulos (`not pd.isna(v)`). Se não houver nenhum valor válido para
uma métrica, o resultado dessa chave é `None`.

### Exemplos

```python
# DataFrame completo
df = pd.DataFrame({
    "date": ["2024-01-01", "2024-01-02", "2024-01-03"],
    "precipitation": [5.0, None, 3.5],
    "temperature": [25.0, 26.5, None],
    "solar_radiation": [6.0, 5.5, 7.0],  # kWh/m²/dia
})
summarize_climate_data(df)
# {"total_precipitation_mm": 8.5,
#  "mean_temperature_c": 25.75,
#  "mean_solar_radiation_mj_m2_day": 22.2}  # (6.0+5.5+7.0)/3 * 3.6

# DataFrame vazio
summarize_climate_data(pd.DataFrame())
# {"total_precipitation_mm": None,
#  "mean_temperature_c": None,
#  "mean_solar_radiation_mj_m2_day": None}
```

## Integração no pipeline

- `run_analysis()` e `run_multi_analysis()` chamam `summarize_climate_data()`
  sobre o `climate_df` obtido e anexam o dicionário ao resultado sob a chave
  `climate_summary` (mantendo `climate_data` e `climate_plot` inalterados).
- Se `climate_df` for `None` ou vazio, `climate_summary` contém três `None`.

## Requisitos de interface

- Na seção "Dados Climáticos (NASA POWER)" da UI, abaixo do gráfico, exibir
  cards/métricas quando `climate_summary` tiver pelo menos um valor não-`None`:
  - **Precipitação total**: X.Y mm
  - **Temperatura média**: X.Y °C
  - **Radiação solar média**: X.Y MJ/m²/dia
- Se todos os valores forem `None`, não exibir cards de resumo.
- Unidades explícitas em cada card.

## Critérios de aceitação

1. `summarize_climate_data` retorna as três chaves com unidades corretas a partir
   de DataFrame válido (teste unitário com mocks/pandas)
2. Função ignora `None`/`NaN` nos cálculos
3. Função retorna `None` por métrica quando não há valores válidos
4. Função não muta o DataFrame de entrada
5. Conversão de radiação kWh/m²/dia → MJ/m²/dia (×3.6) aplicada corretamente
6. Pipeline anexa `climate_summary` aos resultados de `run_analysis` e
   `run_multi_analysis`
7. UI exibe cards de resumo quando há dados; não exibe quando ausentes
8. `python -m pytest tests/ --no-cov` passa (≥100% cobertura configurada)
9. `git diff --check` passa
10. App roda em `http://localhost:8501` — HTTP 200

## Validação visual

- Executar análise com dados climáticos válidos: três cards aparecem com
  unidades corretas
- Executar análise sem dados climáticos (falha de API): nenhum card de resumo
- Verificar que valores batem com cálculo manual dos dados diários mostrados
  no gráfico

## Dependências

- SPEC-15-05 (contexto geográfico — centroide já disponível para clima)
- `src/app/climate.py`, `src/app/pipeline.py`, `src/app/main.py`
- `tests/test_climate.py`, `tests/test_pipeline.py`, `tests/test_streamlit_app.py`