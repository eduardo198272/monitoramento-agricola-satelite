# Spec: Exportação dos Resultados de Análise

## Propósito

Permitir que o usuário baixe os resultados reais de uma análise multiíndice em
PDF para apresentação e em Excel ou CSV para consulta e processamento posterior.
As exportações devem representar o mesmo conjunto de resultados exibido pela
aplicação, sem executar novamente o pipeline científico nem substituir dados
ausentes por valores estimados.

## Escopo

Incluído:

- relatório PDF com exatamente três páginas, uma para cada índice suportado:
  NDVI, NDWI e NDMI;
- mapa estático por página contendo a camada temática do índice sobre imagem de
  satélite, geometria da área e legenda;
- workbook XLSX com abas de índices, clima, anomalias e posição geográfica;
- arquivo ZIP contendo os mesmos conjuntos de dados em CSVs individuais;
- ações de download após análise concluída com os três índices disponíveis;
- validação dos artefatos e testes automatizados sem chamadas de rede reais.

Não incluído:

- exportar/compartilhar dados com serviços externos;
- executar ou recalcular análises durante a geração dos arquivos;
- exportação de análises de índice único como se contivessem os outros índices;
- diagnóstico agronômico, interpolação de série ou inferência de medições ausentes;
- persistir os relatórios gerados no servidor.

## Interface e contratos

### Pré-condição da exportação

As ações ficam disponíveis somente quando a análise mais recente terminou com
sucesso e contém resultados válidos de NDVI, NDWI e NDMI. A análise deve ter sido
executada em modo multiíndice (`Todos`). Uma análise de índice único não satisfaz
essa condição; a interface deve informar que é necessário executar a análise
multiíndice, em vez de gerar indicadores incompletos ou simular dados.

O estado usado na exportação deve incluir, quando disponíveis:

- período inicial e final normalizados como `YYYY-MM-DD`;
- geometria GeoJSON analisada, área em hectares e centro geográfico;
- para cada índice: média, série temporal, tendência, anomalias e imagem/mapa do
  índice retornados pelo pipeline;
- observações e resumo climático existentes no resultado da análise;
- contagem de imagens e metadados da coleção somente quando confirmados pelo
  pipeline.

### Interfaces de serviço

As assinaturas abaixo são contratos propostos para orientar a implementação; os
nomes finais podem seguir a organização modular existente, mantendo entradas e
saídas testáveis e independentes da UI.

```python
def build_export_context(analysis: dict, geometry_geojson: dict,
                         start_date: str, end_date: str) -> dict
```

Valida e normaliza o snapshot da análise. Não faz chamadas a Earth Engine, NASA
POWER ou geocodificadores. Rejeita análise incompleta e datas inválidas.

```python
def render_analysis_pdf(export_context: dict) -> bytes
```

Retorna bytes de um PDF válido com exatamente três páginas, na ordem NDVI, NDWI,
NDMI. Não grava arquivos permanentes.

```python
def render_analysis_xlsx(export_context: dict) -> bytes
```

Retorna bytes de workbook XLSX com abas e colunas especificadas nesta spec.

```python
def render_analysis_csv_zip(export_context: dict) -> bytes
```

Retorna bytes ZIP com um CSV UTF-8 por conjunto de dados, usando cabeçalho mesmo
quando o conjunto estiver vazio.

## Contratos dos artefatos

### PDF

- O PDF contém **exatamente três páginas**, em orientação paisagem ou retrato
  definida pela implementação e validada visualmente; nenhuma página extra de
  capa ou apêndice é permitida.
- Ordem fixa: NDVI, NDWI e NDMI; cada página identifica indicador, intervalo de
  análise, data de geração e área analisada.
- Cada página inclui média disponível, tendência disponível, série temporal com
  amostras reais, anomalias reais do índice e mapa temático estático.
- Cada mapa inclui composição do índice sobre uma imagem-base de satélite,
  contorno da área, legenda/rampa com unidades ou intervalo do índice e
  enquadramento que contenha toda a geometria. O mapa não pode ser apenas uma
  captura do componente interativo do navegador.
- Contexto geográfico e climático compartilhado pode ser repetido de forma
  compacta nas três páginas, preservando o limite de três páginas.
- Métrica, série, clima ou mapa indisponível deve ser identificado explicitamente
  como indisponível; falha ao gerar um mapa não pode ser representada como mapa
  válido nem apagar os demais resultados.
- Conteúdo textual e valores devem permanecer legíveis, sem cortes ou sobreposição.

### Excel e CSV

O XLSX e o ZIP de CSV representam os mesmos conjuntos, com nomes lógicos estáveis:

| Conjunto / aba XLSX | Colunas mínimas |
|---|---|
| `Resumo` | `campo`, `valor`, `unidade`; incluir período, área, contagem de imagens e data de geração quando disponíveis |
| `NDVI`, `NDWI`, `NDMI` | `date`, `value`, `trend`, `anomaly`; uma linha por amostra temporal, com tendência/anomalia associadas à data quando existirem |
| `Clima` | `date`, `precipitation_mm`, `temperature_c`, `solar_radiation_mj_m2_day`; manter nulos para valores ausentes |
| `Anomalias` | `index`, `date`, `value`, `anomaly`, `classification` ou campos efetivamente retornados pelo detector |
| `Geografia` | `field`, `value`, `unit`; incluir área, centroide (latitude/longitude), CRS e GeoJSON completo da geometria como texto |

- Nomes de abas obedecem ao limite/formato XLSX e não variam conforme locale.
- Datas tabulares usam ISO `YYYY-MM-DD`; valores numéricos são células numéricas
  no XLSX e decimal com ponto nos CSVs.
- Unidades ficam explícitas nos nomes das colunas ou no resumo; conversões usam
  somente as métricas já agregadas pelo pipeline.
- Dados ausentes são células vazias/nulos, nunca zero ou string numérica
  fabricada. CSVs usam UTF-8, cabeçalho e vírgula como delimitador.
- O ZIP inclui `resumo.csv`, `ndvi.csv`, `ndwi.csv`, `ndmi.csv`, `clima.csv`,
  `anomalias.csv` e `geografia.csv`, sem caminhos absolutos ou arquivos executáveis.
- O GeoJSON preserva a geometria analisada sem reduzir precisão; CRS declarado
  deve ser explícito (WGS84/EPSG:4326 se essa for a geometria de entrada).

## Regras de negócio

- Exportar somente o snapshot da análise concluída atualmente exibida; mudança de
  área, período ou análise invalida/exporta somente o estado novo.
- Gerar cada artefato sob demanda, em memória ou diretório temporário controlado;
  não persistir dados sensíveis nem deixar arquivos temporários após a resposta.
- Não refazer requisições ao Earth Engine ou NASA POWER durante serialização.
- Não alterar fórmulas, limiares, dados-fonte ou algoritmo de detecção de
  anomalias para adequar o documento.
- Valores comuns (período, área, coordenadas) são compartilhados por formatos
  através do contexto normalizado, evitando divergência entre PDF/XLSX/CSV.
- Geradores devem receber dependências externas injetáveis ou encapsuladas para
  teste offline; falhas por biblioteca ausente, renderização do mapa ou conteúdo
  inválido devem produzir erro tratável pela UI.
- O PDF usa visualização rasterizada do mapa com resolução suficiente para
  leitura; atribuição/licença da fonte de tiles e imagem deve ser mantida quando
  aplicável.

## Critérios de aceitação

1. Dada uma análise multiíndice bem-sucedida com os três resultados, quando o
   usuário solicitar PDF, então baixa um PDF legível com exatamente três páginas
   na ordem NDVI, NDWI, NDMI.
2. Dada cada página do PDF, então ela identifica o índice, apresenta seus dados
   reais disponíveis, série temporal, anomalias e mapa temático sobre imagem de
   satélite com geometria e legenda.
3. Dado que mapa ou métrica não esteja disponível, então o relatório sinaliza a
   ausência sem inventar valor e continua respeitando três páginas.
4. Dada uma análise single-index ou um dos três índices ausente, então a
   exportação completa não é oferecida/é recusada com orientação para executar
   análise multiíndice.
5. Dada uma análise válida, quando o usuário baixar XLSX, então o workbook abre,
   contém as abas/colunas definidas, e as células preservam tipos numéricos,
   datas, nulos e unidades.
6. Dada a mesma análise, quando o usuário baixar CSV, então o ZIP contém os
   sete arquivos CSV definidos, em UTF-8, com cabeçalhos estáveis e dados
   equivalentes ao XLSX.
7. Dado que algum conjunto não possua observações, então seu CSV mantém o
   cabeçalho e a aba correspondente continua presente no workbook.
8. Ao gerar qualquer formato, então não há nova chamada de rede a Earth Engine,
   NASA POWER ou geocodificação.
9. Dado estado de análise inválido, antigo ou sem geometria, então a geração é
   recusada de forma segura, com mensagem útil na interface.
10. Os testes automatizados validam estrutura do PDF, estrutura/valores XLSX,
    membros/conteúdo do ZIP CSV, cenários ausentes e caminhos de erro sem usar
    serviços externos reais.

## Dependências

- `15-ui-v2-dashboard-parity/spec-ui-dashboard-parity.md` — estado visual e
  resultados multiíndice.
- `03-indices/spec-ndvi.md`, `spec-ndwi.md`, `spec-ndmi.md` — semântica dos
  índices.
- `06-series-temporais/spec-serie-temporal.md` e
  `07-anomalias/spec-deteccao-anomalias.md` — dados temporais/anomalias.
- `08-clima/spec-nasa-power.md` — dados, nulos e unidades climáticas.
- `04-mapas/spec-visualizacao-indice.md` e baseline de mapa satélite da SPEC-15.

## Tasks relacionadas

- SPEC-16-01 a SPEC-16-10 — `tasks-exportacao-resultados.md`.
