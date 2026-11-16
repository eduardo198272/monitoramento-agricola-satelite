# Relatório de compilação — quinta rodada

**Resultado técnico:** compilação concluída, **32 páginas Letter**, duas colunas.
Sem erros de compilação, referências/citações indefinidas, `Overfull` ou
`twocolumn too tall`. A contagem automática do cabeçalho é **1–32**.

```sh
/tmp/opencode/tectonic -X compile Relatorio_Final.tex \
  --outdir /tmp/opencode/quinta-rodada/build \
  --keep-logs --keep-intermediates
```

Executado em `docs/artigo_final/`. O PDF inspecionado foi copiado para
`docs/artigo_final/Relatorio_Final.pdf`. Hash e dimensões constam de
`compilacao.json`, `pdfinfo.txt` e `manifesto_entrega.json`.

## Avisos remanescentes

- Caixas `Underfull`, especialmente em colunas estreitas, tabelas e bibliografia.
- Substituições de tamanhos das fontes matemáticas carregadas pela classe.
- Aviso de compatibilidade entre epstopdf e o driver XeTeX.

Não foram ocultados avisos para simular uma compilação limpa. A ausência
de excesso de caixa não é apresentada como ausência de toda limitação visual.
Ver `inspecao_visual.md`, em especial as páginas 10 e 18–21.

## Verificações adicionais

- 63 chaves bibliográficas preservadas; 54 citadas e nove não citadas.
- Geração de bibliografia distinta de `dcu`, com rótulos natbib coerentes.
- Corpos tabulares e arquivos CSV/JSON quantitativos idênticos à quarta rodada.
- 14 expressões numeradas em oito ambientes matemáticos preservadas literalmente.
- Nove testes da rotina de análise aprovados: `9 passed in 0.40s`.
  Não representam reexecução dos 710 testes da aplicação.
- `git diff --check` passou excluindo os SVGs gerados na rodada anterior,
  que já continham espaços finais; nenhum SVG foi alterado nesta rodada.

**Aceite normativo/institucional:** pendente, conforme `../../AUDITORIA_ABNT.md`.
