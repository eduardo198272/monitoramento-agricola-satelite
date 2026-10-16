# Tasks: UI V2 — Paridade Visual do Dashboard

Referência: `spec-ui-dashboard-parity.md`.

| ID | Descrição | Critério de aceite | Dependências | Status |
|---|---|---|---|---|
| SPEC-15-01 | Versionar a imagem-base e fechar contratos visuais/dados | A imagem enviada está em `assets/dashboard-reference.png`; viewport (1536 × 1024) e campos exibidos estão identificados sem métricas sem fonte | Arquivo original fornecido | Concluída |
| SPEC-15-02 | Especificar e configurar tiles Esri no mapa de seleção | `create_selection_map` configura World Imagery explicitamente, atribuição e escala; teste confirma tile layer | SPEC-15-01 | Concluída |
| SPEC-15-03 | Preservar base satélite no mapa temático | `create_thematic_map` exibe a base satélite sob camada temática translúcida e mantém polígono/legenda | SPEC-15-02 | Não iniciado |
| SPEC-15-04 | Construir cabeçalho e barra compacta de controles | Busca, período, índices e análise organizados conforme baseline, mantendo contratos de estado e validação | SPEC-15-01 | Não iniciado |
| SPEC-15-05 | Exibir contexto geográfico da área real | Área em ha; perímetro/centroide somente se calculados geoespacialmente e sem consultas redundantes | SPEC-15-02 | Não iniciado |
| SPEC-15-06 | Implementar agregadores puros para NASA POWER | Precipitação acumulada, temperatura média e radiação média/conversão com nulos e unidades testados | SPEC-15-01 | Não iniciado |
| SPEC-15-07 | Reorganizar painéis de resultados após sucesso | Cards, série, clima, mapa temático e anomalias só renderizam após sucesso e usam dados reais | SPEC-15-04, SPEC-15-05, SPEC-15-06 | Não iniciado |
| SPEC-15-08 | Implementar estados single-index e multiíndice | Single mostra somente índice analisado; Todos mostra índices retornados; troca visual não repete pipeline | SPEC-15-07 | Não iniciado |
| SPEC-15-09 | Aplicar fidelidade visual e responsividade | Comparação desktop contra imagem e layout mobile sem overflow; CSS centralizado | SPEC-15-04, SPEC-15-07 | Não iniciado |
| SPEC-15-10 | Cobrir regressões, executar validação e registrar limitações | Testes isolados passam, cobertura configurada é mantida e checklist visual está documentado | SPEC-15-02 a SPEC-15-09 | Não iniciado |

## Ordem de execução

1. Receber/versionar a imagem original e fechar viewport/campos (SPEC-15-01).
2. Implementar camada-base dos mapas e validar atribuição (SPEC-15-02/03).
3. Reorganizar estrutura da página e contexto da área (SPEC-15-04/05).
4. Criar e testar agregação climática antes de conectar os cartões (SPEC-15-06).
5. Montar painéis condicionados a sucesso e estados single/multi-index
   (SPEC-15-07/08).
6. Ajustar CSS responsivo e revisar visualmente contra baseline (SPEC-15-09).
7. Executar suíte, cobertura e validação operacional de tiles (SPEC-15-10).

## Regras de execução

- Seguir SDD/TDD: atualizar a spec da tarefa, escrever testes primeiro, verificar
  falha, implementar e verificar novamente.
- Não adicionar valores exemplificativos à aplicação para simular a referência.
- Não alterar a lógica científica sem spec específica e validação.
- Mockar Earth Engine, NASA POWER e quaisquer requests nos testes automatizados.
- Verificar contagem de chamadas para impedir consultas remotas redundantes.
- Confirmar visualmente o tile service em browser; falhas de rede não devem ser
  confundidas com falha do pipeline de análise.
- Seguir branch/worktree e PR definidos em `.agent-context/development-rules.md`.
