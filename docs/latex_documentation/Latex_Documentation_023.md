G.4. Alguns convertores 323
acordo com a filosofia do HTML e consequentemente, não produz documento “fiel” ao original.
Ele particiona documentos grandes em pedaços menores e cria recurso de navegação, mas isto
pode ser desativado, se desejar. O HTML gerado por LaTeX2HTML acomoda bem em maioria
dos navegadores, o que tornou a escolha preferida dos desenvolvedores da \eb, enquanto que
TeX4ht tornou a preferência para converter documentos LaTeX em outros formatos. \ote que
o Tex4ht já vem com muitas distribuições LaTeX, incluindo o MikTeX para MS \indows. Além
disso, ele permite converter para formato do Libre Office, sendo que TeXMaker e LyX usam
ele para gerar arquivo de Libre Office.
Um problema do TeX4ht é usar o formato intermediário em DVI, o que dificulta o uso de
imagens em pdf/jpg/png por precisar ser convertidos em eps. À solução para isso é usar
conversores modernos tais como LaTeXML e lwarp que apresentam filosofia similar ao TeX4ht,
de produzir documentos parecidos com a saída do LaTeX. O LaTeXML é implementado em
perl e usa o PDF e XML como o arquivo intermediário, eliminando o problema do TeX4ht. Ele
gera tanto o HTML quanto o epub com boa qualidade, permitindo usar MathML para equações.
A conversão é feito pelo comando latexmlc.
O lwarp é conjunto de pacotes de LaTeX que converte LaTeX para HTML5. As equações e
figuras ficarão no formato SVG por padrão, mas pode usar MathJaX para equações. Ele não
suporta MathML para equações ainda (2024). O script auxiliar lwarpmk é usado na conversão
automática das equações e imagens para SVG.
\ote que muitos editores de escritório como MS Office e LIbre Office permite importar
arquivos HTML.
\riter2LaTeX
site: http://writer2latex.sourceforge.net/
Convertor do editor de texto do Open Office/Libre Office para LaTeX/XHTML+MathML.
Ele pode ser usado como plugin ou pelo comando de linha. Dependendo da instalação do
Libre Office, já vem instalado.
Excel2LaTeX
site: https: //www.ctan.org/pkg/excel2latex
Excel2LaTeX é um macro para MS Excel, para converter planilha do MS Excel para tabela
do LaTeX. Maioria das formatações tais como espacificação das fontes (negrito, itálico, etc),
bordas, celula mescrada, etc são mantidas. Para instalar, copie o arquivo excel2latex.xla
para pasta do MS Office e dê um double click sobre ele. O MS Excel abre o arquivo e
perguntará se vai executar o "macro”. Responda ”sim”e a instalação estará completa. No
MS Excel, selecione a região desejada da tabela e clique em “convert table to LaTeX” (ou
“ferramentas->convert table to LaTeX”). O resultado pode ser copiado para “clipboard” ou
salvo no arquivo.
G.5. Outras ferramentas 324
Calc2LaTeX
site: http://calc2latex.sourceforge.net/
Macro para Open Calc (do Open O{fice} para gerar tabelas de LaTeX a partir da planilha.
Não há atualização recente.
Pandoc
site: https: //pandoc .org/
O Pandoc é um convertor de formato de documentos que suportam diversos formatos,
entre eles, o LaTeX.
G.5 Outras ferramentas
jabref
site: http://jabref.sourceforge.net/
Se usar o BibTeX, é recomendável que use este editor para editar arquivo ”.bib”. Muitos
usuários de LaTeX deixam de usar o BibTeX devido ao chatice de editar o arquivo do BibTeX
que usa o sintaxe diferente do LaTeX, mas com o jabref, as coisas mudam.
Ele também suporta o BibLaTeX (para isso, deverá usar o modo BibLaTeX). Também é
aconselhável usar a codificação utf-8 quando usa o modo BiblTFX para evitar problemas
com caracteres acentuados.
jipdftweak
site: http://jpdftweak.sourceforge.net/
Esta ferramenta é importante para ajustes finais do documento PDF. Permite dividir ou
juntar PDF, trocar ordem das páginas, alterar o tamanho de papel, ajustar o tamanho e
posição do corpo do texto, colocar várias páginas em uma, etc. O domínio do jpdftweak
é útil para quem precisa manipular PDF pronta, como preparar para edição. Para elaborar
poster, poderá diagramar no papel de tamanho 1/4 (1/2 de escala em cada dimensão) com
letra 12pt e ao finalizar, poderá usar o jpdfTweak para ampliar no tamanho normal. Com
o fator de ampliação 2x, a letra ficará com 24pt, apropriado para posters. Com isso, poderá
criar posters sem precisar de pacote ou truque especial. Para quem quer um aplicativo
de comando de linha para processamento em lotes, o Multvalent (https://multivalent.
sourceforge.net/) pode ser interessante, mas ele não está sendo atualizado por muito
tempo. Assim, poderá optar pelo PSPDFUtils (https://github.com/rrthomas/psutils)
e/ou pdfjam (https://github.com/pdfjam/pd{jam}. Para adicionar/remover senhas ou
similares, o PDFTK (https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/ — GUI e
linha de comando) e qpdf (https://github.com/qpdf/qpdf — comando de linha) podem ser
usados. Para recorte rápido do arquivo PDF, use o pdfarranger/PDFSAM comentado a seguir.
G.5. Outras ferramentas 325
pdfarranger (linux, windows e mac OS)
site: https : //github.com/jeromerobert/pdfarranger
É um “fork” do pdfshuffler (ttp://sourceforge.net/projects/pdfshuffler/) que
era somente para linux. Usado para manuseio dos arquivos em PDF. Usando interface
amigável, poderá concatenar arquivos, eliminar páginas, reordenar páginas, rotacionar, etc.
Não é potente como o jPDFTWeak, mas para manuseio simples, ele é prático. Caso não
tiver disponível na sua plataforma, existe o aplicativo implementado em java PDFSAM (http:
//www.pdfsam.org/) que efetua tarefas similares.
xournal++ e jaurnal
sites:
xournal++: https://github.com/xournalpp/xournalpp
jaurnal: http: //www.dklevine.com/general/software/tc1000/jarnal.htm
O xournal++ é uma reimplementação do xournal (http://xournal.sourceforge.net/)
que é um caderno eletrônico, mas pode abrir um arquivo PDF, escrever sobre ele e exportar
como um novo arquivo PDF. Este recurso é interessante para corrigir trabalhos. Se tiver uma
mesa digitalizadora, poderá efetuar correção tão rápida como corrigir sobre texto impresso.
Ele também é usado como losa digital para aulas online (Para losa digital, o Open Board
disponível em https://openboard.ch/index.en.html também é interessante).
O jaurnal é similar ao xournal, mas é implementado em java. O xournal++ é mais
recomendado.
pympress
site: https: //github.com/Cimbali/pympress
O pympress é um visualizador de PDF multi plataforma para apresentação, que permite
usar o modo de tela dupla, exibindo o slide de apresentação em uma tela (do projetor) e notas
do slide correspondênte na outra (do notebook). O beamer permite configurar a saída para
produzir PDF compatível com o pynpress. O pympress permite também destacar (marcar)
o texto durante a apresentação.
Scribus
site: http://www.scribus.net/
O Scribus é um aplicativo para elaborar revistas, jornais, posters, etc como o Microsoft
Publisher (comercial). O Scribus permite inserir “caixa de LaTeX”, o que facilita o desen-
volvimento de material científico. Apesar do usuário de LaTeX costumam querer diagramar o
poster de apresentação no LaTeX, se precisar produzir poster, folhetos, etc com frequência, é
aconselhável aprender a usar o Scribus.
G.6. Algumas alternativas a LaTeX 326
Alguns serviços web
* http://detexify.kirelabs.org/classify.html reconhecimento de símbolos BTFX a
partir do traço manual. Para versão offline para ser instalado no computador, veja https:
//github.com/zoeyfyi/TeX-Match.
* https://huggingface.co/spaces/breezedeus/Pix2Text-Demo Converte imagem em
texto com fórmula LaTeX. É serviço online baseado no aplicativo de comando de li-
nha pix2tex disponível em https://github.com/breezedeus/pix2text que é de código
aberto. \ote que existem diversos serviços online deste tipo, mas muitos não são baseados
nos aplicativos de código aberto, ou nem gratuitos. Um desse serviços gratuito útil é
https://webdemo .myscript.com/views/math/index.html que reconhece a fórmula es-
crito a mão e cria código LaTeX e MathML.
* http://www.imagemagick.org/MagickStudio/scripts/MagickStudio.cgi Serviço de
conversão do formato de imagens.
* https://pt.overleaf.com/ Serviço de web com ambiente LaTeX. Para uso pessoal é
gratuito. Alguns outros serviços similares são https://www.texpage.com/, https://
papeeria.com/ e https://www.authorea.com/. Em geral, o plano gratuíto destes serviços
limita o tempo e/ou número de compilação, ou similar. Portanto, o ideal é ter o TEX
instalado no seu próprio computador.
* https://www.hipdf.com/, https://www.sejda.com/pdf-editor, https://www.
pdfescape .com/ Alguns dos diversos serviços gratuitos para editar PDF online.
\ote que o central de repositório do (La)TEX é o CTAN. Portanto, se estiver procurando
algo, pode dar olhada primeiro no CTAN (https://www.ctan.org/).
G.6 Algumas alternativas a ATEX
O ELaTeX é versátil e potente, porém a parte de programação (como desenvolvimento de
pacotes e ajuste mais avançada de configurações) não é muito fácil por precisar programar
em TEX, o que apresenta a forma difernte das linguagens de programação usual. Apesar de
LuaTEX permitir programar na linguagem Lua, ele ainda não é adotado como TEX padrão
(2025). Também existe caso na qual pretende elaborar documento mais rapidamente sem
muita sofisticação, como efetuar anotações e similares. Nestes casos, poderá procurar por
outras alternativas, para ser usado em paralelo, ou até mesmo substituir o LaTeX.
MarkDown
O MarkDown (https://en.wikipedia.org/wiki/Markdown) é um dos formatos de arquivo
texto que pode ser lido diretamente, mas que também pode ser convertidos em HTML, pdf,
G.6. Algumas alternativas a LaTeX 327
ou similar de forma rápida e simples. Este formato é popular no arquivo “readme” usado
para descrição do programa ou similar, blogs, anotações, etc (o Pandoc suporta fórmulas
matemáticas no modo TEX). Se não quer usar aplicativos do comando de linha como o
pandoc, poderá usar o GhostWriter (https://ghostwriter.kde.org/) que é um editor de
MarkDown, capaz de visualizar o resultado automaticamente em paralelo, assim como efetuar
conversão pelo menu.
typst
O typst é um sistema de diagramação científico em desenvolvimento com sintaxe inspirado
em MarkDown e tem a compilação rápida. AÀ parte de programação usa a linguagem script
própria. O serviço online está em https://typst.app/, enquanto que o compilador em
si para instalação local, está em https://github.com/typst/typst. Se quiser um editor
dedicado, o https://github.com/Bzero/typstwriter é uma das opções gratuítas.
SILE
O SILE (https://sile-typesetter .org/) é um sistema de diagramação de documento
científico em desenvolvimento, com sintaxe inspirado em LaTeX. Para a parte de programa-
ção, usa nativamente a linguagem Lua. O compilador está em https://github.com/sile.
typesetter/sile/.
groff
O groff (https://www.gnu.org/software/groff/) é um sistema clássico, largamente utili-
zado para elaboração de documentos do projeto GNU.
ConTeXt
O ConTeXt (https://en.m.wikipedia.org/wiki/ConTeXt) é um sistema baseado em TEX
(como no caso de L2TEX). Enquanto que o I2TEX tenta esconder as configurações de documentos
(do usuário {inal} para que seja apropriado para submissão de arqtigos e simlares, ou a
elaboração de documentos sem a necessidade do conhecimento técnico de diagramação, o
ConTeXt facilita o acesso de tais recursos para os usuários, o que facilita a elaboração de
documentos genéricos.
G.6. Algumas alternativas a LaTeX 328
Alguns Comentários Finais
Neste texto está direcionado ao usuário de LaTeX, mas não para os desenvolvedores. Assim, não
foi incluído detalhes sobre caixas e similares. Para quem pretende criar comandos e ambientes
complexos ou desenvolver pacotes, o conhecimento sobre caixas é importante. Para este
assunto, recomendo a leitura de outro material tais como [OPHS25] e [wik18]. Também não
foi tratado a camada de programação LaTeX3 que tem forma diferente de desenvolver os pacotes
em relação a LaTeX tradicional, na qual está presente nos pacotes modernos. O interessado em
aprender a desenvolver pacotes, deve consultar documentos tais como https://ctan.org/
pkg/usrguide, https://ctan.org/pkg/clsguide e https://www.alanshawn.com/latex3-
tutorial/, entre outros (O site https://www.latex-project.org/help/documentation/
lista vários documentos deste tipo).
Neste texto, foram apresentados alguns dos pacotes e classes mais utilizados, mas vários
pacotes e classes populares foram omitidos.
Por exemplo, quem trabalha com fórmulas complexas, é recomendável que considere o uso
do pacote mathtools que resolve algumas deficiências do pacote ansmath. Para criar ficha cata-
lográfica, poderá colocar o número total de páginas usando o comando \PreviousTotalPages,
mas dependendo do caso, precisará do pacote como o pageslts.
Para inserir uma ou mais páginas diretamente no documento em vez de inserir como
figuras, usa-se o pacote pdfpages. Quem trabalha com tabelas, pode precisar do pacote
multirow para mesclar linhas, diagbox para dividir células em diagonal, etc., que não foram
citados neste documento. Ainda existem pacotes específicos para xadrez (xskak), diagrama
química (chem{ig}, música (abc, musixtex), etc, além dos pacotes destinados para cada tipo
de ajustes de documentos.
Dentre as classes omitidas aqui, as classes da família koma script e a classe memoir são
um dos mais importantes. Estas classes implementam várias funcionalidades adicionais em
relação as classes básicas.
Como existem pacotes específicos para cada assunto, é impossível conhecer todos eles.
Mas, pelo menos podemos tentar conhecer alguns dos pacotes e classes populares existentes
para área de atuação de cada um de nós.
Referências Bibliográficas 329
Referências Bibliográficas
[Abr24]
[Aral6a]
Aral6b]
GMS04]
\nu86
Lam86
Lam94
LaT25
Marl1l8
Mit25]
OPHS25]
[Pak17]
Elayson Abreu. abntexto: classe para LaTeX. 2024. URL: https://ctan.org/
pkg/abntexto [cited 2024-12-29].
Lauro César Araujo. A classe abntex2: Documentos técnicos e científicos brasileiros
compatíveis com as normas ABNT. 2016. URL: https://ctan.org/pkg/abntex2/
[cited 2018-06-11].
Lauro César Araujo. O pacote abntex2cite: Estilos bibliográficos compatíveis com
a ABNT NBR 60283. 2016. URL: https://ctan.org/pkg/abntex2/ [cited 2018-
06-11].
Michel Goossens, Frank Mittelbach, and Alexander Samarin. The BTRX Compa-
nion (second edition). Adilson-\esley, Reading, MA, 2004.
Donald E. \nuth. The TEÊX Book. Adilson-\esley, Reading, MA, third edition,
1986.
Leslie Lamport. BTÊX, A document Preparation System. Adilson-\esley, Reading,
MA, 1986.
Leslie Lamport. BTRX, A document Preparation System, second edition. Adilson-
\esley, Reading, MA, 1994.
LaTeX Project Team. LTRX for authors, 2025. URL: https://www.latex-
project.org/help/documentation/usrguide.pdf [cited 2025-10-25].
Daniel Ballester Marques. biblatex-abnt 3.3. 2018. URL: https://ctan.org/pkg/
biblatex-abnt/ [cited 2018-06-11].
Frank Mittelbach. LaTeX's hook management, 2025. URL: https://www.latex-
project.org/help/documentation/lthooks-doc.pdf [cited 2025-10-25].
Tobians Oetiker, Hubert Partl, Irene Hyna, and Elisabeth Schlegl. The \ot So
Short Introduction to LaTeX 2. Comprehensive TEX Archive \etwork, 2025. URL:
https://ctan.org/pkg/lshort-english [cited 2025-09-30].
Scott Pakin. The Comprehensive LaTeX Symbol List. 2017. URL: https://ctan.
org/pkg/comprehensive/ [cited 2019-01-15].
Referências Bibliográficas 330
[Tan15] — TillTantau. TikZ&PGF Manual. 2015. URL: https://ctan.org/pkg/pgf/ |cited
2018-06-11).
[Tuto2] — Tutorial Team. Online tutorials on LaTeX, 2002. URL: http://www.tug.org/
tutorials/tugindia/ [cited 2018-06-11].
[wik18] wikibook. BTRX. wikibook, 2018. URL: https://en.wikibooks.org/wiki/LaTeX
[cited 2018-06-11].
Indice Remissivo
Indice Remissivo
, 88
N+, 20
,, 88
r-, 20, 100
vi, 88
m=N .
s> 00 co
.
t osEAZAOAA )
o
-, 10
12pt, 4
vYa', 21
a4paper, 4
Na=, 21
va', 21
ABNT, iv, 157, 225
abntex2, 225
ABNTeX2, 225
abntex2cite, 243
ABNTexto, 235
\abovedisplayskip, 87
abstract, 49
\abstractname, 97
acentuação
direta, 6
modo TFX, 6
modo TeX, 255
acro, 177
\acwopencirclearrow, 199
\addbibresource, 175
\addcontentsline, 136
\addfontfeature, 218
\addto, 97
\addtocounter, 91
AddToHook, 128
\\AddToHook, 115
AddToHookítbegindocument+, 115
\AddToHookWithArguments, 116
\AddToShipoutPictureFG, 167
afterpage, 55
alfabeto
matemático, 267
algorithmicx, 167
algpseudocode, 167
algpseudocodex, 168
\algrenewcommand, 168
align*, 37
alinhamento
centralizado, 11
direita, 11
esquerda, 11
justificado, 11
\Alph, 90
\alph, 90
\smallskip, 87
ambiente, 5, 45
múltiplas linhas, 46
parâmetro, 45
parâmetro opcional, 45
amsbsy, 76
amsmath, 29
amssymb, 29
amsthm, 56
\ang, 144
annotate-equations, 307
answers, 309
\appendix, 51
\appendixname, 97
apêndice, 51
Indice Remissivo
apóstrofos, 6
\ar, 199
\arabic, 90
\arccos, 76
\\\arcsin, 76
\arctan, 76
\arg, 76
arquivo
bbl, 83
bst, 82
referência bibliográfica, 80
arquivos
sty, 269
array, 15
Oremovefromreset, 92
article, 4
aspas, 6
\AtBeginDocument, 115
\author, 51
babel, 4, 95
background, 165, 166
\backmatter, 52
base, 123
beamer, 206
beamerposter, 205
\begin, 5
\belowdisplayskip, 87
bfseries, 73
biber, 175
\bibitem, 78
biblatex, 175
abnt, 246
alphabetic, 177
authortitle, 177
authoryear, 177
draft, 177
langid, 221
numeric, 177
\parencite, 176
reading, 177
romanized, 221
\textcite, 176
translated, 221
verbose, 177
\bibliographystyle, 82
\bibname, 97
BibTeX, 80
H, 82
abbrv, 82
abbrvurl, 135
alpha, 82
alphaurl, 135
amsalpha, 82
amsplain, 82
o, 81l
PCarticle, 83
Obook, 81
Ocomment, 81, 84
Omanual, 83
Qmisc, 83
Ophdthesis, 83
Ostring, 81
comentário, 84
lastchecked, 135
note, 135
plain, 82
unsrt, 82
unsrturl, 135
url, 135
urldate, 135
bibtex
doi, 174
url, 174
urldate, 174
\bigskip, 87
\blindmathpaper, 282
\blindmathtrue, 282
\Blindtext, 282
blindtext, 165, 282
\blindtext, 282
block, 213
bm, 30
\bmod, 76
boldmath, 76
\boldsymbol, 76
book, 4
booktabs, 20, 154
\bottomrule, 154
brazil, 97
brazilian, 97
calligra, 140
cancel, 307
caption, 131, 154
\caption, 61, 131
\caption*, 63, 132
\captionn<idioma>, 97
\captionsetup, 132
capítulo, 48
caracter especial
1, 255
Indice Remissivo
1, 255
caracteres especiais, 5
center, 11
\center, 11
\echapter, 48
\chapter*, 49
\chaptername, 97
\circlearrowleft, 199
circledtext, 143
citações, 21
\cite, 79
\clearcaptionsetup, 132
\cleardoublepage, 54
\clearpage, 54
\learShipoutPictureBG, 167
\eline, 17
\\emidrule, 154
\collectObody, 111
color, 101
named, 101
usenames, 101
\eolor, 101
\ecolorbox, 101
\ecolorlet, 163, 182
colortbl, 20, 155, 156
\columnsep, 89
\columnseprule, 89
\columnwidth, 89
com serifa, 72
comando
múltiplas linhas, 46
comandos
com parâmetros, 44
nome das funções, 76
parâmetro opcional, 44
comandos frágil, 94
combinat, 296
combine, 296
combinet, 296
comentário, 6
comentário, 6
Computer Modern, 139
\contentsname, 97
ConTeXt, 327
contour, 140
\convertcolorspec, 141
convertor, 322
Calc2LaTeX, 324
Excel2LaTeX, 323
Image Magick, 322
LaTeXML, 322
lwarp, 322
Pandoc, 324
sam2p, 322
TeX4ht, 322
\riter2LaTeX, 323
\cos, 76
\cosh, 76
\ecot, 76
\coth, 76
\counterwithin, 92
\counterwithout, 92
\esc, 76
custom-bib, 175
código fonte
programma, 23
datatool, 290
\date, 51
deolum, 18
DeclareCommandCopy, 120
DeclareKeys, 119
DeclareMathOperator, 43
DeclareMathOperator*, 43
\eclareOption, 273
\\def, 114
\defaultfontfeatures, 218
\defaultfontfeatures+, 218
\defineOkey, 107
definir comandos, 43
\\deg, 76
degradê
texto, 141
delimitador, 264
\depthof, 90
derivada, 259
\\det, 76
diagbox, 328
\dim, 76
\dimexpr, 90
\isemulatePackage{setspace}, 124
displaymath, 7
displaystyle, 7
\displaystyle, 260
documentclass, 3
\documentclass, 4
Donald \unuth, 1
\dotfill, 88
\eclareCaptionFormat, 132
X
\eclareDocumentCommand, 116
\eclareDocumentEnvironment, 122
N
Y
N
Indice Remissivo
\doublebox, 161
\doublespacing, 123
draftwatermark, 165, 166
dscription, 13
dsfont, 140
\DTLforeach, 290
\DTL1caddb, 290
\edef, 114
editor gráfico, 317
Dia, 318
FlowFramTk, 319
GIMP, 318
InkScape, 317
LaTeX Draw, 318
TikZit, 319
editor para LaTeX, 316
LyX, 316
TeXMaker/TeXStudio, 316
elemento
flutuante, 60
\else, 110
em, 13, 73
Nem, 13
\emph, 13, 73
\end, 5
ênfase de texto, 13
\enlargethispage, 55
\enskip, 88
\enspace, 88
\ensuremath, 43
enumerate, 13, 15
enumi, 91
enumii, 91
enumiii, 91
enumitem, 136
inline, 137
shortlabels, 137
enumiv, 91
environ, 111
equation, 9
equation*, 37
eso-pic, 165, 166
espaço
depois do comando, 6
não quebrável, 6
estilo da página
plain, 51
estilo literário
francês, 125
exercise, 308
\exp, 76
\expandafter, 107
\ExplSyntaxOff, 224, 269, 283
\ExplSyntaxOn, 224, 269, 283
exsheets, 308
fancybox, 161
fancyhdr, 127
\fancypage, 162
\fancypagestyle, 128
\fancyput, 162
\\fbox, 25, 61, 102, 161
\fboxrule, 103
\fboxsep, 103
\fcolorbox, 102
ferramentas, 324
jabref, 324
jpdftweak, 324
pdfarranger, 325
pympress, 325
scribus, 325
serviços \eb, 326
xournal++/jaurnal, 325
\fi, 110
figura
flutuante, 60
figure, 60
\figurename, 97
float, 149, 153
b, 61
1,61
H, 149
h, 61
p, 61
t, 61
floatfit, 151
flowfram, 205, 302
flowframtk, 306
flushleft, 11
\flushleft, 11
flushright, 11
\flushright, 11
fncychap, 130
Bjarne, 130
Bjornstrup, 130
\\ChNumVar, 130
\ChTitleVar, 130
Conny, 130
Glenn, 130
Lenny, 130
Rejne, 130
Indice Remissivo
Sonny, 130
\\fnsymbol, 91
fonte
comandos antigos, 74
Computer Modern, 72
enfatizado, 73
formato normal, 73
itálico, 73
MLModern, 220
negrito, 73
\ew Computer Modern, 220
nomo espaçado, 72
não negrito, 73
restaurar padrão, 75
romano, 72
samll caps, 73
sem serifa, 72
tamanho, 74
fontenc, 4
fontsetup, 220
fontspec, 218
\fontspec, 218
footnote, 12
\foreignlanguage, 95
\\frac, 8
frame, 206, 207
\\frame, 206, 207
\framebox, 103
framed, 162
\frametitle, 207
\frontmatter, 51
função matemática
nome da, 263
\fussy, 100
gather*, 37
\gced, 76
\\gdef, 114
geometry, 123
bmargin, 123
Imargin, 123
rmargin, 123
tmargin, 123
\geometry, 123
glossaries, 179
glossários, 177
gradient-text, 141
graphicx, 64
groff, 327
gráfico científico, 319
Asymptote, 319
FractInt, 321
Geogebra, 319
GNU Octave, 320
GNU R, 320
gnuplot, 320
Graphvis, 321
LabPlot, 320
LibreCAD, 321
MathMod, 321
Maxima, 320
Gummi, 317
headings, 124
\heightof, 90
\hfill, 88
hhline, 20
hifenização, 95
\hline, 16
\hom, 76
\hrulefil1l, 88
\hspace, 87
\\hspace*, 87
Huge, 75
huge, 75
\hyperlink, 136
hyperref, 134
\hypertarget, 136
hyphenat, 124
\hyphenation, 100
i sem pingo, 6
IBGE, 250
\IBGEtab, 254
idioma, 95
\IfBlankF, 117
\IfBlankT, 117
\IfBlankTF, 117
\IfBooleanF, 117
\IfBooleanT, 117
\IfBooleanTF, 117
|Oifclassloaded, 270
\ifOcompatibility, 270
\IfFileExists, 270
iffont, 219
\iffontexists, 219
\IfFontExistsTF, 219
\iffontsexist, 219
\IfNoValueF, 117
\IfNoValueT, 117
\IfNoValueTF, 117
\Oifstar, 106
Indice Remissivo
iftex, 215
ifthen, 274
\IfValueF, 117
\IfValueT, 117
\IfValueTF, 117
\ifx, 110
imagem externa, 64
imagem PDF
múltiplas páginas, 65
\includegraphics, 64
parâmetro opcional, 65
\includepdf, 235
indentfirst, 55
\index, 84
\indexname, 97
indice remissivo, 84
índice remissivo
com chave, 84
sub-entrada, 84
indice remissivo
trecho, 85
\inf, 76
inkscape, 206
inlinegraphicx, 153
inlinestyle, 7
\\\input, 312
\item, 13
itemize, 13
itshape, 73
jabref, 80, 84
jPDFTweak, 206
justify, 124
\justify, 124
\ker, 76
\kil1, 20
koma script, 328
\label, 10, 61
landscape, 152
LARGE, 75
Large, 75
large, 75
LaTeX, 1
Latin Modern, 139
leaflet, 300
Leslie Lamport, 1
\let, 45, 113
letra
grega, 8
etras gregas, 260
lettrine, 125
NMg, 76
NMlim, 76
\liminf, 76
imitante
duas linhas, 38
\limsup, 76
\linebreak, 12
ineno, 164
\linenumbers, 164
\linespread, 99
\linewidth, 20, 26, 89
inhas em branco, 12
ipsum, 165, 282
\lipsum, 165, 282
ist, 15
ista, 13
descrição, 13
enumerada, 13
controle, 15
inline, 136
item, 13
itemizada, 13
marca de itens, 101
ista de
siglas, 177
simbolos, 177
ista de figuras, 63
lista de tabelas, 63
\istfigurenname, 97
istings, 169
istingsutf8, 170
\istoffigures, 63
\istoftables, 63
\listtablename, 97
\ln, 76
NMog, 76
ongtable, 63
\lstinputlisting, 170
lstlisting, 169
\lstset, 169
LTXexample, 170
Lua(La)TEX, 214
uavlna, 217
LyX, 2
LyX, 284
MacTeX, 2
\mainmatter, 51
\makeatletter, 105, 269
