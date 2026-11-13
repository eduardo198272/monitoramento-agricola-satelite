# Tasks: Organização dos Resultados e Alertas da Análise

Referência: `docs/specs/12-interface-resultados/spec-interface-resultados.md`

| ID | Descrição | Critério de Aceitação | Esforço |
|---|---|---|---|
| SPEC-12-01 | Reorganizar o layout principal após o mapa de seleção | Resumo aparece imediatamente após o mapa de seleção | 1h |
| SPEC-12-02 | Separar visualmente mapa de seleção e mapa temático | Cada mapa possui título e finalidade claros | 30min |
| SPEC-12-03 | Ajustar altura e largura responsiva dos mapas | Uso adequado em desktop e mobile | 45min |
| SPEC-12-04 | Alterar `display_summary()` para receber unidade da área | Cards exibem métricas sem alertas duplicados | 45min |
| SPEC-12-05 | Remover renderização de alerta de `display_summary()` | Nenhuma anomalia aparece no painel em vermelho | 30min |
| SPEC-12-06 | Criar ou consolidar `display_anomaly_alert()` com `st.warning()` | Cada alerta é exibido uma única vez em amarelo | 30min |
| SPEC-12-07 | Manter `st.error()` exclusivamente para erros técnicos e validações | Erros continuam visíveis em vermelho | 30min |
| SPEC-12-08 | Ordenar mapa temático, série temporal e clima após o resumo | Saídas aparecem na ordem definida pela spec | 45min |
| SPEC-12-09 | Garantir que reruns não repitam mensagens nem processem novamente | Estado e resultados permanecem estáveis | 1h |
| SPEC-12-10 | Criar testes de layout e mensagens | Ordem, unicidade e semântica dos alertas cobertas | 1h30 |
