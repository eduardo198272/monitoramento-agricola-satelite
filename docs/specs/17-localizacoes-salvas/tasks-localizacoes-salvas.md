# Tasks: Localizações Salvas

Referência: `spec-localizacoes-salvas.md`.

| ID | Descrição | Critério de aceite | Dependências | Esforço | Status |
|---|---|---|---|---:|---|
| SPEC-17-01 | Definir contrato persistente e configuração SQLite | Caminho configurável/default documentado, tabela/migração inicial e contrato CRUD definidos; nenhum dado salvo em `session_state` como armazenamento primário | Critérios desta spec | 1h30 | Concluída |
| SPEC-17-02 | Implementar repositório SQLite de localizações | Inicialização idempotente, conexão segura, transações e CRUD operam com banco temporário; erros de I/O convertidos em erros tratáveis | SPEC-17-01 | 2h | Concluída |
| SPEC-17-03 | Validar/normalizar nome e GeoJSON antes de salvar | Trim, tamanho, duplicidade case-insensitive, limites e polígono inválido testados; geometria serializa sem perda | SPEC-10-09, SPEC-17-02 | 2h | Concluída |
| SPEC-17-04 | Implementar operações de salvar, listar, buscar e excluir | Serviço de domínio usa repositório; listagem é determinística; ID inexistente e duplicatas têm semântica documentada | SPEC-17-02/03 | 1h30 | Concluída |
| SPEC-17-05 | Implementar fluxo UI `Salvar localização` em diálogo/modal | Ação só aparece para seleção válida; diálogo confirma/cancela, grava uma vez e fornece feedback acessível | SPEC-17-04 | 2h | Não iniciado |
| SPEC-17-06 | Exibir localizações salvas na interação com a busca | Popover/sugestões acionados pelo campo de pesquisa aparecem abaixo dele; lista vem do SQLite, inclui estado vazio/erro e seleção não inicia consulta Nominatim | SPEC-17-04/05 | 1h30 | Não iniciado |
| SPEC-17-07 | Restaurar geometria, pontos/desenho e enquadramento no mapa | Seleção restaura GeoJSON e `ee.Geometry`, centraliza/ajusta zoom, atualiza estado sem chamadas ao geocodificador nem análise automática | SPEC-10-07/09/10, SPEC-17-06 | 2h30 | Não iniciado |
| SPEC-17-08 | Invalidar resultados antigos e gerenciar erros de estado/storage | Troca da seleção limpa resultados incompatíveis; registro corrompido ou banco indisponível não derruba o app e não altera registros válidos | SPEC-17-05/07 | 1h30 | Não iniciado |
| SPEC-17-09 | Cobrir persistência, integração Streamlit e regressões | Suíte cobre CRUD, conexão nova/reinício simulado, UI/rerun, seleção/restauração, duplicatas, geometria inválida e zero geocodificação no restore | SPEC-17-01 a SPEC-17-08 | 3h | Não iniciado |

## Ordem de execução

1. Fechar esquema/configuração e testes do repositório (SPEC-17-01/02).
2. Implementar validação e serviço de domínio (SPEC-17-03/04).
3. Adicionar formulário e lista de localizações na interface (SPEC-17-05/06).
4. Integrar restauração com estado e mapa atuais (SPEC-17-07/08).
5. Executar regressões de persistência e integração (SPEC-17-09).

## Regras de execução

- Seguir SDD/TDD: testes de repositório e validação antes da integração Streamlit.
- Usar banco SQLite temporário nos testes; não compartilhar o banco local de
  desenvolvimento nem depender de credenciais/serviços externos.
- Não armazenar `ee.Geometry` serializado; validar GeoJSON e reconstruir a
  geometria ao restaurar.
- Não alterar a seleção atual até que o registro carregado tenha sido validado.
- Confirmar que reruns não criam registros duplicados nem apagam mudanças do
  usuário.
- Seguir branch/worktree e PR definidos em `.agent-context/development-rules.md`.
