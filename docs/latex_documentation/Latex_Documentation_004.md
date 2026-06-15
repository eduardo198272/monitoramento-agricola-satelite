Para casos em que delimitadores auto ajustáveis não funcionam como esperado, poderá
indicar o tamanho manualmente, colocando a especificação do tamanho antes do delimitador.
O especificador do delimitador grande na ordem crescente são: \big, \Big, \\bigg e \Bigg.
\eja Exemplo 5.5.
Exemplo 5.5: exO05-delimitador-grande.tex
N[ \oigg( \Big(x + (y - 2) \Big) + w \bigg) M
V[ Mlambda \bigg( f(x+0) + NVcdots f(x n) NM
NE + \sum fi=0X"n x i \bigg) V.
((a+=2)+o)
A(f(erO) + f(x,)
n
i=0
A “chave” sobre (ou abaixo) da fórmula é colocado pelo \overbracee \underbrace. \eja
Exemplo 5.6.
Exemplo 5.6: ex05-bracos.tex
V[ \overbraceí1i+1+\cdots+1+ ín-\textívezes )) = n M
V[ NVunderbracefk+k+NYcdots+kI fn-\text{vezes}) = nk N]
n—vezes
—— ——
l+l1+-+l=n
k+k+- +k=nk
n—vezes
Alguns casos de integrais múltiplas estão ilustrados no Exemplo 5.7.
Exemplo 5.7: exO5-integrais.tex
Integrais múltiplas
N
\int a”b f(x)L,dxN; \iint R f(x.y)N,dkxdy N; \iiint B f(x,y,2)N,dxdydz N]
\INidotsint f(x 1,M1dots,x n)V.dx 1lcdots dx n NJ
Integral de linha $\oint f(x)N,dx$.
Integrais múltiplas
/abf(m)da; //Rf(z.y)dzdy //Bf(z,y,z)dmdydz
Integral de linha & f(x) d.
\ote que cdots produz três pontos no meio, enquanto que \ldots produz três pontos
embaixo. Os comandos , e V; inserem espaços extras na fórmula. \eja a Seção 12.2 para
detalhes.
pequenos espaços
5.4 Quebrando fórmulas em várias linhas
Para quebrar uma equação enumeração em mais de uma linha, podemos usar o ambiente
split. ou o aligned.
Para criar alinhamento na equação quebrada, coloca-se o & no ponto de alinhamento,
como no Exemplo 5.8.
Exemplo 5.8: ex05-split.tex
N
\beginfísplity
2x+y=3 W
x-y=1l+a
\end{split}
\i
\begin{equation}
\textísistema 1:) MVleftM
\obegin{split}
2x+y&=3 N
x-y&=l+a
\end{split}
\right.
\end{equation}
\beginfequationY
\textísistema 2: \leftWMt
\begin{aligned}
2x+y&=3 W
x-y&=1+a
\end{aligned}
\right.
\end{equation}
239 +y=3
x—-y=l+a
2r+y=3
sistema 1:% , (1)
x—-y=l+a
2x +y=3
sistema 2:% ' (2)
x—-y=l+a
Podemos tentar usar o ambiente cases para definir sistema de equações como no Exem-
plo 5.9, mas isto não efetua o alinhamento (na posição de igualdade). Não podemos usar o
&, pois o alinhamento seria efetuado de forma próprio para colocar condição da expressão
e não a equação. Assim, é aconselhável usar o split ou aligned dentro das fórmulas (usar
equation caso queira enumeração) em vez de cases.
Exemplo 5.9: exO05-cases-aligned.tex
\begin{equation}
\beginf{cases}
2x+y=1 W
x-y=l+a
\end{cases}
\endí{equation}
\begin{equation}
\beginf{cases}
2x+y&=1 N
x-y&=1+a
\end{cases}
\end{equation}
\begin{equation}
\leftWM \begin{aligned}
2x+y&=1 \W
x-y&=1+a
\endí{aligned} \right.
\endfequationyY
íZw——y:l 3)
x—y=lt+a
íl&v——y =1 (4)
x—-y =l+a
í2z+y=1 &)
x—-y=l+a
Existem diversos ambientes estilo equations. Vamos ver alguns deles:
O ambiente gather produz várias equações, todas centralizadas. Para inibir enumeração
em algumas delas, coloque o \nonumber na equação que deseja remover a enumeração (antes
da quebra de linhas). \eja o Exemplo 5.10
Exemplo 5.10: ex05-gather.tex
T+yY+z=1 (6)
T-yY+z=2 (7)
r+y=0 (8)
rc+y+z=1 (9)
rc—-yY+z=2
I+y=0 (10)
Para equações em várias linhas, com pontos de alinhamento, usa-se o align que pode
inibir enumeração de algumas equações como em gather.
Quando escreve uma expressão grande quebrado em várias linhas, as vezes é legal tabular
cada linha para direita. Este efeito pode ser obtido pelo multline, como do Exemplo 5.11.
Exemplo 5.11: exO05-multiline.tex
\begin{align}
xt+y+z&=1 N
x-y+z&=2 \nonumber N
x+y&=0
\endífaligny
\begin{multline}
Ax+Ay+Az=
a {11}x 1+\cdots +a finkx n+lcdots +\edots +a ínilkx l1+\cdots a ínnkkx n NW
a t11)y 1+\cdots +a finky n+\cdots +\cdots +a íniky lI+\cdots a ínnky n NW
a {11}z 1+\cdots +a finkz n+\cdots +\cdots +a fnilkz l+\cdots a ínniz n
\end{multline}
I+yYy+z=1 (11)
c—-yY+z=2
T+y=0 (12)
Ax + Ay + Az AJ9L] T HAn FT TAl FdnA
A1U H +AandR TT an tT Anndn
ah +o+aõã to +o taa toanto (13)
Para mais ambientes deste estilo, consulte o manual de AMSLaTeX. [GMSO04, Cap. 8]
explica bem os ambientes e comandos matemáticos do AMS (que está sendo discutido parci-
almente neste cap{tulo}.
\ote que, todos os ambientes do estilo equation (equation, gather, align, multline,
etc) apresentam a versão com * na qual remove toda enumeração (versão * equivale a colocar
\nonumber em todas equações). \eja Exemmplo 5.12.
Exemplo 5.12: ex05-align-star.tex
\beginí{align*}
x+y+z&=1 N
x-y+z&=2 W
x+y&=0
\endfalign*y
rI+y+z=l1
r—-yY+z=2
xT+y=0
Para equações de várias linhas, uma linha independente de texto pode ser inserido pelo
comando \intertext.
\eja Exemmplo 5.13.
Exemplo 5.13: exO5-intertext.tex
\begin{align*}
f (x) &=2x+y+3x
\intertextíjuntando o $x$ e usando $y=2x$, temos)
&F5Xx+y N
& = TX
\endíalign*>
f(x) =27 +y+3x
juntando o x e usando y = 2x, temos
= 5t +y
=Tx
\ote que não precisa colocar W antes e depois do \intertext.
5.5 Nome sobre setas e delimitador empilhados
Para colocar nome nas setas, usa-se o \stackrel.
Para colocar limitante de soma, produto, etc em duas linhas, usa-se o \substack.
Para colocar embaixo, poderá usar o \underset.
Simplesmente empilhar um sobre outro, usa-se o \atop.
\eja Exemplo 5.14.
Exemplo 5.14: exO05-stackrel.tex
NC X \stackrelí{\Ntol} \N]
NE f : \undersetíx+(X) \undersetí\mapsto-í\to) \undersetif(x)X(\Y N
NL L i(x)=\prod fisubstackíj=0 W ilne j+) \fracíx-x jkix i-x j) N
NL X \atop Y MJ
-
ds
b<
s
n
s
=
&
S
Ú
|
&
.
KT
so
[x
<
Binomial de \ewton pode ser produzido por binom como no Exemplo 5.15.
Exemplo 5.15: ex05-binom.tex, parte c
Regra de Pascal:
5.6 Subequações
Podemos usar subequações no LaTeX como no Exemplo 5.16.
Exemplo 5.16: ex05-subequacao.tex
TP +Y<l (14a)
y>0O (14b)
As equações 14a e 14b determinam a parte superior do disco.
5.7 Acentuação no modo matemático
Na matemática, usa a acentuação para produzir nomes relacionados ao original tais como
f e f relacionados a f. Tais acentuações difere do modo texto. Alguns desses acentuações
comumente encontrados na matemática são: acento circunflexo, til, ponto, seta e barra.
Além das acentuações, tem também o caso de colorar expoentes como em f e f* que são
relacionados com f. O LaTeX permite produzir estes e outros acentos e símbolos usados como
expoentes especiais na matemática.
comando exemplo
\hat
\tilde
\\dot
\\ddot
\\dddot
\\ddddot
\bar
\ec
d
si a: S: S S
\grave
\acute
\breve
\check
\overset(\circYl)
Alguns deles, como barra, requer alongamento quando tiver mais de um símbolo (ou
A RD Q8 A Q
Qo
símbolo grande). Neste caso, deverá usar versão ajustáveis:
comando exemplo
\widehat abe
\widetilde abe
\overline ab
\overrightarrow AB
\overleftarrow ab
\overleftrightarrow AB
As vezes, precisamos colocar embaixo, como sublinhar.
comando exemplo
\\\underbar abe
\underline abc
\underrightarrow AB
\underleftarrow ab
\underleftrightarrow AB
Colocar a direita (ou como expoente)
comando exemplo
' f
“ANprime f
“"Abackprime f
MVNast f
Acirc 20º
“llcorner x-
“ulcorner x
“\perp 7
Não confundir apóstrofos (usado na derivada { de f, por exemplo}, com o acento agudo.
\ote que i e j sem o ponto é produzido por \imath e \jmath, respectivamente como em ? e j.
\eja o Exemplo 5.17.
Exemplo 5.17: ex05-acentos.tex
NL \hat{f}, \tilde{f}, \dotíxk, \dddot{x}, \baríyl, \overset{lcircHX}, \vec
tv) U
NVC \widehat{ABC}, \overrightarrow({AB}, M
V. f', fONast, 207\circ, \ecívlTNperp M
V[ \ecVYimath \times \ecWjmath=\vec kN]
f!f!i7.x“7g7*ºxãõ
ABO, AB,
F $200,6
ixj=k
Na matemática, colocar “/” sobre o símbolo significa a negação do símbolo. Apesar
de vários símbolos de negação comumente usados estão definidos, pode precisar produzir a
negação de alguns símbolos específicos. Para produzir tal negação, usa-se o comando \not.
Por exemplo, inotWsubset produz &.
\eja o Exemplo 5.18.
Exemplo 5.18: ex05-negacao.tex
Alguns comandos de negação já existentes.
\\linexists X : X \in X U
\iNforall X, X \wnotin X M
NE X \neg MOXAY N
Produzindo com comando \verb+\not+.
NL X \notisubset Y \implies X \cap Y \neq XN
NEX : X \notini x N
\lr \notWperp s M
Alguns comandos de negação já existentes.
AX:XEX
V. , X ÉEX
XxF(X)
Produzindo com comando \not.
XdY=—> XNYEFX
X:X$x
rls
6. Definindo Comandos e Ambientes 43
Capítulo 6
Definindo Comandos e Ambientes
Vamos ver o básico da definição de comandos e ambientes
6.1 . Definindo comandos
Quando tem o comando longo a ser digitado, poderá definir um comando que funciona como
um atalho. Por exemplo, inathbbíR* toda vez que queremos escrever o conjunto dos números
reais é cansativo. Definir comando para vnathbb{R} permite também, trocar facilmente pelo
outro comando de fontes no lugar de \vmnathbb.
Para definir um  comando, usa-se o  \newcommand. Por exemplo,
\newcommand(f \Rset ) imathbb{R}) define o comando NRset que será substi-
tuído pelo \mathbb{RY} quando é compilado. Se quer que \Rset funcione
tanto dentro como fora das fórmulas, poderá usar o \ensuremath como em
\newcommandí \Rset | \ensuremathfimathbb{RI}). \ote que aqui foi evitado de defi-
nir como sendo \real, pois o comando \natural já está definido no LaTeX.
O nome do comando não deve ter números. Por — exemplo,
\newcommandT NR2)f$\mathbb{R} 2$ resulta em erros, pois o nome do comando NR2
contém o número.
Analogamente ao caso de \\Rset, \newcommandí\sen+í\mathrmísent+ define o comando
para função seno. Em geral, para definir nome da função, usa-se o \eclaremathOperator
do pacote amsmath tal como \eclaremathOperatorí\senk+{sen} em vez do wnewcommand.
Ele coloca automaticamente o vmathrm no segundo argumento.
O comando \newcommandfVargmink+fWmathoptWmathrmíarg,min))) define o comando
\argmin para função arg min, mas por ter wnathop, o limitante será colocado embaixo em
vez de ser colocado como fÍndice. \ote o uso de “N,” para inserir pequeno espaço entre arg
emin. Para facilitar, o pacote amsmath define a versão com “*” de \eclaremathOperator
que coloca o nome da função dentro do vmathrm e wmathop.
Quando já existe o comando, poderá redefinir usando o \yrenewcommand.
Se não sabe se existe o comando, poderá usar o \wprovidecommand que define o comando
caso não existir.
Estas definições de comandos costumam ficar no preamble do documento. \eja o Exem-
plo 6.1.
Exemplo 6.1: ex06-newcommand.tex
\documentclass [12pt,a4paper] {article}
\usepackage [T1] {fontenc}
\usepackageíTamsmath,{amssymb}
\newcommandí \Rset \T \ensuremathfWmathbb{RY}>
/AlDeclareMathOperatortílsentísent % modo amsmath
\newcommandfAWsen+íimathrmísenk+Y) % modo normal (sem amsmath)
/AlDeclareMathOperator*{largmintiargmint} % modo amsmath
\newcommandí\argminY+(\mathopí\mathrmíargN,minkYXY % modo sem amsmath
\begin{document}
V[ NVforall \theta \in \Rset, \\cos”2ltheta + \senºAltheta = 1 N
V[ \argmin x f(x) = MleftMx: f(x) = \min (x') f(x') NVrighty) N
\endídocument y
vO e R,cos? 9 +senº0O=1
argmin f(x) = (x : f(a) = min f(x'))
Os comandos podem ter até 9 parâmetros. Os comandos com parâmetros, é criado pelo
comando \newcommandí\nome-do-comando+ [n] fdefinição) onde n é o número de parâme-
tros. No corpo da definição do comando, t1, tt2,H3, ..especificam os parâmetros na posição 1,
2,3, etc.
Quando usa os parâmetros, o primeiro deles pode ser opcional. Neste caso, usa-se a sintaxe
\newcommandí\nome-do-comando+ [n] [v] fdefinição) onde “v” é o valor padrão quando o
parâmetro for omitido. O Exemplo 6.2 ilustra o caso.
Exemplo 6.2: ex06-parametro-opcional.tex
\documentclass [12pt,a4paper] {articley}
\usepackage [T1] {fontenc}
\usepackageTamsmath,amssymb+>
\newcommandí\conj+[1]fYoverlineí(t1)) % com um parametro
\newcommandí \normal [2] [] tNleftN |H2\rightN| (81+) % com parametro opcional
\newcommandfí\seq+ [2] [n] \leftNTH2 O,Mdots,N,tH2 THL1HNrightN+Y) % parametro
opcional pré definido
\beginf{document}
N[ \eonjíz+\edot z = \norma{z}+ 2 \neg \norma[\\\in{ty}{z}"2 N]
A sequência $\seg{x}I$ para $n=5$ é $\seg[5] (x)$.
$\conjílconj ízI+wk=zYconj {w}$
\end{document}
- 2 2
z z=|2| FEl
A sequência fx,,..., t,) para n=5 é (x6,..., L5).
Zw=2U
O comando NYVlet cria uma copia do comando existente. Por exemplo,
\letWcomandocopiaYcomandooriginal cria um comando \comandocopia que é uma cópia do
\comandooriginal. Assim, podemos redefinir o \comandooriginal e se precisar do original,
é só chamar o \comandocopia. Também poderá restaurar o comando original usando o \Mlet.
Por exemplo,
\letWtanoriginalNtan
\renewcommandí\tan)fWmathrmítg>
redefine o comando NVtan, mas se precisar do \tan original, eh só chamar o \tanoriginal.
Para restaurar o original, é só usar o \let novamente com em MletWtanWtanoriginal.
6.2 Criando ambientes
Para trecho maior de dados, o ambiente (o que tem \begin e \end) é mais adequado que
os comandos. Para criar ambientes, usa-se o comando \newenvironment na qual o primeiro
parâmetro é nome do ambiente, segundo é o que vai fazer antes e terceiro é o que vai fazer
depois. Quando tem o parâmetro (que pode ter até nove), coloca o número de parâmetro
como parâmetro opcional de \newenvironment, entre primeiro e segundo parâmetro. Assim
como o comando, o ambiente também pode ter o primeiro parâmetro como opcional. Neste
caso, passa o seu valor padrão após número de parâmetro como sendo parâmetro opcional ao
\newenvironment.
No Exemplo 6.3, o ambiente dem foi definido somente como a ilustração. Em geral, usa o
ambiente proof do pacote amsthm para demonstrações.
Exemplo 6.3: exO06-ambiente.tex
\documentclass [12pt,a4paper] {article}
\usepackage [T1] {fontenc}
\usepackageTamsmath,amssymb+>
\newenvironmentímyenvlfVWbegin{centerkVYem} fYend{center})
%5 com um parâmetro
\newenvironment{mypar}[1] (\parWnoindent \hrulefillNfboxí H1 \NWhrule{ill NW }
TiparWnoindentWhrulefill |NX
& um parâmetro opcional pré definido
\newenvironmentf{dem} [1] [Demonstração] (\textbfíH1:N ) ONhfilllruleílex+ílex
\\par+
\begin{document}
\begin{myenv}
Texto enfatizado e centralizado.
\endímyenv+
\beginímypar{Teste}
Parágrafo com título simples.
\end{mypar}+
\beginídemy
\ldots
\end{dem}y
\beginídemy [Prova]
\\ldots
\end{dem}+)
\endí{document}
Texto enfatizado e centralizado.
Teste
Parágrafo com título simples.
Demonstração:
Prova: .. "
Como não podemos colocar linhas em branco no meio da definição de comandos ou
ambientes para indicar o parágrafo, usa-se o comando \par para esta finalidade. O comando
\noindent desabilita temporariamente a indentação (tabulação para direita) da primeira
linha do parágrafo atual.
\ote que, também pode definir os comandos no modo TEX em vez do modo LaTeX. Para
isso, basta usar o \def que é importante quando um comando define o outro. O \def que
não vamos discutir aqui, deve ser usado com cuidado, pois ele não verifica se o comando exite
ou não, redefinindo caso existir.
6.3 Quebrando o código em várias linhas
Em geral, a definição de comando ou ambiente deve ficar em uma única linha, mas quando
isto é longo, precisamos dividir em mais de uma linha para boa organização. Neste caso,
existe trechos que não podem ser quebrados, mas isto requer um conhecimento extra. Para
contornar isto, note que o LaTeX considera que a próxima linha é uma continuação da linha
atual quando encontrar “%” grudado na última letra ativa (que não seja comentário). Assim,
quando quebrar a definição de comandos ou ambiente em mais de uma linha, coloque o “%”
grudado na última letra. Fique atento de não colocar espaço entre a última letra e “%”. \eja
o Exemplo 6.4.
Exemplo 6.4: ex06-comando-multlinhas.tex
7. Divisão Lógica de Documentos 48
Capítulo 7
Divisão Lógica de Documentos
Neste capítulo, vamos estudar a divisão lógica de documentos.
7T.1 Capítulos, seções e similares
Nos livros e relatórios, os conteúdos são organizados em capítulos, indicado por \chapter. Os
capítulos podem ser divididos em seções indicado pelo comando \section, se assim desejar.
Neste caso, evite ter capítulos com seções e outro sem seções, para ter uniformidades.
Se a seção ficar grandes, podem ser subdivididos em subseções com o comando subsection,
mas tome cuidado para que todas seções tenham subseções.
Existem ainda, \subsubsection  (subsubseções), \paragraph (parágra{os} e
\subparagraph (subparágra{os} que são menos usados.
No caso de artigos, o conteúdo costuma ser divido em seções e caso desejar, seções podem
ser subdivididos em subseções (evitando que tenha seção com subseção e outro sem subseção).
O capítulo inicia-se com o comando \\chapteríT{tulol} e seções com o comando
\sectioníT{tulo}.
Estes comandos aceitam a opção de especificar os “títulos curtos” que são usados no sumá-
rio e cabeçalho, o que podem ser passados como parâmetro opcional colocado antes do título.
Neste formato, usado quando título é longo, tem a forma \\chapter [Título Curto]íT{tulo}
e \section[Título Curto] fT{tulo}
Exemplo 7.1: ex07-capitulo.tex
\chapter[Titulo Curto]íTítulo Longo do Cap{tulo}
Apresentação bem rápida do capítulo.
\section[Título curto]líTítulo longo da seção)
Texto da seção
\sectioníTítulo da outra seção)
Texto da outra seção
\\idots
Capítulo 1
Título Longo do Capítulo
Apresentação bem rápida do capítulo.
1.1 Título longo da seção
Texto da seção
1.2 Título da outra seção
Texto da outra seção
Quando há os capítulos e/ou seções, o sumário podem ser produzidos automaticamente
pelo comando \tableofcontents. Para que o sumário apareça devidamente no documento
final, precisa compilar o documento duas vezes, pois o LaTeX usa o arquivo auxiliar para isso.
Para comandos do tipo capítulos (\chapter, \section, etc), existem as versões com
“*” que não serão enumeradas e não serão colocadas no sumário, apesar de ter a mesma
formatação. Por exemplo, \\chapter*{Resumo} não será enumerado, nem vai no sumário.
No caso de artigos, o resumo tem formatação diferente do restante das seções. Assim,
existe o ambiente especial abstract para o resumo, o que não é mesmo que \\section*t.
\ote a diferença e similaridade do Exemplo 7.2 que usa a versão “*”, com o Exemplo 7.1
que usa a versão normal.
Exemplo 7.2: ex07-capitulo-star.tex
\chapter*{Resumo}
Resumo aqui.
Resumo
Resumo aqui.
7.2 Capa, conteúdo frontal e principal
O Exemplo 7.3 ilustra a estrutura básica de um documentos tipo livro na qual não vamos
colocar a saída aqui, por ocupar várias páginas.
Exemplo 7.3: ex07-matter.tex
\documentclass [12pt,a4paper,oneside] (booky
\usepackage [T1] {fontenc}
\usepackageTamsmath,amssymb+>
\pagestyle{empty}
\begin{document}
% capa
\frontmatter
\chapter*(Resumo)\thispagestyle{empty}
Resumo aqui.
\pagestyle{headings}
\tableofcontents % Sumário
\chapteríPrefácio)
Apresentação do trabalho.
\nainmatter
\chapteríTítulo do Capítulo Aqui)
Apresentação bem rápida do capítulo.
\sectioníTítuo da seção aqui)
Texto da seção
\ldots
\appendix % se existir apêndice
\chapteríTítulo do Apêndice 1) % se existir
Texto do apêndice 1
\ldots
\backmatter % opcional
% referencia biliografica
% indice remissivo, se existir
\endí{document}
O comando \pagestyletempty) antes do \begin{document} remove as enumerações das
páginas para que parte inicial do livro fiquem sem a enumeração.
A capa simples nos livros e relatórios podem ser produzidos pelo comando \naketitle,
desde que seja fornecido algumas informações tais como título, autor e data pelos comandos
\title, \author e Mdate, colocados antes do inaketitle. \eja Exemplo 7.4.
Exemplo 7.4: ex07-maketitle.tex
\documentclass [12pt,a4paper,oneside] {book}
\usepackage [T1] ({fontenc}
\usepackageTamsmath,amssymb]>
\title{Exemplo}
\authoríSadao Massago]
\dateíFevereiro de 2018)
\beginfí{document}
\naketitle
\frontmatter
\\ldots
\endf{document}
\ote que, quando não for especificado a data (não tiver chamda do comando \\\date), será
assumido como sendo \\today que é data de compilação do documento. Se não quer que
apareça data, deve colocar \dateí).
Para criar títulos personalizados nos livros e relatórios, use o ambiente titlepage. \ale
lembrar que nos livros e relatórios, a capa não será contada como páginas, mas todas as outras
páginas, mesmo totalmente em branco (existe no caso de livros impressos), serão contadas.
O comando \frontmatter disponível somente para livros, indica que será matéria pré
textual, tendo as páginas enumeradas em romano minúsculo e sem a contagem de capítulos
(mesmo para versão sem “*”).
O comando \thispagestyle{empty} no \\chapter*{Resumo} remove a enumeração da
página atual (primeira página do “Resumo”) e não vai constar no sumário. \ote que capí-
tulos usa o estilo de página plain que enumera embaixo da página, mesmo que o estilo de
página esteja em empty. Assim, colocar \\\thispagestyletemptyl é necessário para remover
paginação desta primeira página do “capítulo”.
Antes do sumário colocado pelo comando \tableofcontents, foi colocado
\pagestyle{headings} para que volte a colocar páginas e cabeçalho superior. \ote que,
no livro, o que vem antes do sumário não devem ser paginados e não devem constar no
sumário, mas o que vem depois do sumário, costuma ser paginados. Por ser frontmatter, a
paginação será em romano minusculo.
Depois do prefácio, tem o comando \nainmatter (conteúdo textual) que também é disponí-
vel somente para livros. Este comando reinicia a paginação (começa a contar de 1 novamente)
e usa a enumeração em arábico. Também faz começar a contar capítulos.
O comando \appendix indica que, o que segue são apêndices que complementa o docu-
mento. Ele é disponível para livros, relatórios e artigos. No caso de livros e relatórios, o
comando \\chapter começará a produzir título para apêndices em vez de capítulos (escreverá
Apêndice A, Apêndice B, etc em vez de Capítulo 1, Capítulo 2, etc). No caso de artigos, o
comando \section que produzirá os apêndices.
O comando \backmatter também é disponível somente para livros. O \backmatter faz
com que \chapter funcione igual a \chapter* (versão “*”). Como não é costume colocar
\chapter no backmatter, o comando pode ser omitido.
Em geral, a parte final do documento é a referência bibliográfica. Se existir o índice
remissivo, deverá ser colocado depois da referência bibliográfica.
\ote que o relatório é um documento e não é um livro. Assim, todas páginas exceto a capa,
devem estar enumeradas em arábico e em sequencias. Assim, não há divisão de frontmatter
e mainmatter, não existindo comandos correspondentes.
A configuração do documento no artigo é ilustrado no Exemplo 7.5.
Exemplo 7.5: ex07-article.tex
\documentclass [12pt,a4paper] {article}
\usepackage [T1] {fontenc}
\usepackage [english,brazil] {babel}
\usepackageTamsmath,amssymb]>
\title{Exemplo}
\authoríSadao Massago
\dateíFevereiro de 2018)
\beginí{document}
\naketitle
\begin{abstract}
Resumo aqui.
\end{abstract}
& \tableofcontents % so se for artigo longo
\sectioníTítulo da seção 1)
Texto da seção 1
\sectioníTítulo da seção 2)
Texto da seção 2
\ldots
\appendix % se tiver apêndice
\sectioníTítulo do Apêndice 1)
Texto do apêndice 1
\idots
/4 referência biliográfica
\endídocument y
