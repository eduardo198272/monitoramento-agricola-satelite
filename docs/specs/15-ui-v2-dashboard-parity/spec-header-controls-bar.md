# Spec: SPEC-15-04 — Cabeçalho e barra compacta de controles

## Propósito

Reorganizar o layout atual (vertical/empilhado) em duas faixas compactas horizontais no
topo da página, conforme a imagem de referência versionada em
`assets/dashboard-reference.png`. Manter todos os contratos de estado, validação de
datas, geocodificação e semântica de análise existentes.

## Referência visual

Baseline: `assets/dashboard-reference.png` (viewport desktop 1536 × 1024 px).
A referência mostra duas faixas no topo:
1. **Cabeçalho** — identidade do produto
2. **Barra de controles** — busca, botão Pesquisar, período (inicial/final), escolha
   Todos/NDVI/NDWI/NDMI, botão Analisar área

## Escopo

Incluído:
- Função `render_header_bar()` — faixa 1: título e caption
- Função `render_controls_bar()` — faixa 2: busca + botão, data inicial, data final,
  radio horizontal de índice, botão Analisar área (primary)
- Reordenação do `main()` para renderizar: header → controls → mapa → painéis condicionais
- Ajustes em `assets/style.css` para compactação, alinhamento e responsividade
- Testes automatizados isolando serviços externos (mocks)

Não incluído:
- Criação de páginas `pages/about.py`, `pages/help.py` (omitir links se não existirem)
- Alteração da lógica de geocodificação, validação de datas ou pipeline de análise
- Dados sintéticos para preencher painéis

## Arquitetura

- `src/app/main.py`: novas funções `render_header_bar`, `render_controls_bar`,
  `render_selection_map_area`, `render_results_panels`; `main()` reordenado
- `src/app/assets/style.css`: regras `.header-row`, `.controls-row`, responsividade
- `tests/test_streamlit_app.py`: novas classes `TestHeaderBar`, `TestControlsBar`,
  `TestLayoutOrder`; atualização de testes existentes afetados pela reorganização

## Contratos de dados

Mantidos inalterados:
- `st.session_state` keys: `location_query`, `location_result`, `location_center`,
  `location_zoom`, `aoi_geojson`, `aoi_geometry`, `aoi_area_ha`,
  `analysis_mode`, `selected_indices`, `visible_index`,
  `analysis_start_date`, `analysis_end_date`,
  `analysis_status`, `analysis_error`, `analysis_results`,
  `analysis_metadata`, `analysis_map`, `analysis_map_center`
- Funções de pipeline: `run_analysis`, `run_multi_analysis`
- Helpers: `search_location`, `calculate_map_zoom`, `geojson_to_ee_geometry`

## Requisitos de interface

### Cabeçalho (Faixa 1)

- Layout do cabeçalho sem coluna de status técnico; inicialização silenciosa do serviço
- Identidade: título "Monitoramento Agrícola" + caption "Analise a condição da
  vegetação usando imagens de satélite e dados climáticos."
- Inicialização: nenhuma mensagem quando `init_earth_engine()` retorna `True`; em caso
  de falha, exibir `st.error("Earth Engine indisponível")`, instrução de configuração e
  interromper a aplicação para não oferecer análise impossível.
- O status não deve ocupar toda a largura da coluna em telas desktop.

### Barra de controles (Faixa 2)

- Layout horizontal em 5 colunas: busca (input+botão), data inicial, data final,
  índice (radio horizontal), botão Analisar
- Busca: `st.text_input` label "Localidade" (collapsed) + placeholder "Cidade,
  município..." + botão compacto `🔍` com tooltip "Pesquisar localidade".
- Período: dois `st.date_input` label "Data inicial"/"Data final" (collapsed),
  format="DD/MM/YYYY", defaults `DEFAULT_START`/`DEFAULT_END`
- Índice: `st.radio` horizontal, options `["Todos", "NDVI", "NDWI", "NDMI"]`,
  label "Índice" (collapsed), atualiza `analysis_mode` e `selected_indices`
- Analisar: `st.button("Analisar área", type="primary", use_container_width=True,
  disabled=analysis_disabled)` onde `analysis_disabled =
  (aoi_geometry is None or end_date < start_date)`
- Validação inline: se `end_date < start_date`, `st.error("Data final não pode ser
  anterior à data inicial")` e botão desabilitado

### Mapa de seleção

- Renderizado **após** as duas faixas, mantendo lógica atual de desenho/edição/limpeza
- Exibe área em ha quando geometria válida

### Painéis de resultado

- Renderizados **apenas** quando `analysis_status == "success"` e
  `analysis_results` não vazio
- Mesma lógica existente de `display_map`, `display_summary`,
  `display_multi_index_overview`, `display_analysis_details`

## Critérios de aceitação

1. Cabeçalho renderiza a identidade do produto sem status operacional de sucesso.
2. Barra de controles renderiza em faixa horizontal: busca | período | índice | analisar
3. Busca integrada ao geocodificador existente funciona
4. Validação de datas inline (erro se `end < start`) funciona
5. Botão "Analisar área" desabilitado sem geometria ou datas inválidas
6. Seletor `Todos`/`NDVI`/`NDWI`/`NDMI` horizontal atualiza `analysis_mode` e `selected_indices`
7. Mapa de seleção renderiza **após** as duas faixas
8. Painéis de resultado **não** renderizam antes de sucesso
9. Painéis de resultado renderizam após sucesso com dados reais
10. Layout desktop (1536×1024) visualmente próximo da referência e as quatro opções de
    índice cabem em uma linha.
11. Tablet (769–1100px) reorganiza os controles em linhas sem comprimir campos.
12. Mobile (≤768px) empilha cabeçalho/controles; busca permanece em linha com botão
    compacto e opções de índice em grade 2×2, sem overflow horizontal.
13. `python -m pytest` passa com cobertura configurada (≥100%)
14. `git diff --check` passa

## Estratégia de validação visual

- Abrir `http://localhost:8501` em viewport 1536×1024
- Comparar cabeçalho, alinhamento da barra, proporção/altura do mapa, painel da área,
  agrupamento dos cards e ordem dos resultados contra `assets/dashboard-reference.png`
- Verificar separadamente: estado inicial, sucesso single-index, sucesso multiíndice,
  falha/ausência de dados
- Confirmar responsividade em ≤768px (empilhamento lógico)

## Dependências

- SPEC-15-01 (imagem versionada e contratos visuais fechados)
- SPEC-15-02/03 (camada-base Esri nos mapas — já mergeadas em `dev`)
- `docs/specs/14-ui-v2-map-first/spec-ui-v2-map-first.md`
- `src/app/main.py`, `maps.py`, `pipeline.py`, `assets/style.css`
