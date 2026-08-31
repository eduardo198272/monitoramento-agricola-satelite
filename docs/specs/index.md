# Spec-Driven Development - Índice de Especificações

## O que é SDD?

Spec-Driven Development (SDD) é a prática de escrever especificações detalhadas antes de implementar. Cada spec descreve **o que** deve ser construído — propósito, interface, regras de negócio e critérios de aceitação — servindo como contexto único para a IA implementar cada tarefa.

## Fluxo de trabalho

```
1. Ler spec da funcionalidade
2. Escrever testes baseados na spec
3. Implementar o código
4. Verificar que os testes passam
```

## Mapa de especificações

| # | Pasta | Specs | Tasks | Sub-tasks |
|---|---|---|---|---|
| 01 | `01-visao-geral/` | `spec-visao-geral.md` | TASK-001 a TASK-003 | `tasks-visao-geral.md` |
| 02 | `02-earth-engine/` | `spec-busca-imagem.md`, `spec-filtro-nuvem.md`, `spec-filtro-data-area.md` | TASK-012 a TASK-016 | `tasks-busca-imagem.md`, `tasks-filtro-nuvem.md`, `tasks-filtro-data-area.md` |
| 03 | `03-indices/` | `spec-ndvi.md`, `spec-ndwi.md`, `spec-ndmi.md` | TASK-017 a TASK-021 | `tasks-ndvi.md`, `tasks-ndwi.md`, `tasks-ndmi.md` |
| 04 | `04-mapas/` | `spec-mapa-base.md`, `spec-visualizacao-indice.md`, `spec-legenda.md`, `spec-selecao-area.md` | TASK-022 a TASK-025 | `tasks-mapa-base.md`, `tasks-visualizacao-indice.md`, `tasks-legenda.md`, `tasks-selecao-area.md` |
| 05 | `05-streamlit/` | `spec-app.md`, `spec-controles.md`, `spec-mapa-ui.md` | TASK-026 a TASK-030 | `tasks-app.md`, `tasks-controles.md`, `tasks-mapa-ui.md` |
| 06 | `06-series-temporais/` | `spec-serie-temporal.md` | TASK-031 a TASK-034 | `tasks-serie-temporal.md` |
| 07 | `07-anomalias/` | `spec-deteccao-anomalias.md` | TASK-035 a TASK-038 | `tasks-deteccao-anomalias.md` |
| 08 | `08-clima/` | `spec-nasa-power.md` | TASK-039 a TASK-042 | `tasks-nasa-power.md` |
| 09 | `09-mvp/` | `spec-fluxo-completo.md` | TASK-043 a TASK-045 | `tasks-fluxo-completo.md` |
| 10 | `10-mapas-interacao/` | `spec-mapa-interacao.md` | SPEC-10-01 a SPEC-10-14 | `tasks-mapa-interacao.md` |
| 11 | `11-unidades-area/` | `spec-unidades-area.md` | SPEC-11-01 a SPEC-11-09 | `tasks-unidades-area.md` |
| 12 | `12-interface-resultados/` | `spec-interface-resultados.md` | SPEC-12-01 a SPEC-12-10 | `tasks-interface-resultados.md` |
| 13 | `13-cobertura-testes/` | `spec-cobertura-testes.md` | SPEC-13-01 a SPEC-13-14 | `tasks-cobertura-testes.md` |

## Sub-tasks breakdown

Cada spec possui um arquivo `tasks-*.md` com a quebra em sub-tasks implementáveis individualmente:

| Sub-task ID | Spec | Descrição | Esforço |
|---|---|---|---|
| SPEC-01-01 a SPEC-01-04 | Visão Geral | Arquitetura, stack, fluxo, convenções | 4h30 |
| SPEC-02-01 a SPEC-02-13 | Earth Engine | Imagem, nuvem, data/área + testes | 10h |
| SPEC-03-01 a SPEC-03-12 | Índices | NDVI, NDWI, NDMI + testes | 8h |
| SPEC-04-01 a SPEC-04-17 | Mapas | Base, índice, legenda e seleção por desenho + testes | 12h |
| SPEC-05-01 a SPEC-05-14 | Streamlit | App, controles, UI + testes | 10h |
| SPEC-06-01 a SPEC-06-06 | Série Temporal | Computar, plotar + testes | 5h30 |
| SPEC-07-01 a SPEC-07-07 | Anomalias | Detectar, alertar, tendência + testes | 7h |
| SPEC-08-01 a SPEC-08-06 | Clima | NASA POWER, plotar + testes | 5h |
| SPEC-09-01 a SPEC-09-07 | MVP | Pipeline, integração, validação | 11h30 |
| SPEC-10-01 a SPEC-10-14 | Mapa interativo | Pesquisa, seleção, centralização, bloqueio e limpeza | 13h30 |
| SPEC-11-01 a SPEC-11-09 | Unidades de área | Conversão e exibição em hectares ou acres | 6h30 |
| SPEC-12-01 a SPEC-12-10 | Interface de resultados | Layout, alertas e testes de apresentação | 7h45 |
| SPEC-13-01 a SPEC-13-14 | Cobertura de testes | Fixtures, testes de processamento, UI, scripts e validação de 100% | 16h |

## Requisitos Funcionais (RF) mapeados

| RF | Descrição | Specs relacionadas |
|---|---|---|
| RF01 | Selecionar área geográfica por desenho de polígono | `04-mapas/spec-selecao-area.md`, `10-mapas-interacao/spec-mapa-interacao.md` |
| RF02 | Selecionar período de datas | `02-earth-engine/spec-filtro-data-area.md`, `05-streamlit/spec-controles.md` |
| RF03 | Buscar imagens Sentinel-2 | `02-earth-engine/spec-busca-imagem.md` |
| RF04 | Calcular NDVI | `03-indices/spec-ndvi.md` |
| RF05 | Calcular NDWI / NDMI | `03-indices/spec-ndwi.md`, `03-indices/spec-ndmi.md` |
| RF06 | Visualizar mapa temático | `04-mapas/spec-mapa-base.md`, `04-mapas/spec-visualizacao-indice.md` |
| RF07 | Gerar série temporal | `06-series-temporais/spec-serie-temporal.md` |
| RF08 | Detectar anomalias | `07-anomalias/spec-deteccao-anomalias.md` |
| RF09 | Integrar dados climáticos | `08-clima/spec-nasa-power.md` |
| RF10 | Exibir resumo (índice médio, tendência, alerta) | `05-streamlit/spec-mapa-ui.md` |
| RF11 | Pesquisar e centralizar localidades no mapa | `10-mapas-interacao/spec-mapa-interacao.md` |
| RF12 | Bloquear e liberar navegação após seleção do polígono | `10-mapas-interacao/spec-mapa-interacao.md` |
| RF13 | Exibir área em hectares ou acres | `11-unidades-area/spec-unidades-area.md` |
| RF14 | Organizar resultados e alertas na interface | `12-interface-resultados/spec-interface-resultados.md` |
| RF11 | Pesquisar e centralizar localidades no mapa | `10-mapas-interacao/spec-mapa-interacao.md` |
| RF12 | Bloquear e liberar navegação após seleção do polígono | `10-mapas-interacao/spec-mapa-interacao.md` |
| RF13 | Exibir área em hectares ou acres | `11-unidades-area/spec-unidades-area.md` |
| RF14 | Organizar resultados e alertas na interface | `12-interface-resultados/spec-interface-resultados.md` |
