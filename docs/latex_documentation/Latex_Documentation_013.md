considerado como numérico.
Para criar seu próprio arquivo de estilo bst, comece gerando um modelo com makebst do
pacote custom-bib.
O BibkLaTeX suporta o arquivo bib em utf8 e permite que tenha citações dos livros em
caracteres fora do latin e também suporta a localização da referência bibliográfica.
Outro ponto positivo para desenvolvedores é ter maior facilidade de elaborar arquivo de
estilos.
O BiblTFEX não é compatível com a maioria dos pacotes específicos para BibTeX. Também
terá problemas com o pacote titlesec quando usar as opções refsection, refsegment ou
citereset no BibLaTeX.
\ote que, caso não tenha estilo de referência bibliográfica desejado, o truque de copiar
o conteúdo do arquivo bbl (extensão bbl) e ajustar, o que não funciona no BibLaTeX, pois
ele não usa o ambiente thebibliography. Isto vale mesmo que use BibTeX como backend.
Como nem toda revista dispõe de estilos para BibLaTeX (mesmo tendo estilo para BibTeX),
fique atento nesta parte para decidir se vai usar o BibTeX direto, ou usar o BIbLaTeX.
Quando carrega o pacote biblatex, efetua algumas configurações.
\usepackage [
% backend=biber, % padrão
% bibencoding=utf8, % padrão
% natbib=true, % natbib compatible mode (citep, citet, etc)
style=authoryear,
]J{biblatex}
Carrega o biblatex configurado para usar biber como processador de referências biblio-
gráficas. Se usar o bibtex em vez do biber, perderá os recursos estendidos tais como suporte
a utf8 e localização (ajustar ao idioma de cada referéncia) da referência bibliográfica. AÀ
opção natbib está comentado, mas se ativar, terá disponibilidade para usar comandos \\citet
e \citep similar a do natbib. Finalmente, o estilo escolhido é authoryear.
Para indicar os arquivos bib, usa-se o comando \addbibresourcefí<arquivo bib>) que
costuma estar no preamble, onde <arquivo bib> é nome do arquivo bib que deve incluir
necessariamente a extensão (como o .bib). Caso quer indicar vários arquivos bib, deverá
colocar um \addbibresource para cada arquivo bib.
O BibLaTeX suporta o campo url e logo, o endereço da internet devem ser colocados no
campo url em vez do campo note que é para o estilo antigo do BibTeX.
Após efetuar citações normalmente no documento, coloca-se o comando
\printbibliography no lugar onde quer que apareça a referência bibliográfica. \eja
o Exemplo 15.5 com Exemplo 11.3..
Exemplo 15.5: exl5-biblatex.tex
\documentclassfí{article}
\usepackage [brazil] ({babel}
\usepackage [
% backend=biber,
% bibencoding=utf8,
% natbib=true, % natbib compatible mode (citep, citet, etc)
style=authoryear, %4 estilo da citação no texto
% bibstyle=zauthortitle, % estilo da listagem pode ser diferente da citação
no texto
]J{biblatex}
\addbibresourcefexii-bibtex.bibl % não esquecer o .bib
\begin{document}
Para que a citação faça parte do texto (estilo textual), usa-se o comando À
verb+\textcitel)+ como em *“Por exemplo, \textciteíIndianTUG:2000,
Goossens:2004) explicam como usar o BibTeX''.
Para que ele não faça parte do texto, usa-se o \erbtWparenciteíl+, como em
*"Mldots recursos avançados de BibTeX \parencite[Cap.-13] íGoossens
:20043'"'.
O endereço da intenet devem ser colocados no campo \texttt{url} e data do
último acesso em \texttt{urldate}, seguindo o formato \textttiano-mês-dia
, onde ano é com 4 digitos.
\printbibliography
\endí{document}
Para que a citação faça parte do texto (estilo textual), usa-se o comando \\textciteí>
como em “Por exemplo, Tutorial Team (2000) e Goossens e Mittelbach (2004) explicam
como usar o BibTeX”.
Para que ele não faça parte do texto, usa-se o \wparencite{t}, como em “...recursos avan-
çados de BibTeX (Goossens and Mittelbach 2004, Cap. 13)”.
O endereço da intenet devem ser colocados no campo url e data do último acesso em
urldate, seguindo o formato ano-mês-dia, onde ano é com 4 digitos.
Referências
Goossens, Michel e Frank Mittelbach (2004). The BTEÊX Companion (second edition).
Reading, MA: Adilson-\esley,
Tutorial Team (2000). Online Tutorials on LaTeX. http://www.tug.org/tutorials/
tugindia/. Indian TÊEX User Group.
Quando usa o BibELaTeX, a citação textual (que {az parte do texto} será especificado pelo
comando \textcite que corresponde ao \citet do natbib. O comando \parencite produz
citação que não faz parte do texto (corresponde ao \\citep do natbib). O comando \cite
coloca como normal, sem parenteses, mas o detalhe dependerá do estilo. O \autociteíy
dependerão do estilo escolhido também.
Se quer que a referência bibliográfica conste no sumário, coloque
\phantomsection % se estiver usando o hyperref
\printbibliography [heading=bibintoc]
onde \phantomsection é necessário somente quando usa o pacote hyperref para que o link
do sumário para a referência bibliográfica aponte para a página correta.
O estilo padrão do BibLaTeX são numeric, alphabetic, authoryear, authortitle,
verbose, reading e draft, mas existem muitos outros disponíveis em http://mirror.ctan.
org/macros/latex/exptl/biblatex-contrib.
No estilo de BibLaTeX, foi adicionado o campo urldate para indicar a data de consulta
do documento eletrônico, além do campo url para indicar a localização de documentos
eletrônicos.
Para quem pretende criar o estilo novo, note que no BibLaTeX deve implementar tanto
o estilo de referências (como será impresso na referências) com o estilo de citações (como
aparece dentro do texto).
15.19 Siglas e glossários
A lista de síglas, símbolos e glossários podem ser criados pelo pacote acro como no Exem-
plo 15.6, cuja saída será omitida.
Exemplo 15.6: exl5-acro.tex
\documentclass [12pt] {article})
% Não precisa executar o comando externo, mas precisa compilar duas vezes.
% A lista será automaticamente ordenada.
\usepackage [brazilian] ({babel}
%ô\usepackagetarray,longtablel %4 para usar longtable na lista
\usepackageTttabularray) %4 para usar tabularray na lista
\usepackage{Ttacro} % lista de abreviaturas e siglas
% configurando
\acsetupt
%first-style = long-short, % modo "long (short)" (de{ault}
%Zlist/display = used, /é somente usados (de{ault} pode ser all ou used
% list/template=description, % lista de descrição (é default?)
pages/display = none % página impressa: first (default?), all ou none
F
% abreviaturas e siglas
\eclareAcronymíibgeYt
short = (IBGEL,
long = fInstituto Brasileiro de Geografia e Estatístical,
tag = {abrev},
\eclareAcronymíabntYt
short = (fABNTJ,
long = fAssociação Brasileira de \ormas Técnicas),
tag = fabrevl,
B
% Símbolos (explicação dos s{mbolos}
\eclareAcronymípiYt
short = ($\pi$),
long = fRazão entre circunferência e diâmetro),
tag = ísimbl,
first-style = short,
D”
% glossários (explicação do termo)
% Exenlificando o uso de plural não canônica também
\eclareAcronymíprimoYfí
short = fprimol,
short-plural-form = {primos}, % quando é só acrescentar 's' no final, não
é necessário
long = fé o número inteiro cuja único divisor é $\pm 1$, ele ou oposto
dele mesmo),
long-plural-form = ísão números inteiros cuja único divisor é $\pm 18,
ele ou oposto dele mesmo),
% list = íComo será exibido na lista)
tag = íglosk,
first-style = short, % como será na primeira ocorrência
d”
% se tiver a forma plural, poderá usar o \Acp e \acp para acessar.
KKl ll lll lll l lo lllh
% inicio do documento
\hlhhh llll lo h lalolo
\begin{document}
% siglas
\printacronyms [name=(Lista de abreviaturas e siglas), include=abrev, heading
=section*] % só o abrev
\acsetuptípages/display = {irst} % com página da primeira ocorrencia
% Símbolos
\printacronyms [name=(Lista de s{mbolos}, template=tabularray, include=simb]
% só o simb, formato tabelas
\tableofcontents
\sectioníSiglas e grossários)
% Usar \Ac para inicio do parágrafo (primeira letra em maiusuclo) e \ac para
meio do texto (todo em minusculo)
VW4c{abnt} adota a tabela no estilo \actibgel.
Definimos o \acípil como sendo
% NAcp e \acp acessa a forma plural.
Seja $p$, $q$, números \acp{primo}. Então
% \printacronyms [name=(fAbreviaturas, siglas, símbolos e signi{icados},
display=all, heading=section*+] % todas
\acsetupípages/display = none) % sem pagina das ocorrencias
\printacronyms [name=(Glossários), include=glos,heading=section] % só o glos
\endí{document}
A ordenação no acro é pela ordem alfabética dos rótulos (nomes) dos acronomos que
é o primeiro argumento de \eclareAcronym. No exemplo anterior, a diferenciação entre
siglas, símbolos e glossários foi feito pelo valor do tag, mas como permite tag genérico, pode
cometer erros de digitação. Assim as vezes, é preferível usar o pacote com maior rigidez como
o glossaries. O pacote glossaries também permite processar a ordenação pelo comando
externo makeglossaries para ter maior controle. O Exemplo 15.7 ilustra o uso (saída será
omitida).
Exemplo 15.7: exl5-glossaries.tex
\documentclass [a4paper,12pt]í{article}
\usepackage [brazil]{babel}
\{usepackageThyperref}
%usepackage{xtabl} % tabela longa configurável
\usepackage{acro} % necessário para opção acronym
46% Para evitar conflito com xtab: https://golatex.de/viewtopic.php?t=13108
\nakeatletter
VWônamedefíverOsupertabular.styX()
\nakeatother
\usepackage [nonumberl]ist=true,style=index,acronym]{glossaries} % Caso usar o
comando externo, sdrá o makeindex
%usepackage [xindy=(language=portuguese],nonumberlist=true,style=index,
acronym]{glossaries} % Caso usar comando externo, será o xindy (
recomendado)
% Ativando o uso de glossários
%"imakeglossaries % com comando externo (para compilar, execute o
makeglossaries)
\nakenoidxglossaries / com TeX (não precisa executar o comando
makeglossaries)
% comando para criar nova categoria
% \newglossary [<log-ext>] (<name>)(<in-ext>Y(<out-ext>Y<title>)[<counter>]
\newglossary [slg] (symbolskísyilísygYíLista de S{mbolos} % criando categoria
symbols
\hl ol ol ll llll llll
% Entradas de glossários
% abreviaturas e siglas
\newglossaryentryíibgeYt
name=(IBGE),
description=(fInstituto Brasileiro de Geografia e Estatístical,
type=zacronym,
b”
\newglossaryentryí{abnt}t
name=(ABNTJ),
%4sce=IBGE,
description=fAssociação Brasileira de \ormas Técnicas),
type=zacronym
t
% Símbolos (explicação dos s{mbolos}
\newglossaryentry{pi}
o
name=TVYensuremath{\pil}),
sort=(pil,
description=tRazão entre circunferência e diâmetro),
type=symbols
D
% glossário (explicação do termo)
\newglossaryentry{primo}t
name=Í{primo}),
plural=({primos}, % acessados pelo Glspl e glspl
description=fé o número inteiro cuja único divisor é $\pm 1$, ele ou oposto
dele mesmol,
l
%iglsaddall % adicionar todas entradas (padrão é somente usados)
\begin{document}
% siglas: com TeX
\printnoidxglossary [type=acronym,title=(Lista de abreviaturas e siglas),sort
=use]
% siglas: com makeglossaries
%Aprintglossary [typezacronym,title=(Lista de abreviaturas e siglas),sort=use
% Símbolos: com TeX
\printnoidxglossary [type=symbols,title=(Lista de símbolos+,sort=use]
% simbolos: com makeglossaries
Aprintglossary [type=symbols,title=(Lista de s{mbolos},sort=use]
% sumário
\tableofcontents
\sectioníSiglas e glossários)
% Usar \Gls para inicio do parágrafo (primeira letra em maiusuclo) e \gls
Caso desejar usar o comando externo, use o inakeglossaries e \wprintglossary no docu-
mento e chame o comando makeglossaries <nome do arquivo> onde <nome do arquivo>
é nome do arquivo sem a extensão .tex. Este comando efetua a chamada de makeindex ou
xindy com parâmetro adequado para efetuar ordenação.
16. Gráfico e Diagramas 182
Capítulo 16
Gráfico e Diagramas
Os recursos do ambiente picture do LaTeX é bastante limitado, mesmo que use o pacote
pict2e. Assim, costumamos usar os pacotes fora do base e required como o tikz. Neste
capítulo, vamos estudar alguns pacotes relacionados aos gráficos, que não são da base e
required.
16.1.  Misturando cores
O pacote de cores mais recomendados é o xcolor que estende a funcionalidade do pacote
color. Uma das extensões mais importantes do xcolor é a capacidade de especificar a
quantidade de cores e permitir misturar cores.
«
Para misturar cores, use o seguido de percentual. Por exemplo, \coloríblue!30) é
30% de azul.
No caso de \coloríred!30!yellowk é 30% de vermelho e restante (70%) de amarelo.
Em \coloríblue!20!black!30!green) é 30% da mistua de azul com preto e restante
(70%) de verde. Como a mistura de azul com preto é blue!20!black, 20% do total de 30%
que é 6% é azul e o restante que é 80% do total de 30% que é 24% é preto.
Para definir nova cor a partir do existente, use o comando \colorlet.
Por exemplo, \colorletímygreenkígreen!80!yellowk define nygreen como sendo a
mistura de 80% de verde e 10% de amarelo. \eja o Exemplo 16.1.
Exemplo 16.1: exl6-xcolor.tex
Texto pode ser colorido como em \textcoloríredl{vermelho} ou flcolorígreenY
verde). Pode ter fundo colorido \colorboxíyellow!30XfVlcolor{blue} teste).
Alguns exemplos da mistura de cores
\colorboxíblue!30Yí\hspace*{lcm}Y% 30% de azul
4 30% de vermelho e restante (70%) de amarelo
\colorboxíred!30!yellowkYí\hspace*{l1cm})
130% da mistura de azul com preto (20% deste que é 64 do total é azul e
restante 80% que é 14% do total é preto) e restante (70%) de verde
\colorboxíblue!20!black!30!green+\hspace*{1cm}>
& Defindo uma nova cor a partir do eristente
\colorlet{mygreen}ígreen!80!yellowY
\colorboxímygreenk{\hspace*f1cm}Y
Texto pode ser colorido como em vermelho ou verde. Pode ter fundo colorido teste .
Alguns exemplos da mistura de cores Ç. —
A seguir, cores básicos do pacote xcolor.
Tabela 16.1: cores aceitos em todos drivers no pacote xcolor
black | mma blue mpm | Drown | ms cyan —
darkgray | maam gray mm | Sreen | mee | lightgray
lime mem | magenta | mee | olive | eem | OT9D8O | ms
pink purple | meem | 70d | s teal —
violet |mee | \hbhite yellow | mum
Dependendo da especificação do driver, terão muito mais cores, mas é mais prático
trabalhar com cores básicos e suas misturas do que lidar com grande quantidade de nomes
para cores.
16.2 Criando ilustrações gráficas
Para criar ilustrações gráficas, um dos mais indicados é o pacote tikz [Tan15].
O pacote tikz possui muitos módulos (as extensões) que podem ser carregados pelo
comando \usetikzlibrary.
Nos exemplos a seguir, será assumido que tem o código do Exemplo 16.2 no preamble.
Exemplo 16.2: exl16-tikz-preamble.tex
\usepackage{tikz} % pacote gráfico
\usetikzlibrary{babell} % para compatiblidade com o pacote babel, requerido
por algumas bibliotecas como o cd.
\usetikzlibraryí{calc} % calc é para efetuar cálculos matemáticos ou
expressões em coordenadas
\usetikzlibrary(through) % circulo passando por ponto, por exemplo.
\usetikzlibrary{patterns} % preenchimentos
\usetikzlibrarylintersections) % intersecção entre caminhos
\usetikzlibrary{matrix} % matriz no tikz
\usetikzlibrary{cd} % diagrama comutativa
Os comandos gráficos do tikz sempre termina com ponto e vírgula. Ao compilar o código
sem ter terminado com ponto e virgula no trecho de tikz, pode travar o LaTeX. No caso de
estar usando o LyX que não salva antes de compilar, é importante que salve manualmente
antes de compilar. \ote que o “instant preview inset” do LyX não trava. \eja o Exemplo 16.3
para começar.
Exemplo 16.3: ex16-tikz:basico.tex
Poderá desenhar no modo \texttt{inline} como em \tikz \draw[{ill} circle (2
Pt);
ou \tikzí\draw (0,0) -- (1.5,0);) e também como figura independente
\begin{tikzpicture}
\draw[rounded corners=8pt] (0,0) -- (0,2) -- (2,2) -- (2,0) -- cycle;
\end{tikzpicture}
Poderá desenhar no modo inline como em eou . . etambém como [figura indepen-
dente
O comando \draw desenha o elemento. À forma como vai desenhar pode ser configurado
com o parâmetro opcional. “--” indica que vai ligar os pontos a esquerda com da direita
através de uma linha. Cores podem ser passado no parâmetro opcional do \draw. \eja o
Exemplo 16.4.
Exemplo 16.4: exl16-tikz-draw.tex
\begin{center})
\begin{tikzpicture}
\draw (-1,-0.5) -- (1,0.5); %Z segmentos
\draw (0,1) -- (1,1) -- (1,2) -- (0,2); %Z Linhas poligonais
\draw (2,0) -- (3,0) -- (3,1) -- (2,1) -- cycle; %À Linhas poligonais
fechadas (cycle conecta ao ponto iniciaal, {echando a curva}
\draw[rounded corners=8pt] (-1,-1) -- (1,-1) -- (1,-2) -- (-1,-2); % Quinas
arredondadas
\draw[red] (2,-1) |- (3,-2);% Conectando com linha vertical-horizontal
\draw[blue] (2,-1) -| (3,-2); % Conectando com linha horizontal-vertical
& ++(V) desloca o ponto anterior pelo (V), isto é, novo ponto é ponto
anterior + (V).
\draw (4,0) -- ++(1,1) -- ++(1,-1) -- cycle;
\end{tikzpicture}
\end{center}
/
Quando tem mais de um parâmetro opcional, coloque separado pela vírgula. \eja Exem-
plo 16.5.
Exemplo 16.5: ex16-tikz-parametro.tex
\begin{center})
\begin{tikzpicture}
/4 Epessuras: very thin, thin, thick, very thick
\draw[thick] (0,0) -- (1,1);
% Estilo: dashed, dotted
\draw[dotted] (0,0) -- (1,-1);
%5 Setas —->, <-, <->, etc
\draw[->] (0,0) -- (1,0);
/ Combinadas
\draw[color=blue,thick,->] (0,0) -- (-1,0);
\end{tikzpicture}
\endícenter+
A
Podemos definir e usar coordenadas, assim como efetuar alguns cálculos com coordenadas.
\eja o Exemplo 16.6.
Exemplo 16.6: exl6-tikz-coordenadas.tex
\begin{center})
\begin{tikzpicture}
\coordinate (A) at (0,0);
16.2. Criando ilustrações gráficas
\coordinate (B) at (1,0);
\coordinate (C) at (1,1);
\draw (A) -- (B) -- (C) -- cycle;
& interpolação linear das coordenadas
4 S(A)It!(C)$ sera interpretado como sendo (1-t)*(A)+t*(C)
\draw[dotted] (A) -- ($(B)!0.5!(0)$);
&h Interpolação linear com rotação
& rotacionado por angulo de 15 em torno de (B)
\coordinate (D) at ($(B)!1!15:(C0)$);
&h projeção ortogonal
%5 $(A)I!(B)!(C)$ sera pé do perpendicular abaixado de (B)
& sobre a reta determinada pelos pontos (A) e (C)
\coordinate (H) at ($(A)!(B)!(C0)$);
\draw (A) -- (B) -- (C) -- cycle;
\draw[blue] (B) -- (H);
% Para operar com coordenadas (múltplo ou a combinação linear), deverá
colocar entre '$'
\draw[dashed] (A) -- ($-2*(D)$);
/4 Coordenada com rótulos (ja desenha o rótulo quando de{ine}
\eoordinate[label=left:$X$] (X) at (3,0);
\coordinate[label=right:$Y$] (Y) at (4,1);
\draw (X) -- (Y); % ligando direto
\draw[dotted] (X) |- (Y); %Z ligando com vertical/horizontal
\draw[dashed] (X) -| (Y); % ligando com horizontal/vertical
% Coordenada polar.
% As coordenada polar é dado por (angulo:raio).
4 O ângulo é em graus.
\coordinate (u) at (45:1); %Z (angulo:raio)
\coordinate (v) at (90:2);
”& combinação linear das coordenadas
4 \ote que devem ficar delimitados pelo $
\draw[->] (A) -- ($1.5%*(1)+0.5*(v)$);
\coordinate (Z) at (Tsqrt(2)/2),t-sart(2)/2X); % para aplicar cálculo em
cada coordenada, coloque entre chaves
\draw[green] (Z) circle(1ipt);
\end{tikzpicture}
\endf{center}
Retângulos, círculos, elipses e arcos também podem ser desenhados. \eja o Exemplo 16.7.
Exemplo 16.7: exl6-tikz-circle.tex
\begin{center})
\begin{tikzpicture}
& retangulo com dois vertices opostos
\draw (0,-3) rectangle (3,-4);
\draw[rounded corners=5pt] (4,-3) rectangle (7,-4);
\draw[red] (-1.5,0) circle (0.5); % circlo
\coordinate [label=left:$A$] (A) at (0,0);
\coordinate [label=right:$B$] (B) at (1.25,0.25);
\draw (A) -- (B);
” Circulo passando por (B), com centro em (A)
\node [draw,circle through=(B),label=above:$c$] at (A) 1);
\coordinate (X) at (3,0);
\def localRadius{2}
\deflocalAngleí45>
h fazendo circulo na ponta inicial e rotulando como $X$
\draw (X) circle (2pt) node[anchor=south west] 1$X$);
/4 faz o arco e os circulos na ponta final. Rotulando o ponto final como $Y$
\draw (X) arc (O: localAngle:MlocalRadius) circle (2pt) node[anchor=south]
1$Y$);
& Elipse: Atento pelo uso de "and" quando indica os raios da elipse
\draw (5,0) ellipse (0.5 and 1.0);
\end{tikzpicture}
\end{center})
Para desenhar vários elementos, poderá usar o laço como no Exemplo 16.8.
Exemplo 16.8: exl6-tikz-foreach.tex
\begin{center})
\begin{tikzpicture}
/4 repetindo sobre elementos da lista
\foreach \x in 11,3,4,5)fNdraw[blue] (\x,2) circle(2pt);>
/4 repetindo no intervalo
\foreach \x in (1,...,10)\draw[red] (\x,1) circle(2pt);)
/4 repetindo no intervalo com passos (indicar dois primeiros e o último)
\foreach \x in 11,3,...,10) NMdraw[green] (\x,0) circle(2pt);
%4 contador com iteração em letras
& count=\lxi define contador de ítens como \xi
& quando tem mais de um comando, colocar entre chaves
/4 noode é usado para definir nó e colocar elementos na posição
\foreach \x [count = \xil in fa,...,c,A,B,...,DY
L
\draw[orange] (\xi,-1) -- (\xit+tO0.5,-1);
\draw (\xi+0.25,-1.5) node{ibx};
& iteração na lista de pares
& Parâmetro fill e draw indica a cor de contorno e de prenchimento
%4 node desenha um nó (elemento)
& draw no node faz contorno e fill preenche. O anchor é onde é a coordenada
indicada, visto do centro do nó.
\foreach \x/\y [count = \i] in 1£0/0, 1/0, 2/0, 0/1, 1/1, 2/1)
L
\draw[fill=yellow,draw=blue]l (\x,fNy-4I) node[anchor=south west,draw,{ill}f
i);
\endí{tikzpicture}
\end{center}
o (o) o o
o (o) o o o o o o (o) o
o o o o o
Podemos obter intersecções. \eja o Exemplo 16.9.
Exemplo 16.9: exl6-tikz-intersection.tex
\begin{center})
\begin{tikzpicture}
/4 desenhando e definindo coordenadas
\draw (0,0) coordinate (A) -- (2,3) coordinate (B)
(0,2) coordinate (C) -- (3,1) coordinate (D);
\fill[red] (intersection of A--B and C--D) circle (2pt);
4 Outra forma de obter intersecção.
\draw (4,0) coordinate (E) -- (6,3) coordinate (F)
(4,2) coordinate (G) -- (7,1) coordinate (H);
\fill[blue]l (intersection cs:
first line=((E) -- (F)),
second line=(1(G) -- (H))) circle (2pt);
/4 intersecção de 2 circulos ('nome path' {oi usado para nomear}
\draw[name path=circloal]l (1.5,-1.5) circle(1);
\draw[name path=circlob]l (2.5,-1.5) circle(1);
%4 ligando pontos de intersecção
\draw[blue, very thick, name intersections = fof = circloa and circloblX] (
intersection-1) -- (intersection-2);
A intersecção com múltiplos pontoos
\draw[name path=elipsei] (0,-4) ellipse(2 and 1);
\draw[name path=elipse2] (0,-4) ellipse(1 and 2);
& total=\k define 'lk' localmente (só para o comando atual) como número de
pontos. Para tornar '\k' global, acrescente '\pgfertrafiglobal | letkVWkt'
& 'nmame' permite mudar o nome do ponto da intersecção na qual o padrão é '
intersection'
\path[name intersections=fof=elipseil and elipse2, name=P, total=\kY]
pgfextrafiWglobal letNkNk];
& colocar circulos vermelho sobre pontos de intersecção
\foreach \i in (1,2,...,MkYNfill[red] (PNií) circle(2pt);)
& Se precisar, poderá ordenar seguindo o caminho 'caminho', pelo 'sort by=
caminho '
\end{tikzpicture}
\end{center}
&
&
Também podemos desenhar o gráfico das funções e curvas parametrizadas. \eja o Exem-
plo 16.10.
Exemplo 16.10: exl16-tikz-grafico.tex
\beginfí{center}
\begin{tikzpicture}Z[domain=-3.2:3.2]
Aldraw[ldotted] (-3.2,-1.2) grid (3.2,1.2);
\draw[->] (-3.5,0) -- (6.8,0) node[right] f$x$);
\draw[->] (0,-5.2) -- (0,2.2) node[above] f$y$3;
%4 'smooth' é para suavizar a curva pela interpolação
% O ângulo padrão será em graus. Para usar em radianos, acrescente " T" (
espaço seguido de 'r') no parâmetro da função trigonométrica
\draw[smooth,color=blue,domain=-pi-0.3:pi+0.3] plot (\x,ísin(\x r))) node[
below] 1$f (x)=\mathrm{sen}(x)$>Y;
/4 Curvas em coordenada polar. O ângulo padrão será em graus. A função deg()
converte radiano para grau (é mesmo que colocar sufixo " T")
\draw[smooth,color=red,domain=0:2*pi]l plot (fdeg(\x)k:\x) node[abovel f$\rho
(\\theta) =\theta$]);
& curvas paramétricas.
/4 poderá especificar o nome da variável em vez de usar o padrão que é "\\x"
