\textsfíFontes mono espaçado)
\begin{ttfamily}
Texto na fonte mono espaçado.
\endíttfamilyY
\begin{center}
\sffamily
texto centralizado e em sans serif.
\end{center}
fittfamily Texto em nomo espaçado
Texto normal.
Fontes sem serifa
Texto na fonte sem serifa.
Fontes mono espaçado
Texto na fonte mono espaçado.
texto centralizado e em sans serif.
Texto em nomo espaçado
Texto normal.
10.2 Seleção de formas e peso das fontes
No LTFEX, usa-se o comando para trocar forma de fontes, tais como negrito, itálico, etc. Usar
comando adequado no LaTeX é importante para automatizar o processo, não somente para
formatação de textos. O texto enfatizado é produzido pelo comando \emph ou pelo ambiente
em. O comando \emph altera entre fonte reto e itálico para destacar palavras tal como termo
que está sendo definido.
O texto em negrito, por sua vez, é produzido pelo comando textbf ou pelo ambiente
bfseries para dar ênfase maior que destaca no meio do texto. Fonte não negrito que é padrão
pode ser especificado pelo comando \\textmd ou ambiente mdseries.
Ainda existem outras formas tal como o comando \textsc e ambiente scshape para
small caps, também conhecido como “versaletes”, comandos \\textit e ambiente itshape
para itálicos. Também existe o comando \\textsl e ambiente slshape que requer cuidado no
uso.
O formato normal padrão é \textup ou ambiente upshape. \eja Exemplo 10.2.
Exemplo 10.2: exl0-series.tex
\textbfíTexto em negrito)
\begin{bfseries}
\egrito como ambiente
\endíb{series}
\begin{em}
Parágrafo enfatizado. \emphíTexto en{atizado dentro dele}
\end{em}
\textscíSmall Caps)
\begin{center}
\bfseries
\egrito e centralizado.
\textmdí{Normal}
\end{center}
Tt{ilscshape Small Caps dentro dos chaves}
Texto normal
Texto em negrito
\egrito como ambiente
Parágrafo enfatizado. Texto enfatizado dentro dele
SMALL CAPS
\egrito e centralizado. Normal
SMALL CAPS DENTRO DOS CHAVES
Texto normal
\ote que os comandos antigos \rm, \\tt, \bf, \sf, \it e \sc para ajuste de fontes não
devem ser usados, pois não podem ser combinados (por exemplo, não é possível produzir
itálico negrito), além de ter de problemas de ajustes de espaçamentos (como a necessidade de
correção de itálico).
10.3 Tamanho das fontes
Tamanho das fontes são especificados também pelos comandos e o LaTeX efetua ajuste auto-
mático em relação ao tamanho padrão.
O tamanho de menor para maior são definidos pelo ambientes
tiny: uy
scriptsize: scriptsize
footnotesize: footnotesize
normalsize: normalsize
large: large
Large: Large
LARGE: LARGE
huge: huge
Huge: Huge
Lembrando que existem comandos correspondentes a cada um dos ambientes, similar a
outros ambientes de fontes. \eja Exemplo 10.3.
Exemplo 10.3: exl0-size.tex
\begin{Large}
Letra grande (2 escalas acima)
\end{Large}
\begin{em}
\small Parágrafo enfatizado com letra pequena (uma escala abaixo)
\endíemY
fifootnotesize Fonte 2 escalas abaixol
Texto normal
Letra grande (2 escalas acima)
Parágrafo enfatizado com letra pequena (uma escala abaixo)
Fonte 2 escalas abaixo
Texto normal
A fonte com todos atributos padrão é especificado no LaTeX pelo comando \textnormal
ou pelo ambiente normalfont, o que permite restaurar a fonte padrão.
10.4 Ajuste de fontes no modo matemático
No ETEX, as especificações das fontes no texto e na fórmula matemática usam os comandos
diferentes. A especificação da fonte no modo matemático corresponde ao \\text??1) são
\nath??(1): \mathrmí), \maths{t}, \mathttit), \mathb{t}, \mathiti), \mathnormalí),
\nathcalí].
O comando \mnathcalf] que não tem correspondente no modo texto, usa a fonte caligráfica,
mas somente em letras maiúsculas.
Os comandos acima não funcionam para símbolos e eles não podem ser combinados. Por
exemplo, wnathbffWmatrm{A}) é mesmo que \nathrmtA)Y.
Assim, \wnathbf não é apropriado para escrever fórmulas em negrito. Portanto, use
\boldsymbol do pacote amsmath para converter parte da fórmula em negrito. \ote que, nem
todo símbolo torna negrito com \boldsymbol. Neste caso, use o comando \pmb que emula o
negrito, escrevendo três vezes com pequeno deslocamento. \eja Exemplo 10.4.
O pacote amssymb dispõe de mais dois fontes bastante usados na matemática que são
\nathfrak e wnathbb. Em geral, usa-se os pacotes ansmath e amssymb quando produz textos
matemáticos. Então acrescente \usepackageTamssymb,amsmath*] no preamble do documento
como no Exemplo 10.4.
Exemplo 10.4: ex10-fontes-mat.tex
\documentclass [12pt,a4paper] {article}
\usepackage [T1] {fontenc}
\usepackage [brazil] {babel}
\usepackageTamssymb,amsmathy
Alusepackage{bm}
\begin{document}
NE \forall x \in \mathbb{R}, mathrm{sen}+ 2(x)+\cos 2(x)=1 N]
Tfibfseries Para $\pmbíi=0X$: Por definição, $0!=1$.
\endí{document}
\x E R, senº(xr) + cosº(x) =1
Para t = O0: Por definição, 0! = 1.
\ote que nomes (ou abreviações) das funções devem estar em fonte romano reto. Assim,
sen foi produzido, usando mathrm.
Para não precisar especificar {imathrmt}, existem comandos para nomes de maioria das
funções matemáticas mais conhecidas.
Nome das funções pré-definidas:
arccos, arcsin, arctan, arg, mod, cos, cosh, cot, coth, csc, deg, det, dim, exp, gcd, hom,
inf, ker, lg, lim, liminf, lim sup, ln, log, max, min, sec, sin, sinh, sup, tan, tanh, Pr.
\ote que o seno em inglês é sine, abreviado para sin que não coincide com o termo usado
no Brasil que é sen. Neste caso, costuma definir o comando para não ficar digitando mathrm
toda hora. De forma análoga, quando o comando produz nome não usual, como no caso
de tangente que é tan no LaTeX, mas costuma usar tg no Brasil, podem ser redefinidos. À
definição e redefinição de comandos estão na Seção 6.1 do Capitulo 6.
Mesmo com o texto em negrito, a equação não ficará em negrito. Para que todas as
equações de um trecho fiquem em negrito, usa-se o ambiente boldmath. Se quer que somente
alguns símbolos (ou um trecho) fique em negrito, usa-se o comando \boldsymbol do pacote
amsbsy que é carregaado pelo amsmath. \ote que \nathbf produz alfabeto em negrito na
fórmula, mas não os símbolos. Uma observação importante é que o comando \boldsymbol
10.4. Ajuste de fontes no modo matemático T7
e o ambiente \boldmath não funcionam para unicode-math do XelTEX/LualTEX, sendo
necessário substituir por \symbf. Para quem usa ou pretende usar XeLaTeX e/ou LuaLaTeX,
uma solução é colora o código
\nakeatletter
\AtBeginDocumentT%
\eifpackageloadedíunicode-math)1t%
\letYWboldsymbolNsymbf
HVWletysymb{\boldsymbol}%
>
\nakeatother
no preâmbulo para que \boldsymbol e \symbf fiquem ativos com ou sem unicode-math
\eja o Exemplo 10.5.
Exemplo 10.5: exl0-negrito.tex
\documentclassí{tarticle}
\usepackage{amsbsy} % para símbolo em negrito
\beginídocument |
Normal
NE arg=b2+0c72 N
Alguns símbolos em negrito
VNE \boldsymbolí{a} 2=b"2+c"2 N
Um trecho em negrito
\VIWboldsymbolía”2=b"2+cP23N]
\end{document}
Normal
Alguns símbolos em negrito
Um trecho em negrito
11. Referências Bibliográficas e Índice Remissivo 78
Capítulo 11
Referências Bibliográficas e Índice
Remissivo
\eremos como produzir índice remissivo e referências bibliográficas no LaTeX.
11.1 . Referências bibliográficas
Uma referências bibliográficas é uma lista de referências externas usadas no trabalho,
comumente apresentado no final do documento. Esta lista é definido pelo ambiente
thebibliography cuja argumento é o elemento com maior largura, para ajustar alinha-
mento de seus itens. Cada item da referência é especificado pelo comando \bibitem cujo
argumento obrigatório é uma chave e argumento opcional é o rótulo a ser impresso no item
(se for omitido, será usado números). Depois segue os dados da referência bibliográfica como
devem ser impressas. Em geral, esta lista será colocado no final do documento (se existir o
Índice remissivo, será antes do índice remissivo). No Exemplo 11.1, o argumento O0PHS25 do
thebibliography será usado para medir o espaço deixado à esquerda dos itens. Além disso,
cada item tem o rótulo (argumento opcional) a ser impresso como nome. Depois vem a chave
que será usado no documento para citar o item especifico.
Exemplo 11.1: ex11-bib.tex
\beginíthebibliography({0PHS25}
\bibitem[GMSO4] fGoossens :2004)
Michel Goossens and Frank Mittelbach
\emphíThe {NWLaTeX} companion (second edition)), Adilson--\esley, 2004.
\bibitem[Tea00] fIndianTUG:2000)
Tutorial Team, \emphíOnline tutorials on {\LaTeX}),
Indian (NTeX) User Group, 2000.
\bibitem[LL94] fLamport : 1994
Leslie Lamport,
\emphfWLaTeX: A Document Preparation System (2nd Edition)), Addison-\esley
Professional, 1994.
\bibitem[OPHS25] foetiker:2025)
Tobias Detiker et. al.,
\emphíThe \ot So Short Introduction to \emphí\LaTeXel), URL: https://ctan.
org/pkg/lshort-english,
2018.
\end{thebibliography}
Referências Bibliográficas
GMS04] Michel Goossens and Frank Mittelbach The LaTeX companion (second edition),
Adilson-\esley, 2004.
Tea00] Tutorial Team, Online tutorials on BTRX, Indian TEX User Group, 2000.
LL94] Leslie Lamport, LaTeX: A Document Preparation System (2nd Edition),
Addison-\esley Professional, 1994.
OPHS?25] Tobias Oetiker et. al., The \ot So Short Introduction to LaTeX2,, URL:
https://ctan.org/pkg/lIshort-english, 2018.
No texto, uma citação da referência bibliográfica é inserida pelo comando {citetchave}
onde chave é a chave colocado no \bibitem.
Se for citar mais de um item, coloque as chaves separadas pela virgula. Também poderá
colocar informações adicionais como parâmetro opcional do \\cite. \eja Exemplo 11.2.
Exemplo 11.2: exl1-cite.tex
Exemplo de referência bibliográfica (veja-\citeílLamport:1994] e \citel
oetiker:2025)).
Para exemplos usando o BibTeX, poderá consultar
\citeíIndianTUG:2000, Goossens:{2004}.
Para recursos avançados de BibTeX, veja o
\ecite[Cap.-13] fGoossens:2004).
Exemplo de referência bibliográfica (veja [LL94] e /{OPHS25}.
Para exemplos usando o BibTeX, poderá consultar [Tea00, GMS04].
Para recursos avançados de BibTeX, veja o [GMSO04, Cap. 13].
11.2 Usando o BibTeX
Checar qual das referências foram usadas e formatar uniformemente de acordo com as exigên-
cias do editor é uma tarefa difícil. Para automatizar este serviço, podemos usar o BibTeX que
é uma ferramenta especialmente desenvolvida para manipular referências bibliográficas. Os
editores costumam deixar um arquivo de estilo próprio para BibTeX e usando ele, o BibTeX
formatará automaticamente as referências bibliográficas de acordo. Outra coisa importante
que o BibTeX faz é checar quais dos itens foram usados e imprimir somente as referências
citadas no texto.
Para usar o BibTeX, prepara o arquivo de referência bibliográfica separado, com extensão
.bib, que contém informações das referências. Em geral, costumamos usar os aplicativos
gráficos tal como aplicativo gratuito e multi plataforma jabref (http://www.jabref.org/)
para editar o arquivo de BibTeX, mas também pode ser editado manualmente.
Aqui, vamos ver como preparar manualmente o arquivo .bib. \eja o Exemplo 11.3 para
ver como deve ficar o arquivo .bib.
Exemplo 11.3: exl11-bibtex.bib
OcommentíNo estilo antigo de BibTeX que não tem suporte ao campo 'url' (
endereço de internet), coloque o endereço da internet no campo 'note'r
Ostringí(AW="Adilson--\esley"y
OstringíTUG="fWTeX+ User Group")
ObookíLamport:1994,
author=(Leslie Lamport),
title=({NLaTeX}, A Document Preparation System (2nd Edition)),
publisher=AW,
address =(Reading, MA),
year=1994
1”
ObookíGoossens :2004,
author=(íMichel Goossens and Frank Mittelbachk,
title=(The {NLaTeX} companion (second edition)),
publisher=AW,
address =(Reading, MA),
year=2004
s
Obookíoetiker:2025,
author=(Tobians Detiker and Hubert Partl and Irene Hyna and Elisabeth
Schlegl],
title=(The \ot So Short Introduction to fNWLaTeXeí))),
publisher=CTAN,
url=fhttps://ctan.org/pkg/lshort-english,
year=2025
D”
ObookíIndianTUG:2000,
author=(Tutorialí XTeam),
title=fOnline Tutorials on {NLaTeX}),
publisher="Indian " H TUG,
url = fhttp://www.tug.org/tutorials/tugindia/,
year=2000
s
CarticleíMertz:2009,
author=(Andrew Mertz and \illiam Slough),
title=(A TikZ tutorial: Generating graphics in the
spirit of {NTeX}),
journal=TUGboat,
url=fhttp://www.tug.org/TUGboat/tb30-2/tb95mertz.pdf)
volume=30,
number=2,
year=2009
i
O comando de BibTeX inicia com “O” seguido de nome e seus dados entre chaves. Os
dados são listas separados pela virgula na forma forma “chave=dado”, onde dado pode ser
delimitado por aspas ou chaves.
Ocommaent é para acrescentar comentários. A parte do Gcommentí* será ignorado.
Ostring permite definir abreviaturas. No começo do arquivo, foi definido as abreviaturas
AW para “Adilson-\esley” e TUG para “{TEX} User Group” para facilitar a digitação de dados.
\ote que, comandos de TEX devem ficar delimitados pelas chaves extras no arquivo de BibTeX
para evitar alterações. Da mesma forma, abreviaturas que devem manter maiúsculas também
devem ficar entre chaves.
Depois encontra o Gbook que especifica que é dado de um livro. Entre chaves, estão os
dados do livro tais como título, autor, etc, onde cada campo é separado da outra pela virgula
e dados do campo são delimitados pelos chaves ou aspas. \ote que o primeiro elemento de
Obook é uma chave a ser usado dentro do documento pelo comando \\cite e é único que
não é da forma campo = dado do campo. Tanto aspas como chaves podem ser usados para
delimitar dados do campo, mas se dado for uma única palavra como o ano, não precisa do
delimitador.
Relembrando que os comandos de TEX devem ficar delimitados por chaves, o que indica
ao BibTeX para não alterar esta parte (como converter entre maiúsculo e minúsculo). \ote
o uso da abreviatura AW em alguns pontos do documento (sem colocar delimitadores). Esta
abreviatura foi definido no começo do arquivo e será substituído automaticamente pelo seu
valor “Adilson-\esley” pelo BibTeX.
No publisher="Indian "t TUG, “%” faz a concatenação de dois strings Indian, e o
stringTUG que é (NTeX) User Group.
Quando tem vários autores, separe os nomes com “and” que o BibTeX vai entender. Quando
nome ou sobrenome é uma palavra composta, coloque í ) (espaço entre chaves) em vez de
espaço, como em author="Paulo da Silva Gonçalvesí \Junior". Outra forma é usar o
formato “sobrenome, nome” como em author="Gonçalves Junior, Paulo da Silva". No
exemplo, “Tutorial Team” no campo do autor foi escrito desta forma. Parte do campo que
não pode ser retocado (alterar entre maiúsculo e minúsculo, abreviar, etc) como no caso
de comando de LaTeX, coloque entre chaves extras. No caso do sobrenome dos autores,
é recomendável não colocar entre chaves, pois a conversão automática entre maiúsculo e
minúsculo será desativada.
Tendo o arquivo .bib pronto, efetuamos as citações como no caso anterior.
Agora, no final do arquivo, onde colocamos o ambiente thebibliography, substituímos
por
\bibliographystyleí[estilo bib]l>
\bibliographyfexiil-bibtex)
onde [estilo bibl] é o estilo usado para formatar as referências bibliográficas tais como
plain, alpha, etc. e ex1i-bibtex é o nome do arquivo de BibTeX (extensão bib) sem
extensão. Quando tiver mais de um arquivo, separe os nomes pela vírgula.
Agora execute o 1TEX, BibTeX e LaTeX novamente. Em geral, os editores especializados
para ITFEX tem os botões ou menus para rodar o BibTeX, além dos botões de compilar
(executar o LaTeX).
Ao executar BibTeX, será gerado a saída das referências bibliográficas somente com itens
citados. Por exemplo, para as citações do Exemplo 11.2, o artigo com chave Mertz:2009 será
ignorado por não estar citados.
Para mudar a formatação das referências, é só alterar o estilo em \bibliographystyle
e executar o BibTeX e LaTeX novamente. Os estilos básicos são: plain (rótulo numérico),
unsrt (similar a plain, mas sem ordenar — na ordem que {oi citado}, alpha (rótulo pelo
sobrenome e ano), abbrv (similar a plain, mas mais compacto), amsplain (estilo plain do
AMS), amsalpha (estilo alpha do AMS).
Além desses, existem vários outros estilos, dependendo da instalação de cada sistema TEX
em uso.
Se o editor dispõe de arquivos de estilo para BibTeX (com extensão bst), deixe este
arquivo junto com arquivo tex e no \bibliographystyle, passe o nome deste arquivo .bst
sem a extensão. Se arquivo é meuart .bst, o estilo é meuart.
O BibTeX atual suporta a acentuação direta sem problemas (o que não era suportada até
algum tempo atrás), mas não há suporte aos caracteres além do equivalente ao latin1. Para
solucionar este problema, costuma usar o BibLaTeX.
Quando o editor exige um padrão diferente do disponível e não fornece o arquivo de
estilo para BibTeX, podemos contornar o problema da seguinte forma. Primeiro termine o
artigo ou livro com citações necessárias e usando um estilo mais próximo do exigido. Depois
rode o BLaTeX e BibTeX. O BibTeX gerará um arquivo com extensão bbl, com o mesmo
nome do arquivo tex. Este arquivo .bbl contém o ambiente thebibliography com itens de
bibliografia já formatada. Copie ele para documento original onde está o
\bibliographystyleí[estilo {bib}
\bibliographyí[arquivo bib]>
e efetue alterações manualmente.
Não esqueça de comentar o
\bibliographystylefí[estilo {bib}
\bibliographyí[arquivo bib]y)
Para especificar dados no arquivo de BibTeX, além da categoria Obook (livro), existem
muitas especificações de documentos tais como Garticle (artigo), Omanual (documentação
técnica), Gphdthesis (tese de doutorado), etc, uma para cada categoria. Se não enquadrar
em nenhuma das categorias disponíveis, use o Omisc (diversos).
A lista destas categorias e seus campos estão resumidos na tabela a seguir.
tipo bibtex necessário opcional
artigos Carticle auther, title, jour- | volume, number, pages, month,
nal year note
tese (doutorado) Ophdthesis author, title, | type, address, month, note
school, year
dissertação — (mes- | Gmastersthesis | author, title, | type, address, month, note
trado) school, year
anais de conferên- | QOGproceedings title, year editor, volume, number, series,
cia address, month, organization,
publisher, note
artigo no anais de | Ginproceedings | author, title, book- | editor, volume, number, series,
conferêcnia title, year pages, address, month, organiza-
tion, publisher, note
mesmo que inpro- | Gconference author, title, book- | editor, volume, number, series,
ceedings title, year pages, address, month, organiza-
tion, publisher, note
livro Obook author ou editor, | volume, number, series, address,
title, publisher, | edition, month, note
year
11.3. Índice remissivo
quase livro (notas | Abooklet title author, howpublished, address,
e simlares) month, year, note
parte de um livro | Ginbook author ou editor, | volume, number, series, type, ad-
title, chapter ou | dress, edition, month, year
pages, publisher,
year
parte de uma cole- | Gincollection author, title, bo- | editor, volume, number, series,
ção oktitle, publisher, | type, chapter, pages, address,
year edition, month, note
manual Gmanual title author, organization, address,
edition, month, year, note
relatório técnico Otechreport author, title, insti- | type, number, address, month,
tution, year note
não pblicado Gunpublished | author, title, note | month, year
outros Qmisc nenhuma author, title, howpublished,
month, year, note
O texto sem estar com especificação que inicia com “O” será ignorado pelo BibTeX e funci-
ona como comentário. Mas existe o especificador G6comment especial para inserir comentários
para fins de organização.
Como existem muitas categorias e cada categoria tem campos diferentes a ser preenchidos,
editar o arquivo de BibTeX manualmente não é muito simples. Assim, costumamos usar
os aplicativos próprios para isso. Como foi dito antes, um desses aplicativos é o jabref
(http://www.jabref.org/) que funciona em quase toda plataforma e é gratuito.
11.3 Índice remissivo
Para criar o índice remissivo, usa-se o pacote makeidx e o comando \vmakeindex no preamble
do documento para ativar o seu uso.
Para acrescentar itens no índice remissivo, usa-se o comando \indext*, mas lembre-se de
não colocar espaços entre palavra referida e o comando. Para colocar Índice remissivo com
“m
sub-entrada, usa-se o para separar entrada e sub-entrada, mas evite espaços nos lados de
“” (qualquer espaço extra pode causar confusões na organização do índice remissivo).
As vezes, é necessário usar uma “chave” para classificar os itens.
Isto ocorre quando usamos símbolos matemáticos, aspas, ou outros caracteres especiais,
formatação de caracteres, etc. Sem a “chave” de classificação, nakeindex pode classificar
usando o que está escrito, o que nem sempre corresponde a posição correta. Para resolver
este problema, usa-se o \index{chaveCitem}. Por exemplo
Ps ítens em negritoVlindexíitem em negritoOltextbfiítem em negritol),
itens com aspasVWindexíitem com aspasO” ítem com aspas'') e símbolos \indexfí
simbolosCís{mbolos}), etc podem ser colocados com ordenação correta.
inserem entradas em negrito e item com aspas classificado corretamente. Lembre também
que as letras acentuadas costumam vir na posição diferente das não acentuadas. Neste caso
também poderá usar a chave para colocar na posição correta. \eja o Exemplo 11.4.
Exemplo 11.4: exl1-index.tex
Podemos usar índice remissivoVlindexííndice remissivol] com sub-entradaVindexí
índice remissivo!sub-entrada]l.
Também podemos usar *"chave'' para classificar os itens, como itens em
negritolindexíitem em negritoOltextb{iitem em negrito}), itens com aspasy
indexíitem com aspasO” item com aspas'') e símbolos como $\alpha$\indext
alfaC$\alpha$).
Também podemos usar item e enumeração em negritoVlindexíitem e enumeração em
negritoOltextbfíitem e enumeração em negrito)|{textbf}
\printindex % colocar indice remissivo (glossário) aqui.
No corpo do documento, terá nenhuma diferença visual em ter o \indexí] e logo, a sua
saída foi omitida.
Podemos especificar sub-entrada com chaves como em
itens em negrito com sub-entradaVWindextitemOltextbf{item}! textbflem negrito
HNWtextbfícom sub-entrada)).
“
Observe a ordem que usa o “O” e na especificação de itens com chave e subentrada.
Para indicar a ocorrência num trecho, usa-se o \indexfitem|( para iniciar e
\indexíitem|) para finalizar.
Quando um item referê-se ao outro, usa-se o \indexíítem|seetreferência)) com em
grossárioVindexígrossário|seefíndice remissivo)).
Para mudar a fonte usada na enumeração da página, coloque a especificação após “|” ou
Ivv
“|(” dependendo de ser página ou trecho como em
Índice com paginação em negritoVindexíitem e enumeração em negritoOtextbft
ítem e enumeração em negritol|textbf).
Para colocar o Índice remissivo gerado, usa-se o comando \printindex.
Finalmente, para produzir o índice remissivo, deverá executar LaTeX, makeindex e ETEX
novamente. Os editores especializados para LaTeX costuma vir com botão ou menu para
chamar o makeindex.
\ote que, por padrão, o processador makeindex aceita somente até 3 níveis de sub-entrada.
Caso queira mais níveis, poderá optar por usar xindy em vez de makeindex com configuração
adequada. O xindy suporta indexação internacional, além de diversas configurações, entre eles,
aumentar o nível de sub-entradas via arquivo de configuração. \ote que o desenvolvimento do
xindy está parado. Assim, para índice remissivo internacional, é recomendado usar o xindex
ou upmendex em vez de xindy.
No entanto, dependendo do editor, pode não vir com botão para executar o xindex ou
similar, o que requer configuração manual do editor.
O índice remissivo do Exemplo 11.4 ficaria como segue
Indice Remissivo
Índice remissivo, 1
sub-entrada, 1
a, 1
“item com aspas”, 1
item em negrito, 1
item e enumeração em negrito, 1
\ote que O, !, | e " tem significados na entrada de índice remissivo. Para colocar estes ca-
racteres na entrada de Índice remissivo, coloque " antes dele. Por exemplo, \indexí"Gauthor+)
insere “Oauthor” na entrada de índice remissivo.
