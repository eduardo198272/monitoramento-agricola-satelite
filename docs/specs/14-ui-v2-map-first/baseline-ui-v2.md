# Baseline Técnico da UI V2

## Objetivo

Registrar o comportamento atual da interface antes da implementação da UI V2
Map-First. Este documento separa contratos que devem ser preservados, comportamentos
que serão substituídos e pontos que exigem validação durante a migração.

Este baseline foi levantado a partir de `src/app/main.py`, `src/app/pipeline.py`,
`src/app/maps.py`, dos testes existentes e das specs históricas do projeto.

## Fluxo Atual

O ponto de entrada é `main()` em `src/app/main.py`, executado por:

```bash
streamlit run src/app/main.py
```

O fluxo atual é:

1. Configurar a página Streamlit em layout amplo.
2. Exibir o título da aplicação.
3. Inicializar o Google Earth Engine via `init_earth_engine()`.
4. Inicializar chaves de `st.session_state` relacionadas ao mapa, análise e busca.
5. Exibir busca, período, índice e botão de análise dentro da sidebar.
6. Consultar o Nominatim quando o usuário pesquisa uma localidade.
7. Criar o mapa Folium de seleção com `create_selection_map()`.
8. Capturar `last_active_drawing` com `st_folium()`.
9. Converter o GeoJSON para `ee.Geometry`.
10. Executar `main.run_analysis()` quando o usuário solicita a análise.
11. Criar o mapa geemap com a camada temática e a legenda.
12. Exibir resumo, série temporal, clima e alerta abaixo do mapa.

## Estado Atual

| Chave | Responsabilidade atual | Estado V2 relacionado | Observação |
|---|---|---|---|
| `map_obj` | Mapa temático geemap renderizado após análise | `analysis_results` / mapa visível | Mistura objeto de apresentação com estado da análise |
| `analysis_result` | Último resultado de índice único | `analysis_results` | Sobrescreve o resultado anterior |
| `error` | Última mensagem de erro da análise | `analysis_error` | Não diferencia origem do erro |
| `drawn_geometry` | Geometria Earth Engine selecionada | `aoi_geometry` | Valor derivado do GeoJSON |
| `drawn_geojson` | GeoJSON do último desenho | `aoi_geojson` | Fonte que deve ser preservada na V2 |
| `location_center` | Centro atual do mapa de seleção | `location_center` | Contrato a preservar |
| `location_zoom` | Zoom atual do mapa de seleção | `location_zoom` | Contrato a preservar |
| `location_result` | Resultado da última busca | `location_result` | Deve sobreviver à troca de índice e análise |
| `location_query` | Texto do campo de busca | `location_query` | Chave nativa do widget Streamlit |

O estado atual não possui uma chave explícita para área em hectares, índice
visível, modo de análise, status de processamento ou resultados separados por
índice.

## Contratos Atuais

### Entrada da aplicação

```python
def main() -> None
```

O Earth Engine é inicializado antes da área de análise ficar disponível. Se a
inicialização falhar, a aplicação exibe erro e encerra o fluxo de renderização.

### Pipeline de índice único

Há duas implementações de `run_analysis()`:

- `src/app/main.py:run_analysis()` é usada pela UI atual;
- `src/app/pipeline.py:run_analysis()` contém uma implementação equivalente.

Ambas recebem geometria, datas e nome do índice. O pipeline atual suporta
`NDVI`, `NDWI` e `NDMI`, consulta a coleção Sentinel-2, aplica máscara de
nuvens, calcula a mediana, média espacial, área, série temporal, anomalias,

O contrato de sucesso observado é semelhante a:

```python
{
    "success": True,
    "index_name": "NDVI",  # presente na implementação de main.py
    "index_map": ee.Image,
    "time_series": list[dict],
    "time_series_plot": go.Figure | None,
    "anomalies": list[dict],
    "alert": str | None,
    "climate_data": pd.DataFrame | None,
    "climate_plot": go.Figure | None,
    "mean_value": float | None,
    "area_ha": float,
}
```

O contrato de falha observado é:

```python
{
    "success": False,
    "error": str,
}
```

A implementação em `main.py` e a implementação em `pipeline.py` divergem em
detalhes de retorno, tratamento de falha climática e contexto de importação.
A consolidação em `pipeline.py` é responsabilidade da `SPEC-14-13`.

### Busca de localidade

```python
def search_location(query: str) -> dict | None
def calculate_map_zoom(boundingbox: list[str]) -> int
```

`search_location()` normaliza espaços, ignora consulta vazia, consulta o
Nominatim com timeout de 10 segundos e retorna `None` para falha de rede,
resposta vazia ou formato inválido. Em caso de sucesso, retorna:

```python
{
    "display_name": str,
    "latitude": float,
    "longitude": float,
    "boundingbox": list[str],
}
```

`calculate_map_zoom()` valida quatro limites numéricos, calcula o zoom a partir
da extensão do bounding box e limita o resultado ao intervalo de 1 a 20.

### Seleção da área

```python
def create_selection_map(
    center: list | None = None,
    zoom: int = DEFAULT_ZOOM,
    geojson: dict | None = None,
) -> folium.Map

def geojson_to_ee_geometry(geojson: dict) -> ee.Geometry
```

O mapa Folium disponibiliza somente o desenho de polígono, com edição e remoção.
O conversor atual valida o tipo `Polygon`, a existência de coordenadas e um
anel com pelo menos quatro posições, mas ainda não valida explicitamente:

- fechamento do anel;
- três vértices distintos;
- área geográfica maior que zero;
- múltiplos anéis ou geometrias inválidas além do formato básico.

Essas lacunas serão tratadas na `SPEC-14-06`.

### Mapa temático

```python
def create_base_map(
    center: list | None = None,
    zoom: int = DEFAULT_ZOOM,
) -> geemap.Map

def add_index_layer(
    map_obj: geemap.Map,
    index_image: ee.Image,
    index_name: str,
    palette: list | None = None,
    opacity: float = 0.7,
) -> geemap.Map
```

Folium continua sendo o mapa de seleção e geemap continua sendo o mapa de
visualização temática. A V2 deve preservar essa separação, conforme a decisão
arquitetural registrada em `architecture-decisions.md`.

## Matriz de Baseline

| Área | Comportamento atual | Contrato preservado? | Mudança V2 | Task responsável |
|---|---|---:|---|---|
| Layout | Controles principais na sidebar | Não | Workspace map-first sem sidebar necessária | SPEC-14-04 |
| Cabeçalho | Título longo, sem subtítulo operacional | Não | Header compacto com status do serviço | SPEC-14-04 |
| Busca | Sidebar, Nominatim, atualiza centro e zoom | Sim | Mover para acima do mapa | SPEC-14-05 |
| Seleção | Polígono capturado via Folium e `st_folium` | Sim | Manter controle nativo e instrução visível | SPEC-14-08 |
| Validação da área | Validação estrutural parcial do GeoJSON | Parcial | Validar anel, vértices e área | SPEC-14-06 |
| Persistência da área | `drawn_geojson` e `drawn_geometry` | Parcial | GeoJSON como fonte única e derivados sincronizados | SPEC-14-07 |
| Cálculo da área | `geometry.area().divide(10000)` no pipeline | Sim | Expor área persistida no estado da UI | SPEC-14-07 |
| Período | Dois `date_input` na sidebar | Parcial | Barra compacta na área principal | SPEC-14-09 |
| Índices | `selectbox` com NDVI, NDWI e NDMI | Parcial | Seletor horizontal com `Todos` | SPEC-14-10 |
| Datas | UI envia `date`; funções aceitam principalmente strings | Parcial | Normalizar no limite do pipeline | SPEC-14-11 |
| NDMI | Fórmula usa `B8A/B11`, coleção não seleciona `B8A` | Não | Confirmar bandas e testar contrato | SPEC-14-12 |
| Pipeline | `run_analysis` duplicado em `main.py` e `pipeline.py` | Não | Usar `pipeline.py` como fonte única | SPEC-14-13 |
| Multiíndice | Não existe | Não | Adicionar `run_multi_analysis` | SPEC-14-14 |
| Resultado | Apenas um resultado em `analysis_result` | Parcial | Resultados organizados por índice | SPEC-14-16 |
| Mapa pós-análise | Novo mapa geemap é criado após cada análise | Parcial | Trocar índice visível sem novo processamento remoto | SPEC-14-17 |
| Métricas | Resumo de um índice por vez | Parcial | Visão geral multiíndice com dados reais | SPEC-14-18 |
| Clima e séries | Renderizados abaixo do mapa após sucesso | Sim | Reorganizar na mesma página | SPEC-14-19 |
| Erros | Mensagem única em `st.session_state.error` | Não | Status e mensagens por categoria | SPEC-14-20/21 |
| Testes de UI | AppTest verifica sidebar e fluxo atual | Não | Atualizar contratos para map-first | SPEC-14-23 |

## Conflitos com Specs Históricas

| Spec histórica | Regra histórica | Regra V2 | Decisão |
|---|---|---|---|
| `05-streamlit/spec-controles.md` | Controles dentro da sidebar | Controles na workspace principal | V2 substitui a regra visual; contratos de validação permanecem |
| `05-streamlit/spec-app.md` | Área principal recebe mapa e gráficos após controles laterais | Mapa é o centro do fluxo e resultados permanecem na mesma tela | Preservar como histórico do MVP |
| `05-streamlit/spec-mapa-ui.md` | Mapa exibido com fluxo baseado na interface antiga | Folium e geemap ocupam estados diferentes da workspace | Preservar integrações, alterar composição |
| `10-mapas-interacao/spec-mapa-interacao.md` | Seleção, persistência e limpeza da área | Mesmos invariantes, com estado explícito e validação completa | Reutilizar regras de negócio |
| `12-interface-resultados/` | Resultados organizados para uma análise | Resultados separados por índice e visão `Todos` | Evoluir apresentação sem remover métricas existentes |
| `03-indices/spec-ndmi.md` | NDMI usa B8A/B11 | Mesma fórmula até validação científica | Corrigir somente bandas, não alterar fórmula sem decisão |

## Testes Afetados

| Arquivo | Cobertura atual | Impacto esperado |
|---|---|---|
| `tests/test_streamlit_app.py` | Título, sidebar, datas, selectbox, busca e fluxo AppTest | Atualizar expectativas de layout, controles e estado V2 na SPEC-14-23 |
| `tests/test_main.py` | Testa `src.app.main.run_analysis` com mocks locais | Migrar para pipeline centralizado na SPEC-14-22/23 |
| `tests/test_pipeline.py` | Testa `src.app.pipeline.run_analysis` | Expandir para datas normalizadas e multiíndice na SPEC-14-22 |
| `tests/test_maps.py` | Busca, zoom, mapas e conversão GeoJSON | Adicionar casos de anel inválido, área nula e persistência na SPEC-14-22 |
| `tests/test_earth_engine.py` | Bandas, filtros e fórmulas isoladas | Cobrir banda B8A e contrato NDMI na SPEC-14-22 |
| `tests/conftest.py` | Fixtures determinísticas para serviços e séries | Reutilizar para evitar rede e autenticação reais |

Nesta task, os testes são apenas inventariados. Nenhum teste deve ser alterado
antes da task específica correspondente.

## Riscos e Restrições

- `AppTest` precisa isolar `init_earth_engine`, Folium e integrações externas.
- Earth Engine, Nominatim e NASA POWER não devem ser chamados por testes
  unitários ou de contrato.
- O mapa de seleção e o mapa temático usam bibliotecas diferentes e não devem
  ser substituídos simultaneamente sem necessidade.
- `main.py` atualmente contém regra de processamento duplicada; remover a cópia
  sem preservar o contrato pode quebrar testes existentes.
- Datas da UI são objetos `datetime.date`, enquanto Earth Engine e NASA POWER
  possuem contratos baseados em strings ISO.
- A coleção atual não seleciona `B8A`, embora `calculate_ndmi()` dependa dela.
- A alteração de layout deve atualizar testes que procuram widgets na sidebar,
  sem eliminar a validação dos mesmos comportamentos.
- Alterações locais preexistentes fora desta pasta não fazem parte desta task e
  não devem ser incluídas na implementação da UI V2.

## Escopo da SPEC-14-01

Incluído:

- documentação do fluxo, estado e contratos atuais;
- comparação entre implementação duplicada do pipeline;
- matriz de mudanças e vínculo com as próximas tasks;
- inventário de specs históricas e testes afetados;
- registro de riscos técnicos.

Não incluído:

- alteração em `src/app/`;
- alteração em `tests/`;
- criação do estado V2;
- criação de CSS;
- correção de bandas ou fórmulas;
- implementação de `run_multi_analysis()`;
- mudança do layout Streamlit.

## Critérios de Conclusão

- O comportamento atual da UI está descrito de ponta a ponta.
- As chaves atuais de estado e seus equivalentes V2 estão relacionados.
- Os contratos públicos de UI, mapas, busca e pipeline estão registrados.
- As duplicações e divergências entre os dois `run_analysis()` estão explícitas.
- Cada conflito relevante possui uma task responsável.
- Os testes afetados estão identificados sem alteração nesta etapa.
- Nenhum código executável foi modificado para produzir este baseline.
