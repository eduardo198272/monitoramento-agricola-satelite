# Spec: Filtros de Data e Área

## Propósito

Fornecer funções auxiliares para filtrar a coleção de imagens por intervalo de datas e geometria espacial, reutilizáveis em diferentes partes do sistema.

## Interface

```python
def filter_by_date(collection: ee.ImageCollection, start_date: str, end_date: str) -> ee.ImageCollection
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `collection` | `ee.ImageCollection` | Coleção de imagens a filtrar |
| `start_date` | `str` | Data inicial "YYYY-MM-DD" |
| `end_date` | `str` | Data final "YYYY-MM-DD" |

**Retorno**: `ee.ImageCollection` — coleção filtrada por data.

```python
def filter_by_area(collection: ee.ImageCollection, geometry: ee.Geometry) -> ee.ImageCollection
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `collection` | `ee.ImageCollection` | Coleção de imagens a filtrar |
| `geometry` | `ee.Geometry` | Região de interesse |

**Retorno**: `ee.ImageCollection` — coleção filtrada por área.

## Regras de Negócio

- `filter_by_date`: usa `ee.Filter.date(start_date, end_date)`
- `filter_by_area`: usa `ee.Filter.bounds(geometry)`
- Validar que `start_date <= end_date`; caso contrário, lançar `ValueError`
- Validar que as strings de data estão no formato ISO "YYYY-MM-DD"; caso contrário, lançar `ValueError`
- Funções devem ser compostáveis: `filter_by_date(filter_by_area(collection, geom), start, end)`

## Critérios de Aceitação

1. Dado collection e datas válidas, quando filtrar, então retorna imagens apenas no período
2. Dado collection e geometry, quando filtrar, então retorna imagens que intersectam a área
3. Dado `start_date > end_date`, quando filtrar, então lança `ValueError`
4. Dado data em formato inválido, quando filtrar, então lança `ValueError`
5. Dada composição dos dois filtros, quando aplicar ambos, então retorna imagens que satisfazem ambos os critérios

## Tasks Relacionadas

- TASK-015 — Filtrar por data
- TASK-016 — Filtrar por área

## Dependências

- `02-earth-engine/spec-busca-imagem.md`
