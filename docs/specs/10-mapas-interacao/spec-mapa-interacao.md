# Spec: Pesquisa, Centralização e Bloqueio do Mapa

## Propósito

Permitir que o usuário pesquise uma localidade, navegue automaticamente até ela e selecione a área de interesse desenhando um polígono. Após a seleção, o mapa deve enquadrar a área e bloquear a navegação manual até que o polígono seja removido.

A seleção de área será feita exclusivamente pelo mapa interativo. Áreas pré-definidas não fazem parte desta funcionalidade.

## Interface

```python
def search_location(query: str) -> dict | None
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `query` | `str` | Nome de cidade, município, endereço ou localidade |

**Retorno**: dicionário com `display_name`, `latitude`, `longitude` e `boundingbox`, ou `None` quando nenhuma localidade for encontrada.

```python
def create_selection_map(
    center: list[float],
    zoom: int,
    geojson: dict | None = None,
    locked: bool = False,
) -> folium.Map
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `center` | `list[float]` | Centro no formato `[latitude, longitude]` |
| `zoom` | `int` | Nível de zoom entre 1 e 20 |
| `geojson` | `dict | None` | Polígono anteriormente selecionado |
| `locked` | `bool` | Define se a navegação deve estar bloqueada |

**Retorno**: mapa Folium configurado para seleção de polígono.

```python
def geojson_to_ee_geometry(geojson: dict) -> ee.Geometry
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `geojson` | `dict` | Feature ou Geometry GeoJSON retornado pelo mapa |

**Retorno**: `ee.Geometry.Polygon` válida.

```python
def calculate_map_zoom(boundingbox: list[str]) -> int
```

**Retorno**: nível de zoom calculado a partir dos limites da localidade, limitado ao intervalo de 1 a 20.

## Regras de Negócio

- A pesquisa deve usar um serviço de geocodificação configurável; a implementação padrão será Nominatim/OpenStreetMap.
- Toda requisição deve informar um `User-Agent` identificando a aplicação e respeitar as políticas do serviço utilizado.
- A pesquisa deve ignorar consultas vazias ou compostas apenas por espaços.
- Quando houver múltiplos resultados, deve ser utilizado o primeiro resultado relevante e exibido o nome retornado ao usuário.
- A pesquisa deve atualizar o centro e o zoom, mas não deve apagar um polígono já selecionado.
- O mapa deve disponibilizar somente a ferramenta de desenho de polígono.
- O polígono deve ser fechado, conter ao menos três vértices distintos e possuir área maior que zero.
- O GeoJSON deve ser validado antes de ser convertido para Earth Engine.
- Depois de desenhar um polígono, o mapa deve ser centralizado nos limites da seleção.
- Enquanto houver uma seleção válida, arraste, scroll, duplo clique, toque e teclado não devem alterar a posição ou o zoom do mapa.
- Os controles de remoção da seleção devem permanecer acessíveis enquanto o mapa estiver bloqueado.
- O botão `Limpar seleção` deve remover o GeoJSON, a geometria Earth Engine e o estado de bloqueio.
- Uma nova seleção só poderá ser feita depois que a seleção anterior for removida.
- O estado do mapa deve ser persistido em `st.session_state` durante os reruns do Streamlit.
- Falhas de rede, timeout, resposta inválida ou localidade não encontrada devem gerar mensagens orientativas sem interromper a aplicação.

## Critérios de Aceitação

1. Dado um termo válido, quando o usuário pesquisar, então o mapa centraliza na localidade encontrada.
2. Dado um resultado com `boundingbox`, quando a pesquisa terminar, então o zoom enquadra a localidade.
3. Dada uma consulta vazia, quando o usuário pesquisar, então nenhuma requisição é feita e uma orientação é exibida.
4. Dado um termo sem resultados, quando o usuário pesquisar, então a aplicação informa que a localidade não foi encontrada.
5. Dado um erro ou timeout do geocodificador, quando a pesquisa falhar, então a aplicação continua utilizável.
6. Dado o mapa de seleção, quando carregado, então somente a ferramenta de polígono fica disponível.
7. Dado um polígono válido, quando o usuário finalizar o desenho, então o GeoJSON é capturado e convertido para `ee.Geometry.Polygon`.
8. Dado um polígono inválido, quando o usuário tentar analisá-lo, então a análise não é executada e uma mensagem é exibida.
9. Dado um polígono válido, quando a seleção for capturada, então o mapa enquadra a área selecionada.
10. Dado um polígono selecionado, quando o usuário tentar arrastar ou aplicar zoom, então o mapa permanece bloqueado.
11. Dado um polígono selecionado, quando o usuário clicar em `Limpar seleção`, então o polígono desaparece e o mapa volta a ser movimentável.
12. Dado um estado persistido, quando o Streamlit rerenderizar a página, então a seleção e o bloqueio permanecem consistentes.

## Exemplos de Uso

```python
location = search_location("Passo Fundo, RS")
if location:
    center = [location["latitude"], location["longitude"]]
    zoom = calculate_map_zoom(location["boundingbox"])

selection_map = create_selection_map(center, zoom)
map_data = st_folium(
    selection_map,
    returned_objects=["last_active_drawing"],
)

if map_data and map_data.get("last_active_drawing"):
    geometry = geojson_to_ee_geometry(map_data["last_active_drawing"])
```

## Tasks Relacionadas

- SPEC-10-01 a SPEC-10-14 — `tasks-mapa-interacao.md`

## Dependências

- `04-mapas/spec-mapa-base.md`
- `04-mapas/spec-selecao-area.md`
- `05-streamlit/spec-controles.md`
- `05-streamlit/spec-mapa-ui.md`
