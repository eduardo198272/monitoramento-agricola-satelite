# Tasks: Integração de Dados Climáticos (NASA POWER)

Referência: `docs/specs/08-clima/spec-nasa-power.md`

| ID | Descrição | Critério de Aceitação | Esforço |
|---|---|---|---|
| SPEC-08-01 | Implementar `fetch_climate_data(geometry, start_date, end_date, parameters)` com requisição GET à API POWER | DataFrame com colunas date, precipitation, temperature | 2h |
| SPEC-08-02 | Extrair coordenada central da geometry e construir URL da API | Coordenadas extraídas corretamente | 30min |
| SPEC-08-03 | Converter valores nulos (-999) para None no DataFrame | Dados limpos sem -999 | 30min |
| SPEC-08-04 | Escrever testes com mock de requisição HTTP: dados válidos, erro de API | 2+ testes passando | 1h |
| SPEC-08-05 | Implementar `plot_climate_data(climate_df)` com Plotly (barras precip + linha temp) | Figure com eixo Y duplo | 1h |
| SPEC-08-06 | Escrever testes: plot com dados, plot com DataFrame vazio | 2 testes passando | 30min |
