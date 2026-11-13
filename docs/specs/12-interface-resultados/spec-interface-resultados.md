# Spec: Organização dos Resultados e Alertas da Análise

## Propósito

Organizar a interface para que os resultados principais apareçam imediatamente após o mapa de seleção, reduzindo a rolagem necessária, e eliminar a duplicação da mensagem de anomalia.

## Interface

```python
def display_summary(
    index_name: str,
    mean_value: float,
    area_value: float,
    area_unit: str,
    trend: str,
) -> None
```

O painel de resumo deve exibir somente:

- índice selecionado;
- valor médio;
- área e unidade;
- tendência.

A mensagem de anomalia será exibida separadamente:

```python
def display_anomaly_alert(alert: str | None) -> None
```

## Regras de Negócio

- A ordem da tela deve ser: mapa de seleção, resumo, alerta de anomalia, mapa temático, série temporal e dados climáticos.
- O painel de resumo deve ficar imediatamente abaixo do mapa de seleção após o processamento.
- O mapa temático não deve impedir o acesso imediato aos indicadores principais.
- A altura dos mapas deve ser suficiente para uso em desktop e mobile, sem criar rolagem desnecessária.
- `display_summary()` não deve renderizar alertas ou mensagens de erro.
- Uma anomalia detectada deve ser exibida apenas com `st.warning()`.
- A mensagem de anomalia deve conter índice, quantidade e datas detectadas.
- Erros técnicos e erros de validação continuam sendo exibidos com `st.error()`.
- Mensagens informativas e confirmações devem manter seus componentes semânticos (`st.info()` e `st.success()`).
- Quando não houver anomalias, nenhuma mensagem de alerta deve ser renderizada.
- A mudança de ordem não pode disparar novo processamento nem alterar os resultados armazenados.

## Critérios de Aceitação

1. Dado um processamento concluído, quando a página renderizar os resultados, então o resumo aparece imediatamente após o mapa de seleção.
2. Dado um resultado, quando o resumo for exibido, então ele contém índice, valor médio, área, unidade e tendência.
3. Dado um resultado com anomalias, quando a página renderizar, então existe uma única mensagem de anomalia.
4. Dado uma anomalia detectada, quando a mensagem for renderizada, então ela usa `st.warning()` e não aparece em vermelho.
5. Dado um resultado sem anomalias, quando a página renderizar, então nenhuma mensagem de anomalia é exibida.
6. Dado um erro técnico, quando a análise falhar, então a mensagem usa `st.error()`.
7. Dado um resultado com gráficos, quando renderizado, então o mapa temático, a série temporal e o clima aparecem após o resumo.
8. Dado um rerun sem nova análise, quando a página renderizar, então os resultados permanecem na mesma ordem.
9. Dado viewport desktop ou mobile, quando a página carregar, então os indicadores principais ficam acessíveis sem rolagem excessiva.

## Exemplos de Uso

```python
display_summary("NDVI", 0.62, 125.40, "ha", "crescente")
display_anomaly_alert("ALERTA: 2 anomalia(s) detectada(s) no NDVI em: 2025-01-10, 2025-02-14")
```

## Tasks Relacionadas

- SPEC-12-01 a SPEC-12-10 — `tasks-interface-resultados.md`

## Dependências

- `05-streamlit/spec-mapa-ui.md`
- `06-series-temporais/spec-serie-temporal.md`
- `07-anomalias/spec-deteccao-anomalias.md`
- `08-clima/spec-nasa-power.md`
- `11-unidades-area/spec-unidades-area.md`
