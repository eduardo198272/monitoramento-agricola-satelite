# Análise técnica do TCC

## 1. Identificação e alcance

- Autor: Eduardo Steffens Hoppen; orientador informado pelo autor:
  Prof. Carlos Amaral Holbig; Ciência da Computação/UPF.
- Data: 15/11/2026.
- Base: Git `b7c325c`; última alteração funcional relevante `4b3cd2c`.
- Trabalho realizado na worktree `task/TCC-02-evolucao-redacao`, sem commits,
  pushes, merges ou alterações funcionais.
- Fonte principal: código; proposta e especificações são planejamento/rastreio,
  não evidência automática de funcionamento.
- Não foram lidos/expostos `.env`, chaves, tokens, Secrets reais ou bancos do autor.
  O PDF histórico não versionado permanece no checkout principal.

O levantamento abrangeu estrutura, pontos de entrada, todos os módulos Python de
aplicação, HTML/JavaScript da consulta interativa, CSS, dependências, contratos,
testes e documentos acadêmicos principais. O conjunto de Markdown/LaTeX/BibTeX
foi inventariado e os documentos de requisitos, métodos, validação e redação
foram confrontados com o código. Slides didáticos, guias genéricos de LaTeX e
arquivos do modelo antigo são contexto de autoria/formatação, não provas do
artefato. Não se afirma leitura integral de todos os textos científicos externos
ou inspeção visual individual de todos os anexos/PDFs históricos.

## 2. Estrutura do repositório

| Caminho | Papel |
|---|---|
| `streamlit_app.py` | Entrada web; força sessão e conta de serviço; encaminha à aplicação |
| `src/app/main.py` | Entrada local, interface e orquestração de estados |
| `src/app/earth_engine.py`, `pipeline.py`, `time_series.py` | Operações remotas e produtos espectrais |
| `src/app/maps.py`, `map_interaction.py`, `assets/index_hover/` | Seleção, tiles, grade e consulta por cursor |
| `src/app/climate.py`, `anomalies.py` | Contexto meteorológico e regras estatísticas |
| `src/app/saved_locations_*.py`, `locations_*.py` | Domínio, validação, persistência e transferência |
| `src/app/export_*.py` | Snapshot, mapas estáticos, PDF, XLSX e CSV ZIP |
| `src/app/config.py`, `ee_auth.py`, `utils.py`, `styles.py` | Configuração, autenticação, datas e apresentação |
| `src/app/validate_apis.py`, `validate_scenarios.py` | Scripts auxiliares; não equivalem a avaliações executadas |
| `tests/`, `pytest.ini` | Suíte e cobertura de `src/app` |
| `docs/specs/01–17` | Especificações históricas e evolutivas |
| `docs/validation/` | Registros datados com escopos distintos |
| `docs/documentação_artigo/` | Documento técnico inicial, motivação, cronograma e materiais de redação |
| `docs/artigo_final/` | Proposta preservada e relatório institucional atual |
| `docs/modelo_latex/`, `docs/latex_documentation/` | Modelo anterior e material de referência de LaTeX |

## 3. Arquitetura identificada

Monólito modular Python com apresentação Streamlit e componente de navegador;
serviços geoespaciais/climáticos externos. Não há microsserviços próprios, API
REST autoral independente, fila de processamento ou banco de análises.

### Componentes e contratos

1. `main.py` recebe entradas, mantém área/resultados/snapshot em sessão e gerencia
   renderizações. Alterações de geometria limpam resultados incompatíveis.
2. `pipeline.py` calcula produtos individuais ou multiíndice. No multiíndice,
   consulta e máscara são compartilhadas e o clima é obtido uma vez.
3. `earth_engine.py` define coleção, filtros, máscara e índices.
4. `time_series.py` reduz cada imagem a um registro; os resultados são recuperados
   individualmente com chamadas remotas e ordenados.
5. `anomalies.py` calcula janelas, escore, alertas e tendência.
6. `maps.py` reúne geocodificação, Folium, validação, área/perímetro/centroide,
   tiles e amostragem da grade; há funções auxiliares geemap não usadas em todo
   o fluxo principal atual.
7. O serviço de localizações encapsula validação e escolhe repositório SQLite
   ou de sessão. A UI não realiza SQL diretamente.
8. Exportadores recebem contexto normalizado; PDF pode consultar serviços para
   mapas, XLSX e ZIP são serializações locais dos dados disponíveis.

## 4. Tecnologias e integrações

Versões declaradas relevantes: Streamlit 1.55.0, earthengine-api 1.7.17,
geemap 0.37.1, Folium 0.20.0, streamlit-folium 0.25.3, NumPy 2.4.3,
pandas 2.3.3, Plotly 6.6.0, ReportLab 4.5.1, openpyxl 3.1.5,
Pillow 12.1.1, Matplotlib 3.10.8 e Requests 2.32.5.
SQLite/JSON/ZIP/zlib/Base64 provêm da biblioteca padrão. No navegador,
Leaflet 1.9.4 e Proj4 2.15.0 são carregados de CDNs.

| Serviço | Operação efetiva | Não confundir com |
|---|---|---|
| Nominatim público | `search`, texto, `jsonv2`, limite 1, timeout 10 s, User-Agent próprio | Cadastro rural, identificação de culturas, Google Earth |
| Esri World Imagery | Tiles de referência, seleção e composição estática | Imagens Sentinel-2 do período analítico |
| Google Earth Engine | Autenticação, coleção, índices, reduções, amostragem, tiles e thumbnails | Google Earth ou login do visitante |
| Sentinel-2 SR harmonizado | Produto orbital L2A de reflectância | Medição de campo ou correção atmosférica implementada pelo projeto |
| NASA POWER Daily Point | Séries diárias no centroide, comunidade AG | Estação própria, média espacial do polígono ou causalidade climática |

**Condições de uso:** a política pública Nominatim limita o total da aplicação
a no máximo uma requisição por segundo, exige identificação/atribuição e proíbe
autocomplete. A aplicação usa busca explícita e User-Agent, mas não foi
identificado rate limiter global ou cache de busca. Adequação operacional a
tráfego multiusuário e atribuição OSM devem ser revisadas antes de publicação.
Não se efetuaram buscas públicas em lote. Earth Engine tem condições de uso não
comercial e cotas de projeto; não implica gratuidade de todo o Google Cloud.

## 5. Processamento espectral verificado

- Coleção: `COPERNICUS/S2_SR_HARMONIZED`.
- Filtro espacial: interseção com a geometria, sem seleção automática de cultivo.
- Datas: início inclusivo e fim exclusivo; datas iguais não abrangem dia completo.
- Nuvens: `CLOUD_COVERAGE_ASSESSMENT < 20`, do produto, não porcentagem local.
- Bandas selecionadas: B2, B3, B4, B8, B8A, B11, QA60.
- Máscara: QA60 bits 10 e 11 iguais a zero; sem máscara específica de sombra.
  Catálogo informa QA60 mascarada de 25/01/2022 a 28/02/2024 inclusive.
- NDVI: `(B8-B4)/(B8+B4)`.
- NDWI do sistema: `(B8-B11)/(B8+B11)`, NIR–SWIR; não McFeeters verde–NIR.
- NDMI do sistema: `(B8A-B11)/(B8A+B11)`. Fonte USGS confirma família NDMI
  NIR–SWIR, não valida especificamente a seleção B8A/B11.
- `normalizedDifference` mascara entradas negativas; não se adicionou tratamento
  próprio de denominador zero. `copyProperties` preserva data e ID nos derivados.
- B8/B4 são 10 m; B8A/B11 são 20 m; grade/redução solicitada em 10 m não cria
  resolução física nova. QA60 é 60 m.
- Não são implementados SAVI, EVI, NDRE, Landsat, MODIS ou classificação de cultura.

### Produtos não equivalentes

| Produto | Operação | Interpretação |
|---|---|---|
| Mapa por índice | Índice por imagem, depois `collection.median()` | Mediana temporal em cada posição, com suporte válido variável |
| Métrica `mean_value` | `reduceRegion(mean)` sobre composição, scale 10, maxPixels 1e9 | Média espacial da composição; CRS não fixado explicitamente |
| Série | Mesmo tipo de redução em cada imagem | Média espacial por aquisição; não média do período ou de pixel individual |
| Cursor | Célula de grade UTM reprojetada a 10 m da composição | Valor local mediano amostrado/reamostrado, não medição instantânea |

Não há interpolação temporal, agregação mensal ou fusão de imagens do mesmo dia.
Omissão de `None` ocorre na série; a função de anomalias não oferece rotina geral
de saneamento de NaN. O indicador de imagens é anterior à máscara, e o fluxo
individual não devolve esse campo, diferentemente do multiíndice.

## 6. Consulta espacial no navegador

Evidências: `maps.py:preload_index_values/_pack_float_grid/_utm_epsg`,
`main.py:render_analysis_map`, `map_interaction.py:render_index_hover_map`,
`assets/index_hover/index.html:preloadGrids/showLocalValue`.

1. Seleciona zona UTM pelo centro e hemisfério.
2. Reprojeta cada composição a 10 m, recorta, usa float e acrescenta coordenadas
   da grade. Estima tamanho antes de transferir.
3. `sampleRectangle` extrai matrizes na caixa delimitadora projetada, NoData -9999.
4. Envia dimensões, origem, transformação afim, CRS e float32 little-endian,
   zlib/Base64. Limite próprio de dois milhões de valores, com estimativa
   conservadora incluindo coordenadas; não garante aceitação remota.
5. Navegador descomprime com `DecompressionStream`, utiliza `Float32Array` e
   mantém os índices pela chave da análise.
6. `mousemove`: teste de pertencimento com anéis internos, Proj4 para UTM,
   piso de coordenadas/escala e acesso linear à matriz. Não há requisição remota
   por movimento, embora tiles dependam de rede.
7. A transformação JavaScript ignora termos de rotação/cisalhamento, assumindo
   alinhamento da grade construída. Compatibilidade de browsers e correção
   posicional integral não são comprovadas pela cobertura Python.

## 7. Estatística temporal

- Janela: três observações anteriores; primeiros três pontos não sinalizados.
- Média e desvio padrão populacional (`np.std(ddof=0)`).
- Escore `(valor-média)/desvio`; sinaliza somente `z < -1`.
- Desvio zero: não sinaliza, mesmo em queda; escore permanece zero inicial.
- Janela não exclui pontos anteriormente sinalizados.
- Tendência: regressão linear por `np.polyfit` contra `np.arange`, limiares
  ±0,01; não taxa diária; menos de dois pontos retorna estável.
- UI mostra alerta e lista; gráfico padrão não destaca anomalias por marcadores.
- Não há classificação causal, inferência probabilística de doença, treinamento
  ou avaliação de precisão agronômica.

## 8. Meteorologia: métodos e inconsistência observada

O pipeline usa centroide calculado no EE (diferente do centro da caixa do registro
salvo). Requisição `community=ag`, parâmetros PRECTOTCORR, T2M,
ALLSKY_SFC_SW_DWN, datas YYYYMMDD, JSON e timeout 30 s.
Ausência -999 é convertida para `None`. Ordena registros, soma precipitação válida,
calcula média de temperatura válida e média de radiação multiplicada por 3,6.
Mínima/máxima possuem mapeamento interno, mas não são pedidas no fluxo padrão.

### Procedimento adicional realmente executado

Em 15/11/2026 foi consultada, por ferramenta HTTP de leitura, a URL:

```text
https://power.larc.nasa.gov/api/temporal/daily/point?parameters=PRECTOTCORR,T2M,ALLSKY_SFC_SW_DWN&community=ag&longitude=-52&latitude=-28&start=20250101&end=20250102&format=JSON
```

Resposta preservada, reformatada em JSON sem alteração dos valores:
`evidencias/nasa_power_unidades.json`. É um ponto técnico escolhido para
inspecionar contrato, não uma área/cultura investigada. Não houve consulta a
credenciais, execução autenticada EE ou acionamento ponta a ponta da aplicação.

Observações: API v2.10.3, fontes MERRA2/SYN1DEG, padrão LST, duas datas inclusive.
Metadados: mm/day, C, **MJ/m²/day**. A aplicação presume kWh/m²/day.
Para radiação 21,64 e 20,99, média 21,315; multiplicação adicional resultaria em
76,734, fator 3,6 acima da média retornada sob o mesmo rótulo.

Isso caracteriza inconsistência computacional da conversão para a resposta
observada, não imprecisão física do provedor. O mesmo fator aparece nos
exportadores XLSX/CSV. Nenhum código foi corrigido nesta tarefa.
Como conferência local adicional, o JSON salvo foi lido com Python da `.venv`,
seus dois valores de radiação foram inseridos em um DataFrame e passados a
`summarize_climate_data`. A função retornou 76,734; a média independente foi
21,315 e a razão observada foi 3,6. Não houve nova requisição ou inicialização EE.
Uma resposta curta não comprova todos os períodos, disponibilidade contínua,
precisão meteorológica ou comportamento completo do serviço.

## 9. Persistência e representação

- GeoJSON Polygon ou Feature com geometria Polygon; longitude/latitude WGS84.
- Nome até 100 caracteres, trim, comparação por espaços normalizados e casefold.
- UUID, datas UTC e centro de enquadramento da caixa delimitadora.
- SQLite local: `saved_locations`, JSON em texto, caminho configurável,
  esquema versão 1, restrição UNIQUE, consultas parametrizadas e transações.
- O diretório próprio recebe permissões restritas quando suportado; isso não é
  criptografia nem autorização multiusuário.
- Sessão web: dicionário recebido explicitamente de `st.session_state`, cópias
  profundas e isolamento; sem promessa de persistência entre sessões.
- Importador: 100 áreas/2 MiB, valida lote e duplicatas, sem sobrescrever;
  rollback SQLite ou atualização após verificações na sessão.
- Exportação de locais: FeatureCollection com nome e geometria; IDs/datas não
  são portáveis; importação os regenera.
- CRUD existe na camada de serviço; excluir/renomear não é recurso de UI atual.
- Validações dos diferentes caminhos não são topologicamente equivalentes;
  não afirmar conformidade topológica completa.

## 10. Exportações

| Formato | Estrutura real | Limites |
|---|---|---|
| PDF | A4 paisagem, uma página por índice no contexto; resumo, período, área, série, anomalias e mapa estático | Sem nome cadastral/coordenadas explícitas automáticas; resumo de até três anomalias; tendência/contagem ausentes no caminho individual |
| Mapa PDF | Thumbnail EE EPSG:3857 + mosaico Esri, Pillow, contorno, legenda fixa [-1,1], atribuição | Outra escala de cores em relação aos tiles dinâmicos; pode falhar e aparecer indisponível |
| XLSX | Resumo + abas dos índices + Clima + Anomalias + Geografia | 4 + número de índices; campos vazios não inventam classificações |
| CSV ZIP | resumo.csv + CSV dos índices + clima.csv + anomalias.csv + geografia.csv; UTF-8/vírgula/DEFLATE | Não inclui raster GeoTIFF; sem proveniência completa |
| GeoJSON | Transferência de localizações, separada de resultados | Sem histórico analítico e sem autenticação de propriedades |

Dados numéricos e DataFrames são copiados; objetos EE permanecem referências.
Troca de parâmetros bloqueia exportação incompatível; geração sob demanda com
spinner. Não se roda pipeline novamente para cada formato, mas PDF pode buscar
novos tiles/thumbnail. Campos de anomalia por data podem confundir aquisições do
mesmo dia; `classification` não é preenchida pelo detector padrão.

## 11. Observações técnicas para tarefa funcional separada

| ID | Evidência | Impacto / recomendação futura |
|---|---|---|
| OBS-01 | `climate.py:175–178`, `export_csv.py:_climate_rows`, `export_xlsx.py:_write_clima_sheet`; resposta AG | Converter conforme metadados; atualmente há multiplicação adicional por 3,6. Alta prioridade antes de interpretar/exportar radiação |
| OBS-02 | `index.html:updateLegend` lê `args.range`; `map_interaction.py` não envia `range` | Legenda padrão [-1,1] pode não refletir intervalo dos tiles; validar propagação e teste real |
| OBS-03 | `pipeline.py` multi retorna `climate_summary` compartilhado; `main.py` procura dentro do resultado por índice | Resumo pode não aparecer no modo Todos; propagação de metadados deve ser revisada |
| OBS-04 | `run_analysis` não retorna trend/image_count; exportadores leem esses campos | Arquivo individual pode indicar ausência apesar de UI calcular tendência |
| OBS-05 | Datas/índices alterados sem limpar resultados; bloqueio é da exportação | Resultados anteriores podem ficar visíveis sob parâmetros novos; identificar snapshot na apresentação |
| OBS-06 | Reduções scale 10 sem CRS; grade interativa UTM explícita | Verificar correspondência entre resumo e amostra, projeção e reamostragem |
| OBS-07 | QA60 e filtro de produto | Disponibilidade histórica, sombra e suporte variável requerem revisão antes de generalizar análise |
| OBS-08 | CSV/XLSX associam flags por data, série admite duplicatas | Preservar identificação da aquisição ou definir agregação explicitamente |
| OBS-09 | Validação de salvos difere da de análise | Harmonizar validadores em outra tarefa, sem prometer topologia completa |
| OBS-10 | Nominatim público sem limitador global/cache observável | Revisar política: máximo 1 req/s por aplicação, atribuição, privacidade e troca de provedor |
| OBS-11 | `validate_scenarios.py` usa scale 100 e geometrias aproximadas | Não equiparar ao pipeline de scale 10; faixas esperadas não são referência universal ou comprovação de culturas |
| OBS-12 | `validate_apis.py:validate_src_modules` retorna falso mesmo após encontrar projeto, sem inicializar EE | Script auxiliar não é certificado de prontidão; suas mensagens finais não comprovam validação operacional |

Todos são registros documentais; nenhuma regra de negócio foi alterada.

## 12. Verificações e limites

Suíte realmente reexecutada:

```sh
COVERAGE_FILE=/tmp/opencode/tcc02-coverage COVERAGE_CORE=ctrace \
/home/eduardo/Projetos/TCC/monitoramento-agricola-satelite/.venv/bin/python \
-m pytest -q -p no:cacheprovider
```

Resultado: **686 passed in 12.06s**, 2.669 instruções, 834 ramificações,
100% em `src/app`, nenhum item perdido/parcial. Python 3.14.4, Linux x86_64,
pytest 9.0.3, pytest-cov 7.1.0, coverage 7.14.0. Não foram criados novos testes
funcionais nesta tarefa exclusivamente acadêmica.

Fronteiras importantes:
- Índices EE são testados com mocks; não se fez conferência remota independente
  da aritmética ou amostragem.
- Python medido não inclui HTML/JS, CSS ou raiz `streamlit_app.py`.
- AppTest não equivale à interação integral no navegador hospedado.
- Revisão PDF de outubro foi sintética; teste EE anterior foi apenas smoke test.
- Registros de responsividade históricos são de versão anterior e não comprovação
  de usabilidade ou do novo componente hover em todos os navegadores.
- Não houve teste de carga/custo, estudo com usuários ou campo.
- Autor confirmou não realização de estudos por soja/milho/pastagem.

Compilação e checagens documentais estão registradas em `REVISAO_TCC.md`.
