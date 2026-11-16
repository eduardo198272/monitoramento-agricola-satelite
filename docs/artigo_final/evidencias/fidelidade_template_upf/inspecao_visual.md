# Inspeção visual — fidelidade ao template UPF

Foram examinadas individualmente as **32 páginas** do PDF, renderizadas
por Poppler (`pdftoppm -scale-to 1500`). As páginas 30–32 foram reexaminadas
após a projeção final dos metadados para o dcu. As demais imagens permaneceram
idênticas às já inspecionadas, conforme os hashes do manifesto.

Também foram examinadas as páginas 1 e 2 de uma **prévia isolada de coautoria**,
sem ativar essa opção no documento entregue. Não houve aprovação visual humana
ou prova física de impressão.

| Página | Conferência |
|---|---|
| 1 | Logotipo e identificação institucional preservados; títulos PT/EN, autor e nota de filiação sem corte; Abstract/Keywords antes de Resumo/Palavras-chave; números e descritores intactos. Nenhum ajuste novo de fonte ou espaçamento entre letras. |
| 2 | Duas colunas, objetivos, recuos e cabeçalho nativos; citações novamente compostas pelo dcu, sem sobreposição. |
| 3 | Hierarquia e citações com a conjunção nativa `and`; caixa mista; equação (1) legível. |
| 4 | Equações (2)–(3) e termos dos índices preservados; datas incertas continuam explícitas. |
| 5 | SDD e fontes científicas preservados; chamadas narrativas e parentéticas do dcu sem indefinições. |
| 6 | Figuras 1–4 com legendas inferiores centralizadas e dois-pontos; fontes/notas associadas; valores didáticos intactos. |
| 7 | Trabalhos relacionados e início dos métodos, sem alteração da estrutura científica. |
| 8 | Tabela 1 com identificação superior e fonte/nota inferiores; equações (4)–(6) e filtros preservados. |
| 9 | Figura 5 com legenda inferior; equações (7)–(9) preservadas; sem corte de fórmulas ou identificadores. |
| 10 | Figura 6 e equações (10)–(12); permanece o espaçamento vertical elástico da classe, sem tentar compensá-lo por fontes/margens menores. |
| 11 | Métodos do questionário com 32 respostas e distinção de ausências; referências recompostas, texto intacto. |
| 12 | Figura 7 com legenda/fonte inferiores; arquitetura, consentimento e limites preservados. |
| 13 | Tabela 2 com fonte inferior, bordas abertas e conteúdo dos componentes mantido. |
| 14 | Figuras 8–9, legendas e fontes inferiores; diagramas preservados; branco da página de figuras mantido. |
| 15 | Consulta à grade e equações (13)–(14); nenhuma remoção para ajustar a contagem de fórmulas. |
| 16 | Figuras 10–11, legendas e fontes; identificadores e exportações mantidos. |
| 17 | Apresentação da plataforma, referências às capturas e limites narrativos intactos. |
| 18 | Figuras 12–13 com fontes; capturas escuras intactas, sem alteração artificial de contraste ou números. |
| 19 | Figura 14 e seus três painéis; legenda, fonte e nota inferiores associadas. |
| 20 | Figuras 15–16, fontes e ressalva do enquadramento original da série preservados. |
| 21 | Figuras 17–18; relatório exportado continua ilustrativo; textos pequenos das capturas permanecem limitação dos originais. |
| 22 | Figura 19 com telas móveis, QR Code, fonte e nota; página de ilustração sem corte. |
| 23 | Resultados computacionais e demonstração; números, precisão e unidade de radiação preservados. |
| 24 | Figura 20 com legenda inferior e fonte; distribuições e denominadores de 32 respostas mantidos. |
| 25 | Figura 21 e tabela 3; legenda inferior na figura, superior na tabela; fontes/notas presentes; valores e quartis intactos. |
| 26 | Figura 22, fonte/nota inferiores e rótulos originais preservados. |
| 27 | Tabela 4, excertos e discussão; frequências e trechos literais sem alteração. |
| 28 | Tabela 5 e discussão, sem alteração dos objetivos/evidências. |
| 29 | Limitações e conclusão com a mesma pesquisa de 32 respostas; sem acréscimo de resultados. |
| 30 | Declaração de IA intacta; início da bibliografia no dcu, com recuo nativo, títulos por tipo e DOI/URL/acessos preservados. Siglas SI e SDD permanecem em caixa correta. |
| 31 | Continuação da bibliografia; dados eletrônicos e localizadores preservados. A referência de Parnas continua na página seguinte, como permitido pela composição nativa, sem perda de texto. |
| 32 | Final das referências, sem corte de itens; versões, identificadores eletrônicos e autores mantidos. GIS e NDMI protegidos contra conversão indevida de caixa no título. |
| Prévia 1 | Dois nomes, indicador 1 comum e filiação exclusivamente institucional; metadados PDF com ambos; resumos cabem na primeira página. Apenas teste, não confirmação de coautoria. |
| Prévia 2 | Cabeçalho “Hoppen e Rieder”, título corrente e número de página sem sobreposição. |

## Conclusão e limites

- Compilação sem erros, citações/referências indefinidas, `Overfull` ou
  `twocolumn too tall`.
- A saída do dcu foi efetivamente examinada, não apenas selecionada na fonte.
- Não se alteraram pixels, gráficos, tabelas numéricas ou fórmulas.
- A legibilidade dos textos pequenos das capturas continua condicionada
  aos arquivos originais e a uma eventual prova de impressão.
- Os três trabalhos externos indicados não puderam ser inspecionados:
  o repositório entregou verificação antirobô. Este relatório não atesta
  equivalência visual com documentos que não foram obtidos.
