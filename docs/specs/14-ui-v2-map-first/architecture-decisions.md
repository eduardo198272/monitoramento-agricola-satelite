# Decisões de Arquitetura — UI V2 Map-First

## Decisão 1: criar uma nova versão de interface

As specs anteriores descrevem a interface inicial baseada em sidebar. A UI V2
será documentada em uma nova pasta para preservar o histórico do MVP e evitar
alterar retroativamente critérios já implementados.

## Decisão 2: manter a separação entre UI e processamento

- `main.py` controla Streamlit, interação, estado e apresentação.
- `pipeline.py` controla processamento de índices, séries, anomalias e clima.
- `earth_engine.py` controla coleção, bandas, filtros e fórmulas.
- `maps.py` controla mapas, geocodificação e conversões de geometria.
- `styles.py` ou `assets/style.css` controla o estilo visual.

Nenhuma regra científica será duplicada em `main.py`.

## Decisão 3: consolidar o pipeline

`main.py` possui uma implementação duplicada de `run_analysis()`. A UI V2 deve
usar a implementação de `pipeline.py` como fonte única. O contrato de índice
único deve ser preservado e um contrato multiíndice deve ser adicionado para a
opção `Todos`.

## Decisão 4: reutilizar uma coleção por execução

O fluxo multiíndice buscará e filtrará a coleção Sentinel-2 uma vez, aplicará a
máscara de nuvens uma vez e derivará os índices a partir da coleção mascarada.
Os resultados serão armazenados por nome de índice para permitir troca visual
sem nova consulta remota.

## Decisão 5: compatibilidade entre Folium e geemap

O mapa Folium existente continuará responsável pela seleção do polígono. O
mapa geemap continuará responsável pela camada temática e legenda. Eles ocuparão
o mesmo espaço visual da workspace em estados diferentes, pois a substituição
das duas integrações aumentaria o risco de regressão.

## Decisão 6: área como estado derivado da geometria

O GeoJSON é a representação persistida da seleção no mapa. A geometria Earth
Engine e a área em hectares são valores derivados e devem ser atualizados ou
limpos junto com o GeoJSON.

## Decisão 7: correção do NDMI

A implementação atual usa `B8A` e `B11`, mas a coleção não seleciona `B8A`.
Antes da implementação, a combinação de bandas deve ser confirmada na
documentação do projeto. A solução adotada deve selecionar todas as bandas
necessárias e possuir teste explícito do contrato.

## Decisão 8: tratamento de erros

Detalhes técnicos serão enviados ao logger. A UI exibirá mensagens orientativas,
sem stack trace. Mensagens de ausência de imagens, geocodificação e Earth Engine
terão caminhos distintos.

## Decisão 9: CSS centralizado

O estilo será carregado por um único ponto da aplicação. Não serão adicionados
blocos independentes de CSS espalhados pelas funções de renderização.

## Decisão 10: compatibilidade com testes

Alterações na UI devem preservar contratos públicos quando não houver motivo
concreto para quebrá-los. Testes de `AppTest` serão atualizados para refletir a
UI V2, enquanto testes de backend continuarão isolados de rede, autenticação e
Earth Engine real.
