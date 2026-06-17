# Spec: Seleção de Área no Mapa

## Propósito

Fornecer funcionalidade para o usuário desenhar um polígono ou retângulo no mapa para selecionar a área de interesse para análise.

## Interface

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

## Regras de Negócio

- Usar o DrawControl do ipyleaflet ou `geemap.Map.draw_control`
- Habilitar ferramenta de desenho de polígono/retângulo no mapa
- Usuário desenha clicando para definir vértices
- Ao finalizar o desenho, a geometria deve ficar disponível para consulta
- Extrair coordenadas e converter para `ee.Geometry.Polygon` ou `ee.Geometry.Rectangle`
- Se nenhum desenho foi feito, `get_drawn_geometry` retorna `None`

## Critérios de Aceitação

1. Dado map_obj, quando habilitar desenho, então ferramenta de desenho aparece no mapa
2. Dado draw_type="polygon", quando desenhar, então geometria é um polígono
3. Dado draw_type="rectangle", quando desenhar, então geometria é um retângulo
4. Dado nenhum desenho, quando consultar, então retorna None
5. Dado desenho completo, quando consultar, então retorna ee.Geometry válida

## Tasks Relacionadas

- TASK-025 — Draw

## Dependências

- `04-mapas/spec-mapa-base.md`
