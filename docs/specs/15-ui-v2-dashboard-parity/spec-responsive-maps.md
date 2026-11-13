# Spec: SPEC-15-08 — Responsividade e altura dos mapas

## Objetivo

Manter mapas de seleção e temático utilizáveis em desktop, tablet e celular,
reduzindo sua altura em telas estreitas sem afetar gráficos ou outros componentes.

## Implementação

- Definir altura-base de 520 px nos pontos de renderização Python dos dois mapas.
- Preservar essa altura após reruns provocados por seleção de área e pelo clique em
  **Analisar**; o mapa de seleção não pode colapsar quando os resultados aparecem.
- Em viewports até 768 px, definir altura do iframe de mapa em 440 px.
- Em viewports até 480 px, definir altura do iframe de mapa em 360 px.
- Restringir as regras ao iframe dentro de `stCustomComponentV1`, que hospeda os
  componentes de mapa; manter largura fluida e sem overflow horizontal.
- Remover a regra móvel genérica atual que altera altura de todo `stIFrame`.
- Adicionar testes unitários de configuração Python e regras CSS; fazer validação
  visual manual nas larguras 1440, 768 e 390 px.

## Critérios de aceite

1. Seleção e mapa temático usam 520 px como altura-base.
2. Após clicar em **Analisar**, o mapa de seleção mantém sua altura e o mapa temático
   é renderizado com altura integral; nenhum dos dois vira uma faixa estreita.
3. Wrapper e iframe dos mapas preservam altura mínima e recebem alturas de 440 px e
   360 px nos breakpoints definidos.
4. Gráficos e iframes não relacionados a mapas não têm a altura alterada pelas regras.
5. Mapas ocupam até 100% da largura disponível, sem overflow horizontal.
6. Seleção de polígono, controles e legenda permanecem acessíveis.
7. `python -m pytest tests/ --no-cov`, `git diff --check` e resposta HTTP 200 passam.

## Observação de validação

CSS é responsivo por viewport, enquanto Streamlit recebe uma altura numérica inicial
no servidor. Confirmar visualmente que a altura CSS aplicada ao iframe respeita os
breakpoints e não deixa espaço excedente no wrapper do componente.
