\documentclass [12pt,a4paper] {article}
\usepackage [T1] {fontenc}
\usepackage [brazil]{babel}
\begin{document}
Este é primeiro parágrafo.
Continuando o primeiro parágrafo.
Este é o segundo parágrafo.
Espaço extra são eliminados.
\end{document}
Este é primeiro parágrafo. Continuando o primeiro parágrafo.
Este é o segundo parágrafo.
Espaço extra são eliminados.
O comando do LaTeX inicia com o caractere especial “V. O primeiro comando
\documentclass tem como parâmetros delimitados pelos colchetes e outro com chaves. O
que é delimitado pelo chaves é o parâmetro obrigatório (aqui, é o article). Os parâmetros
colocados entre colchetes, separados pela vírgula são os opcionais. Neste exemplo, são 12pt e
a4paper. Opcionais significa que pode ou não colocar tais opções. O parâmetro obrigatório
(colocado entre chaves) do comando \documentclass é o tipo de documentos. Aqui foi esco-
lhido o article (artigo) que tem como objetivo, colocar maior quantidade de informações no
espaço limitado. Outro tipo de documento bastante usados é o book (livro). Os parâmetros
opcionais usados foram 12pt que é o tamanho de letra em 12pt e a4paper que é o tamanho
do papel em padrão A4.
Depois segue com sequência de comandos \usepackage. O \usepackage carrega o pacote
(conjunto de instruções) que configura o documento ou disponibiliza os comandos específicos.
O LaTeX dispõe uma grande quantidade de pacotes, uma para casa situação. No Exemplo 2.2,
foram carregados os pacotes fontenc e babel, todos eles com um parâmetro. O primeiro
pacote fontenc é usado para especificar a codificação das fontes de letras. A opção T1 indica
que a fonte está em T1 que dispõe de letras de 8-bits (acentuadas). Esta opção é útil para
definir a regra de hifenização local do documento no preamble e efetuar busca de texto com
letras acentuadas no PDF final. Além disso, isto evita de ter caracteres trocadas indevidamente
como o “<' e > por j e .
O segundo e último pacote deste exemplo é o babel com a opção brazil. O pacote
babel seleciona a regra de hifenização e nomes dos elementos (como figura, capítulo, etc)
para idioma especificada. AÀ opção brazil ou brazilian escolhe o português brasileiro (não
confundir com a opção portugese que escolherá português de Portugal).
Antigamente (anté 2018), usava-se ainda o pacote inputenc para configurar a codificação
de entrada do documento, o que não é mais necessário, exceto para reviver os documentos
antigos.
Depois encontra o \begin{document}. O comando \\\begin inicia um ambiente. Um
ambiente é uma configuração que será aplicado nos trechos entre \beginf<ambiente>) e
\endí<ambiente>). O \begin{document} e \end{document} determina o ambiente de do-
cumento na qual seus conteúdos serão colocados no arquivo PDF.
A quebra de linha não efetua quebra de linha na saída. Para que tenha um novo parágrafo
de fato, deverá pular uma linha.
\ote que, se tiver mais de um espaço, o LaTeX interpretará como um único espaço.
2.2 Mensagem de erro e correção
Quando ocorre erro de compilação, o TeXMaker mostrará em vermelho na parte de baixo
e indicará a linha onde ocorreu o erro. Maioria dos editores para LaTeX posicionará auto-
maticamente na linha do primeiro erro quando compila. Para demais erros, ao clicar nas
mensagens de erros em vermelho, posicionará automaticamente na linha correspondente a
tais erros. Para melhorar a precisão da localização de erros, quebre o parágrafo em várias
linhas (lembre-se que quebra de linha não afeta o documento {inal}.
Assim, deve corrigir os erros e compilar de novo, até sumir com todos os erros.
Quando compila o documento, o TeXMaker posicionará na página do PDF, correspondente
aonde fica o cursor no editor de texto. Para localizar qual código gerou uma determinada
parte de PDF, clique no botão direito sobre parte do PDF e escolha “clique para ir para a linha”.
2.3 Caracteres especiais
Existem vários caracteres especiais reservados para os comandos e similares do LaTeX. Por
exemplo, “V.é usado para iniciar um comando, chaves é usado para indicar os parâmetros,
etc. Para inserir estes caracteres especiais no documento, deverá usar os comandos especiais
de LaTeX.
No código fonte do Exemplo 2.3, foi colocado somente os trechos que ficam no corpo
do documento. Para que o arquivo compile, deverá colocar entre \beginf{document} e
\end{document}+ do arquivo válido como do Exemplo 2.2.
Exemplo 2.3: ex02-caracteres.tex
& esta é comentário
Alguns caracteres especiais:
\textbackslash, N$, NME, NZ, 186 1, W, V
Alguns acentos no modo TeX (atualmente, não é mais necessário):
V.ia, \a, \e, V., \a, \u
""Abrindo e fechando aspas''
Logo do \LaTeXt) e do NVTeX.
Alguns caracteres especiais: , $, 4, %, & .1,)
Alguns acentos no modo TeX (atualmente, não é mais necessário): á, à, ê, 1, à, ú
“Abrindo e fechando aspas”
Logo do LaTeX e do TEX.
O Exemplo 2.3 mostra alguns comandos para produzir caracteres especiais.
\ote que as letras com a acentuação direta pelo teclado é suportado. No exemplo acima,
foi mostrado a acentuação do modo TEX que pode ser usados em alguns casos especiais. \ote
[188))
que V' acentua a letra seguinte, mas tem pingo e “í” (com acento) não tem pingo. \i é
6i”
o comando para produzir sem pingo. No derivado de e-TeX como o TeX atual, costuma
automatizar a retirada de pingo quando acentua, eliminando a necessidade do uso de i sem
pingo. \ote também que o acento agudo no modo TEX é produzido por apóstrofos e não pelo
acento agudo.
Apóstrofos é aberto por um acento agudo e fechado pelo apóstrofos. Aspas é aberto pelos
dois acentos agudos e fechado pelos dois apóstrofos (fiquem atentos de que fechamento de
aspas é dois apóstrofos e não é aspas).
No LaTeX, quando encontra “%”, o restante desta linha será considerado como comentário
e é ignorado completamente.
Comentário é importante para inserir observações sobre o código, ou desativar um trecho
do código. Em geral, quem quer remover um trecho do código de LaTeX no documento,
simplesmente comenta o trecho, pois se algum dia quiser ativar, é só remover o “%” do
comentário.
Para comentar/descomentar um trecho maior no TeXMaker, selecione o trecho e use o
Editar->Comentar e Editar->Descomentar.
Quando editar um documento, existem palavras que devem aparecer grudados (não pode
ficar primeira parte no final de linha e outra no começo da linha) como no caso de enumeração
de páginas, exemplos, teoremas, etc. Neste caso, usa-se o til (-) em vez do espaço. Por
exemplo, no caso de “página-1”, não acontece de “página” ficar no final de uma linha e “1”
ficar no começo da próxima linha. Outros casos é colocar entre artigos e pronomes, como em
O-Teorema de Pitágoras para evitar que o artigo fique no final de uma linha e restante na
próxima linha.
Por último, quando insere comandos e precisa ter espaço depois dele, coloque um par de
chaves. Por exemplo, “\LaTeX produz” ficaria como “LTg&Xproduz” (grudados) enquanto que
“\LaTeX{t} produz” ficará como “LaTeX produz” (com espaço correto). Também lembre-se
que no comando de LaTeX, maiúsculo e minusculo são distinguidas. Portanto, “Latex” ou
“\Mlatex” resultarão em erros em vez de produzir logotipo de LaTeX.
3. Introdução às Fórmulas Matemáticas 7
Capítulo 3
Introdução às Fórmulas Matemáticas
Neste capítulo, veremos um pouco sobre as fórmulas matemáticas.
3.1 Fórmula textstyle e displaystyle
Uma fórmula matemática (ou modo matemático) textstyle (ou inlinestyle) é uma fórmula
no meio do texto. Por exemplo, denotaremos uma sequência por {x, } e seu limite por
lim,, — cox, é modo textstyle, pois fórmulas estão no meio do texto. Agora as fórmulas
matemáticas que ocupam linha separada de texto como em
—b + \b? — 4ac
=
é denominado de fórmula matemática no modo displaystyle.
A fórmula no modo textstyle devem ficar delimitados entre “$” ou “1(” e ))”, ou ainda
poderá usar o ambiente math. O mais usado é delimitar com “$”.
A fórmula no modo displaystyle devem ficar delimitados entre “$$” (dois dólares) ou
A e ÀAP”, ou ainda poderá usar o ambiente displaymath. E recomendado que delimite com
1 e A]”, pois delimitar com “$$” (dois dólares) dificultará a depuração (achar erros).
Exemplo 3.1: ex03-formulas.tex
Solução da equação $ax 2+bx+x=0$ é dado pela fórmula
N
x=\frací-bYpmilsqgrtíb - 2-4ac))(2a)
J
Elemento da matriz $A$ costuma ser denotado por $a {ij}$
Solução da equação ax? + br + x = O é dado pela fórmula
—b + V.b? — 4ac
t=
Elemento da matriz À costuma ser denotado por a;;
No modo matemático, “” é usado para indicar a potência e “ ” indica o índice. Outros
comandos utilizados foram, \frac que produz frações, onde primeiro parâmetro é numerador
e segundo, o denominador. O comando NVsqrt produz raiz do argumento. O comando \pm
é o símbolo +. Na matemática, muitos símbolos são usados e o LaTeX dispõe de comandos
para cada uma desses símbolos. Em geral, o editor para LaTeX dispõe de painel de inserção
dos símbolos matemáticos para ajudar na elaboração do documento. No caso de TeXMaker,
tem um botão no painel lateral esquerdo que permitem ativar tais painéis, organizados em
grupos. As letras gregas no ETEX são produzidas pelo comando com nome em inglês. Se
nome começar em maiúsculo, será letra grega maiúscula.
\ote que, quando os parâmetros de um comando for mais de um (mais de uma letra, por
exemplo), deverá colocar entre chaves, como foram feitos para \\frac e sqrt.
Isto vale também para expoentes e índices, como foi feito no elemento da matriz (com
Índices de duas letras).
O comando \sqrt aceita o parâmetro opcional (delimitado pelos colchetes) para poder
produzir raiz n-ésima. O $\sqrt [n] (x)$ produz (&/x. O Exemplo 3.2 ilustra algumas letras
gregas e símbolos. \ote que uma tabela completa de símbolos do ETEX [Pak17] está disponível
gratuitamente.
Exemplo 3.2: ex03-simbolos.tex
Algumas letras gregas minúsculas: $\alpha, \beta, \gamma, \lambda, \\\pi$.
Algumas letras gregas Maiúsculas: $\Gamma, \Delta, \Lambda, \Pi, \Omega$.
Alguns símbolos:
$\le, \ge, \neg, \lin, \notin, \lexists, \nexists, \to, \infty, \forall, À
therefore$.
Algumas letras gregas minúsculas: a, 6,7,A,T.
Algumas letras gregas Maiúsculas: T, A, A, IL, .
Alguns símbolos: <,>,£,€,É,3,À,-,0o,V, .
3.2 Modo displaystyle no meio do texto
As fórmulas no meio do texto (textstyle) são produzidos de forma que economize a sua
altura. Por isso, elementos que normalmente ficariam empilhados, ficariam como índice e
expoente. Por exemplo, lim r,, no modo textstyle ficaria como lim . Para que uma
nA+0oo
\nA+0O0 'Tn
fórmula fique como displaystyle no meio do texto, coloque \displaystyle no começo das
fórmulas. O Exemplo 3.3 ilustra o caso.
Exemplo 3.3: ex03-displaystyle.tex
Temos que $\lim ínVtolinftylx n=0$ Ztertstyle
e $idisplaystyle Mim ínVtolinftylx n=0$ Zdisplaystyle
Outros casos $\sum fi=0OX"n i = O+1+\cdots+n$
e $idisplaystyle \sum fi=0X"n i = O+i+\cdots+ng.
Forçando a colocar encima/embaixo
V. \intMUlimits 1 f = \intob af(x)dx N]
Forçar a não colocar encima/embaixo
V[ \suminolimits fk=O0X"n x k = 1 N
Temos que lim =0e lim x,=0
n+0oo
Outros casos z;;oi=0+1+--«+neZi=0+1+--'+n.
i=0
nãoco Tn
Forçando a colocar encima/embaixo
b
1/ f= / f{o}da
Forçar a não colocar encima/embaixo
ZZ:O x, =l
“o»
Para forçar a colocar elementos embaixo em vez de como Índice quando usa o , USa-se
o comando Mlimits, como no Exemplo 3.3.
\ote que, para colocar no modo textstyle nas fórmulas displaystyle, existe o comando
\textstyle que é usado de forma similar a \displaystyle. Nesta família de comandos,
também existe o comando \scriptstyle que tenta reduzir o tamanho das fórmulas.
3.3 Equação enumerada e referências cruzadas
Uma equação enumerada é produzido pelo ambiente equation. Quando algum comando
do LaTeX enumera automaticamente (equações, seções, capítulos, figuras, tabelas, itens
de istas enumeradas, teoremas, etc), sua enumeração pode ser guardada e usada no
outro lugar, recurso conhecido como referência cruzada. Para tanto, coloca-se o co-
mando \labelínome do rótulo) que produz um rótulo que armazena a enumeração e
\refínome do rótulol) aonde quer colocar esta enumeração. O Exeplo 3.4 ilustra o uso
da referência cruzada.
Exemplo 3.4: ex03-ref.tex
\beginfequationkVWlabelíeg:pitagoras)
a 2=b"2+c72
\endfequationY
Pela Equação-\refífeq:pitagoras) da página-\pagerefíieg:pitagoras)\ldots
a?=62+c? (1)
Pela Equação 1 da página 10
Como já foi mencionado, o ambiente equation produz enumeração automática na equação.
Assim, poderá criar um rótulo para referenciar o número desta equação com o comando \label.
O nome do rótulo escolhido para esta equação foi eq:pitagoras. Tome cuidado para não
usar espaços, letras acentuadas ou símbolos especiais, o que dificulta a depuração ou causa
erros. No Exemplo 3.4, “:” foi usado em vez do espaço para separar palavras. \ote que foi
colocado o prefixo “eq” para rótulo da equação. Como pode ter teoremas, equações, figuras,
etc que podem sugerir o mesmo nome, é costume usar algum prefixo para cada categoria, o que
facilitará a lembrar o elemento que é associado ao rótulo. Para referenciar (usar o número)
da equação, foi usado o comando \ref e para referenciar a página, foi usado o comando
\pageref. \ote que os editores especializados para LaTeX, costuma ter recursos de listar os
rótulos existentes para referências, o que facilita a editoração e prevenir erros. Também note
o uso de “-” em vez do espaço para usar referências, o que evita que nome “Equação” fique
no final de uma linha e numeração no começo da próxima linha.
Quando usa a referência cruzada, as enumerações sempre estarão coerentes e se usar o
pacote hyperref, terão link automáticos no documento PDF.
Uma observação importante é o fato do LaTeX utilizar arquivo auxiliar para armazenar
rótulos. Assim, quando usa as referências cruzadas, precisam compilar o documento duas
vezes para ter a enumeração ou link correta.
4. Estrutura de Texto 11
Capítulo 4
Estrutura de Texto
Neste capítulo, vamos ver sobre a formatação de textos.
4.1 . Alinhamentos
O alinhamento do texto padrão no LaTeX é justificado, isto é, alinhado tanto a direita como
a esquerda. Para alinhar somente a esquerda ou a direita, usa-se o ambiente flushleft e
flushright. Para centralizar, usa-se o ambiente center. O Exemplo 4.1 ilustra os alinha-
mentos de texto.
Exemplo 4.1: exO04-alinhamento.tex
Parágrafo normal.
\begin{center}
Parágrafo centralizado.
\end{center}
\beginfflushrighty
Parágrafo alinhado a direita.
\endí{lushright})
Parágrafo normal.
Parágrafo centralizado.
Parágrafo alinhado a direita.
Quando quer alinhar dentro do ambiente (o que tem \begin e \end, poderá colocar
como comando \center, \flushleft e \flushright, respectivamente que o alinhamento se
aplicará até obter o final do ambiente em questão.
Para ter trecho justificado em ambos os lados dentro do ambiente com alinhamento a
esquerda, direita ou centralizada, costuma colocar dentro do ambiente minipage que veremos
na Seção 4.7.
Não é o alinhamento, mas para incluir linhas em branco, deverá colocar “NV” intercalado
com linhas em branco. Para indicar uma nova linha (finalizar uma linha sem esperar atingir
{inal de linha}, coloca se “NN” ou newline. Para inserir quebra de linhas, mas que justifique,
deverá usar o \linebreak, o que é ilustrado no Exemplo 4.2
Exemplo 4.2: exO04-nova-linha.tex
Esta é a primeira linha NW
e esta e a segunda linha
Esta é a primeira linha Mlinebreak
e esta é a segunda linha.
Esta é a primeira linha
e esta e a segunda linha
Esta é a primeira linha
e esta é a segunda linha.
\ote o uso de “NV” para inserir linha em branco.
4.2 \otas de rodapé e ênfase de texto
\ota de rodapé é colocado pelo comando \footnotetí<texto>) que colocará marca de rodapé
no local e <texto> na parte inferior da página atual.
Ele é usado para colocar alguma observação, mas não quer que conste como conteúdo
do documento. Por exemplo, explicação dos termos que aparece, podem ser colocados como
rodapé. \eja o Exemplo 4.3
Exemplo 4.3: ex04-rodape.tex
No meio do texto, podemos colocar a nota de rodapé\footnoteínota que fica na
parte inferior da páginal) para explicações adicionais tais como
significado da palavra, ou fonte que foi usada.
No meio do texto, podemos colocar a nota de rodapé! para explicações adicionais tais
como significado da palavra, ou fonte que foi usada.
'nota que fica na parte inferior da página
Para enfatizar o texto dentro do contexto como os termos a ser definidos, usa-se o comando
\emph{texto} ou o ambiente em. Este comando (ou ambiente) alterna entre fontes romano
reto e itálico para que o trecho seja enfatizado. \ote que os ambientes em tem a versão
de comandos Nem que pode ser usados dentro do outro ambiente (como os comandos de
alinhamento). Caso não esteja dentro do ambiente, poderá delimitar simplesmente pelos
chaves e colocar o comando no começo dele. Isto está ilustrado no Exemplo 4.4.
Exemplo 4.4: ex04-enfase.tex
\emph{Enfatizado} ou
\beginfemlenfatizadoYendíemy
ou
\begin{center}
Nem Centralizado e enfatizado.
\end{center}
ou
flem Enfatizado.)
Texto normal.
Enfatizado ou enfatizado ou
Centralizado e enfatizado.
ou Enfatizado. Texto normal.
4.3 Listas
O texto pode ter várias estruturas básicas, tais como listas, cotações, etc.
Uma das mais utilizadas é listas.
Existem três tipos básicos de listas que são especificadas pelos ambientes enumerate (lista
enumerada), itemize (lista de itens) e description (lista de descrições). Dentro de cada
ambiente, cada item é iniciado com o comando \item. O Exemplo 4.5 ilustra algumas destas
listas.
Exemplo 4.5: exO4-listas.tex
\begin{enumerate}
\item Este é o primeiro item da lista enumerada.
\item Agora, segundo item da lista enumerada
\end{enumerate})
\begin{itemize}
\\\item Este é o primeiro item da lista de itens.
\item Agora, segundo item da lista de itens.
\end{itemize}
\begin{itemize}
\\\item Item com marcador padrão.
\item [$last$] Item com marcador personalizado.
\endí{itemize}
\begin{description}
\\item [enumerada] Cada item recebe uma enumeração.
\\\item [{tenizada}l Em vez de enumeração, recebe um marcador.
\item [descrição] Descrição das palavras.
\endf{descriptiony}
1. Este é o primeiro item da lista enumerada.
2. Agora, segundo item da lista enumerada
* Este é o primeiro item da lista de itens.
e Agora, segundo item da lista de itens.
e Ttem com marcador padrão.
* Item com marcador personalizado.
enumerada Cada item recebe uma enumeração.
itenizada Em vez de enumeração, recebe um marcador.
descrição Descrição das palavras.
As listas podem conter outras listas como itens. \eja Exemplo 4.6.
Exemplo 4.6: exO4-sublistas.tex
\beginfenumerate
\\\item Este é o primeiro item da lista enumerada.
\item Segundo item é lista de itens.
\boegin{itemize}
\\item Este é o primeiro item da lista de itens.
\item Agora, segundo item da lista de itens.
\endí{itemize})
\item Este é o terceiro item da lista enumerada.
\end{enumerate})
1. Este é o primeiro item da lista enumerada.
2. Segundo item é lista de itens.
* Este é o primeiro item da lista de itens.
e Agora, segundo item da lista de itens.
3. Este é o terceiro item da lista enumerada.
Para trabalhar com listas enumeradas, é aconselhável carregar o pacote enumerate que
permite controlar as enumerações. Para isso, acrescente o comando \usepackage{Tenumerate}
no preamble do documento.
No enumerate, passa-se um parâmetro opcional que seria o modelo de enumeração do
primeiro item. Neste modelo, “1”, “i”, “ 1º, “a” e “A” serão considerados contadores e eles
são incrementados a cada item. Se aparecer estas letras que não sejam contadores, delimite
pelos chaves. \eja o Exemplo 4.7.
Exemplo 4.7: exO04-enumerate.tex
\documentclass [12pt,a4paper] {article}
\usepackage [T1] {fontenc}
\usepackagefamsmath,amssymb+>
\{usepackageTenumerate}
\beginí{document}
\begin{enumerate} [Propríikedíalde 1)]
\item $x + (y + 2) = (x + y) + z$ (associativa)
\item $x + y = y + x$ (comutativa)
\endT{enumerate}
\endf{document}
Propriedade 1) x + (y +2) = (x +y) + z (associativa)
Propriedade 2) x +y = y + x (comutativa)
Se precisar de ambientes extras de listas diferentes do padrão, podemos definir usando o
ambiente list, o que não vamos entrar em detalhes.
4.4 Tabelas
Uma tabela no modo texto é produzido pelo ambiente tabular e a tabela no modo matemático
é produzido pelo ambiente array, que apresentam o mesmo sintaxe e a mesma funcionalidade.
O argumento obrigatório destes ambientes é o “alinhamento” das colunas que devem ser
«” ”
especificados com “1” (le{t}, “c” (center), “r” (right) ou “p{largura}” (texto justificado com
largura {ixa}. Para traçar uma linha vertical entre colunas ou no bordo, usa-se o “ |”
, junto as
especificações de alinhamento. Os elementos da tabela é indicado, separado pelo “&”, sendo
que a mudança de linhas é feito pelo “W” que é newline. Para traçar uma linha horizontal,
usa-se o comando “\hline”.
O Exemplo 4.8 é um exemplo de tabelas no modo texto.
Exemplo 4.8: exO04-tabular.tex
\beginttabularY(||1/clrl|l) Z linhas verticais duplas na borda e simples
entre colunas
\hline Z uma linha horizontal no comeco da tabela
& 2&3W \hline Z uma linha horizontal apos esta linha
abc & 3 & 4W
3 &4& $\fraciliNsqart{2}HH5)$ NW \hline Z uma linha horizontal pra
finalizar
\endí{tabular}
Tabela com uma coluna de largura fixa.
\beginftabularYíT|pí3.5cmY|l1|/) \hline
cenouras (500g) & RNA$0,50 W \hline
cogumelos (vidro de 500g) & RNA$5,00 W \hline
batata (1\g) & RN$1,20 \W \hline \hline
total & RN$7,20 W \hline
\endítabular+
Tabela de largura fixa
% largura da tabela é O0.5 de \columnmwidth (largura da linha)
\beginítabular*Y(0.5\columnwidth+feflextracolsepí\\{ill}+)l|1/clrl)
\hline
& 2&3W \hline
abc & 3 & 4W
3 &4& $\fracil+iNsqgrt(2)HH5)$ NW \hline
\endítabular*>
2 3
abc | 3 4
3 4 | 42
Tabela com uma coluna de largura fixa.
cenouras (500g) R$0,50
cogumelos (vidro | R$5,00
de 500g)
batata (1\g) R$1,20
total R$7,20
Tabela de largura fixa
2 3
abc 3 4
Para mesclar células (juntar mais de uma célula como sendo uma única célula), usa-se
o comando multicolumn que tem como primeiro argumento, o número de células a serem
juntados, o segundo especifica o alinhamento da coluna e terceiro, o que vai colocar nesta
célula. \ote que as formatações de colunas do multicolumn deve ser especificado um por um,
independente de estar especificado ou não no começo da tabela.
No Exemplo 4.9 com o ambiente array (para ambiente matemático), foi usado o
multicolumn para juntar duas primeiras colunas da primeira linha, centrando os dados
e traçando linha vertical antes e depois da célula.
Exemplo 4.9: exO04-multicolumn.tex
N
\beginfarrayY(||1/clrl|) \hline
\nulticolumní2X(||{clX12} & 3 W \hline
23 &E&E3&E4W
3 & 4 & \fracítl+\sagrti{2}H5) NW \hline
\endfarray>
\i
2813
o
-
n
+
êlwlà('.«.'à
Para traçar linhas horizontais apenas em algumas células, usa-se o comando \\clineíi-jy
onde “i” e “j” são colunas iniciais e finais onde a linha é traçada. \eja o Exemplo 4.10.
Exemplo 4.10: exO04-cline.tex
