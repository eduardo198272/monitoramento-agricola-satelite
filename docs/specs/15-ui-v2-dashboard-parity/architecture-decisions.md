# Decisões de Arquitetura — Paridade Visual do Dashboard

## Decisão 1: manter Folium e geemap

O mapa de seleção permanece em Folium/`streamlit_folium`; a visualização do
índice permanece em geemap. Ambos recebem configuração explícita de camada-base
de satélite. A troca das bibliotecas não faz parte desta tarefa.

## Decisão 2: usar Esri World Imagery como camada-base inicial

A referência indica `Satellite (Esri)`. O mapa de seleção e o temático devem
configurar explicitamente o serviço World Imagery e sua atribuição, em vez de
depender do provedor padrão do Folium/geemap. A integração deve manter o mapa
utilizável quando os tiles externos não responderem.

## Decisão 3: separar camada-base e camada temática

No mapa temático, a imagem de satélite é contexto/base e o raster de NDVI, NDWI
ou NDMI é uma sobreposição com opacidade que permita ver ambas as informações.
O GeoJSON da área e a legenda permanecem camadas independentes.

## Decisão 4: calcular resumos na fronteira de apresentação/dados existente

Resumo de precipitação, temperatura e radiação deve ser calculado a partir do
`climate_data` que o pipeline já retorna. Preferir helper puro testável, sem
nova chamada de rede e sem colocar regra de agregação espalhada no layout
Streamlit. O contrato do pipeline só deve ser estendido se faltar dado realmente
necessário para o resumo.

## Decisão 5: dados ausentes não são substituídos por valores de demonstração

Cada card exibe valores reais, estado vazio ou `Indisponível`. Valores do
baseline visual são exclusivamente ilustrativos e não podem ser copiados para a
aplicação como métricas fixas.

## Decisão 6: imagem original versionada é pré-requisito da comparação visual

A imagem deve ser armazenada em
`assets/dashboard-reference.png` e ligada a partir da spec. Como o anexo da
conversa não está exposto como arquivo local ao ambiente de edição, deve ser
fornecido no workspace antes da implementação e revisão de paridade. Não criar
substituto artificial.
