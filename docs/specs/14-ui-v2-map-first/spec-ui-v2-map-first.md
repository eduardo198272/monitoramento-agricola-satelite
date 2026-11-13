# Spec: UI V2 — Interface Map-First

## Propósito

Definir a segunda versão da interface do Sistema de Monitoramento Agrícola por
Imagens de Satélite. A interface deve tratar o mapa como a workspace central da
aplicação e conduzir o usuário pelo fluxo:

```text
Localizar → Delimitar a área → Configurar a análise → Analisar → Explorar resultados
```

Esta especificação substitui, para a UI V2, as regras visuais conflitantes das
specs anteriores. As specs do MVP permanecem preservadas como histórico e como
contratos das funcionalidades de backend.

## Escopo

Incluído:

- novo layout map-first sem dependência da sidebar;
- busca de localidade integrada à workspace do mapa;
- seleção, validação, cálculo e persistência da área de análise;
- barra compacta de período e índices;
- opção `Todos` para análise conjunta;
- troca do índice visualizado sem novo processamento remoto;
- organização dos resultados na mesma tela;
- estados de carregamento, sucesso, erro e ausência de dados;
- estilo visual centralizado e responsivo;
- testes de backend, estado e interface.

Não incluído:

- substituição do Streamlit;
- substituição do Google Earth Engine, geemap ou Folium;
- autenticação de usuários;
- banco de dados;
- diagnóstico agronômico definitivo;
- alteração de fórmulas científicas sem validação e decisão registrada.

## Interface

### Ponto de entrada

```python
def main() -> None
```

Executado por:

```bash
streamlit run src/app/main.py
```

### Pipeline de índice único

```python
def run_analysis(
    geometry: ee.Geometry,
    start_date: str | date,
    end_date: str | date,
    index_name: str,
) -> dict
```

O contrato existente deve continuar funcionando para `NDVI`, `NDWI` e `NDMI`.

### Pipeline multiíndice

```python
def run_multi_analysis(
    geometry: ee.Geometry,
    start_date: str | date,
    end_date: str | date,
    index_names: list[str],
) -> dict
```

O retorno deve possuir, no mínimo:

```python
{
    "success": bool,
    "indices": {
        "NDVI": {
            "index_map": ee.Image,
            "time_series": list[dict],
            "time_series_plot": go.Figure | None,
            "anomalies": list[dict],
            "alert": str | None,
            "mean_value": float | None,
            "trend": str,
        },
    },
    "area_ha": float,
    "image_count": int,
    "climate_data": pd.DataFrame,
    "climate_plot": go.Figure | None,
}
```

### Estado da aplicação

O estado da UI deve usar uma fonte de verdade única, com chaves equivalentes a:

```text
location_center
location_zoom
location_result
aoi_geojson
aoi_geometry
aoi_area_ha
analysis_mode
visible_index
analysis_results
analysis_status
analysis_error
```

Nomes diferentes podem ser usados se a mesma responsabilidade e invariantes
forem mantidos.

## Regras de Negócio

### Layout e navegação

- A sidebar não deve ser necessária para executar uma análise.
- O cabeçalho deve exibir `Monitoramento Agrícola` e um subtítulo curto.
- A busca deve aparecer imediatamente acima do mapa.
- O período, os índices e o botão de análise devem ficar na barra principal.
- O mapa deve ocupar a maior parte da largura disponível.
- A altura inicial do mapa deve ser adequada para desktop, preferencialmente
  entre 65% e 75% da altura da viewport quando suportado pelo componente.
- Os resultados devem aparecer abaixo do mapa, sem criar uma segunda página.

### Busca de localidade

- Consultas vazias não devem chamar o geocodificador.
- A pesquisa deve reutilizar `search_location()` e `calculate_map_zoom()`.
- Uma pesquisa válida deve atualizar centro, zoom e texto da localidade.
- Pesquisar uma localidade não deve criar, substituir ou apagar a área de análise.
- Falhas de rede, timeout e ausência de resultado devem manter a aplicação utilizável.

### Seleção da área

- A área só pode ser definida por polígono desenhado no mapa.
- O controle nativo de desenho pode ser mantido.
- Deve existir uma instrução curta e visível como `Desenhar área`.
- Não deve ser criado um botão visual que não acione o mecanismo real de desenho.
- O GeoJSON deve ser validado antes da conversão para Earth Engine.
- O polígono deve possuir pelo menos três vértices distintos, anel fechado e área
  maior que zero.
- A geometria Earth Engine, o GeoJSON e a área em hectares devem persistir nos
  reruns normais.
- A remoção do desenho deve limpar todos os estados derivados da área.
- A área deve ser calculada geoespacialmente, usando `geometry.area()` ou helper
  equivalente, nunca tratando latitude e longitude como coordenadas cartesianas.
- Quando houver área válida, a interface deve exibir estado positivo e hectares.

### Período e índices

- A data inicial padrão deve ser aproximadamente 12 meses antes da data atual.
- A data final padrão deve ser a data atual.
- `data inicial <= data final` é obrigatório.
- Datas fornecidas como `datetime.date` devem ser normalizadas antes de chegar ao
  Earth Engine e à NASA POWER.
- O seletor principal deve exibir horizontalmente `Todos`, `NDVI`, `NDWI` e `NDMI`.
- `Todos` deve representar todos os índices suportados pelo backend.
- O botão `Analisar área` deve permanecer desabilitado sem geometria válida ou
  com período inválido.

### Análise multiíndice

- A coleção Sentinel-2 filtrada deve ser criada uma única vez por execução.
- A máscara de nuvens deve ser aplicada uma única vez por execução.
- Os índices selecionados devem reutilizar a coleção mascarada.
- Dados climáticos, área e contagem de imagens devem ser compartilhados quando
  a execução for multiíndice.
- O mapa deve exibir apenas um índice por vez.
- Após uma análise `Todos`, trocar o índice visível deve reutilizar os resultados
  armazenados e não executar novamente o pipeline remoto.
- A análise não deve ser executada quando não houver área válida.
- NDMI deve possuir todas as bandas necessárias na coleção utilizada. A decisão
  sobre `B8A/B11` ou outra combinação deve ser registrada e testada.

### Resultados

- O mapa de seleção ou temático deve permanecer na mesma workspace principal.
- Após sucesso, exibir contexto da análise com área, período, índice visível e
  quantidade de imagens.
- Quando `Todos` for analisado, exibir uma visão geral com valores reais dos
  índices disponíveis.
- A visão geral não pode usar valores hardcoded ou dados fictícios.
- Séries temporais, anomalias e clima devem ser organizados abaixo do mapa.
- Alertas devem descrever possível anomalia ou variação observada, sem afirmar
  diagnóstico definitivo.
- Exemplos aceitáveis incluem `Possível redução de umidade` e `Variação
  espectral que merece atenção`.

### Estados e erros

- Estado inicial: mapa, busca, período, índices, área vazia e análise desabilitada.
- Estado com área: polígono visível, hectares exibidos e análise habilitada.
- Estado de processamento: mensagem específica sobre imagens, nuvens, índices ou
  série temporal.
- Estado sem imagens: mensagem amigável com sugestão de ampliar o período.
- Estado de erro Earth Engine: mensagem pública compreensível e detalhe técnico
  registrado por logging.
- Estado de erro de geocodificação: orientação para revisar a localidade.
- Stack traces não devem ser exibidos ao usuário.

### Estilo e responsividade

- CSS deve ser centralizado em `styles.py`, `assets/style.css` ou mecanismo
  equivalente.
- Cores base: `#0E1117`, `#161B22`, `#1C2128`, `#30363D`, `#F0F3F6` e `#8B949E`.
- Verde agrícola deve ser usado principalmente em ações e estados positivos.
- Inputs, botões, cards e espaçamentos devem possuir padrões consistentes.
- Não usar gradientes, sombras excessivas ou ícones meramente decorativos.
- Em telas menores, controles devem quebrar sem overflow horizontal e o mapa deve
  continuar utilizável.

### Performance

- Trocar abas ou índice visível não deve repetir chamadas remotas desnecessárias.
- Objetos Earth Engine não devem ser cacheados de forma incompatível com o
  Streamlit.
- Chamadas `getInfo()` devem ser mantidas no mínimo necessário e agrupadas quando
  a arquitetura permitir.
- A organização da UI não deve mover processamento científico para a camada de
  apresentação.

## Critérios de Aceitação

1. Dado o app aberto, quando a página carregar, então a sidebar não é necessária para iniciar uma análise.
2. Dado uma localidade válida, quando o usuário pesquisar, então o mapa é recentralizado sem criar uma área.
3. Dado um mapa sem seleção, quando a página renderizar, então a área aparece como não selecionada.
4. Dado um polígono válido, quando o desenho terminar, então a geometria e os hectares são persistidos.
5. Dado um polígono inválido, quando o usuário tentar analisá-lo, então o pipeline não é chamado.
6. Dado que não exista geometria válida, quando a página renderizar, então `Analisar área` está desabilitado.
7. Dado um período inválido, quando o usuário alterar as datas, então uma mensagem de validação aparece e a análise é bloqueada.
8. Dado o seletor de índices, quando a página renderizar, então `Todos`, `NDVI`, `NDWI` e `NDMI` estão visíveis sem dropdown principal.
9. Dado `Todos`, quando o usuário analisar uma área, então todos os índices suportados são calculados.
10. Dado `Todos`, quando a execução ocorrer, então a coleção e a máscara de nuvens não são recriadas para cada índice.
11. Dado uma análise concluída, quando o usuário trocar o índice visível, então o mapa muda sem nova execução remota completa.
12. Dado uma análise concluída, quando a página renderizar, então os resultados aparecem abaixo do mapa na mesma tela.
13. Dado uma execução multiíndice, quando a visão geral renderizar, então seus valores são derivados dos resultados reais.
14. Dado uma ausência de imagens, quando o pipeline terminar, então uma mensagem amigável é exibida.
15. Dado um erro técnico, quando o pipeline falhar, então a UI não exibe stack trace cru.
16. Dado uma análise com anomalia, quando os resultados renderizarem, então a linguagem indica possibilidade ou variação observada.
17. Dado um rerun normal, quando a página renderizar novamente, então a seleção, o contexto e os resultados permanecem consistentes.
18. Dado uma tela menor, quando a aplicação carregar, então não existe overflow horizontal nos controles principais.
19. Dado a suíte de testes, quando `py -m pytest` for executado, então os testes existentes e novos passam.
20. Dado o relatório de cobertura, quando a suíte terminar, então a exigência configurada de cobertura continua atendida.

## Exemplos de Uso

```python
selected = "Todos"
index_names = ["NDVI", "NDWI", "NDMI"] if selected == "Todos" else [selected]

result = run_multi_analysis(
    geometry=st.session_state.aoi_geometry,
    start_date=start_date,
    end_date=end_date,
    index_names=index_names,
)
```

## Tasks Relacionadas

- SPEC-14-01 a SPEC-14-26 — `tasks-ui-v2-map-first.md`

## Dependências

- `02-earth-engine/spec-busca-imagem.md`
- `03-indices/spec-ndvi.md`
- `03-indices/spec-ndwi.md`
- `03-indices/spec-ndmi.md`
- `04-mapas/spec-selecao-area.md`
- `05-streamlit/spec-app.md`
- `09-mvp/spec-fluxo-completo.md`
- `10-mapas-interacao/spec-mapa-interacao.md`
- `12-interface-resultados/spec-interface-resultados.md`
- `13-cobertura-testes/spec-cobertura-testes.md`
