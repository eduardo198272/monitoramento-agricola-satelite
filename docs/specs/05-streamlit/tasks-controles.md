# Tasks: Controles da Interface

Referência: `docs/specs/05-streamlit/spec-controles.md`

| ID | Descrição | Critério de Aceitação | Esforço |
|---|---|---|---|
| SPEC-05-04 | Implementar `st.sidebar.date_input` para data inicial (default 12 meses atrás) e final (default hoje) | Campos de data com valores padrão | 1h |
| SPEC-05-05 | Implementar `st.sidebar.selectbox` para NDVI/NDWI | Dropdown com opções | 30min |
| SPEC-05-06 | Implementar `st.sidebar.button("Analisar")` desabilitado se datas inválidas | Botão habilitado só com datas válidas | 1h |
| SPEC-05-07 | Implementar validação: data final >= data inicial exibe erro via `st.error` | Mensagem de erro visível quando inválido | 30min |
| SPEC-05-08 | Escrever testes com AppTest: renderizar controles, validar datas, clicar botão | 3+ testes passando | 1h |
