# Acabamento final — template definitivo

O padrão de apresentação indicado pelo pesquisador foi mantido sem alteração
dos arquivos de template. O escopo foi exclusivamente bibliográfico e de
validação, sem nova normalização geral ou reestruturação científica.

## Arquivos

- `../../Relatorio_Final.pdf`: PDF recompilado.
- `../../TEMPLATE_INSTITUCIONAL.md`: registro do padrão definitivo.
- `../../AUDITORIA_ABNT.md`: decisões e sete datas ainda sem confirmação exata.
- `template.json`: hashes da configuração preservada.
- `bibliografia.json`: alterações de metadados e supressões de repetição visual.
- `consultas.json`: fontes consultadas e limitações, sem publicar emails de
  colaboradores ou respostas completas dos repositórios.
- `compilacao.json`, `.log`, `.blg` e `.bbl`: compilação efetiva com dcu.
- `preservacao.json`: comparação do conteúdo científico, imagens e dados.
- `inspecao_visual.md`, `renderizacao.json`: leitura individual das páginas.
- `antes_depois.diff`: comparação exclusiva desta etapa.

Backup anterior: `/tmp/opencode/acabamento-definitivo/antes/`.
As fontes completas consultadas ficaram no cache privado
`/tmp/opencode/acabamento-definitivo/fontes/`.

## Critérios bibliográficos

DOI e URL idênticos são mostrados uma única vez pela saída URL nativa do dcu;
os dois campos continuam presentes na base. DOI e URL diferentes não são
unificados. Não houve edição do `.bst`.

As datas 2026 acrescentadas a três fontes decorrem de commits datados dos
arquivos de documentação, conferidos contra seu conteúdo atual. Não são datas
de acesso disfarçadas de publicação. A hipótese de preencher as demais fontes
com um ano genérico foi rejeitada por falta de evidência.

O adaptador permanece `../../scripts/preparar_bib_dcu.py`. A base estruturada
é `../../referencias_normalizadas.bib`; a projeção ativa é
`../../referencias_institucionais.bib`. Os geradores e configurações de
normalização anteriores não foram reativados.

Sem alteração científica, código funcional, dados originais, commit ou push.
