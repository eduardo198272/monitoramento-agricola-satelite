# Tasks: Cálculo de NDWI

Referência: `docs/specs/03-indices/spec-ndwi.md`

| ID | Descrição | Critério de Aceitação | Esforço |
|---|---|---|---|
| SPEC-03-05 | Implementar `calculate_ndwi(image)` usando `image.normalizedDifference(["B3", "B8"])` | Retorna imagem com banda "NDWI" | 1h |
| SPEC-03-06 | Escrever testes mockados: Green > NIR → NDWI > 0; Green = NIR → NDWI = 0; Green < NIR → NDWI < 0 | 3 testes passando com valores esperados | 1h |
| SPEC-03-07 | Validar funcionamento via `.map()` em ImageCollection | `collection.map(calculate_ndwi)` produz coleção com banda NDWI | 30min |
| SPEC-03-08 | Testar erro quando bandas B3 ou B8 estão ausentes | Lança exceção apropriada | 30min |
