# Seleção de área e busca de localidade

Revisão de 15/11/2026. Arquivo de implementação verificado:
`src/app/main.py`, blob Git `630699f63134bcf72b1f70bf467342f38021f7f4`
(`git hash-object src/app/main.py`).

## Falhas reproduzidas

Os seis casos iniciais de regressão falharam antes da correção:

- Aceitar um desenho alterava o script e o hash reais do componente
  streamlit-folium, provocando remontagem e perda do estado de desenho.
- “Alterar área” limpava os resultados, mas preservava a seleção anterior.
- Uma busca bem-sucedida não descartava a área e os resultados anteriores.
- Eventos de exclusão repetidos podiam reaplicar `last_active_drawing` antigo,
  deixando o botão de análise em desacordo com a seleção.
- O payload inicial `all_drawings=None` consumia prematuramente a proteção
  de restauração de uma localização salva.

O comportamento do navegador hospedado ainda precisa ser confirmado após a
publicação da correção; os testes não substituem essa etapa.

## Correções

- Desenhos ativos permanecem no grupo editável do Leaflet. O Python só injeta
  uma geometria inicial ao restaurar uma localização salva, mantendo estáveis
  script e hash durante o desenho e as atualizações normais.
- Alterar a área limpa geometria, métricas, resultados e arquivos preparados,
  fecha o diálogo de salvamento e recria o mapa com uma revisão de chave nova.
- Ao encontrar uma localidade pela lupa, a seleção é limpa, o mapa é
  recentralizado e a análise aguarda um novo polígono válido.
- Busca vazia, sem resultado ou com falha não descarta a seleção anterior.
- Eventos de desenho já processados são ignorados. Uma lista explicitamente
  vazia não pode reativar o último polígono excluído.
- As mudanças de seleção atualizam imediatamente o estado do botão de análise.
  Nenhuma busca ou edição inicia uma análise sem a solicitação do usuário.
- Localizações salvas não são excluídas; a limpeza afeta a área ativa e seus
  resultados, não o repositório de localizações.

## Verificação

```sh
COVERAGE_CORE=ctrace .venv/bin/python -m pytest -q
```

Resultado: **686 testes aprovados**, 100% de cobertura de linhas e ramificações
em `src/app`, sem reduzir a meta. Ambiente: Python 3.14.4, Streamlit 1.55.0,
streamlit-folium 0.25.3 e coverage 7.14.0.

`tests/test_area_selection_regressions.py` contém nove execuções de teste,
incluindo análise individual e multiíndice, segunda análise com a nova geometria,
busca bem-sucedida e malsucedida, remoção e restauração.
O teste de identidade usa o gerador real de mapa e o hash real do
streamlit-folium; substitui o envio ao componente. Os testes de fluxo usam
widgets reais do Streamlit em AppTest com geocodificação, geometria e pipelines
substituídos. Não requerem credenciais ou chamadas remotas.

O registro anterior de 677 testes em `streamlit-cloud-readiness.md` e o artigo
referem-se expressamente ao software `a9a9677`; não representam a contagem atual.

## Conferência manual após publicação

1. Desenhar área A e executar análise.
2. Clicar em “Alterar área”: resultados e polígono anteriores devem desaparecer.
3. Desenhar área B e clicar uma vez em “Analisar área”: executar para B.
4. Pesquisar outro endereço pela lupa: limpar a área e recentralizar o mapa.
5. Pesquisar um endereço sem resultado: preservar a seleção válida.
6. Restaurar uma localização salva, editar e apagar o desenho: não reaplicar
   polígonos antigos durante as atualizações.
