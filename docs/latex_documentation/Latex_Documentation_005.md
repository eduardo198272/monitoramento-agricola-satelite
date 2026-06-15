Exemplo
Sadao Massago
Fevereiro de 2018
Resumo
Resumo aqui.
1 Título da seção 1
Texto da seção 1
2 Título da seção 2
Texto da seção 2
A Títulodo Apêndice 1
Texto do apêndice 1
O \maketitle produz título do artigo com informações usando título, autor e data forne-
cidos como nas capas dos livros e relatórios.
\ote que não costumamos usar o Índice remissivo para artigos, apesar de ter comandos
disponíveis para isso.
7.3 Limpando o verso das páginas
Embora a tendência atual é elaborar os livros e relatórios eletrônicos para serem lidos direta-
mente, pode ser que queira criar uma versão impressa.
No caso do livro impresso, costuma ser diagramado para impressão em dois lados (opção
da classe de documento twoside) em vez de impressão somente em um lado (opção da classe
oneside). Também podemos usar openright que começa o capítulo somente no lado direito
(openany começa o capítulo tanto no lado esquerdo como no lado direito). Na classe book, se
não tiver a opção “oneside”, será interpretado como “twoside”.
Nestes casos, o verso do sumário, resumo, etc, assim como versos de finais dos capítulos,
se existir, ficarão em branco em vez de ter enumeração de páginas ou cabeçalhos. Para que
isso aconteça, é só inserir o código
\clearpageWthispagestylefempty+\cleardoublepage
antes de cada capítulo ou comandos que produzem os capítulos ou similares, tais como sumário,
referências bibliográficas e índice remissivo. Também é necessário antes do inainmatter. \eja
o Exemplo 7.6 na qual a saída foi omitida.
Exemplo 7.6: ex07-clearpage.tex
\documentclass [12pt,a4paper,openright] fbookY
\usepackage [T1] {fontenc}
\usepackageTamsmath,amssymb+>
\pagestyleífempty>
\beginí{document}
% capa
\frontmatter
\chapter*í(Resumo)\thispagestyleí{empty}
Resumo aqui.
\ecleardoublepage
\pagestyle{headings}
\tableofcontents % Sumário
\clearpageVWthispagestylefempty+\cleardoublepage
\chapteríPrefácio)
Apresentação do trabalho.
\clearpageVWthispagestyle{empty}\cleardoublepage
\nainmatter
\chapteríTítulo do Capítulo 1)
Texto do primeiro capítulo.
\clearpageWthispagestylefempty+\cleardoublepage
\chapteríTítulo do Capítulo 2)
Texto do segundo capítulo.
\\ldots
\clearpageVWthispagestyle{empty}\cleardoublepage
\appendix % se existir apêndice
\chapteríTítulo do Apêndice 1) % se existir
Texto do apêndice 1
\\ldots
\backmatter % opcional: sem efeito visual
\clearpageWthispagestyle{empty}\cleardoublepage
% referencia biliografica
\clearpageVWthispagestylefemptykYcleardoublepage
% indice remissivo, se existir
\endídocument y
O comando \clearpage finaliza a página. Por exemplo, se tiver algo pendente como
figuras a serem colocadas, será feito. Com \thispagestylefempty, desabilita o estilo da
página atual e com \cleardoublepage, inserir página em branco, se necessário.
7T.4 Efetuando pequenos ajustes
O primeiro parágrafo da seção ou capítulo não será indentado (empurrado para direita).
A indentação é feito para distinguir um parágrafo do outro, mas como não tem parágrafo
anterior, não há necessidades de indentação. No entanto, algumas pessoas podem querer
indentar o primeiro parágrafo. Se for o caso, basta usar o pacote indentfirst no preamble
do documento.
Por outro lado, se quer remover indentação de algum parágrafo como no caso do texto
que segue uma fórmula matemática no modo displaystyle, como continuação da fórmula,
basta usar o comando \noindent.
Também pode querer que uma página fique um pouco maior para acomodar o
conteúdo atual. Neste caso, use o comando \enlargethispage. Por exemplo,
\enlargethispageTVWbaselineskip) aumenta a página atual por uma linha. Este tipo de
ajustes requer cuidados para não comprometer a qualidade da diagramação.
Se quer que algum comando seja executado após o término da página atual, use
o pacote afterpage que implementa o comando de mesmo nome. Por exemplo,
Na{terpagefVlclearpage} colocará todas figuras e tabelas pendentes na próxima página.
8. Teoremas e Similares 56
Capítulo 8
Teoremas e Similares
Os ambientes para teoremas e similares podem ser criados de forma apropriadaLaTeX.
8.1. Criando ambiente para teoremas
Para definir o ambiente para escrever teoremas e similares, costuma usar o pacote amsthm
que melhora a usabilidade do Inewtheorem usados para este propósito.
O comando \newtheorem{theorem}tTeorema)[chapter] cria um ambiente cha-
mado theorem que usa como ftítulo “Teorema” com contador vinculado a ca-
pítulo (chapter). Se for artigo, troque o chapter pelo section como em
\newtheorem{theorem}íTeoremal [section].
Se [chapter] ou [section] for omitida, a contagem será feita sequencialemente em todo
documento.
Para definir outros ambiente similares aos teoremas, ftais como axi
oma, lema,  corolário e  proposição, poderá usar o comando tal como
\newtheoremípropositionY [theorem] (Proposição) onde theorem no parâmetro op-
cional na segunda posição indica que será contado junto com o teorema. Asim ficará
Teorema 1.1, Proposição 1.2, etc. O modelo para proposição serve para demais ambientes
similares aos teoremas.
Para ambientes como definição, exemplos e exercícios, devemos usar o estilo definição,
obtido pelo comando \\theoremstyleíde{inition}.
A seguir, usa-se o \newtheorem novamente como
\newtheoremíde{inition} [theorem] (Definição) e mewtheoremí{example} [theorem] (Exemplo].
Para observações e notas, deve mudar para estilo remark com o comando
\theoremstyle{remark}.
\ote que amsthm providencia o ambiente para demonstrações, denominado de proof. \eja
o Exemplo &8.1.
Exemplo 8.1: ex08-teorema.tex
\documentclass [12pt,a4paper] fbookY
\usepackage [T1] ({ontenc}
\usepackage [brazil] (babel)
\usepackageTamssymb,amsmath+
\usepackageT{amsthm} % para configurar o teorema
%5 Definindo teormas e similares. Contador unico, vinculado a capítulos.
\newtheorem{theorem}{Teorema} [chapter] % contador vinculado a capitulos
\newtheoremícorollary [theorem] (Corolário)
\newtheoremí{lemma} [theorem] (Lema-)
\newtheorem{proposition} [theorem] (Proposição)
\newtheorem{axiom} [theorem] {Axioma}
\theoremstyleíde{inition}
\newtheoremíde{inition} [theorem] (Definição)
\newtheoremí{example} [theorem] {Exemplo}
\newtheorem{exercise}TExercíciol[chapter] % contador próprio, vinculado a
capitulo
\theoremstyleíremarky
\newtheorem{remark} [theorem] (Observação)
\beginfí{document}
\chapteríTriângulo Equilátero)
\beginfíde{initiony}
Um triângulo é dito \emphíftriângulo equiláterol) quando todos os lados forem
congruentes.
\endíde{inition}
\begin{theorem}
Todo triângulo equilátero se, e somente se, todos ângulos forem congruentes
\end{theorem}y
\beginfíproofy
\idots
\endíproofy
\beginíremarky
Um triângulo cuja todos ângulos são congruentes é dito \emphfequiângulo].
\end{remark}>
\endí{document}
Capítulo 1
Triângulo Equilátero
Definição 1.1. Um triângulo é dito triângulo equilátero quando todos os lados forem
congruentes.
Teorema 1.2. Todo triângulo equilátero se, e somente se, todos ângulos forem congruentes.
Demonstração.
Observação 1.3. Um triângulo cuja todos ângulos são congruentes é dito equiângulo.
8.2 Parâmetros opcionais
\ote que os ambientes tipo teoremas permite colocar o título como parâmetro opcional do
ambiente. Isto também vale para o ambiente proof quando existem textos entre o enunciado
do teorema e a sua prova. O comando \proofname armazena o “nome” do ambiente proof
que o valor atual é “Demonstração”. Quando a demonstração é finalizada pela equação no
modo displaystyle, a marca do final de demonstração fica na linha de baixo. Para corrigir
isso, existe o comando Mgedhere que indica onde a marca de final de demonstração deve ser
colocada. \eja o Exemplo 8.2.
Exemplo 8.2: ex08-teorema-parametro.tex
\beginfdefinitiony
Um triângulo é dito \emphftriângulo retângulo) quando tem um ângulo reto. O
lado oposto ao ângulo reto é denominado de \emph{hipotenusa} e outros
dois lados são denominados de \emph{catetos}.
\endíde{inition}
\beginf{theorem} [Pitágoras] \labelíthm:pitagoras)
Sejam $\Delta ABC$, um triângulo retângulo onde $a$ é hipotenusa. Então
NE ang=b"2+02 N
\endítheoremy
\begin{remarky}
A reciproca do Teorema-\refíthm:pitagoras) também é verdadeira.
\end{remark}>
\begin{proof} [\proofnameí) do Teorema-\refíthm:pitagoras)]
\idots
Assim, temos que
N[ a2 + pO2 = c”2 \gedhere M
\end{proof}y
Definição 1.4. Um triângulo é dito triângulo retângulo quando tem um ângulo reto. O
lado oposto ao ângulo reto é denominado de hipotenusa e outros dois lados são denominados
de catetos.
Teorema 1.5 (Pitágoras). Sejam AABC, um triângulo retângulo onde a é hipotenusa.
Então
a?=b2+c?
Observação 1.6. A reciproca do Teorema 1.5 também é verdadeira.
Demonstração do Teorema 1.5. ..Assim, temos que
a? +b?º =c
9. Figuras, Tabelas e Imagens Externas 60
Capítulo 9
Figuras e Tabelas Flutuantes, Tabelas
Longas e Imagem Externa
Neste capítulo, trataremos de ilustrações e tabelas.
9.1 Figuras flutuantes
Elemento flutuante é aquele que não precisa ser colocado obrigatoriamente na posição “digi-
tada”, mas que será colocado na melhor posição possível em termos de apresentabilidade.
A figura flutuante é especificada pelo ambiente figure e a tabela flutuante é especificada
pelo ambiente table, respectivamente. \eja o Exemplo 9.1.
Exemplo 9.1: ex09-figura.tex
\beginí{igure} [hbp]
\center
N
Aqui se coloca a primeira figura
N
\caption[Primeira {igura}íPrimeira figura como elemento {lutuante}
\labelífig:simp)
\endífigurey
Aqui se coloca a primeira figura
Figura 1: Primeira figura como elemento flutuante
O Exemplo 9.1 ilustra o uso do ambiente flutuante figure. O parâmetro opcional é uma
sequência de caracteres, especificando a ordem que tentará colocar a figura.
h Onde foi digitado
b na parte inferior da página
t na parte superior da página
p página separada.
! ignorar a restrição de espaçamento.
No ambiente flutuante, o LaTeX tentará as posições seguindo a lista de especificação dos
parâmetros e inserirá na primeira posição que satisfizer a exigência. Caso nenhuma posição
for conveniente, criará uma página separada especialmente para ele.
Durante a tentativa de inserção, existem restrições estéticas tal como considerar inadequado
quando sobra muito pouco espaço para o texto. Restrições como estes podem ser ignorados
quando utilizar a opção “!”
O comando \caption produz enumeração e título da figura, podendo estar no começo
ou no final do ambiente figure. Ele aceita o nome curto como argumento opcional para ser
usado na lista de figuras, caso título da figura for longo.
\ote que, o rótulo colocado pelo \label deverá ficar dentro ou depois de \\caption que é
responsável pela enumeração das figuras.
Para colocar moldura, poderá usar o \fbox, mas ele não pode ter parágrafo como argu-
mento. Neste caso, podemos usar a combinação com minipage como no Exemplo 9.2.
Exemplo 9.2: ex09-figura-fbox.tex
\beginít{igure} [hbp!]
\center
\\{boxTWbegintminipage}toO.SNlinewidth)
\center
Aqui insere a segunda figura
\captioníSegunda {igura} \labelífig:{rame}
\endí{minipage}
) % fbox
\endí{igure})
Aqui insere a segunda figura
Figura 2: Segunda figura
9.2 Tabelas flutuantes
A tabela flutuante é criado da forma similar, usando o ambiente table. Os argumentos
opcionais para controlar a posição de inserção é mesmo da figura. \eja o Exemplo 9.3 que
ilustra a tabela flutuante, contendo texto como elemento.
Exemplo 9.3: ex09-tabela-flutuante.tex
\beginttable) [hbp]
\center
Aqui se coloca a primeira tabela
Y
\captioníPrimeira tabela)
\labelítab:simpy
\end{table}
Aqui se coloca a primeira tabela
Tabela 1: Primeira tabela
\ormalmente, o conteúdo da tabela é criado pelo ambiente apropriado como tabular ou
similar. Alguns casos, podem ser criados como arquivo separado e inserido como no caso de
figuras.
\ote que, podemos criar moldura, incluindo o título da tabela através de fbox combinado
com o minipage, como feito na figura.
No caso do Exemplo 9.4 ilustra o uso de tabular dentro do ambiente table para criar
tabela flutuante.
Exemplo 9.4: ex09-tabela-tabular.tex
\beginfítable [hbp]
\center
\beginftabular|\t|pt3.5cm)|l1/) \hline
cenouras (500g) & RA$0,50 \W \hline
cogumelos (vidro de 500g) & RN$5,00 \W \hline
batata (1\g) & RN$1,20 \W \hline \hline
total & RN$7,20 \W \hline
\endí{tabular}
\captioníUsando tabular) \labelítab:tab)
\endítabley
cenouras (500g) R$0,50
cogumelos (vidro | R$5,00
de 500g)
batata (1\g) R$1,20
total R$7,20
Tabela 2: Usando tabular
\ote que, o comando \supressfloats podem ser usados para impedir que mais floats
«”
sejam inseridas na página específica, mas os “floats” com opção não respeitam este
comando.
Para que “floats” não processados (que ainda não {oram colocados} sejam postos an-
tes de mudar a página, basta usar \clearpage ou \cleardoublepage usado para limpar
configurações de páginas (chamado pelo \chapter, por exemplo).
\ote que, lista de figuras e de tabelas são geradas pelos comandos \listoffigures e
\istoftables que costumam ser colocados depois do \tableofcontents (sumário).
9.3 Tabelas longas
O ambiente tabular é ideal para tabelas pequenas. Mas as vezes precisamos de tabelas grandes
que podem ocupar mais de uma página. Para isso, existe o ambiente longtable implementado
no pacote do mesmo nome. A tabela longa é contado junto com as tabelas flutuantes e não
devem ser colocados dentro do ambiente table. Ele também possui o comando \caption*
(a versão “*” do \caption) que coloca o título, mas não acrescenta na lista de tabelas. Os
parâmetros básicos são mesmo do ambiente tabular.
\eja o Exemplo 9.5. Para que este exemplo funcione, deverá ter \jusepackageTlongtabley
no preamble do documento.
Exemplo 9.5: ex09-longtable.tex
\beginflongtableYílclr|y
\captioníTabela Longal) Mlabelíltab:teste)
W %Z é necessário pular linha após definições preliminares: caption, label,
etc.
\hline
\textbf{centrada} & \textbfípara direita) W \hline \hline
coluna 1 & coluna 2 W \hline
coluna 1 & coluna 2 W \hline
$\dots$ & SNvdots$ |W \hline
coluna 1 & coluna 2 W \hline
\end{longtable}
Tabela 3: Tabela Longa
centrada | para direita
coluna 1 coluna 2
coluna 1 coluna 2
coluna 1 coluna 2
\ote que, ao iniciar o ambiente, coloca as configurações tais como títulos, o que fazer antes
de mudar a página, etc. Depois pula a linha com “NW” e resto segue normalmente. Como
longtable usa o arquivo auxiliar para armazenar sua largura, pode precisar compilar duas
vezes para ter o resultado desejado (assim como acontece com referências cruzadas).
Para efetuar as configurações tais como o que fazer quando muda a página, etc, veja o
manual correspondente.
9.4 Imagem externa
As figuras podem ser elaboradas usando o próprio LaTeX, mas muitas vezes criamos usando
um programa externo. As imagens externas para serem inseridas no documento LaTeX, deverá
estar no formato pdf, jpg/jpeg ou png. O formato pdf costuma ser usado para ilustrações
científicos por ser pequeno e é de alta qualidade (exceto quando convertido de algum formato
bitmap). Se o programa permite gerar pdf, prefira usar este formato. O formato jpg/jpeg é
apropriado para fotos, mas não suporta transparências. O formato png é similar a jpg/jpeg,
mas suporta transparências.
O comando para incluir gráficos externos é \includegraphics implementado no pacote
graphicx (não con{undir com o pacote antigo graphics que tem menos recursos}. Para exem-
plo desta seção, assumimos que tenha \\usepackage{graphicx} no preamble do documento.
\eja Exemplo 9.6.
Exemplo 9.6: ex09-imagem.tex
\beginfí{igure}) [hbp]
\center
\includegraphics [width=O0.5Mlinewidth] (latex-via-exemplos-{ig}
\captioníImagem PDF)
\endí{igure})
Figura 3: Imagem PDF
\ote que não foi colocado a extensão (.pdf) no nome do arquivo. Em geral omitimos a
extensão do arquivo para poder trocar de formatos, se desejar.
No parâmetro opcional, foi colocado width=0.5\linewidth para especificar que largura
é metade da largura da linha atual. Os parâmetros opcionais controlam o tamanho e rotação
das imagens.
width largura da imagem
height altura da imagem
totalheight altura total (quando é rotacionado,height só mede da linha de base para cima).
scale ampliação
angle rotação em graus
origin centro de rotação especificado pela combinação de “1” (le{t}, “r” (right), “t” (top), “b”
(botton) e “c” (center).
keepaspectratio manter proporção quando height e width for especificado simultanea-
mente (usado sem o valor).
No caso de incluir o arquivo PDF com mais de uma página, poderá usar a opção page para
indicar a página a ser incluída.
O Exemplo 9.7 ilustra a rotação por 30º em torno do centro.
Exemplo 9.7: ex09-imagem-rotacao.tex
\beginí{igure} [hbp]
\center
\includegraphics [width=O.5S)linewidth,angle=30,origin=c] (latex-via-exemplos-
{ig}
\captioníImagem PDF)
\endí{igure}
Figura 4: Imagem PDF
As vezes queremos colocar figuras lado a lado para comparação ou para economia de
espaços. Para tanto, podemos usar o minipage, como no Exemplo 9.8.
Exemplo 9.8: ex09-imagem-Íado.tex
\beginífigureY [hbp]
\center
\begin{minipage}(O.4)linewidth)
\center
\includegraphics [width=0.3)linewidth] (latex-via-exemplos-{ig}
\captionílado esquerdo) \labelífig:ladol>
\end{minipage}
\beginíminipageYtoO.4)linewidth)
\center
9.5. Desenhando sobre a imagem externa
\includegraphics [width=O.3]linewidth,angle=30,origin=c]flatex-via-exemplos-
{ig}
\captionílado direito) Mlabelífig:lado2)
\end{minipage}
\endí{igure}
Figura 5: lado esquerdo
Figura 6: lado direito
9.5 Desenhando sobre a imagem externa
As vezes queremos desenhar sobre a imagem externa importada no documento, como no caso
de acrescentar fórmulas ou mais alguns detalhes. Para isso, podemos usar o ambiente gráfico
picture.
No Exemplo 9.9 ilustra a sobreposição para colocar fórmula sobre a imagem externa.
\ote que a imagem foi inserida dentro do ambiente picture.
Observe como e onde foi usado o \unitlength para permitir o ajuste de escala (mudando
o valor de \unitlength) sem perder a posição de sobreposição já ajustada.
Exemplo 9.9: ex09-imagem-sobreposicao.tex
\beginfí{igure} [htbp!]
\center
ú
\unitlength=0.45\linewidth % unidade
\beginfpictureY(1.0,1.0) % caixa reservada
\put (0,0) (\includegraphics [vidth=\unitlength] (latex-via-exemplos-{ig})
& grade para localizar coordenadas
% imultiput(0,0) (0.1,0) t11H V.line(O0, 1) 11))
& imultiput(0,0)(0,0.1) 111H line(1,0)11))
\put (O0.35,0.45) (NLARGE $e"fNpi il+1=0$)
\endípicturel
\captioníTécnica de sobreposicaoWlabelífig:sobreposicao))
\endífigurey
Figura 7: Técnica de sobreposicao
Para quem precisa efetuar sobreposição com frequência, existe o pacote overpic descrito
na Seção 16.3 da página 200.
O ambiente picture é um ambiente gráfico padrão do LaTeX que permite criar ilustrações.
\ote que, para criar ilustrações, existem vários pacotes gráficos apropriados, mas se quiser
usar o ambiente picture, lembre-se de colocar o \usepackage{pict2el} no preamble do
documento para eliminar limitações de alguns comandos gráficos deste ambiente.
O Exemplo 9.10 ilustra os comandos básicos do ambiente picture com o uso do pacote
pict2e.
Exemplo 9.10: ex09-picture.tex
\beginí{igure} [hbtp!]
\center
\unitlength=1cm % medida da unidade
& \linethicknesstimm) % tome cuidado que e comando, mnao a medida
\beginfípictureY(5,4) (0,0)
/4 put coloca o objeto grafico na posição indicada
& line (segmento) e vector (vetor)
/4 Recebe vetor diretor e comprimento do segmento/vetor
\put (4,3.5) (\line(0,1)10.5)) Z segmento
\put (5,3) (\ector(1,1)(0.5)) % vetor
\put (2,2) fNcirclefi+) Z circulo com centro e raio.
\put (1,1) fNcircle*(1.5)) %Z circle* é circulo solido
\put (3,2) floval (3,2)) % oval
\\put (3.5,2) (\makebox(0,0) [cc] ($A=\pi rº2$8)) % Caixa de texto (com {ormulas}
\put(3,0) € \polyline(0,0)(1,0)(1,1)) % linhas poligonais
\put(5,0) f \polygon(0,0)(1,0)(1,1)) % poliígonmos
\put(6.5,0) f \polygon*(0,0)(1,0)(1,1)) % poligonos preenchidos
\thicklines %4 linha mais grossa
\put (4,1) fNqgbezier(0.0,0.0) (1.3,0.0)(2.0,2.8)) % curva bezier quadratica
\thinlines Zlinha normal (mais {ina}
\put (6,1) flcbezier(0.0,0.0)(1.0,0.0)(1.0,1.0)(2.0,3.0))
%4 curva bezier cubica
\end{picture}
\captionfIlustração no formato \TeXí).\\\labelífig:tex))
\endífigurey
Á
Figura 8: Ilustração no formato TEX.
9.6 Caixas gráficas
O pacote graphicx dispões de vários comandos relacionados com a mudança de tamanho e
rotações. Eles são chamados de caixas gráficas. Os argumentos não devem conter quebra de
parágrafos. Assim, se precisar, deverá usar juntamente com o minipage (ou \parbox).
Para escalar, usa-se o \scalebox. Para indicar o tamanho fixo, usa-se o wyresizebox. \eja
o Exemplo 9.11.
Exemplo 9.11: ex09-scale.tex
Tamanho normal.
\scaleboxí12.5)íAmpliado por 2.5 vezes)
\scalebox12)[3] {Ampliado por 2x3 vezes} % 2 no horizontal e 3 em vertical (
de{orma}
\resizeboxí10cmYt!XíCom 10 cm de comprimento)
\resizeboxt!X(£0.5cm)íCom 0.5 cm de altura)
\resizeboxí5cmYtOoO.75cmkíCom Scem$\times$O.7cm) % deforma
9.6. Caixas gráficas 7O
Tamanho normal.
L
Ampliado por 2.5 vezes
Ampliado por 2x3 vezes
Com 10 cm de comprimento
Com 0.5 cm de altura
Com 5cmx0.7cm
O “!” no \resizebox especifica que é calculado automaticamente com outra medida.
A rotação e feito pelo comando \rotatebox, onde parâmetro opcional origin permite
configurar o centro de rotação, combinando “1” (le{t}, “r” (right), “t” (top), “b” (botton) e
«”
c” (center). \eja o Exemplo 9.12.
Exemplo 9.12: ex09-rotate.tex
\rotatebox{30}f{Rotacionado} por $30"\circ$.
\rotatebox [origin=rb] (-30)(Rotacionado) por $-30"\circ$ em torno de lado
direito inferior.
\rotatebox [origin=c] {45}{Rotacionado} por $45"\circ$ em torno de centro.
\reflectboxíRe{letido} está refletido. Mesmo que o \scaleboxí-1XY[1]1
Re{letido}.
\raiseboxfWdepthYfWscalebox{t1}[-1] (Re{letido}) está refletido verticalmente.
\rotatebox [origin=c] (30)flscaleboxt1.5)í{Ampliada e rotacionada})
o por 30º.
*o por —30º em torno de lado direito inferior.
F
&
x
S
obitsRsA está refletido. Mesmo que o obiisRsA.
BSESUSITO está refletido verticalmente.
por 45º em torno de centro.
x
O
Q
n
O \reflectbox reflete horizontalmente. Para refletir verticalmente, use o \scalebox, mas
precisa ajustar a sua altura.
Uma caixa é um bloco e além de ser manipulados no tamanho e posição, também pode
ser usado mais de uma vez. Por exemplo, se quer colocar um certo elemento em mais de
um lugar, ou colocar mais tarde, poderá criar uma caixa e armazenar dentro dele. Neste
texto, não vamos entrar em detalhes sobre caixas (veja o básico sobre caixas na Seção 13.8
do Capítulo 13), mas várias referências discutem sobre isso.
10. Ajuste das Fontes 72
Capítulo 10
Ajuste das Fontes
Neste capítulo, veremos o controle das fontes no LaTeX.
10.1 . Seleção da família de fontes
\um documento, usa-se vários tipos de fontes. Por exemplo, o corpo do documento nos livros
e artigos costuma ser em romano (0 que tem enfeite nas pontas, denominado de seri{a}. Os
títulos dos artigos e livros podem ficar com fontes sans serif (sem seri{a}. O corpo de
slide de apresentação ou poster costuma usar sans serif também. O código de programa,
nome do arquivo, etc que deve ser lido no pé da letra costuma estar como typewriter (mono
espaçado).
Assim, nos documentos científicos, costumam usar três famílias de fontes básicos que são
romano (com seri{a}, sans serif (sem seri{a} e typewriter (mono espaçado) na qual devem
estar em harmonia. O LaTeX usa a fonte Computer Modern por padrão na qual tem essas três
fontes estão coerentes entre si. \ote que podem trocar para outras fontes, se desejar, mas
estas três fontes devem estar em harmonia.
A família das fontes são selecionadas pelo comando \\textrm ou ambiente rmfamily para
romano, o que é padrão para artigos e livros, pelo comando \\textsf ou ambiente sffamily
para sans serif, e pelo comando \texttt ou ambiente ttfamily para typewriter.
Quando aplica a mudança da fonte dentro de um ambiente, o ambiente de ajuste de
fontes pode ser usado como comandos. Se não estiver dentro do ambiente e quer usar a
versão comando do ambiente, poderá delimitar a sua atuação, colocandoo entre chaves. \eja
Exemplo 10.1.
Exemplo 10.1: ex10-family.tex
\textsfíFontes sem seri{a}
\beginís{family}
Texto na fonte sem serifa.
\endís{family}
