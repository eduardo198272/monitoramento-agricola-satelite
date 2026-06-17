# Tasks: Integração do Mapa na UI

Referência: `docs/specs/05-streamlit/spec-mapa-ui.md`

| ID | Descrição | Critério de Aceitação | Esforço |
|---|---|---|---|
| SPEC-05-09 | Implementar `display_map(map_obj)` com `map_obj.to_streamlit(height=600)` | Mapa renderizado na área principal | 1h |
| SPEC-05-10 | Implementar `display_summary(index_name, mean_value, area_ha, trend, alert)` com st.metric | Painel de resumo com indicadores e tendência | 1h |
| SPEC-05-11 | Adicionar spinner (`st.spinner`) durante processamento | Spinner visível enquanto processa | 30min |
| SPEC-05-12 | Exibir st.error se processamento falhar | Erro exibido no lugar do mapa | 30min |
| SPEC-05-13 | Estado inicial: mensagem "Selecione uma área e clique em Analisar" | Texto inicial antes da primeira análise | 30min |
| SPEC-05-14 | Escrever testes com AppTest: fluxo completo UI | Testes de integração da interface | 1h |
