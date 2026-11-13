# Tasks: Visualização de Índice no Mapa

Referência: `docs/specs/04-mapas/spec-visualizacao-indice.md`

| ID | Descrição | Critério de Aceitação | Esforço |
|---|---|---|---|
| SPEC-04-05 | Implementar `add_index_layer(map_obj, index_image, index_name, palette, opacity)` com `map_obj.addLayer()` | Camada adicionada ao mapa com min=-1, max=1 | 1h |
| SPEC-04-06 | Definir paletas padrão: NDVI=["blue","white","green"], NDWI=["brown","white","blue"] | Paletas aplicadas conforme index_name | 30min |
| SPEC-04-07 | Escrever testes: paleta padrão NDVI, paleta padrão NDWI, paleta personalizada | 3 testes passando | 1h |
| SPEC-04-08 | Testar erro quando banda do índice não existe na imagem | Lança ValueError | 30min |
