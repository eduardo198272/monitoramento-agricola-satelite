# Spec: SPEC-15-07 — Interface de resultados unificada

## Propósito

Reorganizar a apresentação dos resultados para que os indicadores principais apareçam
imediatamente após o mapa de seleção, eliminar duplicação de alertas de anomalia e
garantir semântica correta de mensagens (warning para anomalias, error para falhas
técnicas). Manter os dados de análise existentes e evitar reprocessamento em reruns.

## Escopo

Incluído:
- Alterar `display_summary()` para receber `area_unit` e remover parâmetro `alert`
- Criar `display_anomaly_alert(alert: str | None)` que usa `st.warning()` apenas
  quando há anomalias (sem mensagem se não houver)
- Reordenar `render_results_panels()` para: mapa de seleção → resumo → alerta →
  mapa temático → série temporal → clima
- Preservar estado de resultados e metadados entre reruns sem disparar nova análise
- Testes automatizados cobrindo ordem, unicidade e semântica das mensagens

Não incluído:
- Alterações no pipeline de análise (`run_analysis`, `run_multi_analysis`)
- Alterações no resumo climático (SPEC-15-06) ou no contexto geográfico (SPEC-15-05)
- Dados sintéticos ou mocks de produção

## Contratos de dados

### `display_summary`

```python
def display_summary(
    index_name: str,
    mean_value: float,
    area_value: float,
    area_unit: str,
    trend: str,
) -> None:
```

Exibe apenas 4 métricas: índice, valor médio, área com unidade, tendência. Sem alertas.

### `display_anomaly_alert`

```python
def display_anomaly_alert(alert: str | None) -> None:
```

Se `alert` não for `None`/vazio, renderiza **uma única** mensagem com `st.warning()`.
Não renderiza nada se não houver alerta.

### Ordem de renderização em `render_results_panels`

1. Mapa de seleção (já renderizado antes da chamada)
2. Resumo (`display_summary`)
3. Alerta de anomalia (`display_anomaly_alert`)
4. Mapa temático (`display_map` + seletor de índice + visão multiíndice)
5. Série temporal, anomalias detalhadas, clima (`display_analysis_details`)

### Reruns

- `render_results_panels()` lê apenas `st.session_state.analysis_results` e
  `st.session_state.analysis_metadata`
- Não chama `run_analysis` nem `run_multi_analysis`
- Resultados persistem entre reruns

## Requisitos de interface

- Responsividade: altura dos mapas adequada para desktop e mobile
- Unidade de área passada explicitamente (padrão "ha")
- Alerta de anomalia: texto amarela (`st.warning`), contendo índice, quantidade e datas
- Erros técnicos/validação: mantêm `st.error()` existente
- Sem mensagens de anomalia quando não houver anomalias detectadas

## Critérios de aceitação

1. Após análise bem-sucedida, resumo aparece imediatamente abaixo do mapa de seleção
2. Resumo contém índice, valor médio, área+unidade, tendência — sem alerta
3. Se houver anomalias, exatamente uma mensagem `st.warning()` aparece entre resumo e mapa temático
4. Se não houver anomalias, nenhuma mensagem de alerta é renderizada
5. Erros técnicos continuam usando `st.error()`
6. Mapa temático, série temporal e clima aparecem após o alerta (ou resumo se sem alerta)
7. Reruns sem nova análise mantêm resultados na mesma ordem sem reprocessar
8. Viewport desktop/mobile: indicadores principais acessíveis sem rolagem excessiva
9. `python -m pytest tests/ --no-cov` passa com cobertura configurada
10. `git diff --check` passa
11. App roda em `http://localhost:8501` — HTTP 200

## Dependências

- SPEC-15-05 (contexto geográfico)
- SPEC-15-06 (resumo climático)
- `src/app/main.py`, `tests/test_streamlit_app.py`
- `07-anomalias/spec-deteccao-anomalias.md` (formato do alerta gerado)