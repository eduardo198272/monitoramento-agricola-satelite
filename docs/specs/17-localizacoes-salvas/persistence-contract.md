# Contrato de Persistência: Localizações Salvas

Este documento fecha as decisões da SPEC-17-01 para o repositório SQLite. A
implementação começa na SPEC-17-02; carregar a configuração não cria diretórios
nem abre o banco.

## Caminho e ciclo de vida

- `SAVED_LOCATIONS_DB_PATH` aceita um caminho de arquivo SQLite configurável.
- Sem configuração, o caminho é
  `<diretório-de-dados-do-usuário>/monitoramento-agricola-satelite/saved_locations.sqlite3`:
  `%LOCALAPPDATA%` no Windows, `$XDG_DATA_HOME` quando definido em outros
  sistemas, ou `~/.local/share` como fallback.
- A resolução é pura e não cria o diretório nem o arquivo. A inicialização do
  repositório deverá criar o diretório-pai e aplicar permissões restritas quando
  suportadas pelo sistema operacional.
- O banco é local à instalação/instância da aplicação e compartilhado pelos
  usuários dessa instância. Não há isolamento por usuário nesta versão.
- Testes e ferramentas devem injetar caminho para banco temporário; nunca usar o
  banco padrão de desenvolvimento/produção.

## Esquema inicial

Tabela `saved_locations`:

| Coluna | Tipo SQLite | Regra |
|---|---|---|
| `id` | `TEXT` | chave primária, UUID em string |
| `name` | `TEXT` | nome de exibição após trim; obrigatório, até 100 caracteres |
| `normalized_name` | `TEXT` | chave obrigatória e única para comparação sem distinção de caixa e com espaços consecutivos colapsados |
| `geojson_json` | `TEXT` | GeoJSON JSON UTF-8, sem simplificação ou perda de coordenadas |
| `center_lat` | `REAL` | latitude do centro de enquadramento calculado a partir da geometria validada |
| `center_lon` | `REAL` | longitude correspondente |
| `created_at` | `TEXT` | timestamp UTC ISO 8601, imutável após criação |
| `updated_at` | `TEXT` | timestamp UTC ISO 8601, atualizado em alteração futura |

`normalized_name` deve ser protegido por restrição `UNIQUE` no banco, além da
validação de domínio, para impedir duplicatas mesmo em chamadas concorrentes.
O valor normalizado é de comparação e não substitui `name` na apresentação.
GeoJSON é a única geometria persistida: nunca serializar `ee.Geometry`, credenciais
ou resultados de análise. A criação do esquema deve ser idempotente e versionada
por `PRAGMA user_version`; a versão inicial é `1`.

## Contrato de domínio e repositório

- `save_location(name, geojson) -> dict`: valida e normaliza os dados, persiste e
  retorna `id`, `name`, `geojson`, `center`, `created_at` e `updated_at`.
- `list_saved_locations() -> list[dict]`: retorna resumos sem GeoJSON, ordenados
  por `normalized_name` e, como desempate defensivo, por `id`; cada item contém
  `id`, `name`, `center`, `created_at` e `updated_at`.
- `get_saved_location(location_id) -> dict | None`: retorna registro completo;
  identificador inexistente resulta em `None`.
- `delete_saved_location(location_id) -> bool`: retorna `True` se removeu um
  registro e `False` se o identificador não existia.
- Duplicidade após normalização gera erro de domínio tratável pela interface.
  Erros SQLite/I/O devem ser convertidos em erro de armazenamento tratável, sem
  expor detalhes internos ao usuário.
- O repositório encapsula conexões/transações e recebe ou resolve o caminho
  configurado; a UI não acessa SQLite diretamente.
- `st.session_state` pode manter a seleção/restauração corrente para a sessão,
  mas nunca é fonte primária nem cópia persistente da lista de localizações.

## Compatibilidade e testes

O contrato mantém as assinaturas e campos públicos previstos em
`spec-localizacoes-salvas.md`. Testes de repositório devem usar banco temporário,
abrir novas conexões para provar persistência e verificar inicialização repetida.
Não são necessárias credenciais Earth Engine, requests externos ou dados de
usuário para testar persistência.
