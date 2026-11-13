# Spec: Cálculo de NDWI

## Propósito

Fornecer função para calcular o Normalized Difference Water Index (NDWI) a partir de imagens Sentinel-2. NDWI mede o teor de umidade da vegetação usando as bandas do infravermelho próximo (NIR) e infravermelho de ondas curtas (SWIR), conforme Gao (1996).

## Interface

```python
def calculate_ndwi(image: ee.Image) -> ee.Image
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `image` | `ee.Image` | Imagem Sentinel-2 com bandas espectrais |

**Retorno**: `ee.Image` — imagem de uma banda com valores NDWI (-1 a 1).

## Regras de Negócio

- Fórmula: `NDWI = (NIR - SWIR) / (NIR + SWIR)` (Gao, 1996)
- Para Sentinel-2: NIR = banda `B8`, SWIR = banda `B11`
- Usar `image.normalizedDifference(["B8", "B11"])` do Earth Engine
- Valores NDWI:
  - > 0.3: vegetação com alto teor de umidade
  - 0 a 0.3: vegetação com umidade moderada
  - -0.3 a 0: vegetação seca ou solo exposto
  - < -0.3: superfície sem vegetação ou água
- Retornar imagem com nome da banda `"NDWI"`
- Deve funcionar tanto para `ee.Image` individual quanto aplicada via `.map()` em `ee.ImageCollection`

## Critérios de Aceitação

1. Dado image com bandas B8 e B11, quando calcular NDWI, então retorna imagem com banda "NDWI"
2. Dado pixel com NIR > SWIR, quando calcular, então NDWI > 0 (vegetação úmida)
3. Dado pixel com NIR = SWIR, quando calcular, então NDWI = 0
4. Dado pixel com NIR < SWIR, quando calcular, então NDWI < 0 (seco)
5. Dado imagem sem bandas B8 ou B11, quando calcular, então lança erro apropriado

## Exemplos de Uso

```python
collection = get_image_collection(geometry, "2024-01-01", "2024-12-31")
with_ndwi = collection.map(calculate_ndwi)
```

## Tasks Relacionadas

- TASK-018 — Calcular NDWI
- TASK-020 — Função calculate_ndwi
- TASK-021 — Validar índices

## Dependências

- `02-earth-engine/spec-busca-imagem.md`
- `02-earth-engine/spec-filtro-nuvem.md`
