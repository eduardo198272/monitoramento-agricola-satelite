# Spec: Integração do Mapa na UI

## Propósito

Integrar o mapa de seleção, o mapa temático e os resultados da análise na área principal do Streamlit, mantendo os indicadores principais acessíveis após o processamento. A organização detalhada dos resultados está em `12-interface-resultados/spec-interface-resultados.md`.

## Interface

```python
# Exibição do mapa no Streamlit
def display_map(map_obj: geemap.Map) -> None

# Exibição do painel de resumo
def display_summary(
    index_name: str,
    mean_value: float,
    area_value: float,
    area_unit: str,
    trend: str,
) -> None
```

## Regras de Negócio

- Usar `streamlit-folium` para o mapa de seleção e `geemap.Map.to_streamlit()` para o mapa temático
- O mapa de seleção deve estar disponível antes da análise
- Exibir spinner/loading durante o processamento (`st.spinner("Processando...")`)
- Abaixo do mapa, exibir painel de resumo com:
  - Nome do índice selecionado
  - Valor médio do índice na área
  - Área analisada na unidade selecionada
  - Tendência: "crescente" (verde), "estável" (azul) ou "decrescente" (vermelho)
- Exibir anomalias separadamente com `st.warning()`
- Se ocorrer erro no processamento, exibir mensagem de erro com `st.error()`

## Critérios de Aceitação

1. Dado processamento concluído, quando exibir mapa, então mapa aparece na área principal
2. Dado mapa sendo carregado, então spinner é exibido
3. Dado resultado da análise, então painel de resumo aparece abaixo do mapa
4. Dado erro no processamento, então mensagem de erro é exibida
5. Antes de qualquer análise, área principal mostra orientação para desenhar um polígono
6. Dado uma anomalia detectada, então ela aparece uma única vez em amarelo

## Tasks Relacionadas

- TASK-030 — Mapa UI

## Dependências

- `05-streamlit/spec-app.md`
- `05-streamlit/spec-controles.md`
- `04-mapas/spec-visualizacao-indice.md`
