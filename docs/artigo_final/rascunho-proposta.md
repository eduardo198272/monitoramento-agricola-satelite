# Sistema de Monitoramento Agrícola por Imagens de Satélite

## Resumo

A agricultura moderna demanda mecanismos de acompanhamento capazes de apoiar a tomada de decisão em áreas cultivadas, especialmente quando a extensão da lavoura, a variabilidade climática e o custo de inspeções presenciais dificultam o monitoramento frequente. Nesse contexto, o presente trabalho propõe o desenvolvimento de um sistema de monitoramento agrícola baseado em imagens de satélite, com uso de sensoriamento remoto, índices espectrais e dados climáticos gratuitos. O objetivo é desenvolver um protótipo funcional capaz de selecionar uma área de interesse, consultar imagens Sentinel-2 por meio do Google Earth Engine, calcular índices como o Normalized Difference Vegetation Index e o Normalized Difference Water Index, gerar mapas temáticos, produzir séries temporais e indicar possíveis anomalias na vegetação. A metodologia prevê a implementação do sistema em Python, com interface em Streamlit, integração com geemap e Plotly, processamento geoespacial em nuvem pelo Google Earth Engine e consulta complementar a dados climáticos da NASA POWER. A validação será realizada por meio de testes funcionais, análise de três áreas agrícolas representativas, comparação dos valores dos índices com faixas esperadas na literatura e interpretação conjunta com variáveis climáticas, como precipitação, temperatura e radiação solar. Espera-se demonstrar a viabilidade técnica de uma solução acadêmica de baixo custo, reproduzível e baseada em ferramentas abertas para apoiar a análise da condição da vegetação em lavouras, sem substituir a avaliação agronômica em campo.

## 1 Motivação e objetivos

### 1.1 Motivação

A agricultura tem incorporado tecnologias digitais para lidar com desafios relacionados à produtividade, uso eficiente de recursos, variabilidade climática e acompanhamento de grandes áreas de produção. Em muitas propriedades, o monitoramento da lavoura ainda depende de vistorias presenciais, relatórios manuais ou ferramentas comerciais de custo elevado. Esse cenário pode limitar o acesso de pequenos produtores, estudantes e pesquisadores a informações objetivas sobre a condição da vegetação ao longo do ciclo produtivo.

O sensoriamento remoto oferece uma alternativa relevante para esse problema, pois permite observar a superfície terrestre sem contato físico direto, utilizando sensores embarcados em satélites. Imagens multiespectrais possibilitam a análise de bandas que não são percebidas pelo olho humano, como o infravermelho próximo e o infravermelho de ondas curtas. A partir dessas bandas, é possível calcular índices espectrais que resumem características da vegetação, como vigor, densidade e teor de umidade.

Entre os índices mais utilizados está o Normalized Difference Vegetation Index, conhecido como NDVI, que relaciona a reflectância no vermelho e no infravermelho próximo para estimar o vigor da vegetação. Para complementar essa análise, o Normalized Difference Water Index, conhecido como NDWI na formulação voltada ao teor de água da vegetação, utiliza bandas no infravermelho próximo e no infravermelho de ondas curtas. A combinação desses índices permite observar tanto a condição geral da vegetação quanto possíveis sinais de estresse hídrico.

A disponibilidade de imagens Sentinel-2 e o acesso a plataformas como Google Earth Engine tornam possível processar grandes volumes de dados geoespaciais sem exigir armazenamento local de imagens. Além disso, bases climáticas como NASA POWER podem ser utilizadas para relacionar alterações nos índices espectrais com precipitação, temperatura e radiação solar. Dessa forma, há uma oportunidade de desenvolver um sistema acadêmico simples, de baixo custo e reproduzível, capaz de demonstrar a aplicação prática de sensoriamento remoto no monitoramento agrícola.

A motivação deste trabalho está na necessidade de aproximar técnicas de sensoriamento remoto e ciência de dados de um protótipo acessível, voltado à visualização de mapas, séries temporais e alertas preliminares. O sistema proposto não pretende substituir a inspeção em campo nem fornecer diagnóstico agronômico definitivo. Seu propósito é apoiar a análise inicial da lavoura, indicar regiões ou períodos que merecem atenção e demonstrar a viabilidade do uso de dados gratuitos no contexto do agronegócio.

### 1.2 Problema de pesquisa

O problema abordado por este trabalho pode ser formulado da seguinte maneira: como desenvolver um sistema de baixo custo, baseado em imagens de satélite e dados climáticos gratuitos, capaz de auxiliar no monitoramento da condição da vegetação em áreas agrícolas por meio de índices espectrais e séries temporais?

Esse problema envolve aspectos computacionais e metodológicos. Do ponto de vista computacional, é necessário integrar interface, processamento geoespacial, APIs externas, cálculo de índices, geração de mapas e visualização temporal. Do ponto de vista metodológico, é preciso definir quais dados serão utilizados, como os índices serão calculados, quais critérios serão adotados para detectar anomalias e como os resultados serão validados.

### 1.3 Justificativa

A justificativa técnica do trabalho está na possibilidade de integrar tecnologias consolidadas, como Python, Streamlit, Google Earth Engine, Sentinel-2 e NASA POWER, em um fluxo único de análise. Essa integração permite construir um protótipo que processa dados reais e apresenta resultados compreensíveis ao usuário, sem exigir infraestrutura complexa.

A justificativa acadêmica está na aplicação de conceitos de Ciência da Computação a um problema interdisciplinar, envolvendo desenvolvimento de software, processamento de dados, visualização, geoprocessamento e validação experimental. O trabalho também contribui para demonstrar como um sistema computacional pode organizar dados de sensoriamento remoto e clima em uma ferramenta de apoio à análise agrícola.

A justificativa social e prática está relacionada à democratização do acesso a informações sobre lavouras. Embora existam soluções comerciais avançadas, nem sempre elas são acessíveis para pequenos produtores ou ambientes educacionais. Um protótipo baseado em ferramentas gratuitas pode servir como base para estudos, treinamentos, pesquisas futuras e evolução para aplicações mais robustas.

### 1.4 Objetivo geral

Desenvolver um sistema de monitoramento agrícola baseado em imagens de satélite, capaz de calcular índices espectrais, gerar mapas e séries temporais e indicar possíveis anomalias na vegetação, demonstrando a viabilidade do uso de sensoriamento remoto e ferramentas gratuitas como apoio à análise de áreas cultivadas.

### 1.5 Objetivos específicos

- Estudar conceitos de sensoriamento remoto aplicados ao monitoramento agrícola.
- Investigar o uso de imagens Sentinel-2 para análise de vegetação em áreas cultivadas.
- Definir a arquitetura do sistema, integrando interface, processamento e fontes externas de dados.
- Implementar rotinas em Python para consulta de imagens no Google Earth Engine.
- Calcular índices espectrais, com foco em NDVI e NDWI, a partir das bandas do Sentinel-2.
- Gerar mapas temáticos e séries temporais dos índices calculados.
- Integrar dados climáticos da NASA POWER para análise complementar.
- Implementar mecanismo simples de detecção de anomalias com base em desvio estatístico.
- Desenvolver interface web em Streamlit para entrada de parâmetros e visualização dos resultados.
- Validar o protótipo com áreas agrícolas representativas, como soja, milho e pastagem.
- Documentar limitações, resultados esperados e possibilidades de evolução do sistema.

### 1.6 Hipóteses e pressupostos de validação

Como se trata de uma proposta de desenvolvimento de protótipo, a validação será orientada principalmente pelo atendimento aos objetivos e pelo comportamento esperado do sistema. Ainda assim, podem ser considerados os seguintes pressupostos:

- O uso de imagens Sentinel-2 permite obter séries temporais úteis para observar variações de vegetação em áreas agrícolas.
- A combinação entre NDVI e NDWI oferece uma visão mais completa do estado da lavoura do que o uso isolado de apenas um índice.
- A integração com dados climáticos auxilia na interpretação de quedas ou oscilações dos índices espectrais.
- Um protótipo baseado em ferramentas gratuitas é suficiente para demonstrar a viabilidade técnica da abordagem em contexto acadêmico.

## 2 Revisão de literatura

### 2.1 Estratégia de revisão

A revisão de literatura será conduzida como revisão narrativa organizada, com registro das fontes utilizadas e dos critérios de seleção. O objetivo não é executar uma revisão sistemática completa, mas reunir fundamentos técnicos e trabalhos relacionados suficientes para sustentar a proposta, delimitar o problema e justificar a metodologia.

As buscas devem priorizar fontes acadêmicas e documentação oficial. Para a fundamentação conceitual, serão consideradas publicações sobre sensoriamento remoto, índices espectrais, agricultura de precisão e monitoramento de culturas. Para a parte tecnológica, serão utilizadas documentações oficiais do Sentinel-2, Google Earth Engine e NASA POWER, além de materiais relacionados ao desenvolvimento em Python.

Os critérios de inclusão são: relação direta com sensoriamento remoto agrícola, uso de índices espectrais, monitoramento de vegetação, processamento geoespacial em nuvem ou ferramentas utilizadas no sistema. Os critérios de exclusão são: fontes sem relação com agricultura ou vegetação, textos opinativos sem base técnica, materiais sem autoria ou procedência identificável e referências que não possam ser verificadas.

### 2.2 Sensoriamento remoto aplicado à agricultura

Sensoriamento remoto é a técnica de obter informações sobre objetos ou áreas da superfície terrestre sem contato físico direto. Em vez de coletar dados apenas por observação presencial, sensores instalados em satélites, aeronaves ou drones capturam a radiação refletida ou emitida pelos alvos. No contexto agrícola, essa abordagem permite analisar áreas extensas de forma recorrente, reduzindo a dependência de inspeções manuais para a observação inicial da lavoura.

O princípio central dessa aplicação é que diferentes alvos apresentam comportamentos distintos no espectro eletromagnético. A vegetação saudável tende a absorver fortemente a radiação na faixa do vermelho, devido à atividade fotossintética, e a refletir intensamente no infravermelho próximo, em função da estrutura interna das folhas. Já vegetações estressadas, solo exposto, água e áreas urbanizadas apresentam respostas espectrais diferentes. Essa diferença permite transformar medidas de reflectância em indicadores numéricos da condição da vegetação.

No monitoramento agrícola, o sensoriamento remoto é útil para acompanhar desenvolvimento vegetativo, identificar variações espaciais dentro de talhões, observar possíveis falhas de plantio, detectar tendências de estresse e relacionar alterações da vegetação com eventos climáticos. Entretanto, seus resultados devem ser interpretados como indicadores indiretos. A imagem de satélite não identifica automaticamente a causa agronômica de um problema; ela aponta padrões que precisam ser analisados em conjunto com conhecimento de campo, histórico da cultura e dados complementares.

### 2.3 Sentinel-2

A missão Sentinel-2, pertencente ao programa Copernicus, é composta por satélites de imageamento multiespectral voltados ao monitoramento terrestre. A missão oferece alta frequência de revisita e bandas espectrais adequadas à análise de vegetação, solo, água e cobertura terrestre. O instrumento Multi-Spectral Instrument registra bandas em resoluções espaciais de 10 m, 20 m e 60 m, abrangendo faixas do visível, infravermelho próximo e infravermelho de ondas curtas.

Para este trabalho, as bandas mais relevantes são a B4, correspondente ao vermelho, a B8, correspondente ao infravermelho próximo, e a B11, correspondente ao infravermelho de ondas curtas. A B4 e a B8 são utilizadas no cálculo do NDVI; a B8 e a B11 são utilizadas no cálculo do NDWI voltado à umidade da vegetação. A resolução espacial dessas bandas permite analisar talhões agrícolas, embora não permita a identificação de plantas individuais.

O uso de produtos de reflectância de superfície, como a coleção harmonizada Sentinel-2 MSI Level-2A disponível no Google Earth Engine, é adequado para análises temporais porque reduz efeitos atmosféricos em comparação com dados brutos. Ainda assim, é necessário aplicar filtros de data, área e cobertura de nuvens, pois nuvens e sombras podem distorcer o valor dos índices e gerar interpretações incorretas.

### 2.4 Índices espectrais

Índices espectrais são combinações matemáticas entre bandas de uma imagem multiespectral. Seu objetivo é realçar determinadas características da superfície e reduzir a complexidade da análise, convertendo múltiplas bandas em um indicador numérico.

O NDVI é calculado pela razão normalizada entre o infravermelho próximo e o vermelho:

```text
NDVI = (NIR - RED) / (NIR + RED)
```

Em imagens Sentinel-2, o NIR corresponde à banda B8 e o RED à banda B4. Valores próximos de zero indicam baixa presença de vegetação ou solo exposto; valores positivos mais altos indicam vegetação mais densa ou vigorosa; valores negativos costumam estar associados a água, nuvens ou superfícies não vegetadas. Em lavouras, o NDVI tende a variar ao longo do ciclo da cultura, crescendo durante o desenvolvimento vegetativo e reduzindo próximo à senescência ou colheita.

O NDWI, na formulação de Gao voltada à vegetação, utiliza o infravermelho próximo e o infravermelho de ondas curtas:

```text
NDWI = (NIR - SWIR) / (NIR + SWIR)
```

No Sentinel-2, o NIR pode ser representado pela banda B8 e o SWIR pela banda B11. Esse índice é sensível ao conteúdo de água da vegetação, pois a reflectância no SWIR responde de maneira relevante à água presente nas folhas. Assim, valores baixos de NDWI podem sugerir menor teor de umidade ou possível estresse hídrico, especialmente quando interpretados junto com precipitação e temperatura.

Para este trabalho, NDVI e NDWI serão utilizados de forma complementar. O NDVI servirá como indicador principal de vigor da vegetação, enquanto o NDWI apoiará a análise de umidade. A interpretação conjunta reduz o risco de conclusões baseadas em um único indicador e ajuda a separar variações relacionadas ao crescimento normal da cultura de possíveis alterações associadas à disponibilidade hídrica.

### 2.5 Google Earth Engine

O Google Earth Engine é uma plataforma de processamento geoespacial em nuvem que disponibiliza catálogos de imagens de satélite e ferramentas para análise em larga escala. Seu uso é adequado para este trabalho porque evita a necessidade de baixar e armazenar localmente grandes volumes de imagens, transferindo operações como filtragem, composição, cálculo de índices e redução regional para servidores remotos.

No sistema proposto, o Earth Engine será utilizado por meio da API Python. A aplicação consultará a coleção Sentinel-2, filtrará imagens por área, período e percentual de nuvens, calculará índices espectrais e retornará mapas ou estatísticas para a área de interesse. A função de diferença normalizada da plataforma permite implementar índices como NDVI e NDWI de forma direta, desde que as bandas corretas sejam informadas.

Essa escolha tecnológica também contribui para a reprodutibilidade. Como os dados estão em uma coleção pública e as operações são definidas em código, a análise pode ser repetida para diferentes áreas e períodos, respeitando as limitações de disponibilidade de imagens e autenticação do serviço.

### 2.6 Dados climáticos

Dados climáticos são importantes para interpretar a dinâmica dos índices espectrais. Uma queda no NDVI, por exemplo, pode estar associada a senescência natural da cultura, colheita, falha de imagem, nuvens, seca, excesso de chuva, pragas ou outros fatores. A inclusão de variáveis como precipitação, temperatura e radiação solar não resolve automaticamente essa ambiguidade, mas fornece contexto adicional.

A NASA POWER disponibiliza dados meteorológicos e de radiação solar por meio de API, com parâmetros como precipitação diária, temperatura média e radiação solar de superfície. No protótipo, a consulta será feita para o ponto central da área de interesse e para o mesmo intervalo temporal das imagens de satélite. Os dados serão apresentados em gráficos e comparados visualmente com as séries dos índices espectrais.

Essa integração permite que o usuário observe relações temporais, como queda de NDVI após período de baixa precipitação ou variações de vigor após mudanças climáticas. Ainda assim, a interpretação será apresentada como apoio à análise, não como diagnóstico causal definitivo.

### 2.7 Sistemas de monitoramento agrícola e lacuna identificada

Sistemas de monitoramento agrícola por sensoriamento remoto já são utilizados em diferentes níveis de complexidade. Soluções comerciais podem oferecer integração com mapas, sensores, maquinário, bancos de dados e alertas automáticos. Contudo, tais ferramentas podem apresentar custos, restrições de acesso ou complexidade incompatíveis com pequenos produtores, ambientes acadêmicos e protótipos de pesquisa.

A lacuna explorada neste trabalho não é a criação de um método novo de sensoriamento remoto, mas a construção de um fluxo computacional integrado e reproduzível que demonstre, em escala de protótipo, como dados gratuitos podem ser organizados em uma aplicação prática. O diferencial está na integração entre seleção de área, consulta de imagens Sentinel-2, cálculo de índices, visualização temporal, detecção simples de anomalias e comparação com clima em um sistema acessível.

Assim, o trabalho se enquadra como pesquisa aplicada em Ciência da Computação, com desenvolvimento de artefato e validação por estudo de caso. Seu valor está em demonstrar a viabilidade técnica da solução e em documentar claramente os limites do protótipo para que ele possa ser evoluído em trabalhos futuros.

## 3 Materiais e métodos

### 3.1 Caracterização da pesquisa

Este trabalho caracteriza-se como uma pesquisa aplicada, de natureza experimental e tecnológica, com desenvolvimento de um protótipo funcional. A abordagem combina estudo bibliográfico, implementação de sistema computacional e validação empírica por meio de cenários de teste em áreas agrícolas.

O método adotado não se limita à construção da aplicação. Ele define um conjunto de etapas necessárias para demonstrar que o objetivo foi atingido: definição da arquitetura, coleta de dados, implementação dos índices, desenvolvimento da interface, integração climática, testes funcionais, análise dos resultados e documentação das limitações.

### 3.2 Materiais e ferramentas

O sistema será desenvolvido com ferramentas gratuitas ou de amplo acesso acadêmico:

| Recurso | Função no projeto |
|---|---|
| Python | Linguagem principal de desenvolvimento |
| Streamlit | Interface web para interação com o usuário |
| Google Earth Engine | Consulta e processamento de imagens de satélite |
| Sentinel-2 Level-2A | Fonte principal de imagens multiespectrais |
| geemap | Integração entre Earth Engine e mapas interativos |
| Plotly | Geração de gráficos e séries temporais |
| pandas e numpy | Manipulação de dados e cálculos estatísticos |
| NASA POWER | Consulta de precipitação, temperatura e radiação solar |
| pytest | Testes automatizados do sistema |

O protótipo deverá executar localmente em computador pessoal, com autenticação no Google Earth Engine por meio de variável de ambiente contendo o identificador do projeto. O processamento pesado das imagens será realizado no Earth Engine, reduzindo a necessidade de armazenamento local.

### 3.3 Arquitetura proposta

A arquitetura seguirá uma organização em três camadas:

1. Camada de interface: aplicação Streamlit responsável pela entrada de parâmetros e exibição de resultados.
2. Camada de processamento: módulos Python responsáveis por autenticação, consulta de dados, cálculo de índices, séries temporais, anomalias e preparação dos gráficos.
3. Camada de dados externos: Google Earth Engine para imagens Sentinel-2 e NASA POWER para dados climáticos.

O fluxo geral será:

```text
Usuário
  -> Interface Streamlit
  -> Processamento Python
  -> Google Earth Engine
  -> Sentinel-2
  -> Cálculo dos índices
  -> Séries temporais e anomalias
  -> NASA POWER
  -> Mapas, gráficos e alertas
```

Essa arquitetura favorece modularidade, pois separa a interface da lógica de processamento. Também facilita testes automatizados, já que funções como cálculo de índices, geração de séries e detecção de anomalias podem ser validadas separadamente.

### 3.4 Etapas de desenvolvimento

#### 3.4.1 Definição da arquitetura

A primeira etapa consiste em definir os componentes do sistema, o fluxo de dados e as responsabilidades de cada módulo. Serão documentadas as entradas do usuário, as consultas externas, as estruturas de retorno e as visualizações esperadas.

#### 3.4.2 Coleta de dados de satélite

As imagens serão obtidas a partir da coleção Sentinel-2 no Google Earth Engine. O sistema deverá receber a geometria da área de interesse, a data inicial e a data final. Em seguida, aplicará filtros de área, período e cobertura de nuvens.

Serão utilizadas principalmente as bandas:

- B4: vermelho, usada no NDVI.
- B8: infravermelho próximo, usada no NDVI e no NDWI.
- B11: infravermelho de ondas curtas, usada no NDWI.

Os metadados relevantes, como data de aquisição, percentual de nuvens e identificador da imagem, deverão ser preservados para rastreabilidade.

#### 3.4.3 Cálculo de índices espectrais

Para cada imagem válida, o sistema calculará NDVI e NDWI por meio de operações de diferença normalizada. Os resultados serão mantidos como bandas derivadas e utilizados em duas frentes:

- geração de mapa temático para visualização espacial;
- cálculo de estatísticas médias na área de interesse para composição de série temporal.

As estatísticas previstas incluem média, mediana, mínimo, máximo e desvio padrão, quando aplicável.

#### 3.4.4 Desenvolvimento da interface

A interface será implementada em Streamlit. Ela deverá permitir:

- selecionar ou desenhar a área de interesse;
- definir data inicial e data final;
- escolher o índice a ser analisado;
- executar a análise;
- visualizar mapa temático;
- visualizar gráfico de série temporal;
- consultar resumo estatístico;
- visualizar alerta de anomalia, quando existir;
- visualizar dados climáticos associados ao período.

Como o objetivo é um MVP acadêmico, não serão incluídos cadastro de usuários, banco de dados complexo, controle de permissões ou aplicação móvel.

#### 3.4.5 Integração de dados climáticos

O sistema consultará a NASA POWER usando a coordenada central da área de interesse e o mesmo intervalo temporal escolhido para as imagens. As variáveis inicialmente previstas são:

- precipitação diária;
- temperatura média diária;
- radiação solar de superfície.

Os dados serão convertidos para tabela e exibidos em gráficos. A interpretação será feita de forma comparativa, observando se oscilações nos índices coincidem com eventos climáticos relevantes.

#### 3.4.6 Detecção de anomalias

A detecção de anomalias será baseada em série temporal. O critério inicial utilizará média móvel e desvio padrão. Um ponto poderá ser marcado como anômalo quando apresentar queda inferior a um limiar definido, como um desvio padrão abaixo da média da janela anterior.

Esse método foi escolhido por ser simples, interpretável e adequado ao escopo de um protótipo. Sua limitação é que ele não identifica a causa da anomalia e pode ser sensível ao tamanho da janela, à quantidade de imagens disponíveis e à presença de ruídos.

#### 3.4.7 Testes e validação

A validação será realizada em três níveis:

1. Testes automatizados: verificar funções de configuração, autenticação, cálculo de índices, estrutura de retorno e tratamento de erros.
2. Testes funcionais: executar o fluxo completo desde a seleção da área até a exibição dos resultados.
3. Validação interpretativa: comparar séries e mapas com faixas esperadas de NDVI e NDWI, observando o comportamento de áreas de soja, milho e pastagem.

O sistema será considerado funcional se conseguir retornar mapas, séries temporais, dados climáticos e alertas sem falhas impeditivas para entradas válidas.

### 3.5 Cenários de validação

Serão utilizados três cenários agrícolas:

| Cenário | Característica esperada |
|---|---|
| Soja | Aumento de NDVI durante o desenvolvimento vegetativo e redução no final do ciclo |
| Milho | Crescimento gradual do NDVI até o pico vegetativo, com posterior queda |
| Pastagem | Valores relativamente estáveis, com variações associadas a clima e manejo |

As áreas deverão ser definidas durante a execução do projeto. Caso não existam dados de campo disponíveis, a validação ficará limitada à coerência dos índices, comparação com literatura e análise visual das séries temporais.

### 3.6 Cronograma

O cronograma considera a execução do trabalho entre julho e dezembro de 2026. Cada mês é dividido em quatro semanas.

| Atividade | Jul | Ago | Set | Out | Nov | Dez |
|---|---|---|---|---|---|---|
| Definição da arquitetura | S1-S4 |  |  |  |  |  |
| Coleta de dados Sentinel-2 | S3-S4 | S1-S4 |  |  |  |  |
| Implementação de NDVI e NDWI |  | S3-S4 | S1-S4 |  |  |  |
| Desenvolvimento da interface |  |  | S3-S4 | S1-S4 | S1-S2 |  |
| Integração de dados climáticos |  |  |  | S3-S4 | S1-S4 |  |
| Testes e validação |  |  |  |  | S3-S4 | S1-S4 |
| Análise e discussão dos resultados |  |  |  | S4 | S1-S4 | S1 |
| Elaboração do texto final |  |  |  | S3-S4 | S1-S4 | S1-S3 |
| Preparação para defesa |  |  |  |  |  | S1-S4 |
| Banca de defesa |  |  |  |  |  | S4 |

### 3.7 Descrição das atividades do cronograma

A definição da arquitetura compreenderá a documentação dos componentes, fluxo de dados, tecnologias e interfaces entre módulos. A coleta de dados envolverá a configuração do Earth Engine, seleção de áreas, consulta às imagens Sentinel-2 e filtragem por data e nuvem.

A implementação dos índices abrangerá a criação das funções de NDVI e NDWI, geração de mapas temáticos e cálculo de estatísticas para séries temporais. O desenvolvimento da interface incluirá controles de entrada, mapa interativo, gráficos e painel de resumo.

A integração climática envolverá a consulta à NASA POWER e a associação dos dados de clima ao período analisado. Os testes e validação verificarão o funcionamento do fluxo completo, a coerência dos valores calculados e a detecção de anomalias. A análise e discussão dos resultados organizará os achados, limitações e interpretações. A elaboração do texto final ocorrerá em paralelo às últimas etapas, com revisão contínua e preparação para a defesa.

### 3.8 Resultados esperados

Espera-se obter um protótipo funcional capaz de:

- consultar imagens Sentinel-2 para uma área e período definidos;
- calcular NDVI e NDWI;
- gerar mapas temáticos dos índices;
- produzir séries temporais;
- consultar dados climáticos;
- indicar possíveis anomalias;
- apresentar resultados em interface web simples;
- demonstrar a viabilidade de uma solução acadêmica baseada em dados gratuitos.

Também se espera produzir documentação técnica e acadêmica suficiente para explicar as decisões de arquitetura, as limitações do protótipo e os caminhos de evolução.

### 3.9 Limitações

O trabalho possui limitações importantes. A resolução espacial do Sentinel-2 permite análise de talhões, mas não de plantas individuais. A presença de nuvens, sombras e falhas de aquisição pode reduzir a quantidade de imagens úteis. Os índices espectrais indicam padrões de vegetação, mas não identificam diretamente pragas, doenças, deficiência nutricional ou causa exata de estresse.

Além disso, a validação poderá ser limitada pela ausência de dados de campo. Nesse caso, a análise será baseada em coerência espectral, comparação com faixas esperadas e relação temporal com dados climáticos. O sistema também não pretende ser produto comercial completo, pois não incluirá autenticação de usuários, banco de dados robusto, aplicativo móvel, integração com sensores de campo ou diagnóstico agronômico automatizado.

### 3.10 Trabalhos futuros

Como evolução, o sistema poderá incluir:

- suporte a novos índices, como NDMI, SAVI e EVI;
- integração com dados de drones ou sensores IoT;
- armazenamento histórico das análises;
- cadastro de usuários e propriedades;
- comparação entre talhões;
- modelos de aprendizado de máquina para classificação de anomalias;
- alertas automáticos;
- validação com dados de campo;
- integração com bases meteorológicas locais, como INMET.

## 4 Referências-base para conversão em BibTeX

As referências abaixo devem ser revisadas e convertidas para `referencias.bib` na etapa LaTeX.

- EUROPEAN SPACE AGENCY; COPERNICUS. Sentinel-2 Mission. SentiWiki. Disponível em: <https://sentiwiki.copernicus.eu/web/s2-mission>. Acesso em: 24 jun. 2026.
- GOOGLE. Harmonized Sentinel-2 MSI: MultiSpectral Instrument, Level-2A (SR). Earth Engine Data Catalog. Disponível em: <https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED>. Acesso em: 24 jun. 2026.
- GOOGLE. ee.Image.normalizedDifference. Google Earth Engine API Reference. Disponível em: <https://developers.google.com/earth-engine/apidocs/ee-image-normalizeddifference>. Acesso em: 24 jun. 2026.
- NASA. NASA POWER Daily API. Disponível em: <https://power.larc.nasa.gov/docs/services/api/temporal/daily/>. Acesso em: 24 jun. 2026.
- GAO, Bo-Cai. NDWI - A normalized difference water index for remote sensing of vegetation liquid water from space. Remote Sensing of Environment, 1996.
- ROUSE, J. W.; HAAS, R. H.; SCHELL, J. A.; DEERING, D. W. Monitoring vegetation systems in the Great Plains with ERTS. Third ERTS Symposium, 1973.
- PATRICIO, Diego Inácio; RIEDER, Rafael. Computer vision and artificial intelligence in precision agriculture for grain crops: a systematic review. Computers and Electronics in Agriculture, 2018.
- WAZLAWICK, Raul Sidnei. Metodologia de Pesquisa para Ciência da Computação. 2. ed. Elsevier, 2014.
- WAZLAWICK, Raul Sidnei. Metodologia de pesquisa para ciência da computação. 2020. Disponível em: <https://integrada.minhabiblioteca.com.br/books/9788595157712>. Acesso em: 31 mar. 2025.
