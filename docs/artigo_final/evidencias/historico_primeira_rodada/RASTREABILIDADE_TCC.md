# Matriz de rastreabilidade acadêmica do TCC

## 1. Base e critérios

- Revisão de software: `b7c325c`, 15/11/2026; inspeção sem alteração funcional.
- Proposta preservada: `Proposta.tex`, `2_Motivacao_e_objetivos.tex`,
  `3_Revisao_Literatura.tex` e `4_Materiais_Metodos.tex`.
- Requisitos iniciais: seções 9 e 10 de
  `../documentação_artigo/sistema_monitoramento_agricola_imagens_satelite_v1_1.md`.
- Requisitos evoluídos: `../specs/index.md` e especificações 01–17.
- Símbolos de implementação abaixo são relativos à raiz do repositório;
  referências ao artigo são seções/títulos, não páginas, que mudarão com as capturas.
- **Implementado** significa presença no código e evidências indicadas, não
  funcionamento irrestrito com todos os serviços nem validação agronômica.
- **Parcialmente implementado**: parte do contrato existe, mas há recurso ausente
  ou inconsistência identificada. **Não implementado**: recurso sem implementação.
- **Não realizado**: atividade de pesquisa/avaliação não executada.
- **Implementação adicional**: ampliação em relação à proposta acadêmica inicial.
- **Pendente de verificação**: não há evidência suficiente para concluir.

As figuras CAP são espaços reservados; nenhuma captura real foi produzida nesta
revisão. Os diagramas DIA foram elaborados a partir do código e não comprovam
execução operacional.

## 2. Objetivos originais: não substituir pelo escopo ampliado

Os identificadores O01–O11 abaixo são atribuídos nesta matriz aos itens da lista
original, sem alterar a proposta.

| Objetivo original | Objetivo final relacionado | Requisito | Implementação/evidência | Testes existentes | Figura / seção do artigo | Status e ressalva |
|---|---|---|---|---|---|---|
| O01 Estudar sensoriamento remoto | OE1 | Base conceitual | Catálogo oficial, equações e bibliografia; `final_2_fundamentacao.tex` | Não se aplica: estudo bibliográfico não é teste de software | Fundamentação teórica | Implementado; revisão narrativa, não sistemática; obras pendentes listadas em `REVISAO_TCC.md` |
| O02 Investigar Sentinel-2 | OE3 | RF03 | `src/app/earth_engine.py:get_image_collection` | `tests/test_earth_engine.py:TestGetImageCollection` | DIA-02 / Materiais e métodos | Implementado como integração; adequação por cultura não demonstrada |
| O03 Definir arquitetura integrada | OE1 | RNF05 | Módulos em `src/app`; interface, pipeline, serviços, repositórios e exportadores | `test_pipeline.py`, `test_saved_locations_service.py` | DIA-01 / Desenvolvimento e implementação | Implementado; monólito modular com serviços externos, não microsserviços |
| O04 Implementar consulta Python ao Earth Engine | OE3 | RF03 | `get_image_collection`, filtros e `ee_auth.py:initialize_earth_engine` | `test_earth_engine.py`, `test_ee_auth.py` | DIA-01/02 / Aquisição e arquitetura | Implementado; testes substituem API; smoke test anterior é limitado |
| O05 Calcular NDVI/NDWI | OE3 | RF04/05 | `calculate_ndvi`, `calculate_ndwi`; B8/B4 e B8/B11 | `TestCalculateNDVI`, `TestCalculateNDWI` | CAP-09/10 / Índices espectrais | Implementado; testes verificam bandas/chamadas, não aritmética remota real |
| O06 Gerar mapas e séries | OE4/05 | RF06/07 | `pipeline.py:run_analysis/run_multi_analysis`, `time_series.py:compute_time_series`, `maps.py:get_index_map_tile_url` | `test_maps.py`, `test_time_series.py`, `test_pipeline.py` | DIA-02; CAP-09–13 / Agregações e apresentação | Parcialmente implementado no contrato de visualização: legenda pode divergir da escala dos tiles |
| O07 Integrar NASA POWER | OE6 | RF09 | `climate.py:fetch_climate_data/summarize_climate_data` | `test_climate.py`; consulta pública limitada desta revisão | CAP-15; seção 6.3 | Parcialmente implementado: conversão de radiação incompatível com resposta AG observada |
| O08 Detector simples por desvio | OE5 | RF08 | `anomalies.py:detect_anomalies`, janela 3, `z < -1`, `ddof=0` | `tests/test_anomalies.py:TestDetectAnomalies` | DIA-03; CAP-14 / Regra de detecção | Implementado como heurística unilateral; não diagnóstico |
| O09 Interface Streamlit | OE2/04/07 | RF01/02/06/10 | `main.py:main`, controles, mapas, detalhes, exportação | `test_streamlit_app.py`, `test_cloud_entrypoint.py`, `test_area_selection_regressions.py` | CAP-01–19 / Apresentação | Implementado; fluxos isolados não comprovam experiência integral do navegador |
| O10 Validar com soja, milho e pastagem | OE8, mudança de escopo | Avaliação prevista na proposta, § Validação | `validate_scenarios.py` contém protocolo; autor informou que estudos não ocorreram | `test_validate_scenarios.py` testa script com mocks, não culturas | Sem figura experimental / Resultados e discussão | **Não realizado**; limitações de tempo informadas pelo autor; registrar para revisão com orientador |
| O11 Documentar limites e evolução | OE8 | Documentação | Artigo, matriz, relatórios e registros históricos | Validação documental e compilação, não teste agronômico | Discussão e conclusão | Implementado; capturas e referências pendentes permanecem explícitas |

O objetivo geral original é atendido no desenvolvimento do artefato e
**parcialmente na avaliação de sua viabilidade operacional**. Não se declara
comprovada utilidade agronômica, baixo custo total ou facilidade de uso.

## 3. Requisitos funcionais iniciais

| RF inicial | Objetivo final | Módulo e símbolo | Evidência/teste | Figura / seção | Status |
|---|---|---|---|---|---|
| RF01 Selecionar área no mapa | OE2 | `maps.py:create_selection_map`, `main.py:render_selection_map_area/restore_pending_saved_location` | `test_maps.py:TestCreateSelectionMap`, `test_area_selection_regressions.py` | CAP-03/05, DIA-04 / Gerenciamento de áreas | Implementado; uma área ativa, não comparação entre talhões |
| RF02 Definir período | OE3/05 | `main.py:_render_controls_content`, `utils.py:normalize_date`, `earth_engine.py:filter_by_date` | `test_utils.py`, `test_earth_engine.py:TestFilterByDate`, `test_streamlit_app.py` | CAP-07 / Aquisição | Implementado; final exclusivo no EE; igualdade não significa dia completo |
| RF03 Consultar satélite | OE3 | `earth_engine.py:get_image_collection` | `TestGetImageCollection` | DIA-02 / Aquisição | Parcialmente implementado em relação ao V1.1, que também citava Landsat; implementado no MVP posterior restrito a Sentinel-2 |
| RF04 NDVI | OE3 | `calculate_ndvi` | `TestCalculateNDVI` | CAP-09 / Equação NDVI | Implementado; não diagnóstico de “saúde” |
| RF05 NDWI/NDMI | OE3 | `calculate_ndwi/calculate_ndmi` | `TestCalculateNDWI/TestCalculateNDMI` | CAP-10/11 / Equações e nomenclatura | Implementado; nomes correspondem a variantes NIR–SWIR, não umidade direta do solo |
| RF06 Mapa com cores | OE4 | `maps.py:get_index_map_tile_url`, `assets/index_hover/index.html:updateLegend` | `TestIndexPixelPreloading`; legenda examinada por inspeção | CAP-09–12, DIA-05 / Cores e mapas | Parcialmente implementado: `range` não enviado ao componente; não há classes saudável/problema |
| RF07 Série temporal | OE5 | `time_series.py:compute_time_series/plot_time_series` | `TestComputeTimeSeries/TestPlotTimeSeries` | CAP-13 / Produtos temporais | Implementado; médias por aquisição, sem interpolação ou agregação diária |
| RF08 Anomalias | OE5 | `detect_anomalies/generate_alert` | `TestDetectAnomalies/TestGenerateAlert` | CAP-14, DIA-03 | Implementado no sentido estatístico restrito |
| RF09 Clima | OE6 | `climate.py`, `_fetch_climate_context` | `test_climate.py`, `test_pipeline.py` | CAP-15 / Clima e resultado da consulta | Parcialmente implementado: unidade de radiação e resumo multiíndice |
| RF10 Resumo | OE4/05/06 | `main.py:display_summary/display_multi_index_overview/display_analysis_details` | `test_streamlit_app.py:TestPresentation`, `test_coverage_gaps.py` | CAP-08/15 | Parcialmente implementado: informação compartilhada nem sempre propagada; sem coerência de período visível automaticamente garantida |

## 4. Ampliações e requisitos posteriores

| Funcionalidade / requisito posterior | OE | Evidência de implementação | Testes existentes | Figura / seção | Status frente à proposta |
|---|---|---|---|---|---|
| Busca Nominatim / RF11 | OE2 | `maps.py:search_location`, primeiro resultado | `TestSearchLocation`, regressões de busca | CAP-02 / Busca geográfica | Implementação adicional |
| Bloquear/liberar navegação / RF12 | OE2 | Sem controle explícito na UI atual; mapas continuam interativos | Testes antigos de layout não substituem implementação atual | Não planejar captura de controle inexistente | Não implementado no estado atual |
| Hectares/acres / RF13 | OE2 | `display_summary` aceita unidade, mas chamada atual fixa `"ha"`; sem conversor/seletor em `utils.py` | Testes de apresentação não demonstram seletor | CAP-03 / Discussão | Não implementado como escolha de unidades; hectares implementado |
| Organização dos resultados / RF14 | OE4/05 | `render_results_panels`, detalhes e alertas | `TestPresentation`, testes de fluxo | CAP-08–15 | Implementação adicional |
| NDMI B8A/B11 | OE3 | `calculate_ndmi`; futuro na proposta acadêmica | `TestCalculateNDMI` | CAP-11 / Equação NDMI | Implementação adicional; já mencionado em requisito amplo V1.1 |
| Consulta por cursor | OE4 | `maps.py:preload_index_values`, `index.html:showLocalValue` | `TestIndexPixelPreloading`, teste da ponte em `test_coverage_gaps.py`; sem ensaio JS integral | CAP-12, DIA-05 / Pré-carregamento | Implementação adicional; verificação operacional pendente |
| SQLite e recuperação nomeada / RF17 | OE2 | Serviço, repositório e esquema `saved_locations` | `test_saved_locations_repository.py`, `test_saved_locations_service.py` | CAP-04/05, DIA-04 / Persistência | Implementação adicional |
| Repositório por sessão web | OE2 | `saved_locations_session.py`, seleção pelo serviço, ponto de entrada web | `test_locations_transfer.py`, `test_cloud_entrypoint.py` | CAP-06, DIA-01/04 | Implementação adicional; sem permanência entre sessões |
| GeoJSON de localizações | OE2/07 | `locations_geojson.py`, `locations_transfer_ui.py` | `test_locations_transfer.py` | CAP-06 | Implementação adicional |
| Exclusão de localização na UI | OE2 | Serviço/repositório possuem delete; UI não o expõe | Testes de delete são da camada de serviço | Sem captura de exclusão | Parcialmente implementado: backend local apenas |
| PDF / RF15 | OE7 | `export_pdf.py:render_analysis_pdf`, `export_maps.py:render_static_index_map` | `test_export_pdf.py`, `test_export_maps.py` | CAP-16/17, DIA-06 | Implementação adicional; uma página por índice selecionado |
| XLSX e CSV ZIP / RF16 | OE7 | `render_analysis_xlsx`, `render_analysis_csv_zip` | `test_export_xlsx.py`, `test_export_csv.py` | CAP-18/19, DIA-06 | Implementação adicional; 4 + número de índices conjuntos/abas |
| Proteção de snapshot | OE7/08 | `main.py:render_export_actions`, `build_export_context` | `test_export_ui.py`, `test_export_context.py` | CAP-16 / Exportação | Implementação adicional |
| Cloud publicado | OE8 | Há ponto de entrada e documentação; publicação não comprovada | Testes locais e resolução de dependências não equivalem a deploy | Sem captura inventada de site publicado | Pendente de verificação |
| Login de usuários, histórico de análises, GeoTIFF | — | Ausentes; fora da entrega realizada | Não se aplica | Trabalhos futuros | Não implementado |

## 5. Requisitos não funcionais e avaliações

| Requisito / atividade | Evidência | Status e limite | Seção |
|---|---|---|---|
| RNF01 Dados públicos/gratuitos | Sentinel-2, NASA POWER; serviços requerem condições próprias | Pendente de verificação quanto a custo operacional; não declarar todos os serviços abertos ou gratuitos irrestritamente | Discussão / Operação |
| RNF02 Execução local | Entradas Streamlit, suíte executada na `.venv` | Implementado como capacidade de execução local com servidor Streamlit; execução completa autenticada não repetida | Materiais |
| RNF03 Simplicidade/intuitividade | Layout e registro histórico de responsividade | Pendente de verificação por usuários; responsividade não é usabilidade | Apresentação e limitações |
| RNF04 Reprodutibilidade | Código, dependências fixadas, parâmetros, testes, exportações | Parcialmente implementado: sem pacote integral de proveniência e sem inventário exportado de aquisições | Exportação e discussão |
| RNF05 Modularidade | Componentes e repositórios com responsabilidades próprias | Implementado como organização do código; não métrica de manutenibilidade | Arquitetura |
| RNF06 Resposta aceitável (<30 s em spec posterior) | Nenhum benchmark representativo localizado/executado | Pendente de verificação; 12,06 s é duração da suíte, não da análise | Resultados |
| RNF07 Baixo consumo | EE remoto, mas grades e gráficos transferidos | Pendente de verificação; sem benchmark de memória/rede | Pré-carregamento e discussão |
| Validação agronômica por cultura / campo | Autor confirmou ausência | Não realizado | Introdução, resultados, discussão e conclusão |
| Usabilidade, comparação de sistemas, custo e carga | Sem estudo próprio demonstrado | Não realizado nesta avaliação | Discussão |
| Suíte atual | 686 aprovados, 100% em `src/app` | Verificação realizada; não afirmar validade científica integral | Resultados |
| Consulta pública de unidade NASA POWER | Resposta em `evidencias/nasa_power_unidades.json` | Verificação realizada e inconsistente com conversão do código; não é experimento agrícola | Resultado de unidades |

## 6. Decisões para revisão com o orientador

1. Aprovar a delimitação final como pesquisa tecnológica centrada no software.
2. Reconhecer explicitamente O10 como não realizado, sem substituir culturas por
   testes simulados ou por funcionalidades adicionais.
3. Avaliar a suficiência das evidências computacionais, incluindo as inconsistências
   encontradas e a demonstração real ainda a consolidar.
4. Confirmar se serão corrigidos os defeitos em uma tarefa funcional separada antes
   das capturas; preservar a identificação de versão dos dois estados.
5. Revisar fontes bibliográficas pendentes e escopo das alegações da conclusão.
