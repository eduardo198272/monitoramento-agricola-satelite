# SPEC-15-03 — Base satélite no mapa temático

## Objetivo

Configurar Esri World Imagery como base do mapa temático, mantendo a camada do
índice translúcida, a legenda (colorbar) e o polígono da área selecionada.

## Contrato

- Usar o basemap `Esri.WorldImagery` do geemap em `create_base_map`.
- Preservar zoom, centro, camada de índice com `opacity=0.7` (padrão), legenda
  `add_colorbar` e polígono GeoJSON quando fornecido.
- O controle de camadas deve listar a base e o resultado temático.
- Não acessar a rede nos testes automatizados; validar apenas a configuração
  do objeto geemap.

## Aceite

1. `create_base_map` instancia `geemap.Map` com `basemap="Esri.WorldImagery"`.
2. `create_thematic_map` continua retornando mapa com índice, legenda e polígono.
3. Os testes passam sem depender da disponibilidade do endpoint Esri/Earth Engine.
4. Visualmente, em navegador, a base satélite é reconhecível sob o índice, a
   legenda é visível e o polígono permanece.

## Fora de escopo

Fallback visual/estado de erro de tiles, validação de disponibilidade do serviço
em navegador e alteração de `opacity` ou paletas são tratados em outras tarefas.