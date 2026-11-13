\draw[smooth,color=green,domain=-1.8:1.8,variable=\t] plot (fcosh(\t)),ísinh
(\t))) node[above] ($\textíramo de Jx 2-y"2=1$8);
\end{tikzpicture}
\end{center}
ramo de xº —yº =1
O Exemplo 16.11, está usando a função tabelada no arquivo de texto externo. Ele também
faz o uso do laço \foreach para marcar valores sobre eixos.
Exemplo 16.11: exl6-tikz-funcao-tabelada.tex
\beginfí{center}
\begin{tikzpicture}
% eixos
\draw[->] (-2.5,0) -- (2.5,0) node[right] f$x$);
\draw[->] (0,-0.5) -- (0,4.5) node[above] 1$y$);
” grid
\draw[dotted] (-1,0) |- (0,1) -1(1,0);
\draw[dotted] (-2,0) |- (2,4) -- (2,0);
/4 efetuando laço nos parâmetros para marcar escala
\foreach \x in (1-2,-1,1,2) % sobre eixo x
\node at (\x, O) [below] fNxl;
\foreach \y in (11,4) Z sobre eixo y
\node at (O,\y) [anchor=south west] (\y);
/7 gráfico da função tabelada no arquivo externo.
& \ote que tikz não reconhece notação científica
%h mo arquivo de entrada.
\draw[color=blue] plot[smooth] file flatex-via-exemplos-tabela.txtl node [
right] ($y=x"2$);
\end{tikzpicture}
\end{center}
O parâmetro smooth no plot é para suavizar a curva através de interpolação.
Para plotar mais confortavelmente a função tabelada, por exemplo, do arquivo csv que
pode ser exportado facilmente pela planilha eleltrônica, poderá usar o pacote pgfplots que
não será tratado neste texto.
Intersecção envolvendo a curva gerado pelo plot é dado no Exemplo 16.12.
Exemplo 16.12: exl16-tikz-intersection-plot.tex
\begin{center})
\beginftikzpicturel[scale=1.5] % podemos mudar a escala
\draw[domain=-0.3:12*pi+0.3l), name path=plotseno] plot[samples=100, smooth]
(\x, tsin(\x r)));
\draw[name path=eixox] (-0.3, O) -- ($((2 * pi+0.3X,0)$);
% total=lk define '\k' como local. Para tornar '\k' global, acrescente 'À
pgfextrat|global \letVklk)t'
\path[name intersections=fof=plotseno and eixox, name=P, sort by=eixox,
total=\k)] \wpgfextrafWglobal {letNkVNk};
\foreach \i in (11,2,...,\kE)INfill[red] (PNi) circle(2pt);)
\endí{tikzpicture}
\end{center}
Também podemos pintar, preencher com padrão e sombrear (pintar em degradê). \eja
Exemplo 16.13.
Exemplo 16.13: ex16-tikz-pintar.tex
\begin{center})
\begin{tikzpicture}[scale=1.5] % podemos mudar a escala
& ANfill' (pinta) e '\illdraw' (pinta e desenha o contorno) podem ser
usados para pintar. Outra forma é passar o parâmetro 'fill' para o
comando '\draw'.
\filldraw[fill=red!25,draw=blue] (0,1.5) rectangle (1.5,2.5);
\fill[color=red] plot[domain=pi:3*pi]l (\x,(2.5+sin(\x r))) -- cycle;
& '\pattern' preenche com padrão de preenchimento.
/4 Paorâmetro 'draw' é para desenhar o contorno
\pattern[pattern=north east lines, draw=blue] (3,0) circle (1);
& usando a transparência
/4 tt(coordenada) é a coordenada anterior somado com este
\draw[fill=blue] (5,0) rectangle ++(1,1);
\draw[opacity=0.5,fill=red] (5,0) circle (0.7);
& nó (texrto ou similar na posição)
\node [{ill}l=yellow,draw=blue,anchor=south west, circle, double]l at (7,0) t1);
/4 sombra é feito pelo comando '\shade' e sombra com contorno com 'lshadedrauw
' (igual a 'lshade' com parametro 'draw')
%& 'sombra' pode ser degrade e aceita o sintaxe do pacote 'ccolor' (cor!
percentual)
& No função, |x2 nãao funciona. Deve ser (\x) 2.
\shade [domain=-1:1,top color=blue!25,bottom color=red!25,draw=red] plot (\x
, 1-2+(\x)2));
\shade[top color=blue!25,bottom color=red!25,draw=red] plot[domain=2:4] (\x
, T-2+1.5x(\x - 3)72)) -- plot[domain=4:2] (\x
2 1-2.5+(\x - 3) 2)) -- cycle;
\shade [inner color=white,outer color=blue] (5,-2) circle (0.5);
/h fazendo tudo com '\draw'
\draw[red,pattern=north east lines,pattern color=red!25] (1,-3) circle (0.3);
\draw[fill=blue!25,draw=blue]l (2,-3) circle (0.3);
\draw[shade, left color=blue!25, right color=red!25,draw=blue] (3,-3) --
(3.5,-3) -- (3,-4) -- cycle;
\draw (3.25,-3.5) nodeí$x$);
\draw[fill=yellow,draw=blue] (4,-3) node[anchor=south west,draw,{ill}(1);
\end{tikzpicture}
\end{center}+
16.2. Criando ilustrações gráficas
OR ) .
Para traçar grades, existe o comando grid. O Exemplo 16.14 ilustra o seu uso para
produzir papel milimetrado, cuja saída será omitida.
Exemplo 16.14: exl16-tikz-grid.tex
\documentclass [a4paper] {article}
% AM4: 21cmx29.7cm
\usepackage [a4paper,lmargin=0.75cm,textheight=28.05cm,textwidth=19.55cm,
tmargin=0.75cm] {geometry}
\usepackage{tikz}
\pagestylefemptyY% sem enumeração da página
\begin{document}
\begin{center}
\begin{tikzpicture}
\draw [black!20, very thin, step=0.1cml (0,0) grid (19.5,28);
\draw [black!20, step=0.5cm]l (0,0) grid (19.5,28);
\draw [black!20, step=1.0cm, thick] (0,0) grid (19.5,28);
\end{tikzpicture}
\end{center}
\end{document}
O Exemplo 16.15 ilustra o uso de curvas.
Exemplo 16.15: exl6-tikz-curve.tex
\begin{center})
\beginftikzpictureY[scale=1.5] % podemos mudar a escala
& smooth liga suavemente
\draw plot [smooth] coordinates 1(0,0) (1,1) (2,0) (3,-1) (4,0) (5,1));
& smooth cyle fecha suavemente. 'tension' controla as tnsões nos pontos
\draw plot[smooth cycle,tension=1] coordinatesí(6,1) (6,0) (7,0) (7,1));
%4 indicando o ângulo de saida e de chegada para cada aresta (padrão é em
ralação ao eixo OX)
& Para ser relação ao segmento, use a opção 'relatíive'
\draw [red] (0,-2) circle(ipt) to[out=30,in=135, relative] (1,-3) circle(ipt
) to[lout=1-90),in=-45] (0,-4) circle(ipt);
/APara saida e chegada como ângulos suplementares e, é como relativo, poderá
usar o 'bend left/right', útil para diagramas
\coordinate (A) at (2,-2);
\coordinate (B) at (3,-3);
\draw[color=red] (A) circle(i1pt) to [bend left=45] (B) circle(ipt);
\draw[dotted] (A) -- (B);
/4 Curva de bezier pode ser produzido usando pontos de controle.
\draw (4,-3) .. controls (4.5,-2) .. (5,-3); % com um ponto de controle
\draw[dotted] (4,-3) -- (4.5, -2) circle(l1pt) -- (5,-3); Zmostrando o
controole
\draw (6,-3) .. controls (6.5,-2) and (7,-2) .. (7.5,-3); % com dois pontos
de controle
\draw[dotted] (6,-3) -- (6.5,-2) circle(1pt) -- (7,-2) circle(ipt) --
(7.5,-3); úZmostrando o controole
\endí{tikzpicture}
\end{center}
NA O
NAA
Para definir parâmetro opcional para toda figura, passe no parametro opcional do
tikzpicture, mas se quer configurar somente um trecho da figura, existe o ambiente scope.
\eja o Exemplo 16.16.
Exemplo 16.16: exl16-tikz-scope.tex
\begin{center})
\begin{tikzpicture}[color=blue] % cor padrão é 'blue'
\draw[->] (-1,0) -- (5,0);
\draw[->] (0,-0.5) -- (0,4);
/4 conteúdo é rotacionado por 45 graus
éh cor padrão é 'green'
\beginfscopel[rotate=45, color=green]
\draw (0,0) rectangle ++(2,1);
\draw (1,0.5) circle (tfsqrt(1+0.572)));
\endíscopeY
\node [draw=black,color=red] at (3,3) í$x$);
\end{tikzpicture}
\end{center}
Recorte na região é feito pelo comando \clip. Para cortar apenas uma parte da figura,
coloque no ambiente scope, como no Exemplo 16.17.
Exemplo 16.17: ex16-tikz-clip.tex
\begin{center})
\beginf{tikzpicture}
& scope delimita a parte que vai aplicar certa configuração (no caso,
delimitar o \clip)
\begin{scope}
\elip (-2,0) circle (1); % recortar no circulo
/4 valor a ser calculado deve ficar entre chaves (veja no lshade a seguir)
\shade [inner color=white, outer color=blue] (1-2+0.2),0.2) circle(tfi+sqart
(0.08))+); % regangulo preenchido
\end{scope}
\beginfíscopeY
\elip (1,0) circle (1); % recortar no circulo
\draw[pattern=north east lines] (1,0) rectangle ++(3,2); & regangulo
preenchido
\endíscopeY
%4 desenha o contorno
\draw (1,0) circle (1);
\draw (1,0) rectangle ++(3,2);
\endí{tikzpicture}
\endícenter+
Regiões usado no fill, pattern, shade e clip poderão ter mais de uma curva, ou curva
que auto interceptam. Por padrão, a região a ser considerada será pela regra 'non-zero rule”.
Nesta regra, para determinar se P está no lado de dentro, traça-se o raio saindo de P em
alguma direção e para cada cruzamento, atribui '+1º se a orientação do raio com a direção
da curva for positiva e "-1º caso for negativa. Se a soma destes números forem zero, estará no
lado de fora. Se for não nulo, estará no lado de dentro da região.
Nos círculos e elipses, a orientação é positiva (rotação anti-horária). No caso do retângulo,
depende dos vértices. Assim, para obter a região anelar delimitados pelos dois circulos, não
vai funcionar por ter 2 ciruclos na mesma direção. Para contornar este problema, poderá
alterar a regra de detecção da região para 'even odd rule' que considera o P como ponto
exterior quando o raio partindo de P em alguma direção interceptar o caminho número par de
vezes (e interior, se interceptar número impar de vezes). Para isso, basta passar a opção 'even
odd rule' no parâmetro opcional. No caso do \clip que não aceita o parametro opcional,
deverá passar para o parâmetro do scope (ou do tikzpicture). \eja o Exemplo 16.18.
Exemplo 16.18: ex16-tikz-region.tex
\begin{center})
\begin{tikzpicture}
” região com dois contornos
\fill [color=green] (1,0)--(3,0) -- (2,1) -- cycle
(0, -0.5) -- (2,1.5) -- (4, -0.5) -- cycle;
/& 'even odd rule' permite pegar região entre dois circulos
\draw[fill=yellow, draw=blue, even odd rule] (6,0) circle(0.5) (6,0) circle
;
\begin{scope}
\elip (1,-2) circle (0.5) (0,-3) rectangle ++(2,2); % recortar no fora
circulo e dentro do retangulo
\draw[pattern=north east lines] (0,-3) rectangle ++(3,2); % regangulo
preenchido
16.2. Criando ilustrações gráficas
\endíscopeY
\beginfscopel [even odd rule]
& \elip (3,-3) rectangle ++(3,2) (3,-2) circle(0.5) (4,-2) circle(0.5);
\clip (4,-3) circle(0.5) (5.5,-3) circle(0.5) (4.75,-3) circle(1.5);
\draw[pattern=bricks] (3,-5) rectangle ++(3.5,4); % regangulo preenchido
\endíscopeY
\end{tikzpicture}
\endí{center}
O
ITuhnHr
Na matriz do tikz, podemos desenhar sobre ele. \eja Exemplo 16.19.
Exemplo 16.19: ex16-tikz-
matriz.tex
\begin{center}
\begin{tikzpicture}
\matrix (A) [matrix of math nodes,left delimiter=[,right delimiter=11) ]
t(1&2&-1&5W
O & | [draw=red,circle]l 3 & 2& 1 W
O & -2 & \phantomí-Y2 & -4 W
4 separando a matriz da parte aumentada
\draw[thick,dashed,blue]l (A-1-3.north east) -- (A-3-3.south east);
%4 limitando a parte escalonado
\draw[thick,dotted,blue] (A-2-1.north west) -- (A-2-1.north east) -- (A-3-1.
south east);
& onde vai colocar a seta para pivô
\eoordinate (P) at ($(A-2-1)!-2!(A4-2-2)$);
\coordinate (Q) at ($(A-2-1)!-1.31!(A-2-2)$);
/4 colocando a seta na linha de pivô
\draw[->] (P) -- (Q);
\node at ($(P)!-1.2!(Q)$) fpivô);
\end{tikzpicture}
\end{center})
12 15
pivô — 0 2 E 1
0:—-2 2:H4
Caso precisar de recursos mais avançados para matriz, poderá usar o pacote nicematrix,
baseado em tikz.
O diagrama comutativo é uma espécie de tabela com comando \ar para desenhar setas.
\ar é seta e o primeiro parâmetro opcional dele é para que lado vai a seta (pode ser combi-
nado). “r” (direita), “1” (esquerda), “d” (para baixo), “u” (para cima). Também pode usar o
“to=<destino>” para indicar a célula diretamente. O rótulo, caso exista, deve ser delimitado
entre aspas.
No Exemplo 16.20, foi usado o comando \circlearrowleft do  pacote
amssymb. Se estiver usando o unicode-math no X4LaTeX/LuaLaTeX, poderá
definir como sendo \acwopencirclearrow. Para isso, coloque o comando
\providecommandfVcirclearrowleftIí\acwopencirclearrow) no preamble do docu-
mento.
Exemplo 16.20: exl6-tikz-diagrama.tex
\begin{center})
\begin{tikzcd}
A \ar[r, "\phi"] \ar[d, red] \ar[to=2-2, phantom, "\circlearrowleft"
description] & B \ar[d, "\psi" red]l MW
C \ar[r, red, "\varphi" red, "\eta" íswap, bluel)] & D
\end{tikzcd}
” setas curvas
\begin{tikzcd}
A \ar[r, "\phi"] \ar[rr, "f", bend left, red]l & B \arl[r, "\psi", Rightarrow]
& C \ar[loop right]
\end{tikzcd}
/4 cruzando: necessário para diagrama 3D
\begin{tikzcd}
A \arrow[dr] & B \arrow[dl, crossing over]l W
C&D
\end{tikzcd}
\end{center}
CT>D C D
O comando \ar (ou \arrow) traça a seta de acordo com o seu parâmetro. O primeiro
argumento é para onde vai (d = para baixo, r=para direita, l=para esquerda, u=para cima).
Também pode indicar origem e/ou destino pelo índices ou rótulos, usando from e/ou “to”).
As bibliotecas para tikz é extensa, cobrindo vários tipos de desenhos e diagramas. Se
precisar de algo desse tipo, consulte o material para ver se já tem uma biblioteca pronta. Por
exemplo, usando a biblioteca angle, poderá marcar facilmente os ângulos pelo uso de pic,
ou usar a biblioteca decorations para colocar elementos ao longo do caminho, inclusive um
texto.
Além de bibliotecas do tikz (módulos de tikz carregados por \usetikzlibrary), existem
vários pacotes independentes que adicionam funcionalidades no tikz tais como tikz-euclid
para ser usado na elaboração de desenhos geométricos, pgfplots para desenhar gráficos de
funções ou de dados em 2D ou em 3D, etc. que não vamos discutir aqui.
16.3 Mais um pouco sobre sobreposição
Para escrever /desenhar sobre a figura externa pronta, com frequência, existe o pacote overpic
que abre o ambiente picture e ajusta o \unitlength ao mesmo tempo. O padrão é usar o
valor de \unitlength como 1% da maior escala da imagem. O pacote implementa o ambiente
overpic que aceita somente o nome da imagem externa e Overpic com “O' maiúsculo que
permite colocar elemento qualquer no lugar da iamgem externa.
O Exemplo 16.21 produzirá mesmo efeito do Exemplo 9.9.
Exemplo 16.21: exl6-imagem-sobreposicao.tex
\beginfí{igure}) [htbp!]
\center
% opção grid pode ser usado para produzir grade sobre a figura, facilitando
encontrar a posição correta sobre a imagem
% Overpic com 'O0' maiúsculo premite colocar qualquer elemento, em vez de ser
somente imagem externa
%beginfOverpick[grid,tics=10] MVinludegraphics [width=0.45)]linewidth] (latex-
via-exemplos-{igl}
% \put(35,45) (NLARGE $e {Npi i}+1=0$>
% \end{Overpic}
\begin{overpic} [width=0.45)]linewidth] (latex-via-exemplos-{ig}
\put (35,45) (NLARGE $e {Npi i}+1=0$>
\endí{overpic}k
\captionfUsando overpicWlabelífig:overpickl)
\endí{igure})
Para sobrepor elementos mais complexos sobre a imagem, é melhor usar o ambiente
tikzpicture do pacote tikz (do que ambiente picture), como no Exemplo 16.22.
Exemplo 16.22: exl6-imagem-sobreposicao-tikz.tex
\begin{figure}) [htbp!]
\center
\def \picunitíOoO.45\textwidth) % unidade nesta figura
\begin{tikzpicture} [x=\picunit, y=\picunit]
\node [anchor=south west,inner sep=0] (image) at (0,0)
TfVlincludegraphics [vidth=\picunit] (latex-via-exemplos-{igl};
/ grid (grade) serve para localizar a posição correta sobre a imagem
Aldraw[step=0.1] (0,0) grid (1,1);
\node [anchor=south west,inner sep=0] at (0.35,0.45) TNLARGE $e"fNpi i
++1=0$);
\endí{tikzpicture}
\endí{igure})
17. Produzindo Poster e Slides 202
Capítulo 17
Produzindo Poster e Slides
17.1 Poster
Para quem quer produzir o poster (cartaz) diretamente no LaTeX, a maneira mais prática é
diagramar com um quarto (metade de largura e altura) do tamanho desejado, usando letra
12pt. Após finalizar, amplie o poster para produzir no tamanho real. Com tal procedimento,
os caracteres serão ampliados para equivalentes a 24pt. Use a fonte Sans Serif para poster.
Caso de precisar usar a fonte romana, aumente o tamanho de caracteres em torno de 20% a
mais.
Por exemplo, para poster final de 100x120cm, dimensione para 50x60cm, para dimensão
final de AO, dimensione para A2, etc.
Para criar “layout” de divisão em colunas e similares, use o ambiente multicols (do
pacote multicol) e minipage. O enfeite das “caixas de texto” podem ser feitos usando caixas
como o \\fbox.
No Exemplo 17.1, foi usado o pacote l1ipsum para preencher o espaço com texto para ver
como fica a aparência do poster.
Exemplo 17.1: exl17-poster.tex
\documentclass [12pt] {article}
% 12pt torna 24pt após dobrar a dimensão do documento usando jPDFTWeak ou
poster
\usepackage [T1] {fontenc} % codificação da fonte em 8-bits
% \usepackage [ut{8} {inputenck} % acentuação direta em utf-8 (padrão)
\usepackage [brazil]{babel} % em português brasileiro
\usepackageTlmodern) % Fonte Latin Modern (Computer Modern com extensao
latin)
%\usepackage{mlmodern} % Fonte \ew Computer Modern com espessura Book (entre
normal e negrito) para facilitar a leitura
\usepackage{lipsum} % para preencher o espaço (para teste)
% acerto de margens usar metade da dimensão final em cada medida
% para poster final de 100x120cm
% \usepackage [paperwidth=50cm,paperheight=60cm, margin=0.7cm,] {geometry}
% para poster final em AO
% \usepackage[a2paper, margin=0.7cm]{geometry}
% Poster em 90cmx120cm
\usepackage{geometry}
\geometry(paperwidth=45cm,paperheight=60cm,
lImargin=0.7cm,rmargin=0.7cm,tmargin=0.7cm,bmargin=0.7cm)
\usepackage{multicol} % usar varias colunas
\usepackage{Ttgraphicxl} % usar gráficos
\usepackage [usenames] txcolor) % usar cores
\usepackagetfancyboxl % para molduras adicionais nas caixas
\usepackageTsansmath{onts} % sans serif extension to computer modern (use
sans serif na fórmula matemática)
\usepackage [bibencoding=utf8,backend=biber,style=authoryear-comp] {biblatex}
\addbibresourceílatex-via-exemplos.bib)
% espaçamento entre colunas
\setlengthfí\columnsep|í1cmy
% \setlengthfWcolumnseprulel{ipt} %Z separador de colunas
% No poster, nao costuma usar a indentação
\setlengthfWparindentIí{Opt} % sem indentacão
% comando para colocar título customizado
\setlengthfWfboxsep+íOptk % bordas grudadas no conteúdo
%44 caixa de títulos: versão colorida.
\newcommandí \maintitlebox)[1] flshadowboxfYcolorboxíyellowkí\parboxtO.99
columnwidthY(%1))))
\newcommandí \titleboxk[1] (\fboxfVcolorboxíyellowkTNparboxt1.OVYcolumnwidth
HH1
%44 caixa de títulos: versão monocromatica.
% \newcommandí\maintitlebox)[1] fNYshadowboxtWparboxtO.99\columnwidth>tTit133>
% \newcommandí\titlebox)[1] (\fboxtNparboxt1.OYcolumnwidth){H1}))
\renewcommandVfamilydefaultíls{default} % Usar sans serif por padrão
\pagestyle{empty} % sem enumeracao das páginas
\beginf{document}
% \large % aumentar um pouco a letra (apesar de não ser necessário)
\naintitleboxí
\begin{minipage}[t] 1O.98|textwidthy
\begin{center}
\space{ipc}
\Huge
\ofseries
% poderá acrescentar logo, usando inludegraphics
% \includegraphics [height=4pc] [logo-esquerda)
%4 \hfill
Poster de Teste
% \hfill
% \includegraphics [height=4pc] [logo-direita)
\end{center}
\space{ipc}k
\end{minipage}
Y %4 maintitlebox
\space{ipc}
\begin{center}
filhuge Sadao Massago
N
fiNlarge DFQM-UFSCar| (Universidade Federal de São Carlos)
web: \\textttíhttp://www.dm.ufscar.br/$\sim$sadao) N
e-mail: \textttiísadaoCufscar.br)
\end{center}
\space{2pc}
% \hrule \space{ipcl} \hrule
% \setlengthWcolumnseprulef.4pt)
\begin{multicols}(3) % 3 colunas, por ter linha comprida
\section*fWtitleboxíParte 1)
\lipsum[1-2]
\section*fWtitleboxíparte 2)>
\lipsum[1-5]
\section*fWtitleboxíParte 3)
\lipsum[1-6]
\section*fWtitleboxíParte 4)
\lipsum[1-4]
\section*fWtitleboxíParte 5)
\lipsum[1-7]
\section*fWtitleboxíParte 6))
\lipsum[1-3]
\end{multicols} % 2 colunas, por ter linha comprida
\space{ipc}k
\hrule
%idoubleboxt
%Cibegin{minipage}(O.99 textwidthy
%AVNvspace{2pc}
\setlengthVWcolumnseprulef.{5pt}
\begin{multicols}(3) % 3 colunas
AtitleboxíObservação final:)
%ZNlipsum[3]
\nocitet*x
\printbibliography [title=\titleboxíReferências)]
\end{multicols} % 2 colunas
%vspacetíipck
%\end{minipage}
%) % \doubleboxí
\end{document}
Sadao Massago
prqursca o
E
— B
BNT a6
ec
ESTESA
Se quer usar LaTeX para produzir material publicitário como posters, jormais, revistas e
livros ilustrados com a qualidade profissional, o pacote flowfram é o pacote adequado. Além
da sua qualidade final, a facilidade e a versatilidade costumam ser superiores aos pacotes
similares. \eja a Seção D.5 para exemplo.
Para quem estiver acostumado a usar o pacote beamer (pacote para produzir slides de
apresentação), o pacote beamerposter é interessante para produzir poster com cara de apre-
sentação em beamer.
Em vez de usar o LaTeX, poderá usar aplicativos gráficos para criar poster ou similares.
Para posters científicos, ideal é usar o aplicativo que tenha suporte ao LaTeX como no caso do
editor gráfico inkscape e editor para publicações scribus, ambos livres e multi plataforma.
Para aumentar o poster diagramado com fontes 12pt, como do Exemplo 17.1, podemos
usar o aplicativo livre e multi plataforma jPDFTweak que é um aplicativo para pós produção
de documentos PDF, disponível em http://jpdftweak.sourceforge.net/.
Entre várias funções importantes deste aplicativo, existe a função de redimensionamento
para ampliar o poster.
No jPDFTweak:
1. indique o arquivo de entrada em “input”.
2. indique o arquivo de saída em “output”.
3. em [page sizel, cheque o “[v] scale pages” e selecione o tamanho da página como “Page
size” = “escala dobro do original”.
4. clique no [run]
Observação: Para dobrar a escala no papel ISO, escolha dois números para baixo. Por
exemplo, se o original estiver em A2 landscape, escolha AO landscape. Caso a medida
do papel estiver em centímetros, dobre o valor e em seguida, multiplique por 72/2.54 para
converter em postscript point que jPDFTweak usa na largura e na altura do papel. Por
exemplo, se o original estiver com 45 cm x 60cm, vamos colocar 90 x 72/2.54 = 2551.18 e
120 x 72/2.54 = 3401.57 para largura e altura respectivamente.
\ote que, para imprimir na gráfica, basta levar o arquivo e dizer o tamanho do poster que
costuma ampliar na hora de imprimir (ou seja, não é necessário levar arquivo redimensionado).
A largura mais utilizada para poster na gráfica é de até 1 metro, mas depende da gráfica, o
que vale consultar antes de finalizar o poster. Outro ponto a ser considerado no orçamento
é o fato do poster com elemento colorido ser mais caro do que poster totalmente em preto e
branco.
17.2 Slides
Para criar apresentações, costuma usar a classe beamer.
Algumas opções da classe beamer são tamanho da fonte (normalmente usa 12pt, embora
suporta o tamanho maior), handout (para impressão. Ignora o overlay), notes (incluir
notas) e notesonly (somente notas).
A classe beamer usa uma área reduzida com letra normal que será ampliado quando
projetar na tela. Assim, costuma usar a fonte de tamanho 12pt.
Nesta classe, cada tela de slide será delimitada pelo ambiente frame. Tem a versão
comando do frame também, para ser usado quando tem poucos comandos contidos nele,
como no caso de título e sumário.
