# Spec: Unidade de Área em Hectares e Acres

## Propósito

Permitir que o usuário escolha a unidade utilizada para exibir a área analisada. A unidade padrão será hectare, com opção de alternar para acres sem alterar o processamento geoespacial.

## Interface

```python
HECTARE_TO_ACRE = 2.47105

def square_meters_to_hectares(area_m2: float) -> float
def hectares_to_acres(area_ha: float) -> float
def format_area(area_ha: float, unit: str = "ha") -> str
```

| Função | Parâmetros | Retorno |
|---|---|---|
| `square_meters_to_hectares` | `area_m2: float` | Área em hectares |
| `hectares_to_acres` | `area_ha: float` | Área em acres |
| `format_area` | `area_ha: float`, `unit: str` | Texto formatado com valor e unidade |

Unidades aceitas:

- `ha`: hectares;
- `ac`: acres.

## Regras de Negócio

- A área calculada pelo Earth Engine deve permanecer em metros quadrados até a camada de apresentação.
- A conversão padrão será `1 ha = 2,47105 ac`.
- A unidade padrão da aplicação será hectares (`ha`).
- O termo exibido será `acres`; “hacres” não deve ser utilizado.
- Valores negativos devem ser rejeitados.
- Valores nulos, não numéricos ou infinitos devem ser rejeitados.
- A unidade deve ser validada contra o conjunto `{"ha", "ac"}`.
- A troca de unidade deve atualizar os cards sem recalcular a análise.
- O valor deve ser exibido com duas casas decimais.
- A unidade selecionada deve permanecer em `st.session_state` durante os reruns.
- A unidade deve ser aplicada de forma consistente em cards, tabelas, relatórios e futuras exportações.

## Critérios de Aceitação

1. Dado `10000 m²`, quando convertido para hectares, então o resultado é `1 ha`.
2. Dado `1 ha`, quando convertido para acres, então o resultado é `2,47105 ac`.
3. Dado um valor válido, quando a unidade não for informada, então hectares são utilizados.
4. Dado um valor negativo, quando convertido, então uma exceção de validação é gerada.
5. Dado `NaN`, infinito ou tipo inválido, quando convertido, então uma exceção de validação é gerada.
6. Dado o seletor de unidade, quando a aplicação iniciar, então `Hectares (ha)` estará selecionado.
7. Dado `Acres (ac)`, quando o usuário selecionar essa opção, então o card exibe o valor convertido em acres.
8. Dado um rerun do Streamlit, quando a unidade tiver sido alterada, então a escolha permanece selecionada.
9. Dado um resultado de análise, quando a unidade for alterada, então a imagem, os índices e a área analisada não são recalculados.
10. Dado qualquer componente que exiba área, quando renderizado, então ele usa a unidade selecionada.

## Exemplos de Uso

```python
area_ha = square_meters_to_hectares(area_m2)
area_label = format_area(area_ha, unit="ac")
# Exemplo: "247,11 ac"
```

## Tasks Relacionadas

- SPEC-11-01 a SPEC-11-09 — `tasks-unidades-area.md`

## Dependências

- `05-streamlit/spec-controles.md`
- `05-streamlit/spec-mapa-ui.md`
- `09-mvp/spec-fluxo-completo.md`
