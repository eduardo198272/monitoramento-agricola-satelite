# Correções técnicas — segunda rodada

Base: `b7c325c` com alterações locais preservadas; 15/11/2026. Sem commit, push,
merge ou deploy. A redação anterior foi copiada para
`evidencias/historico_primeira_rodada/`; backup integral anterior em
`/tmp/opencode/tcc03-documentacao-anterior.tar.gz`.

## Reprodução e intervenções

Novos testes executados antes da correção produziram 13 falhas e 2 aprovações
(`/tmp/opencode/tcc03-red.log`), demonstrando divergências de contrato.

| Problema / causa | Correção e arquivos | Evidência posterior |
|---|---|---|
| Radiação MJ assumida como kWh, multiplicação duplicada nos exportadores | `climate.py`: unidade explícita, número finito, coluna normalizada; `export_csv.py`, `export_xlsx.py` reutilizam regra | Histórico 21,64 e 20,99 → média 21,315; resumo/PDF/XLSX/CSV exercitados |
| Legenda fixa, tiles com extremos observados | `map_interaction.py`: transmite `range` da grade | Regressão Python e Node de intervalo negativo; constantes e NoData nos testes de mapas |
| Resumo multiíndice não recuperado pela apresentação | `main.py`: combina metadados compartilhados sem mutar índice | Teste dos cartões/detalhes e chamada climática única |
| Earth Engine exclui último dia, NASA inclui | `earth_engine.py`: dia seguinte como limite exclusivo; NASA `time-standard=UTC` | Dia único e fronteira bissexta; testes existentes ajustados ao novo contrato |
| Datas/índices alterados mantinham saídas antigas | `main.py:invalidate_changed_analysis` limpa todos os produtos | Geometria, datas e conjunto analítico invalidam; troca visual não invalida |
| Retorno individual sem contagem/tendência | `pipeline.py` harmoniza metadados | Teste individual/multi com resumo equivalente |
| Anomalias associadas apenas por data | `time_series.py`, `export_context.py`, exportadores: `observation_id`; legado data+valor | Duas observações no mesmo dia conservam flags distintas |
| Dispositivo sem cursor | HTML: evento click reutiliza lookup | Contrato Node; não equivale a teste em telefone físico |

As fixtures antigas de radiação passaram a declarar sua unidade kWh quando esse
era o cenário testado. Asserções foram atualizadas para o contrato inclusivo e para
a nova coluna de aquisição; nenhum teste foi removido nem a meta reduzida.

## Resultados registrados

- Linha de base reexecutada: 686 aprovados em 11,90 s; 2.669 instruções,
  834 ramificações, 100%.
- Execução final após correções: **710 aprovados em 11,73 s**, 0 falhas, 0 ignorados;
  **2.735 instruções e 856 ramificações**, 0 ausentes/parciais, **100%**.
- Linux x86_64, Python 3.14.4, pytest 9.0.3, pytest-cov 7.1.0, coverage 7.14.0.
- Comando final: `COVERAGE_FILE=/tmp/opencode/tcc03-final COVERAGE_CORE=ctrace <venv>/bin/python -m pytest -q -p no:cacheprovider`.
- Escopo: `src/app`; não inclui JS nem entrada da raiz.
- Node separado: `node --test tests/browser/index_hover.test.cjs`, **3/3 aprovados**,
  0 falhas/ignorados; 62,163332 ms na execução final registrada.
  Saídas completas em `evidencias/pytest_segunda_rodada.txt` e
  `evidencias/node_segunda_rodada.txt`. Execução intermediária anterior:
  mesmos 710 aprovados em 11,84 s, sem alteração posterior da aplicação.

## Limites remanescentes

QA60 foi preservada. Catálogo oficial informa indisponibilidade histórica e não
cobre sombra explicitamente. SCL e probabilidade de nuvens são alternativas para
verificação futura, não correções comprovadas nesta rodada. Persistem dependências
de serviços, cotas, CDN e memória; não há benchmark de produção, teste de carga ou
validação agronômica. O limite de grade e o CRS das reduções ainda exigem estudos
numéricos dedicados. Legado sem ID e com mesma data/valor não distingue aquisições.

## Evidências complementares

`nasa_power_unidades.json` é resposta histórica LST e não deve ser chamada de
nova resposta UTC. `transferencia_controlada.json` contém matrizes sintéticas
determinísticas, não dados de campo. QR decodificado em `qr_verificacao.json`.
Capturas reais e suas etapas efetivamente concluídas constam do inventário visual;
timeout da automação não deve ser convertido em sucesso funcional.

Após corrigir seletores e sincronização da automação, as sessões demo8/demo9
foram concluídas com serviços reais e downloads. Demo9 inclui importação GeoJSON
em nova sessão; artefatos, hashes, parâmetros e versão por hashes de código
estão em `evidencias/demonstracao_real/`. As tentativas anteriores interrompidas
não foram usadas para atribuir sucesso às etapas não executadas.
