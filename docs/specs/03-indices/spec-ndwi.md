# Spec: Cálculo de NDWI

## Propósito

Fornecer função para calcular o Normalized Difference Water Index (NDWI) a partir de imagens Sentinel-2. NDWI detecta corpos d'água e mede o teor de umidade da vegetação usando as bandas verde (Green) e infravermelho próximo (NIR).

## Interface

```python
def calculate_ndwi(image: ee.Image) -> ee.Image
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `image` | `ee.Image` | Imagem Sentinel-2 com bandas espectrais |

**Retorno**: `ee.Image` — imagem de uma banda com valores NDWI (-1 a 1).

## Regras de Negócio

- Fórmula: `NDWI = (Green - NIR) / (Green + NIR)`
- Para Sentinel-2: Green = banda `B3`, NIR = banda `B8`
- Usar `image.normalizedDifference(["B3", "B8"])` do Earth Engine
- Valores NDWI:
  - > 0: superfície com água
  - 0 a -0.2: umidade no solo/vegetação
  - < -0.2: superfície seca
- Retornar imagem com nome da banda `"NDWI"`
- Deve funcionar tanto para `ee.Image` individual quanto aplicada via `.map()` em `ee.ImageCollection`

## Critérios de Aceitação

1. Dado image com bandas B3 e B8, quando calcular NDWI, então retorna imagem com banda "NDWI"
2. Dado pixel com Green > NIR, quando calcular, então NDWI > 0 (água)
3. Dado pixel com Green = NIR, quando calcular, então NDWI = 0
4. Dado pixel com Green < NIR, quando calcular, então NDWI < 0 (seco)
5. Dado imagem sem bandas B3 ou B8, quando calcular, então lança erro apropriado

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
