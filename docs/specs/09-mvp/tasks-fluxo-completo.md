# Tasks: Fluxo Completo (MVP)

Referência: `docs/specs/09-mvp/spec-fluxo-completo.md`

| ID | Descrição | Critério de Aceitação | Esforço | Status |
|---|---|---|---|---|
| SPEC-09-01 | Implementar `run_analysis(geometry, start_date, end_date, index_name)` com pipeline de 15 etapas | Retorna dict com todas as 9 chaves do retorno | 3h | ✅ |
| SPEC-09-02 | Calcular área em hectares: `geometry.area().divide(10000)` | Campo area_ha em hectares | 30min | ✅ |
| SPEC-09-03 | Calcular valor médio do índice na área | Campo mean_value entre -1 e 1 | 30min | ✅ |
| SPEC-09-04 | Tratar erros intermediários: retornar dict com success=False + campo error | Pipeline não quebra, retorna erro descritivo | 1h | ✅ |
| SPEC-09-05 | Escrever teste de integração do pipeline completo com dados mockados | Teste valida todas as chaves do retorno | 2h | ✅ |
| SPEC-09-06 | Corrigir bugs identificados nos testes de integração | Todos os testes do pipeline passando | 2h | ✅ |
| SPEC-09-07 | Validar MVP com cenário real (geometria pequena, período curto) | Execução completa sem erros | 2h | ✅ |
| SPEC-09-08 | Adicionar cenários de validação por cultura (soja, milho, pastagem) | 3 cenários documentados e testáveis | 1h | ✅ |
