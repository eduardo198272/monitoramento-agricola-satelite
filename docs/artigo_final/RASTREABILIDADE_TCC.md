# Rastreabilidade — segunda rodada

Base `b7c325c` com correções locais. A matriz detalhada anterior, incluindo IDs
originais O01–O11 e RF/RNF, foi preservada em
`evidencias/historico_primeira_rodada/RASTREABILIDADE_TCC.md`.
Esta matriz atualiza os estados: implementação não significa validação de campo.
Proposta e seus capítulos originais não foram modificados.

| Objetivo | Implementação | Verificação | Artigo / estado |
|---|---|---|---|
| OE1 Fundamentação e arquitetura | Módulos, especificações, referências oficiais | Inspeção/histórico, compilação | Fundamentação e desenvolvimento; implementado |
| OE2 Seleção e reutilização de áreas | `maps.py`, `saved_locations_*`, transferência GeoJSON | Testes CRUD/UI; Chrome busca, desenho, salvar, recuperar, exportar e importar em nova sessão | Apresentação; implementado, sessão temporária |
| OE3 Consulta e índices Sentinel-2 | `earth_engine.py`, `pipeline.py` | Filtros, bandas, máscara e regressão inclusiva; demonstração real limitada | Métodos; implementado, QA60 com limite histórico |
| OE4 Produtos espaciais e lookup | `maps.py`, `map_interaction.py`, HTML | Extremos de legenda, matrizes, Node, capturas disponíveis | Desenvolvimento/apresentação; implementado |
| OE5 Séries e desvios | `time_series.py`, `anomalies.py` | Janelas/tendência/IDs por aquisição | Métodos; heurística, não diagnóstico |
| OE6 Clima | `climate.py`, metadados compartilhados | Resposta NASA preservada, unidades MJ/kWh/desconhecida, resumo multi | Métodos/resultados; corrigido |
| OE7 Saídas portáveis | `export_context.py`, `export_*`, GeoJSON | PDF/XLSX/CSV e isolamento de snapshots; downloads reais e estruturas conferidas | Desenvolvimento; implementado, proveniência parcial |
| OE8 Avaliação | Suíte, Node, navegador e questionário | 710 Python, 3 Node históricos; 31 submissões elegíveis ao questionário; 8 testes sintéticos da análise e conferência independente | Resultados; avaliação descritiva executada, versão pública/ética com pendências |
| O10 original: soja/milho/pastagem | Protocolo histórico, não estudo executado | Testes do script não são dados de cultura | Discussão; não realizado, apreciação do orientador |

## Correções e requisitos de coerência

| Contrato | Regressão |
|---|---|
| Unidade sem pressuposição | `test_radiation_respects_response_units`, histórico multiformato |
| Escala tiles=legenda | `test_component_receives_exact_negative_tile_range`, Node |
| Clima compartilhado | `test_single_and_multi_share_metadata_without_duplicate_climate_calls` |
| Período inclusivo | `test_end_date_is_inclusive_even_for_one_day` |
| Invalidação analítica, visual preservada | `test_analytical_changes_invalidate_all_products`, `test_visual_selection_does_not_invalidate` |
| Aquisições no mesmo dia | `test_same_date_observations_keep_distinct_anomaly_flags` |
| Preparação anterior da pesquisa | `tests/test_user_survey_analysis.py`, somente sintético |
| Análise da planilha | `avaliacao_usuarios/scripts/`, `resultados/validacao.json`; 40 itens fechados, 191 categorias e nota geral |
| Qualitativa | `avaliacao_usuarios/codificacao.json`, 142 células; multirrótulo assistido por IA, aprovação do autor pendente |
| Retificação autorizada | Sete carimbos 16/17→15/11/2026; backup original e auditoria privados, todas as respostas preservadas |

NDMI, lookup local, SQLite/sessão e formatos adicionais são evoluções do artefato;
não substituem retroativamente o estudo agronômico originalmente planejado.

## Matriz da avaliação de percepção

| Dimensão | Fonte efetiva | Saída / vínculo com o artigo |
|---|---|---|
| Perfil | Colunas 3–5 da planilha (base 1) | `perfil_participantes.csv`, três gráficos; `final_4a_usuarios.tex` |
| Execução | Nove itens, colunas 6–14 | `execucao_funcionalidades.csv`, gráfico empilhado; séries/anomalias e exportação agrupadas |
| Experiência | Nove afirmações, colunas 16–24 | `avaliacao_usabilidade.csv`, Likert completo, ausências separadas |
| Utilidade | Onze recursos, colunas 25–35 | `utilidade_funcionalidades.csv`, tabela LaTeX e gráfico complementar |
| Aplicabilidade/intenção | Oito afirmações, colunas 36–43 | `aplicabilidade.csv`, gráfico e cruzamentos sem inferência causal |
| Geral | Coluna 49 | `avaliacao_geral.csv`, `distribuicao_notas.csv`, histograma 0–10; não NPS |
| Discursivas | Cinco perguntas, colunas 44–48 | `categorias_qualitativas.csv`, livro de códigos e tabela de trechos |
| Triagem | Consentimento col. 2, exploração col. 15, impedimento col. 50 | `qualidade.json`, 31 submissões elegíveis, sem identificação individual |
| Versão | Declaração do autor e código inspecionado | Pública anterior às correções versus desenvolvimento `28759bf`; não houve deploy |

As contagens de testes da aplicação são históricas e não foram substituídas
pelos testes dos scripts estatísticos. Os dados de percepção não verificam
as correções ainda não publicadas nem validam diagnóstico agronômico.

## Atualização visual posterior à integração da pesquisa

As ilustrações da apresentação foram substituídas por 16 imagens fornecidas
pelo autor, agrupadas em onze figuras. Originais, cópias, recortes e exclusão
da captura do relatório com radiação pendente estão documentados em
`evidencias/capturas_autor/README.md` e `manifesto.json`. Não foram alterados
os números da demonstração instrumentada, os questionários ou os ensaios
históricos. Capturas antigas permanecem disponíveis. O PDF atual tem
33 páginas; seu registro de compilação está nessa nova pasta de evidências.
