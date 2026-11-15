# Sistema de Monitoramento Agrícola por Imagens de Satélite

Projeto de TCC do curso de Ciência da Computação.

O relatório final utiliza o modelo institucional `CC-EC_TF-TC`. O arquivo
principal e as instruções de compilação estão em [docs/artigo_final](docs/artigo_final/README.md).

## Aplicação

A aplicação integra imagens Sentinel-2 no Google Earth Engine, índices NDVI,
NDWI e NDMI, séries temporais, sinalizações de anomalias e contexto climático
da NASA POWER. Os resultados podem ser exportados em PDF, XLSX e CSV ZIP.
Os indicadores apoiam análise exploratória, não diagnóstico agronômico.

Tecnologias utilizadas:

- Python
- Streamlit
- Google Earth Engine
- NASA POWER, Folium, Plotly, Pandas e NumPy
- SQLite no uso local; memória por sessão e transferência GeoJSON na versão web

## Execução

Após instalar `requirements.txt` em um ambiente virtual:

```sh
# Aplicação local, com SQLite e autenticação local do Earth Engine:
.venv/bin/python -m streamlit run src/app/main.py

# Comportamento da versão web: sessões isoladas e conta de serviço:
.venv/bin/python -m streamlit run streamlit_app.py
```

A autenticação exige projeto habilitado e registrado no Earth Engine.
Consulte [o guia de deploy](docs/deploy-streamlit.md) para configurar Secrets.
Nunca versione `.env`, `secrets.toml` ou chaves JSON reais.

Na versão web, exporte as localizações em GeoJSON antes de sair ou recarregar
a página e importe o arquivo quando voltar. Não há banco externo, recuperação
automática entre sessões ou login de usuários.

## Verificação e estado

```sh
COVERAGE_CORE=ctrace .venv/bin/python -m pytest -q
```

Na revisão de 15/11/2026, a suíte passou com 677 testes e 100% de cobertura
de linhas e ramificações em `src/app`. O tracer C evita uma divergência observada
no SysMonitor do Python 3.14, sem reduzir a meta de cobertura.
Veja [o registro e os limites da verificação](docs/validation/streamlit-cloud-readiness.md).

O código está preparado para publicação no Streamlit Community Cloud, mas a
publicação do site ainda não foi verificada. A avaliação agronômica, os estudos
de caso e partes acadêmicas do relatório continuam pendentes.
