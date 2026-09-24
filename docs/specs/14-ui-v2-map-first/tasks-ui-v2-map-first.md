# Tasks: UI V2 — Interface Map-First

Referência: `docs/specs/14-ui-v2-map-first/spec-ui-v2-map-first.md`

| ID | Descrição | Critério de Aceitação | Esforço | Status |
|---|---|---|---|---|
| SPEC-14-01 | Registrar baseline da UI e contratos atuais | Conflitos entre UI atual, specs antigas e UI V2 documentados sem alterar o comportamento ainda | 30min | Concluído |
| SPEC-14-02 | Definir modelo de estado da UI V2 | Estado inicial, seleção, análise, erro e rerun usam chaves previsíveis e uma fonte de verdade | 1h | Concluído |
| SPEC-14-03 | Criar CSS centralizado e tokens visuais | Cores, espaçamentos, inputs, botões, cards e responsividade ficam em um ponto central | 1h | Concluído |
| SPEC-14-04 | Implementar header e estrutura map-first | Header compacto, subtítulo, status do serviço e mapa rapidamente visível aparecem sem sidebar obrigatória | 45min | Não iniciado |
| SPEC-14-05 | Integrar busca à workspace geográfica | Busca válida atualiza centro e zoom, não cria área e preserva seleção existente | 45min | Não iniciado |
| SPEC-14-06 | Melhorar validação do GeoJSON | Polígono aberto, degenerado, inválido ou sem área são rejeitados com mensagem orientativa | 1h | Não iniciado |
| SPEC-14-07 | Persistir, calcular e limpar a área | Geometria, GeoJSON e hectares permanecem em reruns e são limpos juntos | 1h | Não iniciado |
| SPEC-14-08 | Adicionar indicação de desenho da área | O mapa mantém o controle nativo e exibe uma instrução curta sem botão falso | 30min | Não iniciado |
| SPEC-14-09 | Implementar barra compacta de período | Datas ficam integradas à área principal, com defaults e validação de intervalo | 45min | Não iniciado |
| SPEC-14-10 | Implementar seletor horizontal de índices | `Todos`, `NDVI`, `NDWI` e `NDMI` aparecem sem dropdown principal | 45min | Não iniciado |
| SPEC-14-11 | Normalizar datas para serviços externos | Strings e `datetime.date` são aceitos pelo pipeline e NASA POWER | 30min | Não iniciado |
| SPEC-14-12 | Corrigir bandas necessárias ao NDMI | A coleção seleciona todas as bandas da fórmula adotada e o contrato é testado | 45min | Não iniciado |
| SPEC-14-13 | Consolidar `run_analysis` no pipeline | A UI não mantém cópia duplicada do processamento existente | 1h | Não iniciado |
| SPEC-14-14 | Implementar `run_multi_analysis` | Um fluxo calcula os índices selecionados e compartilha coleção, máscara, área, imagens e clima | 2h30 | Não iniciado |
| SPEC-14-15 | Integrar botão `Analisar área` | Botão fica desabilitado sem área ou com datas inválidas e dispara o pipeline correto | 1h | Não iniciado |
| SPEC-14-16 | Persistir resultados por índice | Resultados de cada índice ficam organizados em estado sem sobrescrever uns aos outros | 1h | Não iniciado |
| SPEC-14-17 | Implementar mapa temático por índice | O mapa usa o índice visível, mantém área e legenda e troca camada sem nova análise completa | 1h30 | Não iniciado |
| SPEC-14-18 | Implementar visão geral multiíndice | Cards exibem métricas reais, tendências disponíveis e quantidade real de imagens | 1h30 | Não iniciado |
| SPEC-14-19 | Organizar séries, anomalias e clima | Conteúdo aparece abaixo do mapa, na mesma página e sem duplicar alertas | 1h | Não iniciado |
| SPEC-14-20 | Implementar estados de processamento e erro | Loading, ausência de imagens, erro de geocodificação e erro Earth Engine têm mensagens distintas | 1h | Não iniciado |
| SPEC-14-21 | Adicionar logging técnico | Falhas são registradas sem expor stack trace cru ao usuário | 30min | Não iniciado |
| SPEC-14-22 | Atualizar testes de backend e mapas | NDMI, bandas, datas, multiíndice, área, limpeza e reutilização de chamadas são cobertos | 2h30 | Não iniciado |
| SPEC-14-23 | Atualizar testes Streamlit com `AppTest` | Layout, estado inicial, busca, área, controles, análise, rerun e troca visual são cobertos | 2h30 | Não iniciado |
| SPEC-14-24 | Executar cobertura e corrigir regressões | `py -m pytest` passa e a exigência de cobertura configurada permanece atendida | 1h30 | Não iniciado |
| SPEC-14-25 | Validar responsividade e integração visual | Desktop e larguras menores não apresentam overflow e o mapa permanece utilizável | 45min | Não iniciado |
| SPEC-14-26 | Revisar diff e documentar limitações | Não há lógica duplicada, chamadas desnecessárias ou funcionalidades existentes removidas | 45min | Não iniciado |

## Ordem de Execução

1. SPEC-14-01 a SPEC-14-03 estabelecem contratos, estado e estilo.
2. SPEC-14-05 a SPEC-14-11 implementam localização e controles da workspace.
3. SPEC-14-12 a SPEC-14-14 corrigem backend e consolidam o pipeline.
4. SPEC-14-15 a SPEC-14-21 integram análise, mapas, resultados e estados.
5. SPEC-14-22 e SPEC-14-23 atualizam a cobertura de backend e UI.
6. SPEC-14-24 a SPEC-14-26 fecham validação, regressões e documentação.

## Estratégia Técnica

- Ler a spec correspondente antes de implementar cada task.
- Manter processamento científico em `earth_engine.py`, `pipeline.py`,
  `time_series.py`, `anomalies.py` e `climate.py`.
- Usar mocks no ponto de uso para Earth Engine, Nominatim e NASA POWER.
- Usar `AppTest` apenas para contratos de interação e renderização estáveis.
- Criar helpers puros para normalização de índice, datas e mensagens quando isso
  reduzir a complexidade dos testes.
- Verificar contagem de chamadas para garantir reutilização da coleção e máscara.
- Atualizar testes junto com cada alteração funcional, não somente ao final.
- Executar `py -m pytest` antes da integração final.
- Executar `py -m coverage report -m` para localizar branches pendentes.
- Não usar dados fictícios na aplicação de produção para preencher métricas.
