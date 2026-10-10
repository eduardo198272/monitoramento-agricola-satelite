# SPEC-15-02 — Tiles Esri no mapa de seleção

## Objetivo

Configurar explicitamente Esri World Imagery como camada-base do mapa de seleção
Folium, sem depender do tile layer padrão do Folium.

## Contrato

- Usar o serviço `https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}`.
- Definir atribuição visível: `Tiles © Esri — Source: Esri, Maxar, Earthstar Geographics, and the GIS User Community`.
- Nomear a camada `Satélite (Esri)` e configurá-la como base (`overlay=False`) com controle habilitado.
- Incluir controle de camadas para expor o seletor da camada-base no mapa.
- Manter escala, zoom, controles de desenho/edição/remoção e GeoJSON selecionado.
- Não acessar a rede nos testes automatizados; testar somente a configuração Folium.

## Aceite

1. `create_selection_map` inclui uma `TileLayer` com URL, atribuição e configuração acima.
2. O controle de escala continua disponível e o controle de camadas lista a camada.
3. Os controles existentes de desenho e a geometria selecionada continuam presentes.
4. Os testes passam sem depender da disponibilidade do endpoint Esri.

## Fora de escopo

Base satélite do mapa temático, fallback visual/estado de erro de tiles e validação
de disponibilidade do serviço em navegador são tratados em outras tarefas.
