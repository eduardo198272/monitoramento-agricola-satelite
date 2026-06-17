# Spec: Seleção de Área no Mapa

## Propósito

Fornecer funcionalidade para o usuário selecionar a área de interesse para análise, seja desenhando um polígono/retângulo no mapa ou escolhendo uma área pré-definida.

## Interface — Desenho

```python
def enable_area_draw(map_obj: geemap.Map, draw_type: str = "polygon") -> None
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `map_obj` | `geemap.Map` | Mapa onde habilitar o desenho |
| `draw_type` | `str` | Tipo: "polygon" ou "rectangle" (default "polygon") |

**Retorno**: `None` — configura o mapa para capturar desenhos.

```python
def get_drawn_geometry(map_obj: geemap.Map) -> ee.Geometry | None
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `map_obj` | `geemap.Map` | Mapa com o desenho do usuário |

**Retorno**: `ee.Geometry` ou `None` — geometria desenhada ou None se nada foi desenhado.

## Regras de Negócio — Desenho

- Usar o DrawControl do ipyleaflet ou `geemap.Map.draw_control`
- Habilitar ferramenta de desenho de polígono/retângulo no mapa
- Usuário desenha clicando para definir vértices
- Ao finalizar o desenho, a geometria deve ficar disponível para consulta
- Extrair coordenadas e converter para `ee.Geometry.Polygon` ou `ee.Geometry.Rectangle`
- Se nenhum desenho foi feito, `get_drawn_geometry` retorna `None`

## Critérios de Aceitação — Desenho

1. Dado map_obj, quando habilitar desenho, então ferramenta de desenho aparece no mapa
2. Dado draw_type="polygon", quando desenhar, então geometria é um polígono
3. Dado draw_type="rectangle", quando desenhar, então geometria é um retângulo
4. Dado nenhum desenho, quando consultar, então retorna None
5. Dado desenho completo, quando consultar, então retorna ee.Geometry válida

## Interface — Áreas Pré-definidas

```python
def get_predefined_areas() -> list[dict]
```

**Retorno**: `list[dict]` — lista de áreas com `{"name": str, "geometry": ee.Geometry}`.

```python
def load_predefined_area(area_name: str) -> ee.Geometry | None
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `area_name` | `str` | Nome da área pré-definida |

**Retorno**: `ee.Geometry` ou `None` — geometria da área ou None se nome não encontrado.

## Regras de Negócio — Áreas Pré-definidas

- Áreas pré-definidas representam talhões ou lavouras de interesse fixo
- Definidas em um arquivo de configuração (JSON ou dict interno) com coordenadas fixas
- Pelo menos 3 áreas de exemplo: "Talhão A", "Talhão B", "Talhão C"
- Usuário seleciona via dropdown no Streamlit
- Ao selecionar, o mapa centraliza e aplica zoom na área escolhida
- `load_predefined_area` faz busca case-insensitive pelo nome

## Critérios de Aceitação — Áreas Pré-definidas

1. Dado `get_predefined_areas()`, quando chamar, então retorna lista com pelo menos 3 áreas
2. Cada área contém chaves "name" (str) e "geometry" (ee.Geometry)
3. Dado nome válido, `load_predefined_area` retorna ee.Geometry correspondente
4. Dado nome inválido, `load_predefined_area` retorna None

## Tasks Relacionadas

- TASK-025 — Draw

## Dependências

- `04-mapas/spec-mapa-base.md`
