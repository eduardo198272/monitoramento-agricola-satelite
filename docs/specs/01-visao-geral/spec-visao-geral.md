# Spec: Visão Geral do Sistema

## Propósito

Definir a arquitetura, fluxo de dados e componentes do Sistema de Monitoramento Agrícola por Imagens de Satélite. Esta spec serve como referência para todas as demais.

## Arquitetura

O sistema segue arquitetura de 3 camadas:

```
[Usuário]
    |
    v
[Streamlit App]  ← Camada de Interface (frontend web)
    |
    v
[Python/Processamento]  ← Camada de Lógica (cálculos, orquestração)
    |
    v
[Google Earth Engine]   ← Camada de Dados (imagens de satélite)
[NASA POWER API]        ← Camada de Dados (clima)
```

## Stack

| Componente | Tecnologia | Versão |
|---|---|---|
| Linguagem | Python | 3.12.6 |
| Interface | Streamlit | 1.55.0 |
| Satélite | Google Earth Engine API | 1.7.17 |
| Geo-visualização | geemap | 0.37.1 |
| Gráficos | plotly | 6.6.0 |
| Processamento | pandas, numpy | 2.3.3, 2.4.3 |
| Testes | pytest, pytest-cov | 9.0.3, 7.1.0 |

## Fluxo de Dados (End-to-End)

1. Usuário desenha polígono no mapa → coordenadas GeoJSON
2. Usuário seleciona data inicial/final
3. Usuário seleciona índice (NDVI/NDWI)
4. Sistema busca imagens Sentinel-2 na área/período via Earth Engine
5. Sistema aplica filtro de nuvens (banda QA60)
6. Sistema calcula o índice selecionado
7. Sistema exibe mapa temático com cores
8. Sistema gera série temporal do índice
9. Sistema detecta anomalias (desvios da média histórica)
10. Sistema busca dados climáticos (NASA POWER) para o período
11. Sistema exibe alertas se anomalias detectadas

## Convenções

- **TDD primeiro**: todo código deve ter teste escrito antes da implementação
- **Earth Engine**: autenticação via `ee.Initialize(project=...)` lendo de `os.getenv("EE_PROJECT_ID")`
- **Coordenadas**: formato GeoJSON (Polygon)
- **NDVI**: `(NIR - Red) / (NIR + Red)`, onde NIR = B8, Red = B4 (Sentinel-2)
- **NDWI**: `(Green - NIR) / (Green + NIR)`, onde Green = B3, NIR = B8 (Sentinel-2)

## Estrutura de Diretórios

```
src/
├── app/
│   ├── __init__.py
│   ├── config.py         # Configurações (APP_NAME, VERSION, EE_PROJECT_ID)
│   ├── ee_auth.py        # Autenticação Earth Engine
│   ├── main.py           # Entry point Streamlit
│   └── utils.py          # Utilitários
tests/
├── test_config.py
├── test_ee_auth.py
└── test_main.py
```

## Tasks Relacionadas

- TASK-001 a TASK-003

## Dependências

- Nenhuma (spec raiz)
