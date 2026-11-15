# Publicação no Streamlit Community Cloud

## Comportamento de armazenamento

- O ponto de entrada web é `streamlit_app.py`, na raiz.
- Na web, as localizações ficam **somente na sessão de cada visitante**, sem
  SQLite, banco externo ou autenticação de usuários.
- Use a barra lateral **Importar / exportar localizações** para transferir
  localizações entre sessões. Exporte antes de sair ou recarregar a página.
- O navegador não salva automaticamente os arquivos: é necessário clicar em
  **Preparar GeoJSON para download** e **Baixar minhas localizações**.
- Os arquivos contêm nomes e coordenadas: compartilhe-os somente com quem pode
  acessar essas informações. O site não oferece um cofre permanente de dados.
- O comando local anterior, `python -m streamlit run src/app/main.py`, mantém
  SQLite por padrão. A execução do ponto de entrada web usa sessões, inclusive
  localmente, para permitir testar o comportamento da hospedagem.

## GeoJSON aceito

Uma `FeatureCollection`, ou uma única `Feature`, com geometrias `Polygon` WGS84
e nome em `properties.name`. Limites: 2 MB e 100 localizações por arquivo.
Nomes são comparados sem diferenciar caixa e normalizando espaços.
Se houver geometria inválida ou nome repetido (no arquivo ou no armazenamento),
**nenhuma localização do arquivo é importada**; registros existentes não são
sobrescritos. IDs e datas internas são gerados novamente ao importar.

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {"name": "Minha área"},
      "geometry": {
        "type": "Polygon",
        "coordinates": [[[-45, -20], [-44, -20], [-44, -19], [-45, -20]]]
      }
    }
  ]
}
```

## 1. Preparar o Google Cloud / Earth Engine

1. Use um projeto registrado para acesso ao Earth Engine, com a Earth Engine API
   habilitada e elegibilidade de uso não comercial/comercial adequada.
2. Crie uma conta de serviço para a aplicação no projeto.
3. Conceda somente as permissões necessárias. Verifique os papéis
   **Earth Engine Resource Viewer** (`roles/earthengine.viewer`) e
   **Service Usage Consumer** (`roles/serviceusage.serviceUsageConsumer`)
   conforme a configuração do projeto. Não conceda Owner/Editor por conveniência.
4. Se a organização permitir chaves, gere uma chave JSON dessa conta.
   Guarde-a fora do repositório; não a envie em chats ou capturas de tela.
   Se a política proibir chaves, será necessário escolher uma hospedagem com
   credenciais gerenciadas (ADC) ou outro mecanismo compatível.
5. Use as chaves somente no painel Secrets do Streamlit. Em caso de exposição,
   revogue a chave no Google Cloud e gere outra.

Referência: <https://developers.google.com/earth-engine/guides/service_account>

## 2. Validar localmente

Use o ambiente virtual e as dependências de `requirements.txt`.
Para testar a autenticação de nuvem, crie `.streamlit/secrets.toml` a partir de
`.streamlit/secrets.example.toml` e substitua os placeholders privadamente.
O arquivo `secrets.toml` e chaves `.json` nesse diretório são ignorados pelo Git.
Cole o JSON completo gerado pelo Google, mantendo o `\n` da chave privada dentro
do bloco TOML com aspas simples triplas.

```bash
.venv/bin/python -m streamlit run streamlit_app.py
```

Sem Secrets, o ponto de entrada web **não abre autenticação interativa**.
A interface informa indisponibilidade do Earth Engine.

```bash
.venv/bin/python -m pytest -q
```

No Python 3.14, se o mecanismo SysMonitor do coverage acusar um caminho de
`finally` não coberto apesar dos testes de erro de conexão, compare com o tracer
C, sem reduzir a meta nem excluir código:

```bash
COVERAGE_CORE=ctrace .venv/bin/python -m pytest -q
```

As dependências também podem ser verificadas sem alterar o ambiente instalado:

```bash
.venv/bin/python -m pip install --dry-run --ignore-installed --only-binary=:all: --python-version 3.12 -r requirements.txt
```

Esse comando verifica resolução e disponibilidade de wheels, não substitui a
instalação e execução reais no Python 3.12 do Cloud.

## 3. Publicar primeiro em homologação

Em <https://share.streamlit.io>, conecte a conta GitHub e selecione **Create app**:

| Campo | Homologação | Produção |
|---|---|---|
| Repository | `eduardo198272/monitoramento-agricola-satelite` | mesmo |
| Branch | `hml` | `main` |
| Main file path | `streamlit_app.py` | mesmo |
| Python | 3.12, após validar instalação limpa | mesma versão validada |

Em **Advanced settings → Secrets**, use o formato do arquivo de exemplo:

```toml
EE_PROJECT_ID = "seu-projeto"
EE_SERVICE_ACCOUNT_JSON = '''
COLE AQUI O JSON COMPLETO DA CONTA DE SERVIÇO
'''
```

O exemplo acima é um molde, não credenciais funcionais. Não publique `.env`,
`secrets.toml`, chaves JSON, tokens ou bancos locais.

O Community Cloud instala `requirements.txt` da raiz. As versões fixadas devem
ser verificadas em ambiente limpo com o Python escolhido antes da promoção.
O arquivo inclui ferramentas de desenvolvimento; uma redução futura deve
preservar dependências transitivas necessárias ao geemap.

## 4. Checklist antes de produção

- Instalação das dependências e inicialização sem prompt interativo.
- Seleção de uma área, NDVI/NDWI/NDMI e dados climáticos reais.
- Exportações PDF, XLSX e CSV, inclusive o indicador de geração do PDF.
- Salvar uma localização, baixar GeoJSON e importar em nova sessão.
- Abrir dois navegadores/sessões: as localizações de um não aparecem no outro.
- Importar arquivo inválido ou duplicado: erro sem importação parcial.
- Conferir limites de recursos e cotas do Earth Engine; visitantes compartilham
  a conta de serviço e seu consumo, embora não compartilhem localizações.

Somente após validar homologação, promover `dev → hml → main` com revisão,
preservando o histórico. Cada app acompanha sua branch; pushes podem atualizar
automaticamente o site. A promoção Git, sozinha, não cria um site no Streamlit.

Referência: <https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy>
