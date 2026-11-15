# Verificação de software e preparação do Streamlit Cloud

## Reexecução da suíte em 15/11/2026

Na revisão de software `4b3cd2c`, em Linux com Python 3.14.4, o comando
`COVERAGE_CORE=ctrace .venv/bin/python -m pytest -q` resultou em **686 testes
aprovados** e **100% de cobertura de linhas e ramificações em `src/app`**.
A medição não inclui `streamlit_app.py` na cobertura. Esta reexecução não
incluiu novas verificações de serviços reais ou do deploy. O registro abaixo
continua descrevendo a revisão anterior e suas condições.

## Identificação e escopo

- Data de referência: 15/11/2026 (UTC).
- Revisão do software: `a9a96775277cea91a297a2db8c3982bc080a7236`.
- Linux x86_64; Python 3.14.4.
- pytest 9.0.3; pytest-cov 7.1.0; coverage 7.14.0.
- Streamlit 1.55.0; earthengine-api 1.7.17; pandas 2.3.3; NumPy 2.4.3.
- As alterações do artigo que acompanham este registro não modificam o software.

Este registro distingue testes locais com dependências simuladas, verificação
mínima de serviço real e preparação de deploy. Não representa avaliação
agronômica, estudo de usabilidade ou validação do site publicado.

## Suíte automatizada

Comando executado na raiz do projeto, com as dependências da `.venv`:

```sh
COVERAGE_CORE=ctrace .venv/bin/python -m pytest -q
```

Resultado: **677 testes aprovados**, sem falhas, com **100% de cobertura de linhas
e ramificações em `src/app`**. O ponto de entrada `streamlit_app.py` é testado,
mas não faz parte do diretório incluído na medição.

O tracer C foi selecionado explicitamente: o SysMonitor no Python 3.14 havia
acusado um caminho de saída de `finally` não coberto, embora testes de erro
de conexão o exercitassem. A execução com tracer C atingiu a meta sem excluir
código ou reduzir o requisito de 100%.

Os testes dos serviços geoespaciais e climáticos usam substitutos controlados,
conforme `tests/conftest.py` e os patches de cada teste; não fazem medições
agronômicas reais. Testes do Streamlit também podem substituir a inicialização
do Earth Engine e os provedores de dados.

### Localizações e interface

`tests/test_locations_transfer.py` verifica:

- exportação/importação com preservação de nomes e polígonos;
- SQLite local e repositório de sessão;
- nomes duplicados, geometria inválida e limites de arquivo;
- rollback de todo o lote em conflitos, sem sobrescrever localizações;
- cópias independentes e separação entre estados de sessão;
- limite da sessão para manter todo o conjunto exportável;
- mensagens de erro e download da interface.

`tests/test_cloud_entrypoint.py` verifica o ponto de entrada web e utiliza
`streamlit.testing.v1.AppTest` com widgets reais para conferir download em uma
sessão e ausência das localizações em outra. Nesse teste, a fronteira de
inicialização remota do Earth Engine é substituída. Isso não simula toda a
infraestrutura do Community Cloud ou toda a interação de um navegador.

## Verificação mínima com Earth Engine real

A inicialização com conta de serviço foi seguida por:

```python
ee.Number(1).add(1).getInfo()
# Resultado observado: 2

ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED").limit(1).size().getInfo()
# Resultado observado: 1
```

As credenciais foram carregadas de `.streamlit/secrets.toml` e o projeto foi
conferido com `.env`. Ambos estão ignorados pelo Git. A chave privada, e-mail da
conta de serviço, tokens e identificadores privados não integram este registro.
O projeto foi configurado para uso não comercial pelo responsável; este teste
não audita faturamento ou elegibilidade.

Para reproduzir o teste sem exibir os Secrets, em ambiente local autorizado:

```sh
.venv/bin/python - <<'PY'
import os
from pathlib import Path
import toml

settings = toml.loads(Path(".streamlit/secrets.toml").read_text(encoding="utf-8"))
for key in ("EE_PROJECT_ID", "EE_SERVICE_ACCOUNT_JSON"):
    os.environ[key] = settings[key]
os.environ["EE_AUTH_MODE"] = "service_account"
try:
    import ee
    from src.app.ee_auth import initialize_earth_engine
    initialize_earth_engine(project_id=settings["EE_PROJECT_ID"])
    ee.data.setDeadline(30000)
    assert ee.Number(1).add(1).getInfo() == 2
    assert ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED").limit(1).size().getInfo() == 1
except Exception as error:
    print("Falha no teste remoto:", type(error).__name__)
    raise SystemExit(1) from None
print("Inicialização, cálculo simples e catálogo: OK")
PY
```

A consulta não seleciona área agrícola ou cultura, não processa bandas
espectrais, não avalia máscaras e não verifica NASA POWER, mapas ou exportação
com serviços reais. Portanto, não comprova execução completa do pipeline,
exatidão de NDVI/NDWI/NDMI ou interpretação agronômica.

## Dependências e publicação

Foi executada a resolução para Python 3.12:

```sh
.venv/bin/python -m pip install --dry-run --ignore-installed --only-binary=:all: --python-version 3.12 -r requirements.txt
```

O comando encontrou as dependências e wheels compatíveis solicitados. Trata-se
de resolução, **não de instalação ou execução reais no Python 3.12**.

O código oferece `streamlit_app.py`, configuração de servidor, modelo de Secrets
sem credenciais reais e [guia de deploy](../deploy-streamlit.md). Nesse ponto de
entrada, localizações usam memória por sessão e transferência GeoJSON, sem
banco externo ou login Google de visitantes; SQLite permanece no comando local.

Na data desta revisão, a publicação e a instalação no Community Cloud não foram
verificadas. O Git contém a implementação; a promoção `dev → hml → main` não
cria, por si só, a aplicação hospedada.

## Pendências de avaliação

- Instalação e execução em homologação e produção no Streamlit Cloud.
- Fluxos reais com geometrias, datas e culturas confirmadas.
- Cálculo independente dos índices, máscaras, escala e tratamento de pixels.
- Conferência das unidades e integração real da NASA POWER.
- Geração de mapas e arquivos com serviços reais, incluindo falhas e latência.
- Avaliação de campo, comparação de sistemas e usabilidade, caso façam parte do
  escopo acadêmico aprovado; nenhuma delas é inferida da cobertura.
