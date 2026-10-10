# Revisão Final da UI V2 — SPEC-14-26

## Escopo e Resultado

Revisão da UI Map-First contra `docs/specs/14-ui-v2-map-first/baseline-ui-v2.md`
e `spec-ui-v2-map-first.md`, cobrindo estado, seleção de área, fluxo de análise,
mapas, métricas, séries temporais, clima, erros e responsividade.

Não foram identificadas funcionalidades de negócio removidas. As alterações de
layout substituem intencionalmente a sidebar do baseline; os contratos de busca,
desenho/remoção da área, índices, período, resultados, clima e série temporal
permanecem cobertos pelos testes de mapas, pipeline e `AppTest`.

## Correções de Chamadas Redundantes

- A UI já calcula e persiste a área em hectares ao selecionar o polígono. Agora
  repassa esse valor ao pipeline. Chamadas diretas ao pipeline continuam
  compatíveis: quando `area_ha` não é informado, o pipeline calcula a área como
  antes.
- Os pipelines já consultam a contagem de imagens. Essa contagem agora é
  reutilizada por `compute_time_series` em todos os índices, evitando novas
  consultas de tamanho da coleção. A função ainda calcula a contagem quando
  chamada isoladamente sem esse argumento.
- O centroide necessário à chamada da NASA POWER agora também fornece o centro do
  mapa temático. A interface deixa de repetir a consulta Earth Engine do
  centroide. Se a API climática falhar depois da obtenção do centroide, o mapa
  ainda usa esse centro e a análise espectral permanece disponível.
- Single-index e multi-index mantêm seus contratos e compartilham as mesmas
  etapas gerais necessárias, com resultados distintos por contrato; nenhuma
  refatoração ampla do processamento foi introduzida.

## Limitações Técnicas Conhecidas

- Análises requerem credenciais/projeto configurados e disponibilidade do Google
  Earth Engine; busca e clima dependem, respectivamente, do Nominatim e da NASA
  POWER.
- Dados climáticos são consultados como ponto no centroide da área, não como
  média espacial do talhão. Falha da consulta climática deixa os dados/clima
  indisponíveis sem invalidar os índices.
- A série temporal ainda busca os detalhes de cada observação com chamadas
  Earth Engine individuais. Períodos com muitas imagens podem aumentar a
  latência; avaliar futuramente uma recuperação em lote, respeitando limites de
  tamanho de resposta.
- Quantidade e qualidade das imagens Sentinel-2 dependem da cobertura disponível
  e da máscara de nuvens. Índices e alertas de anomalia indicam variação
  espectral; não constituem diagnóstico agronômico.
- A suíte automatizada substitui serviços externos por mocks. A confirmação de
  integração com credenciais e serviços reais requer execução de validação
  operacional configurada.

## Verificação

- `py -m pytest`: 309 testes aprovados.
- Cobertura de linhas e branches: 100% (`py -m coverage report -m`).
- `git diff --check`: sem erros.
