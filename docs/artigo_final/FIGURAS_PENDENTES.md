# Planejamento das figuras e capturas do TCC

## Convenções e estado

Data: 15/11/2026. Base: `b7c325c` acrescida das correções locais.

- **CAP-01–17: capturas reais consolidadas**, Chrome, viewport desktop 1680×1100,
  versão local corrigida. Mapas e gráficos foram capturados diretamente em seus
  elementos para manter a legibilidade; CAP-17 é rasterização do PDF baixado.
  Parâmetros em `evidencias/demonstracao_real/manifesto.json`.
  O recorte é entrada demonstrativa, sem confirmação de cultura/propriedade.
- Importação GeoJSON em nova sessão foi verificada, com imagem adicional
  `geojson_importacao.png`; exportação de resultados gerou PDF/XLSX/ZIP reais.
- **CAP-18 e CAP-19: pendentes de captura em visualizador apropriado**. XLSX/ZIP
  foram inspecionados programaticamente, mas isso não é captura de planilha.
- **MOB-01 concluída**: viewport 390×844 e toque com leitura NDMI 0,3228,
  coincidente com a consulta por cursor. Não houve telefone físico.
- Cinco esquemas científicos novos: `fig/conceitos.tex`; curvas e exemplos
  explicitamente conceituais/didáticos. Não são resultados agrícolas.
- Chamadas de figuras estão em `final_3b_plataforma.tex`, seção 5.
- Salvar PNGs em `fig/capturas/`, com os nomes abaixo. A macro em
  `figuras_relatorio.tex` inclui somente imagens existentes; ausência não gera
  placeholder no PDF. O planejamento integral abaixo continua preservado.
- IDs CAP/DIA são estáveis; números “Figura n” são gerados pelo LaTeX e podem mudar.
- Painéis compostos só podem reunir capturas reais, com sequência e contexto
  informados; não alterar dados, cores, rótulos ou mensagens para simular correção.

## Procedimento comum para obtenção

1. Identificar revisão Git, ponto de entrada (SQLite ou sessão), navegador,
   viewport e data/hora. Não capturar Secrets, console autenticado ou dados privados.
2. Selecionar área autorizada para divulgação. Registrar GeoJSON, período e índices
   em um manifesto da sessão demonstrativa; não atribuir cultura sem confirmação.
3. Usar preferencialmente a mesma área e período em mapas, séries e exportações.
   Conservar atribuição Esri e distinção entre mapa-base e Sentinel-2 analítico.
4. Esperar carregamento dos tiles e das grades; registrar falhas sem encobri-las.
5. Manter tipografia legível no PDF em duas colunas. Capturar em resolução
   suficiente (por exemplo, viewport de 1440 px ou maior) sem forçar uma dimensão
   universal. Recortes devem preservar eixos, unidades, índice, contexto e legenda.
6. Não denominar “experimento”, “validação da cultura” ou “prova de precisão”
   uma demonstração de interface. Não executar o script de culturas para preencher
   o artigo como se aquelas áreas e limiares fossem dados confirmados.
7. Se houver correções funcionais futuras, registrar outra revisão e reexaminar
   as observações desta redação antes de substituir as figuras.

Foi iniciada aplicação local usando o caminho autorizado de configuração, sem
copiar ou exibir os valores de Secrets. As imagens não equivalem a publicação
das correções. Tentativas interrompidas permanecem identificadas nos manifestos
temporários; não são classificadas como ponta a ponta bem-sucedida.

## Inventário de capturas

Cada item informa título, destino, estado, conteúdo visível e discussão. O texto
introdutório correspondente já consta da subseção indicada no artigo.

### CAP-01 — Organização inicial da interface
- Arquivo: `fig/capturas/cap01_interface.png`; label `fig:cap01_interface`.
- Destino: §5.1 Visão geral e orientação geográfica.
- Função/estado: aplicação inicial autenticada, sem área e sem resultados.
- Visível: identidade, busca, datas, opções Todos/NDVI/NDWI/NDMI, botão desabilitado
  quando não houver área e mapa-base com atribuição.
- Introdução: a interface centraliza parâmetros e mapa.
- Discussão: prioridade espacial, relação entre entradas e processamento;
  não alegar usabilidade medida.

### CAP-02 — Busca e enquadramento geográfico
- Arquivo: `fig/capturas/cap02_busca.png`; label `fig:cap02_busca`.
- Destino: §5.1.
- Estado: busca real bem-sucedida em nome de localidade não sensível.
- Visível: texto consultado, descrição retornada, mapa centralizado e atribuição.
- Introdução: localização por texto aproxima a navegação da região.
- Discussão: Nominatim fornece coordenadas; Esri fornece tiles; isso não confirma
  propriedade nem integra Google Earth. Respeitar política pública de busca,
  sem autocomplete, no máximo uma requisição por segundo no conjunto da aplicação.

### CAP-03 — Demarcação e métricas
- Arquivo: `fig/capturas/cap03_poligono.png`; label `fig:cap03_poligono`.
- Destino: §5.2 Demarcação, métricas e reutilização.
- Estado: polígono fechado e aceito.
- Visível: contorno completo, área ha, perímetro km, centroide e opção Salvar.
- Introdução: o recorte geométrico determina as consultas e reduções.
- Discussão: área geométrica não é área de cultivo inferida; a escala a 10 m não
  elimina mistura de alvos ou limitações de resolução.

### CAP-04 — Salvamento de área
- Arquivo: `fig/capturas/cap04_salvar.png`; label `fig:cap04_salvar`.
- Destino: §5.2.
- Estado: diálogo aberto com nome demonstrativo e geometria válida.
- Visível: nome, confirmação/cancelamento e contexto do polígono.
- Introdução: o nome permite reutilizar a geometria.
- Discussão: validação antes de gravar, duplicidade case-insensitive, sem nova análise.

### CAP-05 — Listagem e restauração
- Arquivo: `fig/capturas/cap05_restaurar.png`; label `fig:cap05_restaurar`.
- Destino: §5.2.
- Estado: lista real e restauração de um item existente; dois painéis se necessário.
- Visível: nome selecionado, aviso de restauração e polígono recuperado.
- Introdução: restauração reconstrói a área sem geocodificação.
- Discussão: invalida resultados anteriores, não dispara análise; não ilustrar
  exclusão ou renomeação que não existem na UI atual.

### CAP-06 — Portabilidade GeoJSON
- Arquivo: `fig/capturas/cap06_geojson.png`; label `fig:cap06_geojson`.
- Destino: §5.2.
- Estado: ponto de entrada web, painel lateral expandido, arquivo válido preparado.
- Visível: aviso de duração da sessão, limites 100 áreas/2 MB, importação e download.
- Introdução: transferência explícita é a continuidade entre sessões web.
- Discussão: arquivo sob responsabilidade do usuário, IDs regenerados,
  importação integral ou rejeitada; sem sincronização automática.

### CAP-07 — Configuração do processamento
- Arquivo: `fig/capturas/cap07_parametros.png`; label `fig:cap07_parametros`.
- Destino: §5.3 Configuração e síntese.
- Estado: área válida e pedido pronto, antes de executar.
- Visível: datas legíveis, índices escolhidos e polígono.
- Introdução: parâmetros definem o pedido.
- Discussão: data final exclusiva no EE; escolher Todos compartilha coleção/clima,
  mas não torna os índices cientificamente independentes.

### CAP-08 — Painel de resultados
- Arquivo: `fig/capturas/cap08_painel.png`; label `fig:cap08_painel`.
- Destino: §5.3.
- Estado: análise real concluída, preferencialmente Todos.
- Visível: mapa, índice ativo, média, área, tendência e contagem se disponível.
- Introdução: síntese conecta produtos geográficos e estatísticos.
- Discussão: média espacial da composição; contagem antes da máscara não é
  frequência efetiva por pixel; não preencher valores indisponíveis.

### CAP-09 — Mapa NDVI
- Arquivo: `fig/capturas/cap09_ndvi.png`; label `fig:cap09_ndvi`.
- Destino: §5.4 Mapas temáticos.
- Estado: NDVI ativo com grade carregada.
- Visível: área, distribuição, gradiente e legenda reais.
- Introdução: mapa apresenta composição mediana, não aquisição única.
- Discussão: B8/B4; registrar mínimo/máximo usados nos tiles e potencial divergência
  da legenda. Não corrigir cores ou labels apenas na imagem.

### CAP-10 — Mapa NDWI do sistema
- Arquivo: `fig/capturas/cap10_ndwi.png`; label `fig:cap10_ndwi`.
- Destino: §5.4.
- Estado: mesma análise CAP-09, NDWI ativo.
- Visível: polígono, camada azul, gradiente e legenda.
- Introdução: o índice rotulado NDWI utiliza NIR–SWIR.
- Discussão: B8/B11; não denominar água superficial verde/NIR ou umidade do solo.

### CAP-11 — Mapa NDMI do sistema
- Arquivo: `fig/capturas/cap11_ndmi.png`; label `fig:cap11_ndmi`.
- Destino: §5.4.
- Estado: mesma área/período, NDMI ativo.
- Visível: contorno e distribuição em sua paleta.
- Introdução: NDMI complementa a seleção de bandas implementada.
- Discussão: B8A/B11; resolução nativa 20 m nas duas bandas; não justificar
  independência de índices apenas por rótulos ou cores distintas.

### CAP-12 — Consulta interativa por cursor
- Arquivo: `fig/capturas/cap12_cursor.png`; label `fig:cap12_cursor`.
- Destino: §5.5 Exploração interativa.
- Estado: valores pré-carregados, tooltip visível em posição interior válida.
- Visível: índice e valor com quatro casas, contorno e contexto. Painel adicional
  de Fora da área/Sem dado somente se efetivamente observado.
- Introdução: leitura numérica complementa a distribuição visual.
- Discussão: célula da composição mediana em grade UTM a 10 m; não média da área,
  média temporal ou imagem individual. Registrar posição consultada se possível.
  Captura do cursor pode exigir captura de tela do sistema ou automação com hover;
  não desenhar tooltip manualmente.

### CAP-13 — Série temporal
- Arquivo: `fig/capturas/cap13_series.png`; label `fig:cap13_series`.
- Destino: §5.6 Evolução temporal.
- Estado: série real do índice da demonstração.
- Visível: eixos, datas, pontos e nome. Mais de um painel só se acrescentar informação.
- Introdução: médias por aquisição descrevem evolução da área.
- Discussão: irregularidade, lacunas e possíveis datas repetidas; não trajetória
  do pixel sob o cursor; não afirmar ciclo de cultura não confirmada.

### CAP-14 — Sinalização estatística
- Arquivo: `fig/capturas/cap14_anomalias.png`; label `fig:cap14_anomalias`.
- Destino: §5.6.
- Estado: ocorrências reais ou mensagem de ausência.
- Visível: alerta e lista de datas/valores quando existentes.
- Introdução: interface apresenta desvios negativos detectados.
- Discussão: janela 3, limiar estrito, sem causas agronômicas. Não fabricar
  queda, classificador de doenças ou marcador que o gráfico não implementa.

### CAP-15 — Contexto meteorológico
- Arquivo: `fig/capturas/cap15_clima.png`; label `fig:cap15_clima`.
- Destino: §5.7.
- Estado: resposta real disponível; observar diferença entre análise única e Todos.
- Visível: barras de precipitação, linha de temperatura média diária, eixos,
  datas, fonte e cartões somente quando realmente mostrados.
- Introdução: a série agrega contexto ao período.
- Discussão: ponto do centroide, não estação local; máximas/mínimas não solicitadas;
  soma versus média. Informar inconsistência de radiação e ausência possível do
  resumo multiíndice; não esconder o problema no recorte.

### CAP-16 — Geração e download
- Arquivo: `fig/capturas/cap16_exportacao.png`; label `fig:cap16_exportacao`.
- Destino: §5.8 Relatórios e dados.
- Estado: parâmetros coincidentes com análise concluída, ao menos um arquivo pronto.
- Visível: PDF, Excel, CSV ZIP, ações de geração e download.
- Introdução: geração é sob demanda, a partir do snapshot.
- Discussão: mudança de parâmetros bloqueia exportação; existência do botão não
  comprova conteúdo correto de todos os formatos.

### CAP-17 — Relatório PDF real
- Arquivo: `fig/capturas/cap17_pdf.png`; label `fig:cap17_pdf`.
- Destino: §5.8.
- Estado: PDF baixado da análise demonstrada, aberto em leitor.
- Visível: página completa, índice, período, área, métricas, série, anomalias,
  mapa, gradiente, atribuição. Usar detalhes/painéis para garantir legibilidade.
- Introdução: saída visual sintetiza uma página por índice.
- Discussão: três páginas apenas com três índices; escala fixa [-1,1];
  não mapa interativo; mapa indisponível deve permanecer declarado. Nome de área
  e coordenadas não são automaticamente impressos como identificação cadastral.
- Não reutilizar o relatório sintético de 20/10/2026 como análise real.

### CAP-18 — Planilha XLSX
- Arquivo: `fig/capturas/cap18_xlsx.png`; label `fig:cap18_xlsx`.
- Destino: §5.8.
- Estado: arquivo da mesma sessão aberto em Excel/LibreOffice ou visualizador.
- Visível: nomes das abas, exemplos de série/clima/geografia, datas e cabeçalhos.
- Introdução: estrutura tabular permite inspeção e reuso.
- Discussão: 4 + número de índices abas; tendência repetida global; classificação
  causal pode estar vazia; GeoJSON em texto. Não alterar valores exportados.

### CAP-19 — Arquivos CSV e ZIP
- Arquivo: `fig/capturas/cap19_zip.png`; label `fig:cap19_zip`.
- Destino: §5.8.
- Estado: ZIP baixado e um CSV aberto.
- Visível: nomes dos arquivos, cabeçalhos, codificação/data e valores reais.
- Introdução: conjuntos separados favorecem uso em ferramentas externas.
- Discussão: UTF-8, vírgula, DEFLATE, quatro arquivos comuns mais índices;
  ausência representada por campo vazio; nenhum raster GeoTIFF exportado.

## Diagramas técnicos

| ID | Arquivo TikZ / label | Seção | Conteúdo e evidência | Estado |
|---|---|---|---|---|
| DIA-01 | `fig/arquitetura_atual.tex` / `fig:arquitetura-atual` | §4.1 | Servidor, navegador, EE, NASA POWER, Nominatim, Esri, repositórios, arquivos | Produzido/revisado; leitura visual preliminar |
| DIA-02 | `fig/fluxo_analise.tex` / `fig:fluxo-analise` | §3.5 | Filtros, QA60, índice por aquisição, mediana por pixel, média espacial, série e clima | Produzido/revisado |
| DIA-03 | `fig/fluxo_anomalias.tex` / `fig:fluxo-anomalias` | §3.6 | Primeiros pontos, janela, desvio zero, z e sinalização | Produzido |
| DIA-04 | `fig/fluxo_areas.tex` / `fig:fluxo-areas` | §4.4 | Desenho, área ativa, nome, repositório, lista/restauração e GeoJSON | Produzido |
| DIA-05 | `fig/fluxo_consulta_pixel.tex` / `fig:fluxo-consulta-pixel` | §4.6 | Projeção, sampleRectangle, compressão, navegador e consulta local | Produzido |
| DIA-06 | `fig/fluxo_exportacao.tex` / `fig:fluxo-exportacao` | §4.8 | Snapshot, conferência, normalização e geração dos formatos | Produzido |
| DIA-07 | `fig/classes_localizacao.tex` / `fig:classes-localizacao` | §4.4 | Classes reais e dois repositórios | Preservado e reutilizado |

O diagrama `fig/casos_uso.tex` permanece disponível como material anterior,
mas não é incluído para evitar repetir fluxos já cobertos. `figura1.png` a
`figura4.png` pertencem à proposta e não foram reapresentadas como capturas reais.

## Pendências para a versão de entrega

- Inserir as 19 capturas/painéis, atualizar suas legendas e registrar manifesto.
- Decidir com o orientador a distribuição final entre corpo e apêndices, sem
  limite artificial de páginas; não suprimir fluxos essenciais.
- Verificar legendas/escala e unidades antes de sustentar interpretação quantitativa.
- Rever tamanho de letras dos diagramas após as capturas alterarem a paginação.
- Confirmar atribuições e autorização de divulgação de geometrias e imagens.
- Recompilar e revisar referências cruzadas, numeração, contraste e cortes.
