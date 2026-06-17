# Tasks: Buscar Imagem Sentinel-2

Referência: `docs/specs/02-earth-engine/spec-busca-imagem.md`

| ID | Descrição | Critério de Aceitação | Esforço |
|---|---|---|---|
| SPEC-02-01 | Implementar função `get_image_collection(geometry, start_date, end_date, cloud_cover_max)` com assinatura completa | Função criada no módulo `earth_engine.py`, retorna `ee.ImageCollection` | 1h |
| SPEC-02-02 | Implementar filtro de data (`ee.Filter.date`) e geometria (`ee.Filter.bounds`) na coleção | Coleção filtrada corretamente por data e área | 30min |
| SPEC-02-03 | Implementar filtro de cobertura de nuvens (`CLOUD_COVERAGE_ASSESSMENT`) | Coleção filtrada por `cloud_cover_max` | 30min |
| SPEC-02-04 | Escrever testes parametrizados: datas válidas, geometria, cloud_cover_max=0, cloud_cover_max=100, coleção vazia | 4+ testes passando com cobertura | 1h |
| SPEC-02-05 | Tratar edge cases: data inválida, geometria nula, período sem imagens | Lança `ValueError` para entrada inválida, coleção vazia para sem dados | 30min |
