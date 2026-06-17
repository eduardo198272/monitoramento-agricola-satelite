# Tasks: Cálculo de NDMI

Referência: `docs/specs/03-indices/spec-ndmi.md`

| ID | Descrição | Critério de Aceitação | Esforço |
|---|---|---|---|
| SPEC-03-09 | Implementar `calculate_ndmi(image)` usando `image.normalizedDifference(["B8A", "B11"])` | Retorna imagem com banda "NDMI" | 1h |
| SPEC-03-10 | Escrever testes mockados: NIR > SWIR → NDMI > 0; NIR = SWIR → NDMI = 0; NIR < SWIR → NDMI < 0 | 3 testes passando com valores esperados | 1h |
| SPEC-03-11 | Validar funcionamento via `.map()` em ImageCollection | `collection.map(calculate_ndmi)` produz coleção com banda NDMI | 30min |
| SPEC-03-12 | Testar erro quando bandas B8A ou B11 estão ausentes | Lança exceção apropriada | 30min |
