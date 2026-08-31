# Spec: Cobertura Completa e Qualidade dos Testes

## Propósito

Definir a estratégia para elevar a cobertura de testes automatizados do código em
`src/app` para 100% de linhas e branches, mantendo os testes determinísticos,
isolados de serviços externos e capazes de detectar regressões funcionais.

Esta especificação cobre tanto os módulos de processamento quanto a interface
Streamlit e os scripts executáveis de validação incluídos no escopo de
`--cov=src/app`.

## Interface

O trabalho não cria uma API de produção. Ele define contratos de teste para as
interfaces públicas existentes:

| Componente | Interfaces a cobrir |
|---|---|
| `earth_engine.py` | `filter_by_date`, `filter_by_area`, `get_image_collection`, `mask_clouds`, `calculate_ndvi`, `calculate_ndwi`, `calculate_ndmi` |
| `maps.py` | `search_location`, `calculate_map_zoom`, `create_base_map`, `add_index_layer`, `add_colorbar`, `create_selection_map`, `geojson_to_ee_geometry`, `enable_area_draw`, `get_drawn_geometry` |
| `time_series.py` | `compute_time_series`, `plot_time_series` |
| `anomalies.py` | `detect_anomalies`, `generate_alert`, `compute_trend` |
| `climate.py` | `fetch_climate_data`, `plot_climate_data` |
| `pipeline.py` | `run_analysis` |
| `main.py` | `init_earth_engine`, `display_map`, `display_summary`, `run_analysis`, `main` |
| `validate_apis.py` | `print_header`, `print_result`, validadores individuais e `main` |
| `validate_scenarios.py` | `print_header`, `print_result`, `create_test_geometry`, validadores de soja, milho, pastagem e `main` |

### Recursos de teste

- `pytest` para execução e parametrização;
- `pytest-cov` para cobertura de linhas e branches;
- `unittest.mock` para HTTP, Earth Engine, autenticação, Streamlit e funções internas;
- `streamlit.testing.v1.AppTest` para testes de widgets e renderização da aplicação;
- fixtures e factories compartilhadas em `tests/conftest.py`.

### Comando oficial

```bash
py -m pytest
```

O comando deve respeitar a configuração existente em `pytest.ini`, incluindo
`--cov-branch` e `--cov-fail-under=100`.

## Regras de Negócio

- A cobertura mínima de linhas deve ser 100%.
- A cobertura mínima de branches deve ser 100%.
- Todo ramo condicional relevante deve possuir pelo menos um teste explícito.
- Testes não podem depender de rede, credenciais, projeto Earth Engine ou estado externo.
- Chamadas a Nominatim e NASA POWER devem ser substituídas por respostas mockadas.
- Chamadas ao Earth Engine devem usar objetos mockados e verificar argumentos importantes.
- Falhas esperadas devem ser testadas com `pytest.raises` ou com validação do retorno definido pela interface.
- Os testes devem validar valores, mensagens, efeitos e chamadas relevantes, e não somente ausência de exceções.
- Os scripts `validate_apis.py` e `validate_scenarios.py` permanecem no escopo de cobertura e devem ser testados sem executar serviços reais.
- Testes de Streamlit devem cobrir estados inicial, sucesso, validação, erro, alertas e reruns.
- A execução repetida da suíte deve produzir o mesmo resultado.
- O aumento de cobertura não deve alterar o comportamento funcional da aplicação.
- Qualquer refatoração para testabilidade deve preservar interfaces públicas e comportamento observável.

## Critérios de Aceitação

1. Dado o repositório com as dependências instaladas, quando `py -m pytest` for executado, então todos os testes passam.
2. Dado o relatório de cobertura, quando a suíte terminar, então a cobertura total de linhas é 100%.
3. Dado o relatório com `--cov-branch`, quando a suíte terminar, então todos os branches são cobertos.
4. Dado qualquer chamada HTTP de produção, quando um teste for executado, então a chamada real não é realizada.
5. Dado qualquer chamada Earth Engine, quando um teste for executado, então autenticação e processamento remoto não são necessários.
6. Dado `main.py`, quando o fluxo de UI for testado, então os caminhos de inicialização, pesquisa, seleção, análise, gráficos, alertas e erros são exercitados.
7. Dado `run_analysis`, quando cada índice suportado for selecionado, então os ramos NDVI, NDWI e NDMI são executados.
8. Dado uma coleção vazia, dados ausentes ou falha intermediária, quando o componente for testado, então o comportamento de fallback especificado é verificado.
9. Dado um erro de cada tipo nos scripts de validação, quando o validador for executado, então o retorno booleano e a mensagem correspondente são verificados.
10. Dado o relatório final, quando `term-missing` for analisado, então não existem linhas ou branches pendentes em `src/app`.
11. Dada uma segunda execução imediata, quando a suíte for executada novamente, então o resultado e a cobertura permanecem estáveis.
12. Dado o código de produção, quando a implementação dos testes for concluída, então não há exclusões de módulos para mascarar a cobertura.

## Exemplos de Uso

### Execução completa

```bash
py -m pytest
```

### Execução de um módulo durante o desenvolvimento

```bash
py -m pytest tests/test_pipeline.py --cov=src/app/pipeline.py --cov-branch
```

### Verificação de branches pendentes

```bash
py -m coverage report -m
```

### Mock de serviço externo

```python
@patch("src.app.climate.requests.get")
def test_api_error(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout()
    ...
```

## Tasks Relacionadas

- SPEC-13-01 a SPEC-13-14 — `tasks-cobertura-testes.md`

## Dependências

- `01-visao-geral/spec-visao-geral.md` — convenções de TDD e modularidade;
- `05-streamlit/spec-app.md` — comportamento da aplicação;
- `09-mvp/spec-fluxo-completo.md` — contrato do pipeline;
- `10-mapas-interacao/spec-mapa-interacao.md` — pesquisa e mapa interativo;
- `11-unidades-area/spec-unidades-area.md` — apresentação e conversão de área;
- `12-interface-resultados/spec-interface-resultados.md` — layout, mensagens e alertas;
- `pytest.ini` — configuração oficial de cobertura.
