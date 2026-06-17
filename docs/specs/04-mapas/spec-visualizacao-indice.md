# Spec: Visualização de Índice no Mapa

## Propósito

Fornecer função que adiciona uma camada temática ao mapa exibindo o NDVI ou NDWI calculado sobre a área de interesse, com paleta de cores representando os valores.

## Interface

```python
def add_index_layer(
    map_obj: geemap.Map,
    index_image: ee.Image,
    index_name: str,
    palette: list = None,
    opacity: float = 0.7
) -> geemap.Map
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `map_obj` | `geemap.Map` | Mapa base onde adicionar a camada |
| `index_image` | `ee.Image` | Imagem com banda do índice (NDVI ou NDWI) |
| `index_name` | `str` | Nome para a camada ("NDVI" ou "NDWI") |
| `palette` | `list` ou `None` | Lista de cores hex. Se None, usar paleta padrão |
| `opacity` | `float` | Opacidade da camada (0-1, default 0.7) |

**Retorno**: `geemap.Map` — mapa com a camada adicionada.

## Regras de Negócio

- Paleta NDVI padrão: `["blue", "white", "green"]` (azul=água, branco=solo, verde=vegetação)
- Paleta NDWI padrão: `["brown", "white", "blue"]` (marrom=seco, branco=úmido, azul=água)
- Usar `map_obj.addLayer(index_image, {min: -1, max: 1, palette: palette}, index_name)`
- Não recriar o mapa, apenas adicionar camada ao existente
- Se `index_image` não tiver a banda especificada, lançar `ValueError`

## Critérios de Aceitação

1. Dado map_obj e index_image, quando adicionar camada, então mapa exibe a camada temática
2. Dado index_name="NDVI", quando adicionar, então usa paleta azul-branco-verde
3. Dado index_name="NDWI", quando adicionar, então usa paleta marrom-branco-azul
4. Dado palette personalizada, quando adicionar, então usa a paleta fornecida

## Tasks Relacionadas

- TASK-023 — NDVI mapa
- TASK-024 — Legenda

## Dependências

- `04-mapas/spec-mapa-base.md`
- `03-indices/spec-ndvi.md` ou `03-indices/spec-ndwi.md`
