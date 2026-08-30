# Tasks: Pesquisa, Centralização e Bloqueio do Mapa

Referência: `docs/specs/10-mapas-interacao/spec-mapa-interacao.md`

| ID | Descrição | Critério de Aceitação | Esforço |
|---|---|---|---|
| SPEC-10-01 | Implementar cliente de geocodificação com Nominatim usando `requests`, timeout e `User-Agent` | Consulta válida retorna localidade, coordenadas e limites | 1h30 |
| SPEC-10-02 | Validar consultas vazias e normalizar a entrada do usuário | Consulta vazia não gera requisição | 30min |
| SPEC-10-03 | Tratar localidade não encontrada, timeout, HTTP error e JSON inválido | Cada falha gera mensagem orientativa sem quebrar a UI | 1h |
| SPEC-10-04 | Implementar `calculate_map_zoom(boundingbox)` | Zoom válido entre 1 e 20 é calculado para diferentes extensões | 1h |
| SPEC-10-05 | Adicionar campo de pesquisa e botão na sidebar | Usuário consegue pesquisar e recebe o nome encontrado | 1h |
| SPEC-10-06 | Persistir consulta, centro, zoom e resultado em `st.session_state` | Estado permanece após rerun | 1h |
| SPEC-10-07 | Criar `create_selection_map()` com Folium e `streamlit-folium` | Mapa renderiza e retorna eventos do desenho | 1h30 |
| SPEC-10-08 | Configurar Draw para permitir somente polígonos | Ferramentas de linha, retângulo, círculo e marcador ficam desabilitadas | 30min |
| SPEC-10-09 | Validar GeoJSON e converter polígono para `ee.Geometry` | Feature válida é convertida; entradas inválidas são rejeitadas | 1h |
| SPEC-10-10 | Implementar centralização e enquadramento do polígono | Área selecionada permanece visível e centralizada | 1h |
| SPEC-10-11 | Implementar estado bloqueado do mapa | Arraste, zoom e gestos não alteram a visualização | 1h30 |
| SPEC-10-12 | Implementar `Limpar seleção` e remoção do desenho | Estado é limpo e mapa volta a aceitar navegação | 1h |
| SPEC-10-13 | Remover referências de áreas pré-definidas da documentação, UI e testes | Não há opção nem dependência de talhões fixos | 1h |
| SPEC-10-14 | Criar testes unitários e funcionais do fluxo | Pesquisa, validação, persistência, bloqueio e limpeza cobertos | 2h |
