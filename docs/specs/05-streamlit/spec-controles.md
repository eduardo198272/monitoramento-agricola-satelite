# Spec: Controles da Interface

## Propósito

Fornecer os controles de entrada do usuário na sidebar: seleção de datas, seleção de índice (NDVI/NDWI) e botão de análise.

## Interface

Os controles são elementos nativos do Streamlit inseridos na sidebar:

```python
# Sidebar: seleção de período
start_date: date = st.sidebar.date_input("Data inicial", value=default_start)
end_date: date = st.sidebar.date_input("Data final", value=default_end)

# Sidebar: seleção de índice
index_name: str = st.sidebar.selectbox("Índice", options=["NDVI", "NDWI"])

# Sidebar: botão de ação
analyze: bool = st.sidebar.button("Analisar")
```

## Regras de Negócio

- **Data inicial**: default = 12 meses atrás
- **Data final**: default = hoje
- **Validação**: data final não pode ser anterior à data inicial (exibir erro se inválido)
- **Índice**: dropdown com opções "NDVI" e "NDWI"
- **Botão "Analisar"**: desabilitado se datas inválidas; habilita quando válido
- Ao clicar no botão, inicia o pipeline: buscar imagens → calcular índice → exibir mapa

## Critérios de Aceitação

1. Dado app aberto, sidebar exibe campo de data inicial com valor default
2. Dado app aberto, sidebar exibe campo de data final com valor default
3. Dado app aberto, sidebar exibe dropdown com NDVI e NDWI
4. Dado data final anterior à inicial, quando interagir, então exibe mensagem de erro
5. Dado datas válidas, botão "Analisar" está habilitado
6. Dado clique no botão com datas válidas, então pipeline de análise é acionado

## Tasks Relacionadas

- TASK-027 — Data
- TASK-028 — Índice
- TASK-029 — Botão

## Dependências

- `05-streamlit/spec-app.md`
