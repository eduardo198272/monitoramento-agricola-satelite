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
| OE8 Avaliação | Suíte, Node, navegador, protocolo de pesquisa | 710 Python, 3 Node; pesquisa sem dataset real | Resultados; parcialmente concluído |
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
| Análise da pesquisa | `tests/test_user_survey_analysis.py`, somente sintético |

NDMI, lookup local, SQLite/sessão e formatos adicionais são evoluções do artefato;
não substituem retroativamente o estudo agronômico originalmente planejado.
