# Spec: Cálculo de NDMI

## Propósito

Fornecer função para calcular o Normalized Difference Moisture Index (NDMI) a partir de imagens Sentinel-2. NDMI mede o teor de umidade da vegetação usando as bandas do infravermelho próximo (NIR) e infravermelho de ondas curtas (SWIR), sendo especialmente útil para detectar estresse hídrico.

## Interface

```python
def calculate_ndmi(image: ee.Image) -> ee.Image
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `image` | `ee.Image` | Imagem Sentinel-2 com bandas espectrais |

**Retorno**: `ee.Image` — imagem de uma banda com valores NDMI (-1 a 1).

## Regras de Negócio

- Fórmula: `NDMI = (NIR - SWIR) / (NIR + SWIR)`
- Para Sentinel-2: NIR = banda `B8A` (865nm), SWIR = banda `B11` (1610nm)
- Usar `image.normalizedDifference(["B8A", "B11"])` do Earth Engine
- Valores NDMI:
  - > 0.4: vegetação muito úmida
  - 0.2 a 0.4: vegetação com umidade adequada
  - 0 a 0.2: vegetação com estresse hídrico leve
  - -0.2 a 0: vegetação seca ou solo exposto
  - < -0.2: superfície sem vegetação
- Retornar imagem com nome da banda `"NDMI"`
- Deve funcionar tanto para `ee.Image` individual quanto aplicada via `.map()` em `ee.ImageCollection`

> **Nota**: NDMI e NDWI (Gao) compartilham a mesma fórmula `(NIR - SWIR) / (NIR + SWIR)`, diferenciando-se pelas bandas: NDMI usa B8A/B11, NDWI usa B8/B11. Para uso agrícola, NDMI é o índice mais difundido para detecção de estresse hídrico.

## Critérios de Aceitação

1. Dado image com bandas B8A e B11, quando calcular NDMI, então retorna imagem com banda "NDMI"
2. Dado pixel com NIR > SWIR, quando calcular, então NDMI > 0 (vegetação úmida)
3. Dado pixel com NIR = SWIR, quando calcular, então NDMI = 0
4. Dado pixel com NIR < SWIR, quando calcular, então NDMI < 0 (seco)
5. Dado imagem sem bandas B8A ou B11, quando calcular, então lança erro apropriado

## Exemplos de Uso

```python
collection = get_image_collection(geometry, "2024-01-01", "2024-12-31")
with_ndmi = collection.map(calculate_ndmi)
```

## Tasks Relacionadas

- (Opcional — implementar após NDVI e NDWI)

## Dependências

- `02-earth-engine/spec-busca-imagem.md`
- `02-earth-engine/spec-filtro-nuvem.md`
