# Tasks: Seleção de Área no Mapa

Referência: `docs/specs/04-mapas/spec-selecao-area.md`

| ID | Descrição | Critério de Aceitação | Esforço |
|---|---|---|---|
| SPEC-04-12 | Implementar controle base de desenho de polígono | Ferramenta de desenho disponível no mapa | 1h |
| SPEC-04-13 | Implementar conversão de GeoJSON para `ee.Geometry.Polygon` | Retorna geometria válida ou erro de validação | 1h |
| SPEC-04-14 | Escrever testes de polígono válido, inválido e ausência de seleção | Cenários de seleção cobertos | 1h |
| SPEC-04-15 | Remover áreas pré-definidas da UI, API e testes | Seleção ocorre exclusivamente por polígono | 1h |
| SPEC-04-16 | Integrar mapa de seleção ao Streamlit | GeoJSON é recebido pelo Python após o desenho | 1h30 |
| SPEC-04-17 | Validar fluxo básico de seleção no navegador | Usuário desenha e confirma área sem erro | 1h |
