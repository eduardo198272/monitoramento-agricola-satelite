# Relatório de Andamento do Trabalho de Conclusão de Curso

**Aluno:** Eduardo Steffens Hoppen — 198272
**Curso:** Bacharelado em Ciência da Computação
**Instituição:** Universidade de Passo Fundo
**Orientador:** Prof. Carlos Amaral Holbig
**Data:** 03 de setembro de 2026

## 1. Objetivo do trabalho

O trabalho tem como objetivo desenvolver um sistema de baixo custo para auxiliar o monitoramento agrícola por meio de imagens de satélite, índices espectrais, dados climáticos e detecção de possíveis anomalias na vegetação. A proposta é oferecer uma aplicação acadêmica reproduzível, capaz de apoiar a análise de áreas cultivadas sem substituir a avaliação agronômica em campo.

O sistema está sendo desenvolvido em Python, com interface em Streamlit, processamento geoespacial no Google Earth Engine, mapas interativos com geemap/Folium, gráficos com Plotly e dados meteorológicos obtidos pela API NASA POWER.

## 2. Status atual

O projeto encontra-se em **fase avançada de implementação do MVP (Produto Mínimo Viável)**. A arquitetura foi definida e os principais módulos do sistema já estão implementados: autenticação e acesso ao Earth Engine, consulta de imagens Sentinel-2, filtragem por área, período e cobertura de nuvens, cálculo de índices, mapas, séries temporais, detecção de anomalias, integração climática e interface web.

Também foi concluída uma etapa significativa de qualidade de software. O baseline inicial, registrado em 31/08/2026, possuía 135 testes aprovados e 47% de cobertura de linhas. Após a ampliação da suíte, o registro de 03/09/2026 informa 245 testes aprovados, 100% de cobertura de linhas e nenhum branch parcialmente coberto nos módulos de produção.

## 3. Funcionamento do sistema

O fluxo principal de utilização ocorre da seguinte forma:

1. O usuário pesquisa uma localidade ou navega até a região de interesse.
2. Desenha um polígono no mapa para delimitar a área agrícola.
3. Define as datas inicial e final da análise.
4. Seleciona o índice espectral desejado: NDVI, NDWI ou NDMI.
5. O sistema consulta a coleção Sentinel-2 no Google Earth Engine e aplica filtros de localização, período e nuvens.
6. As imagens válidas são mascaradas e processadas para gerar o índice selecionado.
7. São calculados o mapa temático, o valor médio do índice e a área da região em hectares.
8. O sistema produz uma série temporal, estima a tendência da vegetação e identifica possíveis anomalias.
9. Como complemento, consulta a NASA POWER para obter precipitação, temperatura e radiação solar no período analisado.
10. Os resultados são apresentados em mapa interativo, gráficos e painel-resumo, incluindo alertas quando são identificadas alterações relevantes.

O NDVI é utilizado como indicador do vigor da vegetação, enquanto o NDWI e o NDMI complementam a análise relacionada à umidade. A interpretação conjunta com os dados climáticos permite contextualizar variações observadas nas séries temporais.

## 4. Etapas do cronograma

| Etapa | Situação | Resultado principal |
|---|---|---|
| Definição da arquitetura e requisitos | Concluída | Estrutura modular, stack tecnológica e fluxo definidos |
| Integração com Google Earth Engine | Implementada | Consulta Sentinel-2, filtros e autenticação estruturados |
| Implementação dos índices | Implementada | NDVI, NDWI e NDMI disponíveis no processamento |
| Mapas e seleção de área | Implementada | Mapa interativo, desenho de polígono e legenda |
| Interface Streamlit | Implementada | Controles, análise e apresentação dos resultados |
| Séries temporais e anomalias | Implementada | Evolução temporal, tendência e alertas |
| Integração climática | Implementada | NASA POWER, limpeza dos dados e gráficos climáticos |
| Testes automatizados | Concluída | 245 testes aprovados e 100% de cobertura registrada |
| Validação experimental e análise dos resultados | Em andamento | Consolidar execuções reais e interpretação por cultura |
| Redação final e preparação da defesa | Pendente | Elaborar capítulos, revisar texto e preparar apresentação |

## 5. Próximos passos

As próximas atividades serão concentradas na execução e documentação da validação experimental com cenários de soja, milho e pastagem. Serão analisados os valores e as tendências dos índices, comparando-os com faixas esperadas e com dados climáticos do mesmo período. Em seguida, os resultados serão organizados em tabelas, gráficos e discussões para compor o texto do TCC.

Também serão finalizados os capítulos de arquitetura, implementação, resultados, limitações e conclusão. Por fim, será realizada a revisão geral da documentação, a preparação dos slides e os ensaios para a defesa.

## 6. Consideração final

O desenvolvimento técnico encontra-se bem encaminhado, com o MVP estruturado e os componentes principais integrados. A principal etapa restante é transformar a implementação e os testes automatizados em resultados experimentais documentados, consolidando a análise científica e a redação final do trabalho.
