# Tasks: Mapa Base

Referência: `docs/specs/04-mapas/spec-mapa-base.md`

| ID | Descrição | Critério de Aceitação | Esforço |
|---|---|---|---|
| SPEC-04-01 | Implementar `create_base_map(center, zoom)` com `geemap.Map()` | Mapa criado com centro e zoom especificados | 1h |
| SPEC-04-02 | Configurar centro padrão (-28.0, -52.0) e zoom 10 | center=None usa coordenadas de Passo Fundo/RS | 30min |
| SPEC-04-03 | Adicionar Layer Control e barra de escala ao mapa | Controles visíveis no mapa renderizado | 30min |
| SPEC-04-04 | Escrever teste: centro personalizado vs centro padrão | 2 testes passando | 30min |
| SPEC-04-05 | Escrever teste de renderização: mapa criado é instância de geemap.Map e compatível com to_streamlit | 1 teste passando | 30min |
