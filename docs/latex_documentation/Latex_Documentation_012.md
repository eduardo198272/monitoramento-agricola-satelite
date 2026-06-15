locale=DE, % Alemão: virgula como decimal
table-format=4.2, % 4 digitos, 2 digitos decimais
table-number-alignment=center % alinhar no decimal
\begin{longtblr})
[
caption = fTabela longal, % titulo
label=(ftab:longal, % rotulo para referências cruzadas
)
Ú
colspec = (XX[r,sil), % X é largura automatica. Segundo X tem como
parâmetro opcional r (direita) e si (número usando pacote siunitx)
rowhead = 1, % primeira linha será repatida em todas páginas
row{1} = ffont=\b{series}, % linha de título
rowleven) = fgray!50), % linhas par em cinza
row{Zz} = ffont=\bfseries,whitelk, % última linha
1”
\toprule
texto & \\textínúmero) W \midrule
linha 1 & 1.1 W % \vmidrule
linha 2 & 2.2 W % \midrule
linha 3 & 3.3 W % \midrule
linha 4 & 4.4 W % \midrule
linha 5 & 5.5 W % \midrule
linha 6 & 6.6 W % \midrule
linha 7 & 7.7 W % \midrule
linha 8 & 8.8 W % \midrule
linha 9 & 9.9 W % \midrule
linha 10 & 10.10 W % \midrule
linha 11 & 11.11 \W
\bottomrule
\end{longtblr}
15.155 Moldura, enumeração das linhas e marca d'água
Para enfeitar o documento, como colocar moldura nos elementos, usamos os pacotes adicionais,
exceto molduras simples fornecidos pelo \fbox.
O pacote fancybox oferece caixas com molduras extras tais como \shadowbox (com
sombra), doublebox (moldura dupla) e \ovalbox (moldura com quinas arredondadas).
\ote que \shadowbox não permite controlar a cor da sombra. Se quer caixas mais sofisti-
cadas, poderá usar o pacote tcolorbox. No caso de querer construir uma caixa personalizada,
também podemos usar o pacote gráfico tal como o tikz. \eja o Exemplo 15.30.
Exemplo 15.30: exl15-fancybox.tex
\shadowboxíCaixa com sombral
\doubleboxíCaixa com moldura duplay
\ovalboxíCaixa com quina arredondada )
\\OvalboxíOutra caixa com quina arredondada-)
Caixa com sombra'
Caixa com moldura dupla
Caixa com quina arredondada |
Outra caixa com quina arredondada
Ç
Lembre-se que, se o conteúdo tiver parágrafo, deverá usar em conjunto com o minipage.
Também permite colocar conteúdo ou moldura na página com comandos tais como \fancyput,
\thisfancyput, \fancypage e \\thisfancypage.
Por exemplo, o código
\thisfancypageí%
\setlength{NWfboxsep}([8pt)%
\setlength{\shadowsize}íSptY,
\shadowbox+(>
acrescenta moldura com sombra na página atual.
Para colocar moldura nos conteúdos longos que podem ocupar mais de uma página, po-
demos usar o pacote framed. Para colocar cor de fundo, deverá definir a cor do fundo
shadecolor. Para isso, é recomendado usar o pacote xcolor visto na Seção 16.1 do Capí-
tulo 16 (não é o pacote color) que tem facilidade de manipulação das cores. Assim, para
executar o código do Exemplo 15.31, deverá carregar tanto o pacote framed como o xcolor.
Exemplo 15.31: exl5-framed.tex
\beginí{ramed}
O texto com moldura pode ser produzido facilmente com o pacote \textttí
{ramed}.
\endí{ramed})
\colorletíshadecolorkíblack!15) % cor do fundo usando xcolor
\beginí{shaded*}
O texto com fundo pode ser produzido facilmente com o pacote \textttí{ramed}.
\endí{shaded*}
\begin{leftbar}
O ambiente \textttile{tbar}] coloca traço no lado esquerdo do texto.
\endíle{tbar}|
O texto com moldura pode ser produzido facilmente com o pacote framed.
O texto com fundo pode ser produzido facilmente com o pacote framed.
| O ambiente leftbar coloca traço no lado esquerdo do texto.
O comando \colorlet do pacote xcolor permite definir cor a partir das cores existentes.
black!15 é 15% de preto. \eja a Seção 16.1 do Capítulo 16 para mais detalhes sobre recursos
de xcolor.
\ote que, diferente das caixas padrões do LaTeX ou do pacote graphicx, os ambientes do
framed podem quebrar em linhas e em páginas.
Para criar caixa de texto similar ao recado fixado, usa-se o pacote postit, como no
Exemplo 15.32.
Exemplo 15.32: exl5-postit.tex
\beginí{PostItNote}
\Mlipsum[1] [1-2]
\end{PostItNote}
úhtikz rendering, with lipsum paragraph
\beginfPostItNotel [Render=tikz]
\lipsum[1] [1-2]
\endf{PostItNote}
Atikzv2 rendering, with lipsum paragraph
\begin{PostItNote}l [Render=tikzv2]
\lipsum[1] [1-2]
\endí{PostItNote}
Lorem ipsum dolor sit amet,
consectetuer adipiscing elit.
Ut purus elit, vestibulum ut,
placerat ac, adipiscing vitae,
felis.
Lorem ipsum dolor sit amet,
consectetuer adipiscing elit.
Ut purus elit, vestibulum
ut, placerat ac, adipiscing
vitae, felis.
=
Lorem ipsum dolor sit amet, i
consectetuer adipiscing elit.
Ut purus elit, vestibulum ut,
placerat ac, adipiscing vitae,
felis.
O pacote postit requer xfp que deve ser carregado no preáâmbulo.
Para indicar as correções a serem efetuadas, é útil ter linhas enumeradas. Para enumerar
as linhas do documento, usa-se o pacote lineno.
Para que as fórmulas também sejam enumeradas, use
\usepackage [mathlines] {lineno})
no preamble. Os comandos \linenumbers e \nolinenumbers são usados para ativar/de-
sativar as enumerações. Se pretende enumerar todo documento, coloque \linenumbers no
preamble. Para enumerar a cada “<n>” linhas, use modulolinenumbers[<n>]. \eja o
Exemplo 15.33.
Exemplo 15.33: exl5-lineno.tex
\linenumbers % ativa a enumeracao das linhas
\nodulolinenumbers[3] % enumerar de 3 em 3
Mlipsum[1] % preencher
\nolinenumbers % desativa a enumeração das linhas
\lipsum[1] % 1 paragrafos
% enumerando so um trecho.
\resetlinenumber % reset the line number
\nodulolinenumbers[1] % enumerar todas
\beginí{linenumbers}
\lipsum[2] % 2 paragrafos
\endí{linenumbers}
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Ut purus elit, vestibulum ut,
placerat ac, adipiscing vitae, felis. Curabitur dictum gravida mauris. \am arcu libero,
3 nonummy eget, consectetuer id, vulputate a, magna. Donec vehicula augue eu neque.
Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis
egestas. Mauris ut leo. Cras viverra metus rhoncus sem. \ulla et lectus vestibulum
s urna fringilla ultrices. Phasellus eu tellus sit amet tortor gravida placerat. Integer
sapien est, iaculis in, pretium quis, viverra ac, nunc. Praesent eget sem vel leo ultrices
bibendum. Aenean faucibus. Morbi dolor nulla, malesuada eu, pulvinar at, mollis ac,
o nulla. Curabitur auctor semper nulla. Donec varius orci eget risus. Duis nibh mi,
congue eu, accumsan eleifend, sagittis quis, diam. Duis eget orci sit amet orci dignissim
rutrum.
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Ut purus elit, vestibulum ut,
placerat ac, adipiscing vitae, felis. Curabitur dictum gravida mauris. \am arcu libero,
nonummy eget, consectetuer id, vulputate a, magna. Donec vehicula augue eu neque.
Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis
egestas. Mauris ut leo. Cras viverra metus rhoncus sem. \ulla et lectus vestibulum
urna fringilla ultrices. Phasellus eu tellus sit amet tortor gravida placerat. Integer
sapien est, iaculis in, pretium quis, viverra ac, nunc. Praesent eget sem vel leo ultrices
bibendum. Aenean faucibus. Morbi dolor nulla, malesuada eu, pulvinar at, mollis ac,
nulla. Curabitur auctor semper nulla. Donec varius orci eget risus. Duis nibh mi,
congue eu, accumsan eleifend, sagittis quis, diam. Duis eget orci sit amet orci dignissim
rutrum.
1 \am dui ligula, fringilla a, euismod sodales, sollicitudin vel, wisi. Morbi auctor lorem
2 non justo. \am lacus libero, pretium at, lobortis vitae, ultricies et, tellus. Donec
3 aliquet, tortor sed accumsan bibendum, erat ligula aliquet magna, vitae ornare odio
« metusami. Morbi ac orci et nisl hendrerit mollis. Suspendisse ut massa. Cras nec ante.
s Pellentesque a nulla. Cum sociis natoque penatibus et magnis dis parturient montes,
s nascetur ridiculus mus. Aliquam tincidunt urna. \ulla ullamcorper vestibulum turpis.
7  Pellentesque cursus luctus mauris.
No Exemplo 15.33 foi usado o comando \lipsum que gera textos aleatórios em grego para
preencher as páginas para testes. Logo, precisa carregar o pacote lipsum no preamble para
que o exemplo funcione. Para caso que queira preencher com texto contendo fórmulas, existe
o pacote blindtext.
Existem vários pacotes que permitem colocar conteúdos em todas as páginas, como no
caso de marca d'água. Entre eles, vamos ver o caso do uso de background, draftwatermark
e eso-pic.
O código
\documentclasstarticle)
\usepackageTbackground]
\usepackage{tikz} % necessário carregar para usar background
\usepackageTxcolor>
\usepackagetTtgraphicx)
\usepackage{lipsum}
\backgroundsetuptcolor=red,opacity=0.2,contents=fNsffamilyNWbfseries RASCUNHO
+
\beginf{document}
\lipsum
\endí{document}
Coloca a marca d'àgua “RASCUNHO” em todas páginas, usando o pacote background.
\ote que, se quer colocar a imagem externa, basta usar o \includegraphics em vez de
texto. Para desativar/modificar a marca d'água no meio do documento, basta chamar o
\backgroundsetup novamente.
O mesmo efeito pode ser obtido pelo pacote draftwatermark como segue.
\documentclassf{tarticle}
\usepackageTdra{twatermark}Y
\usepackage{tikz}
\usepackageíxcolor+)
\usepackageTgraphicx>)
\usepackage{lipsum}
\raftwatermarkOptionsítcolor=red,text=(\tikzí\node [opacity=0.2] (\sffamilyX
b{series RASCUNHO}\XY % versão 2.x (nova)
% \etWatermarkTextí\sffamilyNWbfseries|Huge RASCUNHO) % versão antiga
\beginf{document}
\lipsum
\endí{document}
A funcionalidade é similar ao background, mas não consegue controlar a opacidade da
imagem do fundo. Uma forma de contornar isso é usar o \tikz como no exemplo anterior.
Outro pacote é o eso-pic. Apesar de ser mais difícil de usar por basear no ambiente
picture, era um pacote popular e pacotes/documentos mais antigos podem fazer uso dele.
Por exemplo, o código
\documentclass{tarticle})
\usepackageTgraphicx)
\usepackageTfeso-picl
\usepackagetxcolor+)
\usepackage{lipsum}
% marca d'agua
% \ersão sem * é para toda página. \ersão * é somente na página corrente
\AddToShipoutPictureBGT
CVAtPageLowerLefti, Este é padrão
\unitlength=\paperwidth
\put (0.3,0.5) firotatebox{45}1%
\scaleboxí3\fNHugeNsffamilyWbfseriescoloríblack!25+Rascunho)Y%
Y.
ZIANAtPageLowerLeft
\AVNAddToShipoutPictureBG
\begin{document}
\lipsum[1-4]
\endí{document}
após carregar o pacote eso-pic, colocará a palavra “Rascunho” rotacionado por 45º em todas
as páginas como marca d'água. O comando \AddToShipoutPictureBG criará um ambiente
picture. Logo, podemos colocar os comandos aceitos no ambiente picture dentro dele.
Para limpar o fundo, usa-se o \learShipoutPictureBG.
Os comandos do eso-pic tem a versão “BG” para atrás da página como marca d'agua
e versão “FG” para colocar na frente da página. Por exemplo, \AddToShipoutPictureFG
coloca na frente em vez de trás da página.
Caso pretende colocar marca d'água sem o pacote, poderá usar o recurso de VAWddToHook
do LaTeX em vez de usar o pacote, como no exemplo a seguir.
\documentclassf{tarticle}
\usepackageTgraphicx>)
\usepackage{xcolor}
\usepackage{tikz}
\usepackage{Tlipsum}
% marca d'água personalidada.
% neste comando, poderá receber parametro opcional para repassar para \node
\newcommandí\t {kzwatermark} [1] [draw=red, text=red]í
\begin{tikzpicture} [overlay, remember picture]
\node [rotate=45, scale=5, tH1] at (current page) flWbfseriesysffamily
RASCUNHO) ;
\endí{tikzpicture}
F
% comando para colocar marca d'água: poderá desativar/alterar com o uso de À
newcommand
\newcommandfWputwatermarkYí
\tikzwatermark[opacity=0.33, fill=yellow, draw=red, text=red]
dº
% shipout é chamado quando gera páginas
% Adiciona no shipout
/ANAddToHookíshipout/foregroundkl % na frente
\AddToHookíTshipout/background+l % atrás
\putwatermark
dº
\beginf{document}
\lipsum[1-4]
\end{document}
O shipout é chamado quando criar cada página. \ote que no exemplo, foi criado co-
mando auxiliar \putwatermark para colocar marca d'água em vez de colocar marca d'água
diretamente, o que permite redefinir dentro do documento para desativar/modificar o mesmo.
15.16 Algorítmo e código fonte
Para algoritmos, poderá usar o pacote algorithmicx que destaca entre pacotes com mesma
finalidade, por poder configurar a forma como será exibido. Para usar, carrege o pacote
algpseudocode que carregará o pacote algoritmicx e define estilo para pseudo código. \eja
o Exemplo 15.34
Exemplo 15.34: exl5-alg.tex
\beginfalgorithmicY[1] Z iniciar enumeração das linhas
\Procedure{DotProd}í$u,v$) \CommentíProduto interno de u e vl
\State $pygets 0$ \CommentílInicializa como OJ
\Forí$iNgets 1, 1dots, n$)
\State $p \gets p + u i*v i$
\\\EndFor
\State \textbf{return} $p$\Commentíretorna o valorY
\EndProcedure
\end{algorithmic}
1: procedure DoTPROD(u, v) D> Produto interno de u e v
2 p+o D> Inicializa como O
3 for i & 1,...,n do
4: PE PHTUXRU;
5 end for
6 return p D retorna o valor
7: end procedure
Como o pacote usa a palavra-chave em inglês, pode querer traduzir para português.
Para isso, use o comando \algrenewcommand para redefinir palavra-chaves no preambulo do
documento.
Por exemplo, o código
\usepackageTalgpseudocode)
% traduzindo a palavras-chave
\algrenewcommandValgorithmicprocedurefVWtextbfí{procedimento}])
\algrenewcommandValgorithmicforí\textbf{para})
\algrenewcommandValgorithmicdofWtextbfiífaça))
\algrenewcommandValgorithmicendfí\textbfí{im})
traduzirá a palavra-chaves do algoritmo anterior para português brasileiro. Ajustando o
“return” para “retorne”, terá a saída
1: procedimento DoTPROD(u, v) D> Produto interno de u e v
2 p+o D Inicializa como O
3 para i & 1,..., n faça
4: PE PpTUtrU;
5 fim para
6 retorne p > retorna o valor
7: fim procedimento
Para traçar linhas verticais para blocos indentados, poderá usar o pacote algpseudocodex
que é compatível com o algpseudocode.
O Pacote algorithmicx vem com padrão, mais dois estilos que são para linguagem Pascal
e C, mas para colocar código fonte de um programa, costuma usar o pacote listings que
implementa o ambiente lstlisting na qual formata o código de acordo com a linguagem de
programação escolhida.
Ele já vem com configurações para diversas linguagens de programação, tais como Ada,
Algol, Assember, awk, bash, Basic, CH, C++, C, Cobol, Delphi, Fortran, Gnuplot, HTML,
Java, Lisp, Logo, Lua, Make, Mathematica, Matlab, Metapost, Modula-2, Objective C,
Octave, Pascal, Perl, PHP, Prolog, Python, GNU R, Ruby, SAS, Scilab, sh, SQL, TeX, XML,
entre vários outros. Se a linguagem pretendida não estiver na lista, poderá definir uma nova
linguagem de programação.
Para o seu uso, costuma efetuar configurações iniciais no preamble com o comando
\lstset e no ambiente de lstlisting, efetuar mais alguns ajustes se necessário. \eja o
Exemplo 15.35
Exemplo 15.35: exl5-listings.tex
\begin{lstlisting} [language=Python,caption=({Bhaskara}]
import math
t obter solução de ax“2 + bx +c = O
def bhaskara(a, b, c):
delta = b*b - 4*a*c;
if delta < O:
return [];
elif delta == O:
return [-b/(2*a)]
else:
return [(-b-math.sqgrt(delta))/(2*a),(-btmath.sqgrt(delta))/(2+a)]
\end{lstlisting}
Exemplo 15.36: Bhaskara
import math
* obter solução de ax 2 +tbr+tc=0O
def bhaskara(a, b, c):
delta = b*b - 4*a*c;
if delta < O:
return [];
elif delta ==
return [-b/(2*a)]
else:
return [(-b-math.sqrt(delta))/(2*a),(-btmath.sqgrt(delta))/(2*a)]
A formatação de saída depende da configuração do lstlisting. AÀ saída do Exemplo 15.35
foi obtida pela configuração
\lstsetfí
numbers=none,
breaklines=true,
breakautoindent=true,
columns=fullflexible, % para poder copiar código do PDF
\eepspaces=true, % to keep indentation
basicstyle=\ttfamily, % using monospaced font, prevent that hiphen are
replaced by minus (solving insure on copy/paste code {rom pdf}
keywordstyle=\color{blue}
frame=lines, %únone, single, line
\ote o uso de columns=fullflexible para que o código fonte copiado do PDF não fique
bagunçado, e basicstyle=\ttfamily para que o hifen não ser trocado pelo sinal de menos, o
que ajuda o leitor que cópia o código do documento para editor de texto. O keepspaces=true
é para não eliminar espaços, pois o alinhamento é essencial para programa em Python
Para o arquivo externo, podemos usar o comando \lstinputlisting que carrega o código
diretamente do arquivo fonte.
\ote que listings não tem suporte nativo a utf8. Portanto, quando usa os caracteres
acentuadas, deverá tomar cuidados. Para o Mstinputlisting funcione no utf8, basta carre-
gar o pacote listingsutf8, mas para o código colocado diretamente no ambiente 1stlisting,
deverá criar tabela de caracteres unicode correspondente. Para não ter tal trabalho, poderá
executar no XalTEX ou LuaLaTeX em que tem total suporte a unicode.
Quando queremos colocar o trecho do código de LaTeX juntamente com a sua saída, o pacote
showexpl é prático. Ele usa o pacote listings para listar o código fonte. AÀA configuração
inicial é feito com \istsetíexplpreset=1...))nopreamble. Os parâmetros em explpreset
serão aplicados somente no ambiente LTXexample, enquanto que os parâmetros fora dele são
aplicados tanto para lstlisting como LTXexample.
O ambiente LTXexample aceita os parâmetros do lstlisting e também o pos e preset
que especificam a posição onde colocar a saída, e a configuração inicial antes de executar o
código. \eja o Exemplo 15.37.
Exemplo 15.37: exl5-showexpl.tex
\begin{LTXexample} [pos=b,caption={NWLaTeXY}
% comentario
Teorema de Pitágoras afirma que
NE ar2 = poo+cen2 N
\end{ltxlisting}
Ticting 1: LaTeX
Teorema de Pitágoras afirma que
% comentario
Teorema de Pitágoras afirma que
NE a2 = poa+c”2 NM a2 =V.+2
O valor de “pos” que determina onde ficará a saída do resultado do código em relação
6n” [12$))
ao do código fonte, podem ser “t”, “b”, “1”, “r” ,“o” ou “i”, que são abreviaturas de “top”
(encima), “bottom” (embaixo), “left” (esquerda), “right” (direita), “outer” (lado de {ora} e
“inner” (lado de dentro).
Na saída do Exemplo 15.37, pode notar a falta de espaço vertical após o título, o
que faz título esconder atrás do código e da sua saída. Teoricamente, o parâmetro op-
cional belowcaptionskip do ambiente lstlisting deveria ajustar tal espaçamento, mas
devido a forma como showexpl foi implementado, isto não acontece por não chamar o
\lsteInit encarregado disso. Para corrigir, a atualização de valor pode ser inserido dentro
do \SXCKillAboveCaptionskip que é chamado antes de criar o titulo no LTXexample. Para
isso, coloque o código
\nakeatletter
\renewcommandWSXOKil1lAboveCaptionskipí%
\ifx|lstôcaptionVCemptyYelse
\lsteIfSubstring tWlsteêcaptionpos
TNWskip-\abovecaptionskipY()%
vfi
\ifx|lstObelowcaptionVWundefined \else Zadicionado
\belowcaptionskip=\lstObelowcaptionirelax % adicionado
\fi Zadicionado
D7
\nakeatother
no preamble do documento. \ote que a configuração inicial do ambiente LTXexample não
será alterado, mas agora podemos ajustar o espaçamento entre o título e o corpo com o
parâmetro belowcaptionskip como em lstlisting.
\ote que o \usepackage e similar estão desabilitados dentro do ambiente LTXexample e se
o código precisar, deverá estar carregado no preamble do documento principal. Agora outro
exemplo, supondo que amssymb está carregado no documento principal (para usar umathbb).
\eja o Exemplo 15.1.
Exemplo 15.1: ex15-showexpl-completo
\begin{LTXexample} [pos=b,caption=(\LaTeXT) completol,belowcaptionskip=
baselineskip]
\documentclass{article})
\usepackage [T1] {fontenc}
\usepackage [brazil] ({babel}
\usepackageTamssymb,amsmath+
\newcommandí\senYí\mathrm{sen}Y
\beginf{document}
% comentario
N[ \forall \theta \in \mathbbíRI, \coso2ltheta + \senºANtheta = 1 N
\endí{document}
\endí{LTXexample}
Listing 2: LaTeX completo
\documentclass{article}
\usepackage [T1] (ffontency
\usepackage [brazil] {babel}
\usepackageTamssymb,amsmath+
\newcommandí\senYí\mathrm{sen}y)
\beginf{document}
% comentario
V[ NVforall1l \theta \in \mathbbf{RI}, \coso2ltheta + \senºANtheta = 1 N
\endí{document}
vO E R,cos? 0 +senºO=1
15.17º Ênfase modo antigo e cancelamento
Além da ênfase em itálico, também poderá usar o sublinhado como era feito na maquina de
escrever.
O pacote ulem implementa várias formas de “sublinhar” o texto. Para que os comandos
emph e \em, assim como o ambiente em não sejam trocados pelo comando de sublinhar texto,
use a opção normalem. Assim, coloque \usepackage [normalem] {ulem} no preamble para
poder usar diversos efeitos de “sublinhar” o texto.
\eja o Exemplo 15.2.
Exemplo 15.2: exl5-ulem.tex
Sublinhando: \ulinefimportantel N
Sublinhando com linha dupla: \uulinefurgentel N
Com onda: \uwave{barcol} N
Cancelando o texto: \sout{errado} N
Removendo: \xout{removido} N
Linha tracejada: \dashulinefítracejadal N
Linha pontilhada: \dotulinef{pontilhada}
Sublinhando: importante
Sublinhando com linha dupla: urgente
Com onda: barco
Cancelando o texto: errado
Removendo: hEXAGYIAO
Linha tracejada: tracejada
Para destacar texto, costuma usar o pacote soul como no exemplo 15.3, na qual a cor de
destaque foi configurado com os comandos
\usepackage{soul} % para destacar
\usepackage{xcolor} % para configurar cores
\setulcolor{green} % cor para sublinhar
\setstcoloríredl % cor para cancelar
\sethlcoloríyellowlk % cor para destaque
Exemplo 15.3: exl5-soul.tex
Espaçado: \sofespaçadol) N
Small Caps: \capsíSmall Caps+ N
Sublinhado: \ul{sublinhado} N
Cancelando o texto: \stí{errado} N
Destacando: \hl{destacando}
Espaçado: espaçado
Small Caps: SMALL CAPS
Sublinhado: sublinhado
Cancelando o texto: errado
Destacando: destacando
Para caso de cancelar parte das equações, veja o exemplo da Seção E.l (página 307).
15.18 Mais sobre referências bibliográficas
Na citação original do LaTeX, usa-se o mesmo padrão tanto para caso de fazer parte do texto
(citação textual) ou não fazer parte do texto (citação dentro de parenteses). Para fazer esta
distinção e controlar melhor a forma de citação, foi desenvolvido o pacote chamado natbib.
O pacote natbib possui comandos \citet, usado para citações textuais e citep para
citações entre parenteses (ele já coloca parenteses automaticamente).
Além disso, o natbib permite configurar a formatação de citações. \eja o Exemplo 15.4
com Exemplo 11.3.
Exemplo 15.4: exl5-natbib.tex
\documentclass{tarticle})
\usepackage [brazil]{babel}
\usepackageí{tnatbib}
\begin{document}
Para que a citação faça parte do texto (estilo textual), usa-se o comando À
verbtlcitet+ como em * "Por exemplo, \citetíIndianTUG:2000, Goossens:2004)
explicam como usar o BibTeX''.
Para que ele não faça parte do texto, usa-se o \erbtWcitept Como em *“À
ldots recursos avançados de BibTeX \citep[Cap.-13] íGoossens:2004)''.
\bibliographystyle{apalike} % escolha um estilo
\bibliographyfexii-bibtex) % arquivo de referências
\endí{document}
Para que a citação faça parte do texto (estilo textual), usa-se o comando \\citet como
em “Por exemplo, Tutorial Team (2000); Goossens and Mittelbach (2004) explicam como
usar o BibTeX”.
Para que ele não faça parte do texto, usa-se o \citep Como em “...recursos avançados de
BibTeX (Goossens and Mittelbach, 2004, Cap. 13)”.
Referências
Goossens, M., Mittelbach, F. (2004). The BTÊEX Companion (second edition).
Adilson-\esley, Reading, MA.
Tutorial Team (2000). Online Tutorials on LaTeX. Indian TEX User Group.
http://www.tug.org/tutorials/tugindia/.
O comando \cite tradicional também estará disponível, funcionando como \citet no
caso do estilo autor-ano e como \citep no caso do estilo numérico.
Usando a opção do pacote ou comandos apropriados, podermos configurar o estilo de
citações.
\ote que nos estilos antigos, os campos tais como “url” e “doi” não serão usados (logo,
não aparecem nas referências). Para que URL apareça na referência desses estilos antigos,
colocavam no campo “note”.
Para estilos mais modernos como do natbib, o URL deve ser colocado no campo “url” e
a data do último acesso em “urldate”. No estilo antigo em que urldate é ignorado, coloque
o último acesso em “note”.
Estilo padrão do natbib são plainnat, abbrvnat, unsrtnat. Também suporta vários
bst de outros pacotes do estilo autor-ano tais como apalike, newapa, (chicago, named, etc
do chicago), (agsm, dceu, kluwer, etc do harvard), (astron, apa, humanbio, etc do astron),
(authordate<n> e aaai-named do authordate<n>).
\ote que bst não compatíveis com autor-ano, como o estilo padrão do BibTeX será
