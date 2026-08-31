# Baseline de Cobertura de Testes

## Execução

- Data: 2026-08-31
- Comando de medição: `py -m pytest --cov-fail-under=0`
- Relatório detalhado: `py -m coverage report -m`
- Testes coletados: 135
- Testes aprovados: 135
- Cobertura total de linhas: 47%
- Branches: 206 no total, com 23 parcialmente cobertos

O comando oficial `py -m pytest` ainda termina com falha porque `pytest.ini`
exige cobertura mínima de 100%. O baseline abaixo registra o ponto de partida
antes da execução das tarefas SPEC-13-02 em diante.

## Resultado por Módulo

| Módulo | Statements | Não cobertos | Branches | Parcial | Cobertura | Lacunas principais |
|---|---:|---:|---:|---:|---:|---|
| `__init__.py` | 5 | 0 | 0 | 0 | 100% | Nenhuma |
| `anomalies.py` | 42 | 0 | 18 | 0 | 100% | Nenhuma |
| `climate.py` | 46 | 0 | 18 | 1 | 98% | Branch `64->67` |
| `config.py` | 6 | 0 | 0 | 0 | 100% | Nenhuma |
| `earth_engine.py` | 43 | 0 | 8 | 0 | 100% | Nenhuma |
| `ee_auth.py` | 7 | 0 | 2 | 0 | 100% | Nenhuma |
| `main.py` | 159 | 96 | 48 | 9 | 37% | Fluxo Streamlit, apresentação, análise e inicialização |
| `maps.py` | 105 | 9 | 48 | 11 | 87% | Validações, desenho, busca e exceções |
| `pipeline.py` | 36 | 2 | 8 | 2 | 91% | Linhas 36 e 38; branches opcionais |
| `time_series.py` | 32 | 5 | 8 | 0 | 88% | Linhas 15-24; coleção sem dados e redução |
| `utils.py` | 0 | 0 | 0 | 0 | 100% | Nenhuma |
| `validate_apis.py` | 146 | 146 | 26 | 0 | 0% | Script inteiro ainda sem testes |
| `validate_scenarios.py` | 178 | 178 | 22 | 0 | 0% | Script inteiro ainda sem testes |
| **Total** | **805** | **436** | **206** | **23** | **47%** | **Prioridade: `main.py` e scripts de validação** |

## Ordem de Tratamento

1. Criar fixtures compartilhadas para eliminar duplicação e manter os testes isolados.
2. Cobrir branches residuais de `climate.py`, `time_series.py`, `maps.py` e `pipeline.py`.
3. Cobrir as funções de apresentação e o fluxo Streamlit de `main.py`.
4. Cobrir `validate_apis.py` e `validate_scenarios.py` sem rede ou Earth Engine real.
5. Reexecutar `coverage report -m` para fechar os branches restantes.
