# Spec: Legenda do Mapa

## Propósito

Fornecer função que adiciona legenda colorida ao mapa, indicando a escala de valores do índice exibido (NDVI ou NDWI).

## Interface

```python
def add_colorbar(
    map_obj: geemap.Map,
    palette: list,
    index_name: str,
    min_val: float = -1,
    max_val: float = 1
) -> None
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `map_obj` | `geemap.Map` | Mapa onde adicionar a legenda |
| `palette` | `list` | Lista de cores hex da paleta |
| `index_name` | `str` | Nome do índice para o título da legenda |
| `min_val` | `float` | Valor mínimo da escala (default -1) |
| `max_val` | `float` | Valor máximo da escala (default 1) |

**Retorno**: `None` — modifica o mapa in-place.

## Regras de Negócio

- Usar `geemap.Map.add_colorbar()` ou criar elemento HTML/CSS personalizado
- Legenda deve mostrar gradiente horizontal com a paleta
- Abaixo do gradiente, exibir valores numéricos (min, meio, max)
- Título da legenda: nome do índice
- Posicionada no canto inferior direito do mapa
- Dimensões aproximadas: largura 300px, altura 40px (gradiente)

## Critérios de Aceitação

1. Dado map_obj e palette, quando adicionar legenda, então legenda aparece no canto inferior direito
2. Legenda exibe o gradiente de cores correspondente à paleta
3. Legenda exibe "NDVI" ou "NDWI" como título conforme index_name
4. Legenda exibe os valores -1, 0, 1 na escala

## Tasks Relacionadas

- TASK-024 — Legenda

## Dependências

- `04-mapas/spec-visualizacao-indice.md`
