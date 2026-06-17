# Spec: Estrutura do App Streamlit

## Propósito

Definir a estrutura geral da aplicação Streamlit, incluindo layout, navegação e organização dos elementos da interface.

## Interface

```python
def main() -> None
```

Ponto de entrada da aplicação. Executado via `streamlit run src/app/main.py`.

## Regras de Negócio

- **Título**: "Monitoramento Agrícola por Imagens de Satélite"
- **Layout**: usar `st.set_page_config(layout="wide")` para aproveitar tela cheia
- **Sidebar**: contém controles de entrada (data, índice, botão)
- **Área principal**: contém mapa e gráficos
- **Organização**:

```
+--------------------------------------------------+
|  TÍTULO                                           |
+----------+---------------------------------------+
| Sidebar  |  Área Principal                        |
|          |                                        |
| [Data    |  +-------------------------------+    |
|  início] |  |        Mapa Interativo         |    |
|          |  |                               |    |
| [Data    |  +-------------------------------+    |
|  fim]    |                                        |
|          |  +-------------------------------+    |
| [Índice] |  |     Gráfico Série Temporal     |    |
|          |  |                               |    |
| [Analisar|  +-------------------------------+    |
|  Botão]  |                                        |
|          |  +-------------------------------+    |
| Status   |  |     Painel de Alertas         |    |
|          |  +-------------------------------+    |
+----------+---------------------------------------+
```

## Critérios de Aceitação

1. Dado `streamlit run main.py`, quando executar, então app abre com layout wide
2. Sidebar contém controles de entrada
3. Área principal contém mapa e espaço para gráficos
4. Título "Monitoramento Agrícola por Imagens de Satélite" é exibido

## Tasks Relacionadas

- TASK-026 — App

## Dependências

- `01-visao-geral/spec-visao-geral.md`
