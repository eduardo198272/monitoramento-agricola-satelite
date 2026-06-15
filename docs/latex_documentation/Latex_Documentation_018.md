\defWWt Y%
P
\usepackage [
backend=biber, % aceita acentuação direta no arquivo bib (recomendável).
style=abnt, % Sistema alfabético
%style=abnt-numeric, % Sistema numérico
%style=zabnt-ibid, % \otas de referência
% language=brazil, % padrão
% bibencoding=utf8, % padrão
]tbiblatex)
% \citeonline como \\textcite
\letlciteonlineVtextcite
\letyapudonlineYtextapud
\addbibresourcefex1i9-biblatex-abnt.biblk % arquivo bib
% Consertando o titulo que biblatex redefiniu
\efineBibliographyStringsíbraziliank+(bibliography=tReferências))
% Para biblatex: consertando para Referências ficar em maiusculo no sumário
\defbibheadingíbibliography[\bibname] (%
\chapter*(t1>
\bibmark
\ifnobibintocYelse
\phantomsection
\addcontentslineítockíchapter+í\uppercaseí(t1))
\fi
\prebibhook
d”
% Iniciando o docuemnto
\begin{document}|
Este modelo foi baseado no documento de \texttt{abntex2} \citeíbook:abntex2:
araujok.
Para citações textuais, deverá usar o comando \werb+\textcitet+ como descrito
em \textciteíbook:biblatex-abnt:marques).
% Para mais de uma citação por vez, use a versão plural \erbt+\cites+ e À
verb+\textcites+ (não é necessário).
Para citações de citações, usar o comando \verbt+\apud+ ou \verbt+\textapud+t.
Existem vários outros comandos neste estilo. \eja o
\textcitelbook:biblatex-abnt:marques) para mais detalhes.
Também poderá usar o BibTeX em vez do BibLaTeX. \eja o \\textciteíbook:
abnt2cite:araujo) para detalhes.
%
\phantomsection
% para que link do hyperref funcione corretamente para referencias
bibliograficas no sumario e no bookmark. Parece não ser necessário na
classe abntex2
\printbibliography%/[heading=bibintoc]
% [heading=bibintoc] é para acrescentar a referências no sumário (caso tenha
). Não é necessário para classe abntex2
\endí{document}
O arquivo ex19-biblatex-abnt.bib fica como segue.
Obookíbook:abntex2:araujo,
author=íLauro César Araujo),
title=(A classe abntex2: Documentos técnicos e científicos brasileiros
compatíveis com as normas (TABNTJX),
url=fhttps://ctan.org/pkg/abntex2/),
urldate=12018-06-{12},
year=2016
J7
Obookíbook:abnt2cite:araujo,
author=(Lauro César Araujo),
title=(0O pacote abntex2cite: Estilos bibliográficos compatíveis com a TABNTY
TNBR) {6023},
url=fhttps://ctan.org/pkg/abntex2/),
urldate=12018-06-12],
year=2016
1”
Obookíbook:biblatex-abnt:marques,
author=íDaniel Ballester Marques),
title=(fbiblatex-abnt 3.3),
url=fhttps://ctan.org/pkg/biblatex-abnt/],
urldate=12018-06-12],
year=2018
J”
A saída do Exemplo 19.4 e algo como segue.
Este modelo foi baseado no documento de abntex2 (Araújo, 2016a).
Para citações textuais, deverá usar o comando \\textcite como descrito em Marques
(2018).
Para citações de citações, usar o comando \apud ou \\textapud.
Existem vários outros comandos neste estilo. \eja o Marques (2018) para mais detalhes.
Também poderá usar o BibTeX em vez do BibLaTeX. \eja o Araújo (2016b) para detalhes.
Referências
ARAUJO, Lauro César. A classe abntex2: Documentos técnicos e científicos
brasileiros compatíveis com as normas ABNT. [S. L.: s.n.), 2018. Disponível em:
https://ctan.org/pkg/abntex2/. Acesso em: 12 jun. 2018.
ARAUJO, Lauro César. O pacote abntex2cite: Estilos bibliográficos compatíveis
com a ABNT NBR 6023. |S. L.: s.n.], 2016. Disponível em: https://ctan.org/pkg/
abntex2/. Acesso em: 12 jun. 2018.
MARQUES, Daniel Ballester. biblatex-abnt 3.3. [S. L.: s.n.], 2018. Disponível em:
https://ctan.org/pkg/biblatex-abnt/. Acesso em: 12 jun. 2018.
Para mais detalhes sobre comandos do estilo ABNT para BibLaTeX, veja [Mar18].
Observação 19.1. O novo estilo bibliográfico de BIbLaTeX para ABNT (conformidade com a
nova regra ABNT, NBR 10520:2023) está em desenvolvimento no site https://github.com/
abntex/biblatex-abnt, mas a versão beta foi postado no CTAN somente em outubro de
2024. Por este motivo, o estilo da referência bibliográfica distribuída junto com TEX um pouco
antigo, pode não estar de acordo com a norma atualizada. Se for o caso e deseja utilizar a
versão nova, deverá abaixar e instalar manualmente seguindo a instrução do site. Caso não
conseguir instalar, poderá extrair todos os arquivos do pacote e colocar junto com o arquivo
tex. Para verificar se está com o novo estilo, veja se URL (endereço da internet) da referência
bibliográfica ficará sem estar entre “<” e “>” (versão antiga ficará entre estes dois s{mbolos}.
19.5 Tabelas em ABNT
Tanto o ABNTeX2, como o ABNTexto, implementa sua forma de criar tabelas curtas em ABNT,
mas ainda não tem a funcionalidade para tabelas longas (2024). As tabelas no ABNT devem
obedecer as normas do Instituto Brasileiro de Geográfica e Estatística (IBGE). Para ter
conformidade com o estilo de IBGE (que ABNT adota), poderá usar o pacote tabularray, mas
requer ajustes. Um pacote que efetua tal ajuste é o tabularray-abnt que implementa o estilo
abnt para tabelas e quadro para quadros (tabela para apresentação de conteúdo textual em vez
de dados numérico). O pacote também implementa o “wrapper” abnttblr , tallabnttblr e
longabnttblr que aplica o tema abnt sobre tblr , talltblr e longtblr, com a possibilidade
de alterar a fonte usada pelo comando \SetAbntTblrFont. Como este pacote é muito recente
(2025), o sistema TeX pode não vir com ele. Se for o caso, abaixe o arquivo tabularray-
abnt .sty do ctan (https://ctan.org/pkg/tabularray-abnt) e instale manualmente ou
deixe junto como o arquivo .tex. Para usar, coloque a opção \theme=abnt ou theme=quadro
no parâmetro opcional de talltblr (ou tblr com opção tall) ou longtblr (ou tblr com
opção long), ou use a versão abnt correspondente.
Agora, supondo que o tabularray (e tabularray-abnt) com ajuste ao uso de booktabs
por \seTblrLibraryfbooktabsk, assim como os pacotes url (ou hyperref) e xcolor es-
tejam carregados. Então poderá diagramar as tabelas normalmente com o tallabnttblr e
longabnttblr, passando a fonte e nota adicional com o parâmetro remark, como no Exem-
plo 19.5, cuja a saída foi omitida.
Exemplo 19.5: ex19-abnt-table.tex
A Tabela Tabela-\refítab:abnt:{lutuante} é o que auto posiciona. Para tabela
flutuante, poderá usar \texttt{tabular} ou similar normalmente, mas
neste exemplo, foi usado o \\texttt{talltblr}] que aceita mesmos parâmetros
de \\texttt{longtblr}] como o rodapé, etc, mas que pode ser colocado
dentro do ambiente \texttt{table}.
\beginí{table} [hbp!]
\centering
\begin{talltblr}
[
theme=abnt, % Formatar como ABNT
caption=fUm t{tulo},
label=ftab:abnt:{lutuante}l,
reamrkíFontel=fElaboração do autor), % Usando comando definido no preamble
premabulo
n
colspec = (1XX), % colunas de largura automatica
rowleven) = fgray!15), % linha par em cinza
D”
\toprule ZNhline
produto & preço N
\nidrule ZNhline
cenouras (500g) & RA$0,50 W
cogumelos (vidro de 500g) & RNA$5,00 W
batata (1\g) & RN$1,20 \W \midrule % \hline
total & RN$6,70 \W
\bottomrule /\hline
\end{talltblr}
\endítabley
A Tabela-\refítab:abnt:longa) foi criado pelo ambiente \texttt{longtblr} (
que é mesmo que \textttítblr|) com opção *“long'' no primeiro parâmetro do
argumento), que requer duas compilações seguidas para ajustar
corretamente devido a configuração no preambulo.
\boegin{center})
\begin{longtblr}y
[4
theme=abnt, % Formatar como ABNT
caption = fInflação (IPCA) e juro de poupança de 2022), % titulo
label=ftab:abnt:longal, % rotulo para referências cruzadas
reamrk{Fonte}=(\urlíhttps://blog.nubank.com.br/ipca-2022/INY
\urlíhttps://brasilindicadores.com.br/poupanca/Y),
remarkí\otalk=(íPode colocar uma nota que é opcional],
[)
n
colspec = ÍXXX), % colunas de largura automatica
rowhead = 1, % primeira linha será repetida em todas as páginas
row{1} = ffont=\b{series}, % linha de título
rowleven) = fgray!50), % linha par em cinza
row{Z} = ffont=\bfseries,whitelk, % última linha
H
\toprule
Mês & Inglação & Poupança N
\idrule
Janeiro & 0,54 & 0,5608 W
Fevereiro & 1,01 & 0,5000 W
Março & 1,62 & 0,5976 W
Abril & 1,06 & 0,5558 W
Maio & 0,47 & 0,6671 MW
Junho & 0,67 & 0,6491 W
Julho & -0,68 & 0,6639 W
Agosto & -0,36 & 0,7421 W
Setembro & -0,29 & 0,6814 W
Outubro & 0,59 & 0,6501 \W
\ovembro & 0,41 & 0,6515 W
Dezembro & 0,62 & 0,7082 W
\bottomrule
Acumulado do ano & 5,79 & 7,8997 W
\begin{longtblr}
Se preferir, poderá reduzir as fontes do corpo da tabela para \footnotesize, o que é
exigido em algumas instituições que usam a norma ABNT. Para tal, poderá colocar a tabela
entre \begin{footnotesize} e \endí{ootnotesize}. Para que isto seja feita automatica-
mente, use o comando \etAbntTblrFontí\\{ootnotesize} que altera as fonte no ambiente
abnttblr, tallabnttblr e longabnttblr. Em seguida, troque tblr, talltblr e longtblr
para correspondente abnt.
No ABNT, tabelas com descrições qualitativas (textos em vez de números) é denominado
de “quadros”. As classes ABNTeX2 e ABNTexto não implementa o “quadro” ainda (2024). O
pacote tabularray-abnt implementa o tema quadro para esta finalidade.
\ote que na tabela (tabela de apresentação de dados numéricos), não deve ter fechamento
lateral, devendo ser fechado na parte superior e inferior, mas não deve haver linhas horizontais
no corpo da tabela. Também deve ter linha de titulo das colunas no começo da tabela, separada
de corpo da tabela pela linha horizontal. No caso de tabelas longas que ocupam mais de uma
página, estas linhas de títulos devem ser repetidos em todas páginas.
No quadro (tabela de apresentação de dados não numéricos), deve ter fechamento e grades
divisório.
O tema “quadro” configurará para quadro no modo ABNT, como no Exemplo 19.6. AÀA
distinção entre tabela e quadro será feito pelo theme=quadro, na primeira opção do parâmetro
opcional de longtblr ou talltblr (ou da versão abnt correspondente).
Exemplo 19.6: ex19-abnt-quadro.tex
Sem a opção do tema *"quadro'', será produzido a tabela. \ote que na tabela
não pode fechar os laterais (Exemplo-\refítab:talltblr:simples)).
\beginfítableY[hbp!]
\begin{tallabnttblr})
[
caption=(Tabela curta simples),
label=ftab:talltblr:{simples},
remarkíFontel=(Elaboração do autor],
[)
Ú
colspec = {XX},
D”
\toprule
nome & valor
a & 1 W \wnidrule
c & 2 W \bottomrule
\end{tallabnttblr}y
\end{table}
O quadro é produzido pelo tema \texttt{quadro} como no Exemplo-\refíquadro:
longol. \ote que, quadro deve fechar todos os lados e fazer divisório.
\begin{longtblr}
L
theme=quadro, % um quadro
caption=(tUm quadro longo simples),
label=fquadro:longolk,
remarkíFontel=(Elaboração do autor],
remarkí\otak=(íUsando o tema quadro para produzir quadrol,
[)
n
colspec = TXX),
vlines,hlines, % fazer grade
1”
linha 1 & texto 1 W
linha 2 & texto 2 \W
linha 3 & texto 3 \W
linha 4 & texto 4 \W
linha 5 & texto 5 W
%ipagebreak % quebrando página para teste
linha 6 & texto 6 W
linha 7 & texto 7 W
linha 8 & texto 8 \W
linha 9 & texto 9 W
linha 10 & texto 10 \W
\endílongtblry
Quadro flutuante será produzido pelo ambiente \textttíquadrol, como no
Quadro-\reffquadro:{lutuante}.
\beginíquadroY [hbp!]
\begin{talltblr}
"
theme=quadro, % um quadro
caption={Quadro flutuante simples},
label=fquadro:{lutuante},
remarkíFontel=(TElaboração do autor),
[)
ÃL
colspec = (XX),
vlines,hlines, % grades
1”
Nome 1 & Sobrenome 1 W
Nome 2 & Sobrenome 2 W
\endítalltblry>
\end{quadro}
A diferença entre tblr/talltblr/longtblr com abnttblr/tallabnttblr/longabnttblr
e que nas versões abnt pode configurar a fonte da tabela com \SetAbntTblrFont, além de
já aplicar o tema abnt por padrão.
No ABNTeX2, a tabela ou quadro curto produzido pelo VIBGEtab com o ambiente table ou
quadro estará em sincronismo com os produzidos pelo tema abnt ou quadro nos ambientes
de tabularray ou tabualrray-abnt.
No caso da classe ABNTexto, o ambiente quadro não é providenciado. Então use o ambiente
table para o caso de querer usar o quadro curto flutuante, em vez do ambiente quadro. Dentro
do ambiente table, use a legenda com a entrada quadro que estará em sincronismo com o
tema quadro do tblr e similar.
A lista de quadros poderá ser produzido pelo comando \listadequadros. No caso de
*”
ABNTeX2 ou derivados da classe memoir, use a versão para não constar no sumário. No
caso de abntexto, terá o comando makelogq para lista de quadros, que funcionará de forma
similar a nakelot.
No caso de ABNTexto, se tiver pouco espaço entre “FIGURA ??” com o nome das figuras
na lista de figuras, ou similares, poderá aumentar com os comandos
\renewcommandfí\loflabelwidthY17.5em) % da lista de figuras
\renewcommandfWlotlabelwidthYT7.5em) %& da lista de tabelas
\renewcommandí\loglabelwidthl{Sem} % da lista de quadros
A. Símbolos Básicos de LaTeX 255
Apêndice AÀ
Símbolos Básicos de LaTeX
Aqui, veremos os símbolos básicos de LaTeX que não requer o uso de pacotes adicionais.
Em geral, os editores atuais para LaTeX costumam apresentar painel de inserção de sím-
bolos, o que torna desnecessário ter lista de símbolos em mão. Atualmente, muitos sistemas
disponíveis na internet tais como alguns blog's, wiki's e sistema de ensino/aprendizagem
moodle costumam ativar a fórmula LaTeX através de mimetex, mathjax, \aTeX, ou similar.
Alguns destes permitem somente os comandos e símbolos básicos sem os pacotes para deixar
mais leve, enquanto que outros ativam os pacotes do AMS por padrão para incrementar a sua
funcionalidade.
Aqui será apresentado somente os símbolos básicos que poderão ser usados em qualquer
sistema na qual o suporte da fórmula ETEX esteja ativa. Para usar o sistema na qual os
pacotes do AMS está ativa, é aconselhável procurar os símbolos e construções adicionais no
outro material.
Existem pacotes específicos para cada área, adicionando símbolos e funcionalidades adici-
onais. Assim, é importante estudar pacotes relacionados à área desejada. Por exemplo, na
área de matemática, costuma usar os pacotes do AMS (amsmath, amssymb, amsthm).
Para procurar símbolos incomuns, existe uma lista completa de símbolos do LaTeX [Pak17]
disponível gratuitamente.
A.1 Caracteres especiais e acentuação no modo TEX
Alguns caracteres são reservados no LaTeX e requer o uso de comandos para inserir no docu-
mento. Além dos caracteres reservados, alguns caracteres extras (não ASCII) também podem
ser produzidos. Dependendo do caso, ainda precisa da acentuação pelo comando (acentuação
no modo TEX) como no caso de usa o BibTeX no sistema TEX antigo (anterior a 2018) na
qual não consegue lidar com os caracteres acentuados.
O Exemplo A.llista estes comandos que devem funcionar para qualquer configuração.
Exemplo A.1: ex-a-especiais-acentuacao.tex
A.l. Caracteres especiais e acentuação no modo TEX 256
Caracteres especiais (modo texto e matemático)
ICEAVAACEAVVEAEATCAAT :
\copyright \dag \ddag \dots NP \pounds NS
% O backslash ('V)') também é caractere especial, mas usa o comando diferente
para o modo texto (\tertbackslash) e modo matemático (\lbackslash).
Caracteres não \texttt{ASCII} (modo texto)
\aa NAA \ae NAE
\ij NIJ
NM1 NL No NO
\oe NDE \ss NSS
Acentuação no modo texto
VIAYV"Tay
V. la
INSUSAVEES,
\tAYN=fay
\TiA tar
V. lay
\A TLar
\botfAXNbTar
vWetoHNetec
\aAfaHNdfar
\ETAYNHÍTaY
\ríakNríar
\etAKNtia)
\fa+\ufar
W4tAYNWTtar
Circulando a letra
\textcircled(AkNtextcircledia)
i e j sem pingo
iN
Apóstrofos e aspas
"(ou”” )e!'
A.2. Símbolos no modo texto 257
(ou P MP e"
Pontos para abreviaturas, colocar espaço forçado \erb*+l + depois dele
para distinguir do ponto final como em "i N éN ''.
O ponto sem espaço depois dele é inserido com \erb+NO.+ como em *"pVle.vie.i
neoo
Caracteres especiais (modo texto e matemático)
(1)S% &%
Oit.. 9£$
Caracteres não ASCII (modo texto)
â ÃE
ul
Ho0
oe EBB
Acentuação no modo texto
Ãs Ás Àa An ÀR Àà —
Ãà Aa G; Aa Ãé Àà A Ãs Ãã
Circulando a letra
GVO)
i ejsem pingo
yY
Apóstrofos e aspas
“(ou)e”
“(ou“)e
Pontos para abreviaturas, colocar espaço forçado N depois dele para distinguir do ponto
final como em “i. é. ”.
O ponto sem espaço depois dele é inserido com N. como em “p.v.i.””.
”
\ote que, para abrir apóstrofo (ou aspas), usa-se um (ou dois) acentos agudos e para
fechar, usa-se um (ou dois) apóstrofos. Na falta de acento crase no teclado, poderá substituir
cada um dos acentos crase por dois acentos circunflexos seguidos de um espaço.
Os comandos \i e \j produz i e j sem pingo para ser acentuados. Por exemplo, “saída”.
No LaTeX atual, devem produzir corretamente mesmo sem usar \i como em “saída”.
A.2 Símbolos no modo texto
Alguns comandos dos símbolos funcionam tanto no modo matemático, como no modo texto,
mas maioria dos comandos funcionam somente no modo texto ou no modo matemático.
O Exemplo A.2lista comandos que funcionam no modo texto (incluindo os que funcionam
tanto no modo texto como no modo matemático).
Exemplo A.2: ex-a-simbolos-texto.tex
A.2. Símbolos no modo texto 258
Comandos que funcionam tanto no modo texto como no modo matemático.
MENF NS NZA 16 Z
\copyright \dag \ddag \dots
NP \pounds NS
Comando que funcionam somente no modo texto.
Altexrtasciicircum 4 mesmo que V.
Altertasciitilde & mesmo que 1-(7
\textasteriskcentered
\textbackslash
\textbar
\textbardbl
Altertbraceleft 4 use V
Altertbraceright % use V
\textbullet
/Altertcopyright & use \lcopyright
Altertdagger & use \dag
Altertdaggerdbl % use \ddag
Altertdollar %4 use V$
Altertellipsis 4 use \dots
Altertemdasht+) /& mesmo que ——-
/ltertendash & mesmo que --
1g
/Alterterclamdown %4 mesmo que !*
Altertquestiondown % mesmo que ?”
Altertgreater % use >
Altertless % use <
\textordfeminine
\textordmasculine
Altertparagraph %4 use V.
\textperiodcentered
Altertquotedblleft Zuse *”
Altertquotedblright 4 use ''
Altertquoteleft % use *
Altertquoteright % use '
\textregistered
Altertsection %4 use V.
A.3. Símbolos matemáticos 259
Altertsterling % use lWpounds
\texttrademark
Altertunderscore %4 use V
\textvisiblespace
Comandos que funcionam tanto no modo texto como no modo matemático.
1)38% &É
Oqtt
ES
Comando que funcionam somente no modo texto.
*Al-
iê
ao,
©TM
Pontos de exclamação e interrogação invertidos são obtidos, colocando acento crase
após eles. Na falta do acento crase no teclado, existem os comandos \\textexclamdown e
\textquestiondown para produzir eles.
Existem muitos outros símbolos que podem ser acessados no modo texto com o uso do
pacote textcomp que faz parte da base do sistema TEX.
A.3 Símbolos matemáticos
Mo modo matemático, algumas construções básicas estão disponíveis, como ilustrado no
Exemplo A.3. Para construções mais complexas, deve considerar o uso do pacote amsmath de
AMS que faz parte da base do sistema TEX.
Exemplo A.3: ex-a-construcao.tex
Algumas construções básicas
$
x (n) % expoente
x titl) Z índice
x i tn+1) Z índice e expoente
f' & derivadoa de f
\frac{mXink} 4 fração
\sqgrt{2} % raiz quadrada
\sart[n]ltx) % raiz n-ésima
\stackrel({\fNtol} Z colocando nome encima
TX \atop \Y % empilhando
{idisplaystyleNmathoptX} iºj) %Z índice encima/embaixo
$
A.3. Símbolos matemáticos 260
f j
” Ls n+1 sm X
Algumas construções básicas " x;, , x7* f íx/ªç/i = Y)i(
O comando \mathop permite colocar elementos embaixo/encima em vez de índice/expoente
no modo display. Para usar temporariamente o modo display dentro do modo inline,
basta usar o comando Mdisplaystyle.
Existem caracteres que podem ser usados diretamente na qual o L1TEX substitui direta-
mente com o símbolo adequado. Estes símbolos, juntamente com os símbolos que funcionam
também no modo texto (apresentado também no Exemplo A.2) estão no Exemplo A.4.
Exemplo A.4: ex-a-simbolos-basicos.tex
Comandos que funcionam tanto no modo texto como no modo matemático.
BE NF NE NZA 16 IAS
%Xcopyright \dag \ddag \dots$
%XP \pounds NS$
Símbolos que podem ser usados diretamente
$P /<D>DE, . 5318
$:$ é para relação (para pontuação, use $\colon$)
Comandos que funcionam tanto no modo texto como no modo matemático.
08% &L Ott.. ES
Símbolos que podem ser usados diretamente
+—:/<>=,.;! : é para relação (para pontuação, use : )
As letras gregas maiúsculas estão disponíveis somente uma parte dela, como pode ser
observado no Exemplo A.5 que lista estes comandos.
Exemplo A.5: ex-a-grega.tex
Letra grega minúscula
$\alpha \beta \gamma \delta \epsilon \varepsilon$
$izeta \eta \theta \artheta \iota \kappa Mlambda$
$\mu \nu \xi o \pi \arpi \rho \arrho \sigma \arsigma$
$\tau \\\upsilon \phi \arphi \chi \psi \omega$
A.3. Símbolos matemáticos 261
\ote que \\texttt{omikron} não tem comando correspondente por ser mesmo
símbolo que o ““o'' minúsculo.
Letra grega maiúscula (muitos deles são mesmos da letra romana maiúscula,
não tendo comandos correspondentes)
$\Gamma \Delta \Theta \Lambda \Xi \Pi$
$\Sigma \psilon \Phi \Psi \Omega$
Letra grega minúscula aByõee GCnIdVIkKA pvreomwpoos TuÁEXUw
\ote que omikron não tem comando correspondente por ser mesmo símbolo que o “o”
minúsculo.
Letra grega maiúscula (muitos deles são mesmos da letra romana maiúscula, não tendo
comandos correspondentes)
TAOAEIM X—XYTOVWVN
Agora, veja os operadores binários e relações binária no Exemplo A.6. que requer coman-
dos.
Exemplo A.6: ex-a-simbolo-binario.tex
Operadores binários
$\amalg \ast \bigcirc \bigtriangledown \bigtriangleup$
$\bullet \cap \cdot \circ \cup Mdagger \ddagger \diamond$
$\div \mp \odot \ominus \\\oplus \oslash \otimes \pm$
$isetminus \sqcap \sqcup \star \times \triangleleft \triangleright$
$\yuplus \ee \wedge \wr$
\ota: Para indicar o grau, costuma usar o \erbt+\circ+t como em $90"\\\circ$.
Operadores de tamanhos variáveis.
$\bigcap \bigotimes \bigwedge \bigcup \bigsqcup \coprod$
$\bigodot \biguplus \int \bigoplus \bigvee \oint$
$iysum \prod$
Exemplo: $\sum fi=1X"nVfracíi+(i)k$ e
$\prod fi=1)"n i = il$
Relação binária
A.3. Símbolos matemáticos 262
$\approx \asymp \bowtie \cong \dashv \doteg$
$\equiv \frown \mid \models \parallel \perp$
$\prec \preceg \propto \\sim \\simeg \smile \succ \succeg$
Operadores binários
UxOVA eN:-oUjlo =FOOCGSOSH \IUXxXAD UVA
\ota: Para indicar o grau, costuma usar o \circ como em 90º.
Operadores de tamanhos variáveis.
NOGAULIT OWS/ESV$ > Exemplo: 27 , 3 el i=
Relação binária
RX<NEAEZ s=A| Fl <\oxuvso >>
A diferença entre wnid e | é que o primeiro é um operador binário (como em a | b que é a
divide b), enquanto que o segundo não é (como em |a| que é valor absoluto de a)
Setas estão ilustradas no Exemplo A.7.
Exemplo A.7: ex-a-setas.tex
Setas
$\Downarrow \downarrow \hookleftarrow \hookrightarrow$
$\leftarrow \Leftarrow \eftrightarrow MVeftrightarrow$
$NMlongleftarrow \Longleftarrow Mlongleftrightarrow \Longleftrightarrow$
$\longmapsto \Longrightarrow \longrightarrow \mapsto$
$\nearrow \nwarrow \ightarrow \rightarrow \searrow \\swarrow$
$\uparrow \parrow \updownarrow \pdownarrow$
A seta dupla \erb+\Longleftrightarrowt costuma ser usado para *'se, e
somente se'', mas com pequeno ajuste no espaçamento. Para simplicidade,
existe o comando \erbt+\iff+t que produz $N)iff$.
No pacote \texttt{amsmathl}, define também o \erbtlimplies+t para "““implica''
que tem mesmo símbolo que \erbt+\Longrightarrowt, mas com espaçamento já
ajustado devidamente.
Arpões
$\leftharpoondown \\leftharpoonup \rightharpoondown \rightharpoonup$
$irightleftharpoons$
