# Spec: SPEC-15-05 — Exibir contexto geográfico da área real

## Propósito

Exibir perímetro em km e centroide (lat/lon) derivados geoespacialmente da geometria
selecionada, junto à área em ha já existente, no painel de contexto da seleção. Evitar
consultas redundantes ao Earth Engine agrupando as métricas em uma única avaliação
remota.

## Escopo

Incluído:
- Função `calculate_area_context(geometry: ee.Geometry) -> dict` em `maps.py`
  retornando `area_ha`, `perimeter_km`, `centroid` (lat, lon)
- Atualização de `render_selection_map_area()` para chamar o helper, persistir
  `aoi_perimeter_km`, `aoi_centroid` no estado e exibir as três métricas
- Extensão de `clear_area_selection_state()` para limpar os novos campos
- Reutilização do centroide calculado no pipeline (`run_analysis`,
  `run_multi_analysis`, `climate.py`) via parâmetro opcional retrocompatível

Não incluído:
- Exibição de perímetro/centroide nos painéis de resultado pós-análise (somente no
  contexto da seleção)
- Alteração da lógica de desenho/validação do polígono
- Dados sintéticos para preencher as métricas

## Contratos de dados

### Estado da UI (novas chaves)

```
aoi_perimeter_km: float | None
aoi_centroid: tuple[float, float] | None  # (lat, lon)
```

Defaults: `None` em `UI_STATE_DEFAULTS`, limpos em `clear_area_selection_state()`.

### Helper geoespacial

```python
def calculate_area_context(geometry: ee.Geometry) -> dict:
    """
    Retorna {"area_ha": float, "perimeter_km": float, "centroid": (lat, lon)}.
    Lança ValueError se a geometria for inválida ou métricas não finitas/positivas.
    """
```

- Área: `geometry.area().divide(10000).getInfo()`  (m² → ha)
- Perímetro: `geometry.perimeter().divide(1000).getInfo()`  (m → km)
- Centroide: `geometry.centroid().coordinates().getInfo()` → `[lon, lat]`,
  retorna `(lat, lon)` para consistência com uso em mapas/clima
- Agrupar as três em `ee.Dictionary` e um único `getInfo()` quando tecnicamente
  viável; caso contrário, chamadas sequenciais aceitas mas documentadas

### Pipeline (retrocompatível)

- `run_analysis(geometry, start_date, end_date, index_name, area_ha=None,
  perimeter_km=None, centroid=None) -> dict`
- `run_multi_analysis(...)` análogo
- `fetch_climate_data(..., coordinates=None)` — se `coordinates` (lon, lat)
  for fornecido, usa diretamente; caso contrário calcula como hoje

## Requisitos de interface

- No bloco de sucesso da seleção (`render_selection_map_area`), exibir:
  - `Área selecionada: X.XX ha`
  - `Perímetro: Y.YY km`
  - `Centroide: lat, lon` (formato decimal, 4–6 casas)
- Mensagens só aparecem quando geometria válida; em erro, preservar estado
  anterior e exibir erro compreensível
- Reruns sem atualização do mapa preservam as três métricas
- Remoção explícita do desenho limpa área, perímetro, centroide e estado de análise

## Critérios de aceitação

1. Helper `calculate_area_context` retorna as três métricas com unidades corretas
   a partir de geometria EE válida (teste unitário com mock)
2. Helper lança `ValueError` com mensagem orientativa para geometria inválida,
   área/perímetro não finitos ou ≤ 0
3. Ao capturar polígono válido, UI exibe as três métricas e persiste no estado
4. Rerun normal preserva área, perímetro e centroide
5. Remoção do desenho limpa todas as métricas e estado de análise
6. Falha ao calcular contexto não substitui seleção/métricas anteriores
7. Pipeline usa centroide fornecido sem recalcular; chamadas sem o argumento
   continuam funcionando
8. `python -m pytest` passa com cobertura configurada (≥100%)
9. `git diff --check` passa
10. App roda em `http://localhost:8501` — HTTP 200

## Validação visual

- Abrir app sem área: nenhuma métrica exibida
- Desenhar polígono válido: três linhas aparecem com valores reais
- Redesenhar: métricas atualizam
- Apagar desenho: métricas somem, estado de análise limpo
- Ampliar/reduzir janela: sem overflow horizontal, layout responsivo

## Dependências

- SPEC-15-02 (tiles Esri no mapa de seleção — já mergeada)
- `src/app/maps.py`, `src/app/main.py`, `src/app/pipeline.py`, `src/app/climate.py`
- `tests/test_maps.py`, `tests/test_streamlit_app.py`, `tests/test_pipeline.py`