# Spec: Filtro de Nuvens (QA60)

## Propósito

Fornecer função que aplica máscara de nuvens utilizando a banda QA60 das imagens Sentinel-2, removendo pixels com nuvens e cirros.

## Interface

```python
def mask_clouds(image: ee.Image) -> ee.Image
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `image` | `ee.Image` | Imagem Sentinel-2 individual |

**Retorno**: `ee.Image` — imagem com pixels de nuvem mascarados (valor 0).

## Regras de Negócio

- Extrair banda `QA60` da imagem
- Bits 10 e 11 da banda QA60 indicam presença de nuvens e cirros respectivamente
- Criar máscara: `qa60.bitwiseAnd(2 << 10).eq(0)` (sem nuvens) E `qa60.bitwiseAnd(2 << 11).eq(0)` (sem cirros)
- Aplicar `image.updateMask(mask)` para remover pixels com nuvem
- Retornar a imagem com nuvens mascaradas (pixels mascarados não aparecem no mapa nem nos cálculos)

## Critérios de Aceitação

1. Dado image com banda QA60, quando aplicar `mask_clouds`, então retorna imagem com máscara aplicada
2. Dado pixel com bit 10 = 1 (nuvem), quando aplicar máscara, então pixel é mascarado
3. Dado pixel com bit 11 = 1 (cirro), quando aplicar máscara, então pixel é mascarado
4. Dado pixel sem nuvens nem cirros, quando aplicar máscara, então pixel permanece visível

## Tasks Relacionadas

- TASK-014 — Filtrar QA60

## Dependências

- `02-earth-engine/spec-busca-imagem.md`
