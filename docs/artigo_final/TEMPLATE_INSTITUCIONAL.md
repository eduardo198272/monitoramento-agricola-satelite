# Padrão definitivo de apresentação

Por determinação expressa do pesquisador, o novo template encaminhado pelo
professor é o **padrão oficial e default deste trabalho**, não uma configuração
provisória. A etapa de acabamento não reabre essa decisão.

## Configuração preservada

A referência operacional é a configuração ativa de `Relatorio_Final.tex`
com `CC-EC_TF-TC.cls`, `autoria.tex`, `normalizacao.tex` e
`figuras_relatorio.tex`. Seus hashes estão em
`evidencias/acabamento_definitivo/template.json`.

- Apresentação dos autores/orientador e filiação conforme a configuração vigente.
- `natbib/dcu`, incluindo as conjunções geradas pelo estilo.
- Abstract, Keywords, Resumo e Palavras-chave.
- Legendas, fontes, notas, tipografia, margens, espaçamentos, duas colunas,
  cabeçalhos, rodapés, logotipo e identidade visual preservados.
- Nenhum retorno automático à bibliografia personalizada, legendas superiores,
  travessões ou outras configurações das antigas rodadas de normalização.
- A opção de coautoria permanece com o valor já vigente. A condição de
  confirmação de coautoria não torna o template provisório e não foi alterada
  nesta etapa de acabamento.

Os apontamentos antigos sobre falta de comparação externa não reabrem a
adoção do padrão informada pelo pesquisador. Esta etapa não declara ter
recebido ou autenticado um pacote independente adicional: preserva os
arquivos ativos identificados no manifesto, sem substituir a classe.

## Manutenção bibliográfica

`referencias_normalizadas.bib` é a base estruturada vigente;
`scripts/preparar_bib_dcu.py` projeta esses dados para
`referencias_institucionais.bib`, lido pelo BibTeX/dcu.
O adaptador não modifica o estilo bibliográfico.

Quando a URL é **exatamente** `https://doi.org/` seguida do DOI cadastrado,
o endereço aparece uma única vez, na saída URL nativa do dcu.
DOI e URL continuam armazenados na base; endereços distintos continuam
apresentados separadamente. Não há deduplicação por aproximação.

As correções de metadados devem ter evidência rastreável e não implicam
mudanças de apresentação ou nova revisão científica.

Mudanças futuras de template exigem nova instrução expressa ou novo modelo
encaminhado pelo professor; não decorrem automaticamente de regras gerais
de normalização.
