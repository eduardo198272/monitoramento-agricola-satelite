# Spec: Detecção de Anomalias

## Propósito

Fornecer funções para detectar anomalias na série temporal do índice de vegetação, identificando quedas atípicas que possam indicar problemas na lavoura (pragas, seca, etc.).

## Interface

```python
def detect_anomalies(
    time_series: list[dict],
    window_size: int = 3,
    std_threshold: float = 1.0
) -> list[dict]
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `time_series` | `list[dict]` | Série temporal `[{"date": ..., "value": ...}]` |
| `window_size` | `int` | Janela móvel para calcular média/desvio (dias, default 3) |
| `std_threshold` | `float` | Número de desvios padrão para considerar anomalia (default 1.0 — 1 sigma conforme metodologia) |

**Retorno**: `list[dict]` — lista de pontos marcados com `{"date": ..., "value": ..., "anomaly": bool, "z_score": float}`.

## Regras de Negócio

- Para cada ponto, calcular a média e desvio padrão dos pontos na janela anterior
- Calcular z-score: `z = (valor - média) / desvio_padrão`
- Se `z < -std_threshold` (valor muito abaixo da média), marcar como anomalia
- Se desvio_padrão = 0, não marcar como anomalia (divisão por zero)
- Se `z` for positivo (acima da média), não marcar como anomalia
- Retornar cópia dos dados com campos adicionais, sem modificar original
- Primeiros `window_size` pontos: não é possível calcular (insuficientes), marcar como não anomalia

## Critérios de Aceitação

1. Dado série com anomalia (ponto muito abaixo da média), quando detectar, então ponto é marcado anomaly=true
2. Dado série sem anomalias, quando detectar, então todos são anomaly=false
3. Dado série com desvio=0, quando detectar, então não marca anomalia
4. Primeiros N pontos (window_size) não são avaliados como anomalia

```python
def generate_alert(anomalies: list[dict], index_name: str) -> str | None
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `anomalies` | `list[dict]` | Série com detecções |
| `index_name` | `str` | Nome do índice |

**Retorno**: `str` ou `None` — mensagem de alerta ou None se sem anomalias.

## Regras de Negócio (Alertas)

- Se houver anomalias, retornar: "ALERTA: {N} anomalia(s) detectada(s) no {index_name} em: {datas}"
- Se não houver anomalias, retornar None

## Critérios de Aceitação (Alertas)

1. Dado anomalias detectadas, quando gerar alerta, então retorna string com N e datas
2. Dado nenhuma anomalia, quando gerar alerta, então retorna None

## Análise de Tendência

```python
def compute_trend(time_series: list[dict]) -> str
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `time_series` | `list[dict]` | Série temporal `[{"date": ..., "value": ...}]` |

**Retorno**: `str` — "crescente", "estável" ou "decrescente".

## Regras de Negócio (Tendência)

- Calcular coeficiente angular (inclinação) via regressão linear simples dos valores ao longo do tempo
- Se inclinação > 0.01: "crescente"
- Se inclinação < -0.01: "decrescente"
- Caso contrário: "estável"
- Se menos de 2 pontos na série, retornar "estável" (dados insuficientes)

## Critérios de Aceitação (Tendência)

1. Dado série com valores crescentes, quando computar tendência, então retorna "crescente"
2. Dado série com valores decrescentes, quando computar tendência, então retorna "decrescente"
3. Dado série sem tendência clara, quando computar, então retorna "estável"
4. Dado série com menos de 2 pontos, quando computar, então retorna "estável"

## Tasks Relacionadas

- TASK-035 — Média
- TASK-036 — Desvio
- TASK-037 — Detectar
- TASK-038 — UI alerta

## Dependências

- `06-series-temporais/spec-serie-temporal.md`
