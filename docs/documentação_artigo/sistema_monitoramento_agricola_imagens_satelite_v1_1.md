# Sistema de Monitoramento Agrícola por Imagens de Satélite

**Documento Técnico V1.1**

- **Versão:** 1.1
- **Autor:** Eduardo Steffens Hoppen
- **Data:** 10/03/2026
- **Projeto:** MVP de Monitoramento Agrícola com Sensoriamento Remoto

---

## 1 Visão Geral

Este documento descreve a especificação técnica do sistema de monitoramento agrícola baseado em imagens de satélite, desenvolvido como um protótipo funcional (MVP — Minimum Viable Product). O sistema tem como objetivo utilizar dados gratuitos de sensoriamento remoto para analisar a saúde da vegetação em áreas cultivadas, permitindo a visualização de índices espectrais ao longo do tempo e auxiliando na identificação de possíveis anomalias na lavoura.

A solução proposta utiliza imagens de satélite, dados climáticos e técnicas de processamento geoespacial para gerar indicadores que podem ser utilizados por produtores rurais, técnicos agrícolas e pesquisadores como apoio à tomada de decisão. O sistema será desenvolvido com tecnologias acessíveis e de código aberto, permitindo a reprodução dos resultados e a evolução futura do projeto.

O foco desta versão do documento é definir a estrutura inicial do sistema, seus stakeholders, objetivos, escopo, tecnologias e requisitos, servindo como base para o desenvolvimento do MVP e para a elaboração do trabalho acadêmico.

## 2 Objetivo

O objetivo deste trabalho é desenvolver um sistema de monitoramento agrícola baseado em imagens de satélite, capaz de analisar índices de vegetação e umidade para auxiliar na identificação de possíveis anomalias em áreas cultivadas.

A solução proposta utiliza dados gratuitos de sensoriamento remoto e informações climáticas para permitir a visualização dinâmica da saúde da lavoura ao longo do tempo, apoiando produtores rurais, técnicos agrícolas e pesquisadores na tomada de decisão.

O sistema será implementado como um protótipo funcional, permitindo a seleção de áreas no mapa e a geração automática de índices como NDVI e NDWI, demonstrando a viabilidade do uso de tecnologias de geoprocessamento, sensoriamento remoto e ciência de dados no contexto do agronegócio.

Além disso, o projeto busca validar a utilização de ferramentas modernas como Google Earth Engine e Python para o desenvolvimento de aplicações de monitoramento agrícola de baixo custo.

## 3 Stakeholders

Os principais stakeholders do sistema são definidos a seguir.

### 3.1 Produtor Rural

O produtor rural é o principal usuário do sistema. Ele utiliza a solução para acompanhar a saúde da lavoura e identificar possíveis problemas nas áreas cultivadas.

**Expectativas**

- Visualizar a área da propriedade no mapa
- Acompanhar o estado da vegetação
- Identificar regiões com possível problema
- Obter informações de forma simples

**Dores**

- Dependência de vistoria manual
- Falta de ferramentas acessíveis
- Alto custo de soluções comerciais

### 3.2 Técnico Agrícola / Agrônomo

O técnico agrícola ou agrônomo utiliza o sistema para interpretar os dados gerados e apoiar a tomada de decisão em campo.

**Expectativas**

- Visualizar índices espectrais
- Comparar períodos
- Identificar anomalias
- Apoiar diagnóstico

**Dores**

- Falta de integração entre dados
- Dificuldade em analisar imagens manualmente
- Ferramentas complexas ou caras

### 3.3 Gestor da Propriedade

O gestor da propriedade utiliza o sistema para ter uma visão geral da situação da produção.

**Expectativas**

- Resumo da situação da área
- Identificação de problemas
- Apoio para priorização de ações

**Dores**

- Falta de visão consolidada
- Dependência de relatórios manuais

### 3.4 Pesquisador / Desenvolvedor

O pesquisador é responsável por desenvolver e validar o sistema como prova de conceito.

**Expectativas**

- Validar a metodologia
- Demonstrar viabilidade técnica
- Produzir resultados acadêmicos

**Dores**

- Limitação de dados
- Limitação de ferramentas pagas
- Necessidade de reproduzir resultados

## 4 Escopo do MVP

O MVP (Minimum Viable Product) terá como objetivo validar a utilização de imagens de satélite para monitoramento agrícola, implementando apenas as funcionalidades essenciais para demonstrar a viabilidade do sistema.

O sistema deverá permitir:

- Selecionar uma área no mapa
- Consultar imagens de satélite gratuitas
- Calcular índices espectrais
- Visualizar mapas
- Visualizar evolução ao longo do tempo
- Detectar possíveis anomalias
- Consultar dados climáticos básicos

O sistema não terá nesta fase:

- Cadastro de usuários
- Banco de dados complexo
- Integração com máquinas agrícolas
- Diagnóstico agronômico completo
- Aplicação mobile
- Sistema multiusuário

O objetivo desta fase é validar a tecnologia, não criar um produto comercial completo.

## 5 Stack Tecnológica

> Para o desenvolvimento do MVP foi definida uma stack tecnológica baseada em

ferramentas gratuitas, amplamente utilizadas na área de ciência de dados, sensoriamento remoto e desenvolvimento de protótipos.

A escolha das tecnologias prioriza simplicidade, baixo custo e facilidade de reprodução dos resultados.

### 5.1 Linguagem de Programação

A linguagem principal utilizada será Python.

**Motivos da escolha**

- Amplo suporte para ciência de dados
- Bibliotecas para geoprocessamento
- Integração com Google Earth Engine
- Facilidade para criação de protótipos
- Grande comunidade acadêmica

**Bibliotecas previstas**

- ee (Google Earth Engine API)
- geemap
- pandas
- numpy
- plotly
- geopandas
- rasterio (opcional)

### 5.2 Plataforma de Sensoriamento Remoto

Será utilizada a plataforma Google Earth Engine.

O Google Earth Engine é um ambiente de processamento geoespacial em nuvem que permite acessar grandes volumes de imagens de satélite sem necessidade de download local.

**Motivos da escolha**

- Acesso gratuito para pesquisa
- Grande acervo de imagens
- Processamento em nuvem
- API Python
- Muito usado em pesquisas acadêmicas

**Dados utilizados**

- Sentinel-2
- Landsat 8 / 9
- MODIS (opcional)
- Dados climáticos NASA
- Dados climáticos INMET

### 5.3 Interface do Sistema

> Para a interface do MVP será utilizado Streamlit.

Streamlit é um framework Python que permite criar aplicações web simples sem necessidade de desenvolvimento front-end complexo.

**Motivos da escolha**

- Desenvolvimento rápido
- Integração com Python
- Suporte a gráficos
- Suporte a mapas
- Ideal para protótipos

**Funcionalidades previstas**

- Seleção de período
- Seleção de índice
- Visualização de mapa
- Visualização de gráfico
- Exibição de valores médios

### 5.4 Bibliotecas de Mapa

> Para visualização geográfica serão utilizadas as bibliotecas:

- geemap
- folium
- leaflet (via geemap)

**Essas bibliotecas permitem**

- Mostrar mapas
- Desenhar áreas
- Sobrepor imagens
- Exibir camadas

### 5.5 Bibliotecas de Gráfico

> Para visualização temporal serão utilizadas:

- plotly
- matplotlib (opcional)

**Essas bibliotecas permitem**

- Gráfico de série temporal
- Comparação de índices
- Visualização interativa

### 5.6 Dados Climáticos

O sistema poderá utilizar dados climáticos gratuitos para análise complementar.

**Fontes possíveis**

- NASA POWER
- INMET
- NOAA

**Dados utilizados**

- Precipitação
- Temperatura
- Radiação solar

Esses dados serão utilizados para comparação com índices espectrais.

## 6 Arquitetura do Sistema

O sistema será desenvolvido com arquitetura simples, composta por interface, camada de processamento e serviços externos.

**Arquitetura geral**

Usuário → Interface Web → Python → Earth Engine → Dados Satélite → Resultado → Interface

**Descrição do fluxo**

1. O usuário acessa a interface web
2. O usuário seleciona a área de interesse
3. O usuário define o período de análise
4. O sistema consulta o Earth Engine
5. O Earth Engine processa as imagens
6. O sistema calcula os índices
7. O sistema gera mapa
8. O sistema gera gráfico
9. O resultado é exibido na interface

### 6.1 Componentes do Sistema

O sistema será composto pelos seguintes componentes:

**Interface Web**

**Responsável por**

- Entrada de dados
- Exibição de mapas
- Exibição de gráficos

**Tecnologia**

Streamlit

**Camada de Processamento**

**Responsável por**

- Calcular índices
- Consultar Earth Engine
- Processar dados

**Tecnologia**

Python

**Serviço de Imagens**

**Responsável por**

- Fornecer imagens de satélite
- Filtrar nuvens
- Processar bandas

**Tecnologia**

Google Earth Engine

**Serviço Climático**

**Responsável por**

- Fornecer dados de clima

**Fontes**

NASA INMET

## 7 Fluxo de Dados

O fluxo de dados do sistema será o seguinte:

1. Usuário seleciona área
2. Sistema envia coordenadas
3. Sistema consulta Earth Engine
4. Earth Engine retorna imagens
5. Sistema calcula NDVI
6. Sistema calcula NDWI
7. Sistema gera estatísticas
8. Sistema gera mapa
9. Sistema gera gráfico
10. Sistema exibe resultado
**Fluxo simplificado**

Entrada → Processamento → Índices → Análise → Visualização

## 8 Justificativa da Arquitetura

A arquitetura foi escolhida para atender aos seguintes requisitos:

- Baixo custo
- Facilidade de implementação
- Reprodutibilidade acadêmica
- Uso de dados gratuitos
- Execução local
- Simplicidade

A utilização do Google Earth Engine evita a necessidade de armazenamento local de grandes volumes de dados, permitindo que o sistema funcione mesmo em computadores comuns.

O uso de Python e Streamlit permite criar um protótipo funcional com baixo esforço de desenvolvimento, mantendo compatibilidade com bibliotecas científicas.

## 9 Requisitos Funcionais

Os requisitos funcionais descrevem as funcionalidades que o sistema deve possuir para atender aos objetivos definidos.

### RF01 – Selecionar área no mapa

O sistema deve permitir que o usuário selecione uma área geográfica para análise.

A seleção poderá ser feita por:

- desenho no mapa
- escolha de área pré-definida

### RF02 – Definir período de análise

O sistema deve permitir que o usuário selecione um intervalo de datas para análise.

**Exemplos**

- mês
- safra
- intervalo personalizado

### RF03 – Consultar imagens de satélite

O sistema deve consultar imagens de satélite disponíveis para a área e período selecionados.

**Dados utilizados**

- Sentinel-2
- Landsat

### RF04 – Calcular NDVI

O sistema deve calcular o índice NDVI para a área selecionada.

O índice será utilizado para estimar a saúde da vegetação.

### RF05 – Calcular NDWI / NDMI

O sistema deve calcular índices relacionados à umidade da vegetação.

**Objetivo**

- detectar possível estresse hídrico

### RF06 – Exibir mapa com índice

O sistema deve exibir um mapa com cores representando o valor do índice.

**Exemplo**

- verde = saudável
- amarelo = médio
- vermelho = problema

### RF07 – Exibir série temporal

O sistema deve exibir um gráfico mostrando a evolução do índice ao longo do tempo.

### RF08 – Detectar anomalias

O sistema deve indicar quando o valor do índice estiver fora do padrão esperado.

**Critérios possíveis**

- queda brusca
- valor abaixo da média
- desvio estatístico

### RF09 – Consultar dados climáticos

O sistema deve permitir consultar dados climáticos da região.

**Dados possíveis**

- chuva
- temperatura
- radiação

### RF10 – Exibir resumo da análise

O sistema deve mostrar um resumo da situação da área analisada.

**Exemplo**

- índice médio
- tendência
- alerta

## 10 Requisitos Não Funcionais

Os requisitos não funcionais descrevem restrições e características do sistema.

### RNF01 – Uso de dados gratuitos

O sistema deve utilizar apenas dados gratuitos ou de acesso público.

### RNF02 – Execução local

O sistema deve poder ser executado em computador pessoal.

### RNF03 – Interface simples

A interface deve ser simples e fácil de usar.

### RNF04 – Reprodutibilidade

Os resultados devem poder ser reproduzidos.

### RNF05 – Modularidade

O sistema deve permitir futuras melhorias.

### RNF06 – Tempo de resposta aceitável

O sistema deve responder em tempo adequado para uso acadêmico.

### RNF07 – Baixo consumo de recursos

O sistema não deve exigir hardware avançado.

## 11 Casos de Uso

### Caso de Uso 1 — Analisar área

> Ator: Usuário

Fluxo:

## 1 Seleciona área

## 2 Seleciona período

3. Sistema calcula índices
4. Sistema mostra mapa
5. Sistema mostra gráfico

### Caso de Uso 2 — Ver evolução da lavoura

> Ator: Técnico

## 1 Seleciona área

## 2 Escolhe safra

## 3 Visualiza série temporal

## 4 Identifica variações

### Caso de Uso 3 — Detectar problema

> Ator: Produtor

## 1 Seleciona área

## 2 Executa análise

3. Sistema indica alerta
4. Usuário verifica região

### Caso de Uso 4 — Comparar com clima

> Ator: Pesquisador

## 1 Seleciona área

## 2 Consulta índice

## 3 Consulta clima

## 4 Compara dados

## 12 User Stories

Agora no formato ágil.

### US01 — Selecionar área

> Como produtor rural

> Quero selecionar uma área no mapa

> Para analisar a lavoura

### US02 — Escolher período

> Como usuário

> Quero escolher o intervalo de datas

> Para analisar uma safra

### US03 — Visualizar NDVI

> Como técnico agrícola

> Quero visualizar o NDVI

> Para avaliar a vegetação

### US04 — Visualizar NDWI

> Como agrônomo

> Quero visualizar a umidade

> Para detectar estresse hídrico

### US05 — Ver mapa colorido

> Como usuário

> Quero ver o mapa com cores

> Para entender rapidamente

### US06 — Ver gráfico

> Como usuário

> Quero ver o gráfico temporal

> Para analisar evolução

### US07 — Detectar anomalias

> Como gestor

> Quero ver alertas

> Para saber onde investigar

### US08 — Comparar com clima

> Como pesquisador

> Quero ver chuva e índice juntos

> Para entender variações

### US09 — Ver resumo

> Como usuário

> Quero um resumo simples

> Para tomar decisão rápida

### US10 — Repetir análise

> Como pesquisador

> Quero repetir análise

> Para validar resultados

## 13 Fundamentação Técnica

Esta seção apresenta os conceitos técnicos utilizados no desenvolvimento do sistema, incluindo sensoriamento remoto, índices espectrais e uso de imagens de satélite para monitoramento agrícola.

O sistema proposto utiliza dados de satélite para analisar o estado da vegetação em áreas cultivadas, permitindo a identificação de possíveis anomalias ao longo do tempo.

### 13.1 Sensoriamento Remoto

Sensoriamento remoto é a técnica de obtenção de informações sobre a superfície da Terra sem contato direto, utilizando sensores instalados em satélites, aviões ou drones.

No contexto agrícola, o sensoriamento remoto permite:

- monitorar lavouras
- acompanhar crescimento
- detectar estresse hídrico
- identificar áreas com problemas
- analisar grandes áreas rapidamente

Os sensores capturam diferentes comprimentos de onda da luz refletida pela superfície.

A vegetação saudável possui comportamento espectral característico:

- absorve luz vermelha
- reflete infravermelho próximo

Essa diferença permite calcular índices de vegetação.

### 13.2 Satélite Sentinel-2

O sistema utilizará imagens do satélite Sentinel-2.

O Sentinel-2 faz parte do programa europeu Copernicus e fornece imagens gratuitas da superfície terrestre.

**Características**

- Resolução de até 10 metros
- Revisita a cada 5 dias
- Dados gratuitos
- Múltiplas bandas espectrais

**Bandas importantes**

| Banda | Uso |
|---|---|
| Blue | Visual |
| Green | Visual |
| Red | NDVI |
| NIR | NDVI |
| SWIR | Umidade |

O Sentinel-2 é amplamente utilizado em pesquisas agrícolas.

### 13.3 Índices Espectrais

Índices espectrais são cálculos matemáticos feitos a partir das bandas do satélite.

Eles permitem estimar características da vegetação.

Os índices utilizados neste projeto são:

- NDVI
- NDWI
- NDMI (opcional)
- EVI (opcional)

#### 13.3.1 NDVI

O NDVI (Normalized Difference Vegetation Index) é o índice mais utilizado para análise da vegetação.

Fórmula:

`NDVI = (NIR − RED) / (NIR + RED)`

**Interpretação**

Valor Significado

< 0.2 pouca vegetação

0. 2 – 0.5        vegetação média
0. 6 – 0.8        vegetação saudável
O NDVI permite identificar:

- crescimento da lavoura
- falhas
- estresse
- áreas degradadas

#### 13.3.2 NDWI / NDMI

O NDWI e NDMI são índices relacionados à umidade.

São utilizados para detectar:

- estresse hídrico
- falta de água
- seca

Fórmula genérica:

`NDWI = (NIR − SWIR) / (NIR + SWIR)`

Valores baixos podem indicar falta de água.

#### 13.3.3 Uso dos índices no sistema

O sistema utilizará os índices para:

- gerar mapas coloridos
- gerar gráficos
- detectar anomalias
- comparar períodos

Os índices não substituem análise agronômica, mas são úteis como indicador.

### 13.4 Google Earth Engine

O Google Earth Engine é uma plataforma de processamento geoespacial em nuvem.

Ele permite acessar grandes volumes de dados sem necessidade de download.

**Funcionalidades**

- acesso a imagens de satélite
- cálculo de índices
- filtragem por data
- filtragem por nuvem
- análise temporal

**Motivos da escolha**

- gratuito para pesquisa
- rápido
- confiável
- amplamente usado na academia

O sistema utilizará a API Python do Earth Engine.

### 13.5 Uso de Dados Climáticos

O sistema poderá utilizar dados climáticos para complementar a análise.

**Fontes**

- NASA POWER
- INMET
- NOAA

**Dados utilizados**

- precipitação
- temperatura
- radiação solar

Esses dados ajudam a interpretar variações no NDVI.

**Exemplo**

queda do NDVI + falta de chuva → possível estresse hídrico

## 14 Limitações do Sistema

O sistema proposto possui algumas limitações.

- Não detecta pragas diretamente
- Não substitui inspeção em campo
- Dependência de imagens sem nuvem
- Resolução limitada do satélite
- Não considera todos fatores agronômicos

O objetivo é fornecer apoio à decisão, não diagnóstico definitivo.

## 15 Trabalhos Futuros

O sistema pode ser expandido em versões futuras.

**Possíveis melhorias**

- Detecção automática com Machine Learning
- Integração com drones
- Integração com sensores IoT
- Cadastro de usuários
- Banco de dados
- Aplicação mobile
- Suporte a múltiplas áreas
- Alertas automáticos
- Análise por talhão
- Integração com máquinas agrícolas

## 16 Conclusão

O presente documento técnico definiu a estrutura inicial do sistema de monitoramento agrícola baseado em imagens de satélite, estabelecendo os objetivos, stakeholders, escopo do MVP, tecnologias utilizadas, arquitetura proposta e requisitos funcionais e não funcionais. A solução foi concebida com foco na utilização de dados gratuitos de sensoriamento remoto e ferramentas acessíveis, demonstrando a viabilidade do desenvolvimento de uma aplicação capaz de analisar a saúde da vegetação por meio de índices espectrais como NDVI e NDWI. A definição detalhada das user stories, dos casos de uso e da fundamentação técnica fornece uma base sólida para a implementação do protótipo, permitindo que o projeto evolua de forma organizada nas próximas etapas. Espera-se que o sistema desenvolvido contribua para demonstrar o potencial do uso de sensoriamento remoto e ciência de dados no contexto do agronegócio, servindo como apoio à tomada de decisão e como base para futuras melhorias, incluindo o uso de técnicas mais avançadas de análise, integração com dados de campo e expansão para aplicações em larga escala.
