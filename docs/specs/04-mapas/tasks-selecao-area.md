# Tasks: Seleção de Área no Mapa

Referência: `docs/specs/04-mapas/spec-selecao-area.md`

| ID | Descrição | Critério de Aceitação | Esforço |
|---|---|---|---|
| SPEC-04-12 | Implementar `enable_area_draw(map_obj, draw_type)` com DrawControl do ipyleaflet | Ferramenta de desenho habilitada no mapa | 1h |
| SPEC-04-13 | Implementar `get_drawn_geometry(map_obj)` extraindo coordenadas como `ee.Geometry` | Retorna ee.Geometry ou None se sem desenho | 1h |
| SPEC-04-14 | Escrever testes: polígono desenhado, retângulo desenhado, nenhum desenho | 3 testes passando | 1h |
