# Spec: Integração do Mapa na UI

## Propósito

Integrar o mapa interativo e os resultados da análise na área principal do Streamlit, exibindo o mapa temático após o processamento.

## Interface

```python
# Exibição do mapa no Streamlit
def display_map(map_obj: geemap.Map) -> None

# Exibição do painel de resumo
def display_summary(
    index_name: str,
    mean_value: float,
    area_ha: float,
    trend: str,
    alert: str = None
) -> None
```

## Regras de Negócio

- Usar `geemap.Map.to_streamlit(height=600)` para renderizar o mapa no Streamlit
- O mapa só deve ser exibido após o botão "Analisar" ser clicado e o processamento concluído
- Exibir spinner/loading durante o processamento (`st.spinner("Processando...")`)
- Abaixo do mapa, exibir painel de resumo com:
  - Nome do índice selecionado
  - Valor médio do índice na área
  - Área analisada em hectares
  - Tendência: "crescente" (verde), "estável" (azul) ou "decrescente" (vermelho)
  - Alerta se anomalia detectada (vermelho) ou "Normal" (verde)
- Se ocorrer erro no processamento, exibir mensagem de erro com `st.error()`

## Critérios de Aceitação

1. Dado processamento concluído, quando exibir mapa, então mapa aparece na área principal
2. Dado mapa sendo carregado, então spinner é exibido
3. Dado resultado da análise, então painel de resumo aparece abaixo do mapa
4. Dado erro no processamento, então mensagem de erro é exibida
5. Antes de qualquer análise, área principal mostra mensagem "Selecione uma área e clique em Analisar"

## Tasks Relacionadas

- TASK-030 — Mapa UI

## Dependências

- `05-streamlit/spec-app.md`
- `05-streamlit/spec-controles.md`
- `04-mapas/spec-visualizacao-indice.md`
