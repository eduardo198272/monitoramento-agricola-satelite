# Spec: Cálculo de NDVI

## Propósito

Fornecer função para calcular o Normalized Difference Vegetation Index (NDVI) a partir de imagens Sentinel-2. NDVI mede a vitalidade da vegetação usando as bandas do infravermelho próximo (NIR) e vermelho (Red).

## Interface

```python
def calculate_ndvi(image: ee.Image) -> ee.Image
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `image` | `ee.Image` | Imagem Sentinel-2 com bandas espectrais |

**Retorno**: `ee.Image` — imagem de uma banda com valores NDVI (-1 a 1).

## Regras de Negócio

- Fórmula: `NDVI = (NIR - Red) / (NIR + Red)`
- Para Sentinel-2: NIR = banda `B8`, Red = banda `B4`
- Usar `image.normalizedDifference(["B8", "B4"])` do Earth Engine
- Valores NDVI variam de -1 a 1:
  - < 0: água, neve, nuvens
  - 0 a 0.2: solo exposto, rocha, areia
  - 0.2 a 0.5: vegetação esparsa
  - 0.5 a 1.0: vegetação densa e saudável
- Retornar imagem com nome da banda `"NDVI"`
- Deve funcionar tanto para `ee.Image` individual quanto aplicada via `.map()` em `ee.ImageCollection`

## Critérios de Aceitação

1. Dado image com bandas B8 e B4, quando calcular NDVI, então retorna imagem com banda "NDVI"
2. Dado pixel com NIR > Red, quando calcular, então NDVI > 0 (vegetação)
3. Dado pixel com NIR = Red, quando calcular, então NDVI = 0 (solo exposto)
4. Dado pixel com NIR < Red, quando calcular, então NDVI < 0 (água)
5. Dado imagem sem bandas B8 ou B4, quando calcular, então lança erro apropriado

## Exemplos de Uso

```python
collection = get_image_collection(geometry, "2024-01-01", "2024-12-31")
with_ndvi = collection.map(calculate_ndvi)
```

## Tasks Relacionadas

- TASK-017 — Calcular NDVI
- TASK-019 — Função calculate_ndvi
- TASK-021 — Validar índices

## Dependências

- `02-earth-engine/spec-busca-imagem.md`
- `02-earth-engine/spec-filtro-nuvem.md`
