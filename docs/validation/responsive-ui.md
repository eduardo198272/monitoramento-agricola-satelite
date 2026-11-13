# Validação Responsiva da UI Map-First

## Execução

- Data: 2026-10-10
- Navegador: Chrome headless com a aplicação Streamlit em execução
- Páginas verificadas: workspace inicial com mapa e controles
- Critério: largura do documento e do corpo igual à viewport, sem overflow horizontal; iframe do mapa presente, dentro da largura disponível e com altura utilizável.

## Matriz de Viewports

| Viewport | Largura do documento/corpo | Iframe do mapa | Resultado |
|---:|---:|---:|---|
| 1440 × 900 | 1440 px | 1270 × 600 px | Passou |
| 1024 × 900 | 1024 px | 854 × 600 px | Passou |
| 768 × 900 | 768 px | 726 × 600 px | Passou |
| 390 × 900 | 390 px | 369 × 585 px | Passou |
| 320 × 900 | 320 px | 299 × 585 px | Passou |

Os controles horizontais quebram linha nas larguras verificadas, e o mapa permanece dimensionado dentro da viewport. O breakpoint mobile reduz a altura do mapa para preservar espaço vertical sem tornar a área de interação pequena.

## Regressão Automatizada

- `py -m pytest`: 307 testes aprovados.
- Cobertura: 100% de linhas e branches dos módulos configurados.
