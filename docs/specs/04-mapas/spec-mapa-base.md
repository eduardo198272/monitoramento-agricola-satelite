# Spec: Mapa Base

## Propósito

Fornecer função que cria um mapa interativo base utilizando geemap, centralizado na área de interesse do usuário.

## Interface

```python
def create_base_map(center: list = None, zoom: int = 10) -> geemap.Map
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `center` | `list` ou `None` | Coordenadas [lat, lon] do centro do mapa. Se None, usar [-28.0, -52.0] (default RS) |
| `zoom` | `int` | Nível de zoom inicial (1-20, default 10) |

**Retorno**: `geemap.Map` — mapa interativo do folium/ipyleaflet.

## Regras de Negócio

- Usar `geemap.Map()` para criar o mapa
- Adicionar controle de camadas (Layer Control) ao mapa
- Adicionar barra de escala
- Mapa deve permitir zoom e pan interativos
- Centro padrão: região de Passo Fundo/RS (-28.0, -52.0)
- Mapa base padrão: Satélite (ROADMAP ou SATELLITE)

## Critérios de Aceitação

1. Dado center e zoom, quando criar mapa, então mapa é centralizado nas coordenadas fornecidas
2. Dado center=None, quando criar mapa, então usa centro padrão
3. Mapa retornado é instância de `geemap.Map` e renderizável via `to_streamlit()`
4. Mapa deve conter controle de camadas visível

## Tasks Relacionadas

- TASK-022 — Mapa base

## Dependências

- Nenhuma (pode ser implementado de forma independente)
