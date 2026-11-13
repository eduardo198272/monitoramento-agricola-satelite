\beginftabularY(||1/1r|l|) \hline
\textbf{Produto} & \wmulticolumní2HT|c| | \textbfíPreços)) \\hline
cenouras & RN$1.00 & (por \g) W \clineí2-3)
& RN$0.20 & (por unidade) W \hline
cogumelos & RN$4.00 & \multicolumní1Xíf|r||Xf(por vidro)) W \clinefi-1) X
clineí3-3)
pêssego & & \multicolumníi-ílr||Xt(por \g)) W \hline
\endítabulary>
Produto Preços
cenouras | R$1.00 (por \g)
R$0.20 (por unidade)
cogumelos | R$4.00 (por vidro)
pêssego (por \g)
No Exemplo 4.10, o comando multicolumn foi usado somente para formatar a coluna
(colocar linha vertical) e não para juntar células.
Para alinhar os decimais, usamos o pacote dcolumn que define um novo especificador
de colunas na tabela, especificado por Dí<decimal em TeX>Yí<decimal em PDF>Yí<casas
decimais>.
<decimal em TeX> é a especificação de pontos decimais usado no arquivo TeX (como
escreve no TeX), <decimal em PDF> é o decimal utilizado para documento de saída PDF,
€ O <casas decimais> é o número de casas decimais a serem considerados (casas decimais
excedentes serão truncados). Caso a especificação do número de casas decimais for negativo,
qualquer número de casas decimais é aceito sem ser truncados (alinhando nos pontos decimais).
Como especificar três parâmetros toda vez que precise alinhar os pontos decimais é traba-
lhoso, é sugerido que defina um especificador no preamble, usando o comando newcolumntype
como abaixo:
\usepackage{dcolumn}
\newcolumntypetd]Y[1] 1DT.XfVNVcdotH+iH1)>
\newcolumntypet.X(DT.XYC.X(-1))
\newcolumntypetí,X(D1,XY1,X(2))
Ele define especificador de colunas “d<num>” que é interpretado como DT .Y(í Yí<num>>
e, “” e “” que serão interpretados como sendo DT .Y1.XY1-1) e D1,X1,X12) respectivamente.
«” “”
\ote que podemos modificar os comandos anteriores para que “” seja convertida para “,
ou vice versa. \eja o Exemplo 4.11.
Exemplo 4.11: exO04-dcolumn.tex
\documentclass [12pt,a4paper] {article}
\usepackage [T1] {fontenc}
4.4. Tabelas
\usepackageTamsmath,amssymb]>
\usepackage{Tdcolumn}
\{newcolumntypetd}[1]1DT.XtYcdot)iH1))
\newcolumntypet.XfíDi.\T.+(-1))
\newcolumntypetí,XtD1,XY1,X12X)
\begin{document}
\beginttabular+í|dt-1)|/d€23|. |, 1)
\hline
1.2 & 1.2 &1.2 &1,2 W
1.23 & 1.23 &12.5 &300,2 W
1121.2& 1121.2&861.20 &674,29 W
184 & 184 &10 &69 W
4 & 4&&8,4 W
& &.4 & W \hline
\endí{tabular}
\endí{document}
1-2 1-2 1.2 1,2
1-23 1-23 12.5 300,2
1121-2 1121-2 861.20 | 674,29
4 4 4
Para ter as colunas igualadas automaticamente, usamos o pacote tabularx que define o
ambiente tabularx onde primeiro argumento é largura da tabela e segundo é especificação de
colunas, mas apresenta um especificador de coluna especial “X”. Todas as colunas especificadas
por “X” terá mesma largura (largura destas colunas depende da largura da tabela). \eja o
Exemplo 4.12.
Exemplo 4.12: exO04-tabularx.tex
\documentclass [12pt,a4paper] {article}
\usepackage [T1] {fontenc}
\usepackageTamsmath,{amssymb}
\usepackageí{ttabularx}
\begin{document}
\beginftabularx+fNMlinewidthYt|c|X|cIlX|>
\hline
\nulticolumní2X(|c|+fNtexttt{multicolumn} ) &
\scshape Terceira & \scshape Quarta W \hline
primeira & a largura desta coluna depende da largura da
tabela. &
terceira & Quarta coluna funciona da forma similar a segunda e terá a mesma
largura da segunda W \hline
\endítabularxY
\endí{document}
multicolumn TERCEIRA | QUARTA
primeira | a largura desta coluna depende | terceira | Quarta coluna funciona da
da largura da tabela. forma similar a segunda e terá
a mesma largura da segunda
No Exemplo 4.12, foi usado o comando \linewidth que é a medida da largura da linha
atual. Este comando aparece frequentemente quando queremos ajustar largura de um elemento
para largura da linha atual. Mais sobre medidas, veja a Seção 12.1 e Seção 12.2 do Capítulo 12.
O comando \footnote{texto} que coloca o “texto” no rodapé do documento funciona
também dentro do tabularx.
Para ajustes de tabelas de forma mais profissional, pode precisar do booktabs (não é da
categoria base/required) e se precisar traçar linhas duplas ou similares na tabela, podemos
usar o pacote hhline. Também existe o pacote para tabela colorida colortbl (não é da
categoria base/required). Não entraremos em detalhes destes pacotes, mas vale observar
que hhline não funciona no tabularx.
4.5 Ambiente de tabulação
Ambiente de tabulação é bastante útil para escrever conteúdos alinhados em diversos pontos,
tal como no caso de algoritmos. O ambiente é especificado pelo tabbing.
Para marcar a posição de tabulação, usa-se o comando N=. Quando uma linha for usado
somente para marcar posição, coloca-se o comando \kil1l no final dele, para que o mesmo
não seja impresso.
Para formatar conteúdos tabulados, é comum que queira tabular várias linhas sucessivas.
O comando \V+ translada a margem esquerda por uma tabulação e N- retira uma tabulação da
margem esquerda. Com isso, podemos diagramar textos tabulados como no caso do algoritmo
do Exemplo 4.13.
Exemplo 4.13: ex04-tabbing.tex
\beginttabbing)
mmN=mm N=mm N=mm N=mm N= \kill % apenos para marcar tabulação
\E Solução real da equação $ax"2+bx+c=0$ pela fórmula de Baskara NJ N
$\Delta = b"”2-4ac$ \W
se d < O então tH W %Z aplicar uma tabulação em todas linhas de abaixo
escreva *"não há solução real'"' W
pare - MW %Z retirar uma tabulação de todas linhas de abaixo
senão N \W
$x 1 = \frací-b-\sagrtílWDeltal-+í2al$ N
$x 2 = \frací-b+\sagrtí\Delta)Y{2a}$ - \W
fim se
\endítabbingy
( Solução real da equação ax? + br + c = O pela fórmula de Baskara )
A = b? — 4ac
se d < O então
escreva “não há solução real”
pare
senão
— —b—V.
L = 20
x = =V.
2 20
fim se
Se por algum motivo, pretende usar a acentuação no modo TFX dentro do ambiente
tabbing, note que existe três acentos no modo TEX que não podem ser usados dentro do
tabbing que são V', V.eN=. Estes comandos são reservados para controle de tabulação.
Assim, estes três comandos devem ser substituídos pelos comandos Na', Na” e \a= respecti-
vamente (eles só {uncionam dentro do tabbing}.
Existem vários outros comandos que podem ser explorados no ambiente tabbing, mas
não vamos entrar em detalhes. Uma observação é que no caso de algoritmos ou código fonte
de programas, existem pacotes específicos que implementam ambientes bem mais fáceis e
versáteis do que tabbing.
4.6 Textos de citações, versos e verbatim
O ambiente quote é usado para escrever citações (trecho de outra {onte}, exemplos e frases
importantes. O Exemplo 4.14 foi extraído do “The \ot (So) Short Introduction to BTFX2e”
[OPHS25].
Exemplo 4.14: ex04-quote.tex
""Uma regra da tipografia sobre
o comprimento de uma linha é:
\beginfí{quote}
Em média, nenhuma linha deve
ser maior que 66 caracteres.
\endíquote
Este é o motivo pelo qual as
páginas do \aTeXí) possuem as
bordas tão grandes e também o
motivo pelo qual os jornais usam
impressão em colunas''.
“Uma regra da tipografia sobre o comprimento de uma linha é:
Em média, nenhuma linha deve ser maior que 66 caracteres.
Este é o motivo pelo qual as páginas do LaTeX possuem as bordas tão grandes e também
o motivo pelo qual os jornais usam impressão em colunas”.
No ambiente quote usado para colocar citações (trecho tirado da outra {onte}, o texto
inteiro ficará com margens maiores a esquerda e a direita, o que tornaria visível quando
colocar texto maior.
Quando o texto da citação é formado por vários parágrafos, pode querer que os parágrafos
sejam indentados (tabulados para a direita). Neste caso, use o ambiente quotation em vez de
quote. O Exemplo 4.15 também usa o trecho do [OPHS25] que explica os ambientes similares
a quote, ficou com parágrafo indentado:
Exemplo 4.15: exO04-quotation.tex
\eja que a cópia do trecho do *"The \ot (So) Short Introduction to \LaTeX2e
'' que explica os ambientes similares a \textttíquotel, ficou com
parágrafo indentado:
\beginfquotationY
""Existem dois ambientes similares: os ambientes quotation e verse.
Como ambiente \texttt{quotation} faz a indentação dos parágrafos,
ele é usado para citações longas que se estendem por vários parágrafos.
O ambiente \texttt{verse} é usado em poemas onde as quebras de linhas são
importantes.
As linhas são separadas por \erb+\W+ e por uma linha em branco no fim de
cada verso''.
\end{quotation}
\eja que a cópia do trecho do “The \ot (So) Short Introduction to BTFX2e” que explica
os ambientes similares a quote, ficou com parágrafo indentado:
“Existem dois ambientes similares: os ambientes quotation e verse. Como
ambiente quotation faz a indentação dos parágrafos, ele é usado para citações
longas que se estendem por vários parágrafos. O ambiente verse é usado em
poemas onde as quebras de linhas são importantes. As linhas são separadas
por W e por uma linha em branco no fim de cada verso”.
No caso de versos, a linha que for quebrado pela falta de espaços, mas que constitui a
mesma linha de cima, deve estar tabulado para direita. O ambiente verse encarrega deste
serviço.
O Exemplo 4.16 é um exemplo do “Humpty Dumpty” do [OPHS25], colocado na caixa
com largura insuficiente. Para criar caixas mais estreitas, foi usado o ambiente minipage que
será tratado na Seção 4.7 do Capítulo 4.
Exemplo 4.16: exO04-verse
\begin{flushlefty}
\beginíminipageYtO.SNlinewidth)
\beginf{verse}
Humpty Dumpty sat on a wall:\W
Humpty Dumpty had a great fall.\W
Al1 the \ing's horses and all
the \ing's menW
Couldn't put Humpty together
again.
\endí{verse}
\end{minipage}
\endí{lushleft}
Humpty Dumpty sat on a wall:
Humpty Dumpty had a great fall.
All the \ing's horses and all the
\ing's men
Couldn't put Humpty together
again.
Para inserir o código fonte de programas ou similar, usa-se o ambiente verbatim que
coloca o texto de jeito que está (cópia verbatim). Este ambiente possui também a versão “*”
X” “o»
verbatim*. Sem o “*”, coloca o espaço e com o , coloca o caractere “” no lugar de espaço.
\eja a diferença entre o código colocado pelo verbatim e verbatim* do Exemplo 4.17.
Exemplo 4.17: exO04-verbatim.tex
\beginf{verbatim}
\begin{quote}
texto citado, texto importante ou exemplos.
\end{quote}
\end{verbatim}
\beginfíverbatim*>
\obegin{quote}
texto citado, texto importante ou exemplos.
\end{quote}
\end{verbatim*}
\beginí{quote}
texto citado, texto importante ou exemplos.
\endíquoteY
\begin{quote}
texto citado, texto importante, ou exemplos.
\end{quote}
O ambiente verbatim é usado para colocar conteúdos que devem ser lidos letra por letra,
como no cado do código fonte de programas ou trecho de documentos muito importantes.
Para nome das variáveis do programa, nome de arquivos, etc que são curtos, mas também
precisam ser lidos letra por letra, existe a versão comando que é \verb. No \verb, o primeiro
caractere é o delimitador do argumento que deve ser usado também para indicar o final do
argumento. Este delimitador pode ser escolhido (só não pode ser “*”), mas fique atento que
exXx” « »”
o final do argumento deve usar mesmo caractere. ÀA versão com exibe o espaço como
\eja o Exemplo 4.18.
Exemplo 4.18: ex04-verb.tex
O comando \erb+tN%Z+ produz *“NZ'"'.
Nome de arquivos com espaço tal como \erb*|meu arquivo.tex|
não é recomendado para \LaTeX, pois dificulta a sincronização de PDF com o
código fonte.
Use *“\verbt-+'' no lugar de espaço, como em \erb*|meu-arquivo.texl|.
O comando N% produz “%”.
Nome de arquivos com espaço tal como meu varquivo.tex não é recomendado para LaTeX,
pois dificulta a sincronização de PDF com o código fonte. Use “-” no lugar de espaço,
como em meu-arquivo.tex.
”
Para textos longos no ambiente verbatim deve carregar o pacote verbatim no “preamble
Este pacote efetua algumas melhorias no ambiente verbatim e também implementa o comando
\erbatiminput que insere o arquivo externo diretamente no ambiente verbatim.
\ote que, para inserir trecho dos códigos fontes de programas, existem pacotes apropriados
que é mais prático do que usar o ambiente verbatim.
4.7 Caixa minipage
O ambiente minipage cria uma “caixa” que não é exatamente uma estruturação de textos, mas
é usado frequentemente quando não encontra ambiente pronto para estruturação desejada.
Por exemplo, podemos colocar um bloco de texto justificado no lado direito da página,
como no Exemplo 4.19.
Exemplo 4.19: exO04-minipage.tex
\beginfflushrighty
\begin{minipage}tO.SMlinewidth)
Este texto ficará justificado, mas como fica dentro de \textttíminipagel,
podemos colocar no lado direito.
Para tanto, basta colocar \texttt{minipage} dentro do \textttí{lushright}.
Claro que podemos colocar equações, figuras e outros elementos sem problemas.
Por exemplo, o a equaçao do Teorema de Pitágoras foi posto a seguuir:
NE angsbo2+c72 N]
\end{minipage}
\endí{lushright}
Este texto ficará justificado, mas como fica
dentro de minipage, podemos colocar no lado
direito. Para tanto, basta colocar minipage
dentro do flushright. Claro que podemos
colocar equações, figuras e outros elementos
sem problemas. Por exemplo, o a equaçao do
Teorema de Pitágoras foi posto a seguuir:
a? =b?+c?
O argumento obrigatório para o ambiente minipage é a largura da “caixa”. No Exem-
plo 4.19, foi usado 0. 5Ml inewidth que é metade da largura da linha.
Este ambiente é importante para colocar um parágrafo de texto dentro dos comandos
que não aceitam os parágrafos. Por exemplo, \\{boxt*} coloca moldura no elemento, mas
não aceita o parágrafo de texto. Então, como colocar moldura no texto com várias linhas,
ou nas figuras? É simples: colocar tudo no minipage e colocar dentro do fbox, como no
Exemplo 4.20.
Exemplo 4.20: exO04-minipage-fbox.tex
\fboxt
\beginfíminipageY+toO.75\linewidthk %3 3/4 da largura de linha
Usando o \textttíminipagel, podemos colocar moldura no texto com parágrafo
como este.
O \textttí{box} não acusa erros por ter parágrafo, pois o que está dentro de
\texttt{minipage} é apenas um * objeto''.
Este truque funciona também para outros comandos que impede de colocar
parágrafos, mudar linhas, etc.
\ote que as notas de rodapé\footnoteírodapé é colocado pelo comando \texttt
Tfitextbackslash {ootnoteWtextoN} ) |
colocado dentro do minipage ficará na parte de baixo do \\texttt{minipage} e
não da página.
O padrão dentro do \texttt{minipage} é enumerar eles como letra e não com
números.
\end{minipage}
) % fboxr
Usando o minipage, podemos colocar moldura no texto com pará-
grafo como este.
O fbox não acusa erros por ter parágrafo, pois o que está dentro
de minipage é apenas um “objeto”.
Este truque funciona também para outros comandos que impede de
colocar parágrafos, mudar linhas, etc.
\ote que as notas de rodapé* colocado dentro do minipage ficará
na parte de baixo do minipage e não da página. O padrão dentro
do minipage é enumerar eles como letra e não com números.
*rodapé é colocado pelo comando \footnoteí{texto}
Para elementos com poucas linhas de código, a versão comando \parbox é mais prático de
ser usado. Mas \parbox é mais simplificado do que minipage, podendo perder alguns recursos.
Por exemplo, alguns comandos e ambientes tais como \verb e verbatim não funcionam dentro
do \parbox. Assim, prefira usar o minipage sobre \parbox. \eja o Exemplo 4.21.
Exemplo 4.21: ex04-parbox.tex
Texto normal
\fboxTlparboxTí3cm+ítexto em várias linhas. W Com moldura.))
Texto continua.
texto em várias
Texto normal |linhas. Texto continua.
Com moldura.
O primeiro parâmetro do \parbox é a largura, como no caso de minipage. Tanto no
minipage como o parbox, \\linewidth dentro dele é a largura da caixa passada como parâ-
metro.
4.8 Colunas múltiplas de texto
Dependendo do documento, usa-se mais de uma coluna. Isto é o caso de alguns artigos
que podem usar duas colunas, ou poster que costuma usar três colunas ou mais. Mesmo
no documento de uma coluna, o índice remissivo costuma ficar em duas colunas. Apesar
da maioria das classes de documentos tem implementado a opção de documento em duas
colunas (opção twocolumn) e comandos para alternar entre uma e duas colunas (comandos
\onecolumn e \twocolumn), a forma mais prático é usar o pacote multicol que implementa
o ambiente muticols que permite criar qualquer número de colunas. O padrão é não traçar
linhas separando colunas, mas isto pode ser alterado, como no Exemplo 4.22. Aqui foi usado
o \setlength para alterar a medida da espessura de linha que separa as colunas. Medidas
serão tratadas em Seção 12.1 e Seção 12.2 do Capítulo 12. O Exemplo 4.22 ilustra o uso de
múltiplas colunas.
Exemplo 4.22: exO04-multicols.tex
\documentclass [a4paper,12pt]{article}
\usepackage [T1] {fontenc}
\usepackage [brazil]{babel}
\usepackageTtcolor]
\usepackage{Tcolor})
\usepackage{multicolY} % permite usar multiplas linhas
” espessura da linha que separa as colunas (Opt para desabilitar)
\setlengthfVYcolumnsepruleY{1ipt}
\begin{document}
Este parágrafo está como uma única coluna, padrão para maioria das classes
de documentos.
\begin{multicols}(2) Z inicia duas colunas
Este parágrafo está em duas colunas.
O ambiente \texttt{multicols} balanceia os conteúdos em colunas para que
todas colunas tenham mesmo tamanho.
Se preferir que passe para próxima coluna somente quando a coluna ficar
cheia, use a versão ""*'' que não balanceia seus conteúdos.
Se quer finalizar a coluna manualmente, poderá usar o \erbt+\columnbreak+
que finaliza a coluna atual e passa para próxima coluna.
\end{multicols} % finaliza o mode de duas colunas
Agora está no modo de uma única coluna novamente.
\endídocument >
Este parágrafo está como uma única coluna, padrão para maioria das classes de documen-
tos.
Este parágrafo está em duas colunas. O |car cheia, use a versão “*” que não balanceia
ambiente multicols balanceia os conteúdos | seus conteúdos.
em colunas para que todas colunas tenham | Se quer finalizar a coluna manualmente, po-
mesmo tamanho. Se preferir que passe para | derá usar o \columnbreak que finaliza a co-
próxima coluna somente quando a coluna fi-| luna atual e passa para próxima coluna.
Agora está no modo de uma única coluna novamente.
5. Aprofundando nas Fórmulas Matemáticas 29
Capítulo 5
Aprofundando nas Fórmulas
Matemáticas
Neste capítulo, vamos aprofundar mais nas fórmulas matemáticas. Para suporte à ma-
temática, os pacotes amssymb e amsmath são usados. Portanto, coloque o comando
\usepackageíamssymb,amsmath*] no preamble do documento.
5.1. Usando algumas fontes matemáticas
Na matemática, além dos símbolos especiais e letras gregas, também usam alfabetos romanos
de formatos diferentes. Por exemplo, para o conjunto dos números, costuma usar “negrito
do quadro negro” (por exemplo, letra de traço duplo do AMS). Tais fontes são selecionados
pelos comandos apropriados. Aqui veremos alguns dos mais usados.
O conjunto dos números como real, racional, etc, usam a letra maiúscula em “negrito do
quadro negro”. Para tanto, poderemos usar o comando \mathbb.
Para Conjunto de funções contínuas, costuma usar a letra “C” maiúscula na forma cali-
gráfica. A fonte caligráfica é indicado pelo comando \mathcal.
Para algumas áreas de matemática, ainda usam a versão enfeitada de caracteres oferecido
pelo comando \mathfrak.
Para nome das funções, devemos usar a letra romana reta. O LaTeX dispõe de comandos
prontos para maioria das funções comumente usadas, mas as vezes precisamos escrever o nome
da função que não está pronto, como o sen que representa a função seno em português. Como
LaTeX implementa nome das funções em inglês, o nome disponível para seno é sin produzido
pelo comando \sin. Também notemos que no Brasil costuma usar tg para tangente e não
o tan.
Para estes e outros casos, podemos especificar os nomes das funções que LaTeX não dispõe,
colocando dentro do comando \mathrm que usa a fonte romana reta. \eja o Exemplo 5.1.
Exemplo 5.1: ex05-mat-fontes-basico.tex
\documentclass [12pt,a4paper] farticle>
\usepackage [T1] {fontenc}
\usepackage [brazil] (babel)
\usepackageTamssymb,amsmath+
\beginí{document}
Exemplo do uso de letra caligráfica e de "“negrito do quadro negro''.
NE f \in \mathcal{C}(\mathbbfíRI, mathbb{R}) N
Exemplo da letra romana maiúscula enfeitada $\mathfrak{R}$.
Exemplo do nome das funções
N[ \forall \theta \in \mathbbíRI, \cos 2ltheta + \mathrm{sen} 2\theta = 1
N
Outro exemplo: $\mathrmítgkNtheta = NVfracílmathrm{sen}\theta){lcosYtheta}S$.
N
\nathopfWmathrmí{argN,mink} x f(x)
\i
\endí{document}
Mx : f(xX) = vmin (x') f(XxX')NX
Exemplo do uso de letra caligráfica e de “negrito do quadro negro”.
{FECIRR}
Exemplo da letra romana maiúscula enfeitada R.
Exemplo do nome das funções
v e R,cos?º d + senº0 = 1
senô
cos 0*
argmin f(x) = (x : f(e) = min f(6))
Outro exemplo: tgô =
Se precisar deixar algum trecho da fórmula em negrito, poderá usar o comando \\bm do
pacote bm.
\ote que no argmin, o r será colocado embaixo e não como índice. Para que o que foi
colocado como Índice fique embaixo, usa-se o comando \mathop. O comando h, usado no
meio de argmin é um comando de espaçamento usado na fórmula que insere pequeno espaço.
Mais sobre espaçamentos no modo matemático, veja a Seção 12.1 e Seção 12.2 do Caítulo 12.
Em geral, costuma definir comandos para nome das funções no preamble do documento
para facilitar a digitação. AÀ definição de comandos e ambientes serão estudados na Seção 6.1
do Capítulo 6.
Os comandos para nome das funções pré-definidas estão na Seção 10.4 do Capítulo 10.
5.2. Texto, função por partes e matrizes 3l
5.2 Texto, função por partes e matrizes
Para inserir texto nas fórmulas, usa-se o comando \text do pacote amsmath. Evite de usar o
\nbox para este propósito.
Para ilustrar, vamos usar o ambiente cases usado para definir funções por partes, no
Exemplo 5.2.
Exemplo 5.2: ex05-mat-text.tex
NA
Ix| = \begin{cases}
x, & \textí se |) x \wWweg O W
-x, & \\textí caso contráriokNW
\endí{cases}
J
” ím, ser>O0
L =
—x,  caso contrário
O caractere “&” indica o ponto de alinhamento e W indica a mudança de linha.
O pacote amsmath dispõe de ambiente para produzir matrizes. O ambiente matrix produz
matriz sem o delimitador, pmnatrix é delimitado pelos parenteses, bnatrix é delimitado pelos
colchetes,Bmatrix é delimitado pelas chaves, vmatrix é delimitado pelas retas verticais e
\matrix é delimitado pelas retas verticais duplas. Eles estão ilustradas no Exemplo 5.3.
Exemplo 5.3: exO05-matriz.tex
N
\obegin{pmatrix}
1& 2&3 \W
2& 3&4 \W
3&4&5
\endí{pmatrix},
\begin{bmatrix}
1& 2&3 \M
2& 3&4 W
3&48&5
\endíbmatrixk,
\beginf{vmatrix}
1& 2& 3 W
2& 3&4NMW
3&48&o5
\end{vmatrix},
\beginfí\matrix)
1& 2&3W
2& 3&4\MW
3&48&o5
\endí\matrix)
J
123 12311123 |123
2 3 4),/2 3 4/,/12 3 4/,]2 3 4
3 45/ |34 5) 384 5/)/|/345
5.3 Delimitadores auto ajustáveis, chaves embaixo e in-
tegrais
Existem delimitadores auto ajustáveis que aumenta conforme o seu conteúdo aumenta de
altura. Para usar ele, use \left antes do delimitador esquerdo (tais como “(”, “[”, “” “|”
, , , , ,
N”, “\langle”, “M1floor”, “Mlceil”J)e use \left antes do delimitador direito (tais como
)” , AN E AV, Arangle”, “Arfloor”, “Arceil”). Para colocar delimitador somente
em um dos lados, “” é usado para indicar delimitador vazio (quando tem somente em um
[13))
dos lados, outro lado seria “”). Cuidado para não usar || para barra vertical dupla. \eja o
Exemplo 5.4.
Exemplo 5.4: exO05-delimitador.tex
NE MeftyW|\frací\fracíl+ix+HiNsqart [3] (x 2+1)) \rightN| N
VIMeftMx \in [0,1) : \fracíx+i)ix-1) < O \rightyY N
VNL 2\left [1+\fracíNMleft (1+\frac{1H5}\right) 2X0€2] \right]l+5 N
V. Meft. \fracíx 2Hx+1)\right| fx=1) = NVfrac{1}02] N
V[ MeftyMlangle f, g \rightirangle = \int ba f(x)g(x)dx NM
x+1l
1):
í:ce[o, ) -” 1<0?
2 [1+(1+T%)2] +5
