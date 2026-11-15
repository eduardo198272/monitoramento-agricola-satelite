# Sistema de Monitoramento Agrícola por Imagens de Satélite

Projeto de TCC em Ciência da Computação para apoiar o monitoramento agrícola
com imagens Sentinel-2, índices de vegetação e umidade, dados climáticos e
detecção de possíveis anomalias. Os resultados não substituem avaliação
agronômica em campo.

## Funcionalidades e tecnologias

- Interface Python/Streamlit com seleção de área e mapas interativos.
- Google Earth Engine para imagens Sentinel-2 e índices NDVI, NDWI e NDMI.
- Séries temporais, tendências, alertas e dados climáticos da NASA POWER.
- Exportação de resultados em PDF, XLSX e CSV; localizações em GeoJSON.
- Localizações salvas em SQLite no modo local ou isoladas por sessão no ponto
  de entrada web.

## Instalação e execução

Na raiz do repositório, crie um ambiente virtual e instale as dependências:

```sh
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Os exemplos usam Linux/macOS; no Windows, use `.venv\Scripts\python`.
Para acessar dados do Earth Engine é necessário um projeto habilitado e
credenciais válidas. Para o ponto de entrada web, configure os Secrets conforme
o [guia de deploy](docs/deploy-streamlit.md) e execute:

```sh
.venv/bin/python -m streamlit run streamlit_app.py
```

Esse comando usa localizações temporárias por sessão e autenticação não
interativa. Para executar o modo local com SQLite e autenticação interativa,
configure `EE_PROJECT_ID` no ambiente ou em `.env` e execute:

```sh
.venv/bin/python -m streamlit run src/app/main.py
```

Não versione credenciais, `.env`, Secrets ou bancos locais. Veja o
[guia de deploy](docs/deploy-streamlit.md) para detalhes, limitações e
transferência de localizações entre sessões.

## Testes

```sh
COVERAGE_CORE=ctrace .venv/bin/python -m pytest -q
```

`pytest.ini` exige 100% de cobertura de linhas e ramificações para `src/app`.
Os testes automatizados não substituem validação com serviços reais ou
validação agronômica.

## Documentação

- [Índice de especificações](docs/specs/index.md)
- [Preparação e deploy no Streamlit Cloud](docs/deploy-streamlit.md)
- [Registro de verificação de software](docs/validation/streamlit-cloud-readiness.md)
- [Cenários de validação](docs/validation/scenarios.md)
- [Relatório final do TCC e compilação](docs/artigo_final/README.md)
- [Fluxo de desenvolvimento](docs/development-workflow.md)

O projeto e o relatório acadêmico permanecem em desenvolvimento. Registros de
validação datados descrevem a revisão e as condições informadas em cada documento.
