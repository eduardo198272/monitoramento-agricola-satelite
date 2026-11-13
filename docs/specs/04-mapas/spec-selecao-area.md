# Spec: Seleção de Área no Mapa

## Propósito

Fornecer a interface base para o usuário selecionar a área de interesse desenhando um polígono no mapa. Pesquisa, centralização, bloqueio e persistência da seleção são detalhados em `10-mapas-interacao/spec-mapa-interacao.md`.

## Interface — Desenho

```python
def enable_area_draw(map_obj: geemap.Map) -> None
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `map_obj` | `geemap.Map` | Mapa onde habilitar o desenho |
**Retorno**: `None` — configura o mapa para capturar desenhos.

```python
def get_drawn_geometry(map_obj: geemap.Map) -> ee.Geometry | None
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `map_obj` | `geemap.Map` | Mapa com o desenho do usuário |

**Retorno**: `ee.Geometry` ou `None` — geometria desenhada ou None se nada foi desenhado.

## Regras de Negócio — Desenho

- Usar uma integração que retorne o GeoJSON ao Streamlit, atualmente `folium` com `streamlit-folium`
- Habilitar somente a ferramenta de desenho de polígono
- Usuário desenha clicando para definir vértices
- Ao finalizar o desenho, o GeoJSON deve ficar disponível para consulta no Python
- Extrair coordenadas e converter para `ee.Geometry.Polygon`
- Se nenhum desenho foi feito, `get_drawn_geometry` retorna `None`

## Critérios de Aceitação — Desenho

1. Dado map_obj, quando habilitar desenho, então ferramenta de desenho aparece no mapa
2. Dado o controle de desenho habilitado, quando desenhar, então geometria é um polígono
3. Dado uma ferramenta diferente de polígono, então ela não está disponível
4. Dado nenhum desenho, quando consultar, então retorna None
5. Dado desenho completo, quando consultar, então retorna ee.Geometry válida

## Tasks Relacionadas

- TASK-025 — Draw

## Dependências

- `04-mapas/spec-mapa-base.md`
