# Tasks: Detecção de Anomalias

Referência: `docs/specs/07-anomalias/spec-deteccao-anomalias.md`

| ID | Descrição | Critério de Aceitação | Esforço |
|---|---|---|---|
| SPEC-07-01 | Implementar `detect_anomalies(time_series, window_size, std_threshold)` com cálculo de z-score por janela móvel | Retorna lista com campos anomaly e z_score | 2h |
| SPEC-07-02 | Tratar edge cases: desvio padrão zero, primeiros N pontos sem avaliação | Divisão por zero evitada, primeiros pontos não-anomalia | 1h |
| SPEC-07-03 | Escrever testes mockados: série com anomalia, sem anomalia, desvio zero, poucos pontos | 4+ testes passando | 1h |
| SPEC-07-04 | Implementar `generate_alert(anomalies, index_name)` | Retorna string "ALERTA: N anomalias em: datas" ou None | 30min |
| SPEC-07-05 | Escrever testes: alerta com anomalias, alerta sem anomalias | 2 testes passando | 30min |
