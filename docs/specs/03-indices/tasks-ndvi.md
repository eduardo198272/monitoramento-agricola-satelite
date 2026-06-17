# Tasks: Cálculo de NDVI

Referência: `docs/specs/03-indices/spec-ndvi.md`

| ID | Descrição | Critério de Aceitação | Esforço |
|---|---|---|---|
| SPEC-03-01 | Implementar `calculate_ndvi(image)` usando `image.normalizedDifference(["B8", "B4"])` | Retorna imagem com banda "NDVI" | 1h |
| SPEC-03-02 | Escrever testes mockados: NIR > Red → NDVI > 0; NIR = Red → NDVI = 0; NIR < Red → NDVI < 0 | 3 testes passando com valores esperados | 1h |
| SPEC-03-03 | Validar funcionamento via `.map()` em ImageCollection | `collection.map(calculate_ndvi)` produz coleção com banda NDVI | 30min |
| SPEC-03-04 | Testar erro quando bandas B8 ou B4 estão ausentes | Lança exceção apropriada | 30min |
