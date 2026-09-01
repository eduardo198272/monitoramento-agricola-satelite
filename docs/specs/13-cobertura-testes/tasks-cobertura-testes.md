# Tasks: Cobertura Completa e Qualidade dos Testes

Referência: `docs/specs/13-cobertura-testes/spec-cobertura-testes.md`

| ID | Descrição | Critério de Aceitação | Esforço | Status |
|---|---|---|---|---|
| SPEC-13-01 | Gerar baseline de cobertura com linhas e branches por módulo | Relatório inicial registrado, incluindo lacunas de `main.py`, scripts e módulos parcialmente cobertos | 30min | ✅ |
| SPEC-13-02 | Criar fixtures compartilhadas para HTTP, Earth Engine, séries e DataFrames | Fixtures determinísticas e reutilizáveis sem chamadas externas | 1h30 | ✅ |
| SPEC-13-03 | Cobrir branches residuais de `climate.py` | API, coordenadas inválidas, parâmetros customizados, valores `-999`, DataFrame vazio e gráficos parciais cobertos | 45min | ✅ |
| SPEC-13-04 | Completar cobertura de `time_series.py` | Coleção vazia, valores nulos, ordenação, redução e gráficos com dados e sem dados cobertos | 45min | ✅ |
| SPEC-13-05 | Completar cobertura de `maps.py` | Validações de zoom, GeoJSON, índices, palettes, desenho, busca, respostas inválidas e exceções cobertas | 1h | ✅ |
| SPEC-13-06 | Completar cobertura de `pipeline.py` | NDVI, NDWI, NDMI, índice inválido, coleção vazia, falha geral, falha climática e resultados opcionais cobertos | 1h | ✅ |
| SPEC-13-07 | Testar funções de apresentação de `main.py` | `display_map` e `display_summary` cobrem tendências, cores, alertas e ausência de alerta | 1h | ✅ |
| SPEC-13-08 | Testar `run_analysis()` de `main.py` | Sucesso, erro, ausência de imagens, índices, séries, clima, mapas e alertas cobertos | 2h | ⬜ |
| SPEC-13-09 | Testar o fluxo Streamlit com `AppTest` | Estado inicial, pesquisa válida, pesquisa sem resultado, datas inválidas, seleção, análise e rerun cobertos | 2h | ⬜ |
| SPEC-13-10 | Cobrir `validate_apis.py` sem rede | Sucesso, HTTP diferente de 200, JSON incompleto, timeout, conexão, erro genérico, imports e autenticação cobertos | 2h | ⬜ |
| SPEC-13-11 | Cobrir `validate_scenarios.py` sem Earth Engine real | Geometria, três culturas, dados insuficientes, critérios inválidos, exceções e resumo final cobertos | 2h | ⬜ |
| SPEC-13-12 | Cobrir branches residuais identificados pelo relatório | `coverage report -m` não apresenta linhas ou branches pendentes nos módulos de produção | 1h | ⬜ |
| SPEC-13-13 | Executar a suíte completa e corrigir regressões | `py -m pytest` termina com código 0 e cobertura de 100% | 1h | ⬜ |
| SPEC-13-14 | Documentar a estratégia e o procedimento de manutenção | Spec, tasks e instruções de execução estão atualizadas e reproduzíveis | 30min | ⬜ |

## Ordem de Execução

1. SPEC-13-01 e SPEC-13-02 estabelecem a medição e a infraestrutura.
2. SPEC-13-03 a SPEC-13-06 completam os módulos de processamento e integração.
3. SPEC-13-07 a SPEC-13-09 cobrem a interface e o fluxo de aplicação.
4. SPEC-13-10 e SPEC-13-11 cobrem os scripts executáveis incluídos no escopo.
5. SPEC-13-12 e SPEC-13-13 fecham branches residuais e validam a meta de 100%.
6. SPEC-13-14 registra o resultado e o procedimento para novas alterações.

## Estratégia Técnica

- Usar `patch` no ponto de uso, e não no módulo de origem.
- Usar `side_effect` para forçar cada exceção e branch de fallback.
- Usar `pytest.mark.parametrize` para entradas inválidas e índices suportados.
- Criar respostas HTTP mínimas, incluindo status, JSON válido, JSON inválido e payload incompleto.
- Criar objetos Earth Engine mockados com encadeamentos explícitos (`size`, `map`, `median`, `reduceRegion`, `getInfo`).
- Verificar chamadas críticas, como parâmetros de API, `scale`, reducers e nomes de bandas.
- Para Streamlit, usar `AppTest` para widgets e testes unitários com mocks para funções de renderização.
- Testar o retorno de `main()` dos scripts sem executar rede ou autenticação reais.
- Reexecutar cobertura após cada grupo de módulos para localizar branches ainda pendentes.
- Manter a exigência atual de 100% em `pytest.ini`, sem usar `omit` ou `no cover` para esconder código não testado.
