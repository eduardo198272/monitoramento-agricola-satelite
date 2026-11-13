# Tasks: Série Temporal

Referência: `docs/specs/06-series-temporais/spec-serie-temporal.md`

| ID | Descrição | Critério de Aceitação | Esforço |
|---|---|---|---|
| SPEC-06-01 | Implementar `compute_time_series(collection, geometry, index_name, scale)` com `reduceRegion(ee.Reducer.mean())` | Retorna `list[dict]` ordenada por data | 2h |
| SPEC-06-02 | Extrair data via `image.date().format("YYYY-MM-dd")` | Campo "date" em formato ISO | 30min |
| SPEC-06-03 | Remover entradas com valor None (sem dados na região) | Lista filtrada sem None | 30min |
| SPEC-06-04 | Escrever testes: série com dados, coleção vazia, valores None removidos | 3+ testes mockados | 1h |
| SPEC-06-05 | Implementar `plot_time_series(data, index_name)` com Plotly (scatter + line) | Figure do Plotly com eixo Y -1 a 1 | 1h |
| SPEC-06-06 | Escrever testes: plot com dados, plot sem dados (retorna None) | 2 testes passando | 30min |
