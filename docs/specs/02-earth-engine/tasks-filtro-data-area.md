# Tasks: Filtros de Data e Área

Referência: `docs/specs/02-earth-engine/spec-filtro-data-area.md`

| ID | Descrição | Critério de Aceitação | Esforço |
|---|---|---|---|
| SPEC-02-09 | Implementar `filter_by_date(collection, start_date, end_date)` com validação de formato ISO e ordem | Filtra por `ee.Filter.date`; lança `ValueError` se inválido | 1h |
| SPEC-02-10 | Implementar `filter_by_area(collection, geometry)` com `ee.Filter.bounds` | Filtra imagens que intersectam a geometria | 30min |
| SPEC-02-11 | Escrever testes para filter_by_date: datas válidas, start > end, formato inválido | 3+ testes passando | 1h |
| SPEC-02-12 | Escrever testes para filter_by_area: geometria válida, geometria nula | 2+ testes passando | 30min |
| SPEC-02-13 | Testar composição dos filtros: `filter_by_date(filter_by_area(...), ...)` | Ambos filtros aplicados corretamente em sequência | 30min |
