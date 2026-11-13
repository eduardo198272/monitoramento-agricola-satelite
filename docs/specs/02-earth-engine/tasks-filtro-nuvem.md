# Tasks: Filtro de Nuvens (QA60)

Referência: `docs/specs/02-earth-engine/spec-filtro-nuvem.md`

| ID | Descrição | Critério de Aceitação | Esforço |
|---|---|---|---|
| SPEC-02-06 | Implementar função `mask_clouds(image)` extraindo banda QA60 e aplicando máscara nos bits 10 e 11 | Função retorna imagem com updateMask aplicado | 1h |
| SPEC-02-07 | Escrever testes para mask_clouds: pixel com nuvem (bit10=1), pixel com cirro (bit11=1), pixel limpo | 3 testes mockados passando | 1h |
| SPEC-02-08 | Integrar mask_clouds com get_image_collection via `.map()` | `collection.map(mask_clouds)` executável sem erro | 30min |
