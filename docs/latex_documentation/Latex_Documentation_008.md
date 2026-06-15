e \fcolorbox [modelo] ffcor+íbcolor+ítextol (caixa de texto com cor bcolor e cor do
contorno {color} são usados. \eja o Exemplo 13.4.
Exemplo 13.4: exl3-color.tex
Cor normal. flcolor{redl} Somente neste trecho muda de cor.) Aqui é cor
normal.
Combinando:
\textcoloríwhiteYlVYcolorboxíblackkítexto colorido na caixa colorida))
Cor normal. Somente neste trecho muda de cor. Aqui é cor normal.
[(GTorilosta E RaTa(osAM texto colorido na caixa colorida
O comando \normalcolor retorna para cor padrão (dentro do trecho com cores persona-
lizados), o que pode ser útil em alguns casos.
Segue uma tabela de cores básicos.
Tabela 13.1: cores aceitos em todos drivers no pacote color
black | maa | \hite red mDN | STSn | ms
blue | mum | CY90 | m | Magenta | mem | \OloOW | meem
Para mais opções de cores, poderá usar opções dvipsnames,usenames na opção do pacote
color, mas memorizar muitas cores não é produtivo. Assim, costuma usar o pacote mais
avançado de cores como o xcolor (veja a Seção 16.1 do Capítulo 16) que permite misturar
CcoOres.
13.8 Uso de caixas
Para criar comando um pouco complexo, é importante ter noção sobre as caixas. No LaTeX,
os elementos são colocados nas caixas e serão distribuídas nas páginas. Estas caixas não são
quebráveis. Por exemplo, wnbox cria uma caixa e coloca o seu argumento. Como a caixa não
pode ser quebrada, se colocar uma palavra dentro do \nbox, ele não será hifenizada, apesar
disso não ser a forma elegante de proibir a hifenização de uma palavra. Antigamente, também
usava o nbox para inserir texto no meio das fórmulas, o que é feito atualmente pelo comando
\text do pacote amsmath.
A versão completa do wnbox é o inakebox que aceitam parâmetros opcionais. Por exemplo,
um strut (espaço reservado verticalmente) pode ser criado rapidamente com o \nakebox
com auxílio de \strut (\strut reserva altura de uma linha).
Outras caixas que é usado com certa frequência é o \fbox que coloca moldura e \parbox
que é uma versão simples de minipage.
No caso de \fbox, as medidas \fboxsep e \fboxrule controlam o espaço entre conteúdo
e moldura, assim como a espessura de linha da moldura.
Uma versão completa com \\fbox é o \framebox que pode controlar a largura e o posicio-
namento. Usando em combinação com o comando \strut que insere espaço vertical, poderá
criar um retângulo com \framebox.
O \parbox permite colocar textos com parágrafos e similares, o que é proibido nas maioria
das caixas. Assim, colocando os elementos dentro do \parbox, poderá usar textos com
parágrafos e similares dentro da caixa comum. \ote que, alguns casos mais complexos, requer
o uso do minipage em vez do \parbox.
\eja o Exemplo 13.5.
Exemplo 13.5: exl3-caixa-fbox.tex
Exemplo de um \\textttístrut imbox{Nstrut}, continuação.
Texto com espaçoWnakebox [2em] {Nstrut}, continuação.
\fboxíTexto com moldura-
\setlength{\fboxsep}{10pt}
\setlength{NWfboxrule}{5pt}
\fboxíTexto com moldura personalizada)
\setlengthfí\fboxsepY{Opt}
\setlengthfWfboxrulel{ipt}
\framebox [5em] fNstrutY %Z um retângulo
\fboxtZ moldura no texrto com mais de uma linha
\parboxí\textwidthYT1%Z
Linha 1W
Linha 2
-
Exemplo de um strut, continuação.
Texto com espaço , continuação.
Texto com moldura
Texto com moldura personalizada
Além de permitir manipulações (mudar de tamanho, posição, rotação, etc), o uso de
caixas permite utilizar o elemento várias vezes. Por exemplo, poderá replicar várias vezes
um elemento, ou efetuar medidas antes de posicionar os elementos. Para salvar uma caixa,
usa-se o comando \sbox ou \\savebox. Uma caixa salva pode ser usado usado pelo \usebox.
Para salvar uma caixa, inicialmente cria uma variável para armazenar usando o wnewsavebox.
Depois salva a caixa usando \\\savebox. Uma caixa salva pode ser referenciado quantas vezes
queira, pelo comando \usebox. Para alterar a altura onde caixa será colocada, poderá usar o
comando \raisebox. \eja o Exemplo 13.6.
Exemplo 13.6: exl3-caixas.tex
\newsavebox{imybox} % cria a variavel para caixa
\saveboxíiWmyboxYíTestel % armazena conteudo
\useboxí\mybox)
\useboxí\mybox)
\raiseboxí-2ex)(TWuseboxí\mybox)>
Outra linha
Teste Teste
Teste
Outra linha
Diferente do parâmetro do comando, os atributos (cor, por exemplo) do elemento dentro
da caixa salva não podem ser alterados. Assim, quando precisar usar mesmo elemento mais
de uma vez com atributos diferentes (como no caso do texto sombreado), precisará criar um
comando em vez de salvar e reusar as caixas.
\ote que uma barra pode ser criado pelo comando \rule, embora ele não seja uma caixa.
\eja o Exemplo 13.7.
Exemplo 13.7: exl3-rule.tex
\rulefo.5SYtextwidth){1pt}
Texto
\rule[O.{Ntextwidth} [1ptX(O0.iltextheight)
continuação
Texto continuação
14. Algumas Dicas Para Criar Comandos e Ambientes 105
Capítulo 14
Algumas Dicas Para Criar Comandos
e Ambientes
14.1. Acessando os comandos com “O&”, criando coman-
dos versão “*” e parâmetro do tipo chave=valor
As vezes precisamos usar os comandos ou ambientes que contém “O” no seu nome. O
caso típico é redefinir comandos existentes tais como \naketitle, estilo de cabeçalho das
páginas, etc. \ote que os comandos e ambientes que usam “O” no seu nome são comandos
sensíveis e devem ser usados com cuidado. Para acessar estes comandos e ambientes, coloque
\makeatletter antes de usar e + depois.
Por exemplo, ajustar o espaçamento de linhas como sendo espaçamento simples, para o
texto de rodapé, mesmo que esteja usando espaçamento um e meio ou dupla no corpo do
documento, pode ser feito, acrescentando a seguinte código no preamble do documento.
\nakeatletter % ativa uso de * O'' no nome
\renewcommandVOmakefntext [1] 1%
\parindent lem%,
% inicio da alteralcíckN-ao
\linespread(1) NVecurrsize \noindent
% \hbôxtel.sSemílhss|Omake{nmark})tH1)
\\hbexteo.45emiNhss omake{nmark})t1)
% fim da alteralcíckN-ao
\nakeatother % desativa o uso de *“O'' no nome
Outro exemplo e o caso de usar linhas pontilhadas no sumário.
\nakeatletter
\renewcommand*W1OsectionfVYOdottedtoclineí(1)(1.5em)12.3em)y)
\nakeatother
no preamble do artigo habilita o uso de linhas pontilhadas no sumário, para se-
ções. Para habilitar o pontilhado no capítulo do sumário é mais complexo. \eja o
código do https://tex.stackexchange.com/questions/62438/how-to-add-leaders-to-
table-of-contents-without-tocloft.
\renewcommand*\l€echapter [2] %,
\\ifnum \\cOtocdepth >\mÔne
\addpenaltyt-\\\ehighpenaltyY%
\skip 1.0em \eplusNpe
\setlengthVYetempdimat1.SemY”,
\begingroup
\parindent \z \rightskip \epnumwidth
\parfillskip -NOpnumwidth
\leavevmode \bfseries
\advanceWleftskipVYCOtempdima
\hskip -Meftskip
tilnobreak
\xleadersWhboxT$\mOth
\nkern \edotsep mulhboxt.kWmkern \edotsep
mu$)\hfill%
\nobreakYhbexteYCopnumwidthílhss H2XNpar
\penaltyVChighpenalty
\endgroup
\i
\ote que, no LaTeX, existem vários comandos e ambientes que tem versão normal e versão
e*X”» 4X”
na qual a versão é uma variação da versão normal. Para criar os comandos versão
“*”, usa-se o comando \eifstar que determina se está ou não usando a versão “*”, mas seu
uso requer cuidados.
O código
\nakeatletter
\defwnyemphfí\eifstar N omyemphNCemyemph+ % selecionando os comandos
\newcommandí \emyemph+ [1] fVunderlinef{t1}) % versao “x
\newcommandT \eCemyemph+[1] (\emphtt13) % versao normal
\nakeatother
define a versão normal e versão “*” do \nyemph. \ote que na primeira linha foi usado o
\def em vez de inewcommand, o que é necessário quando o comando tem parâmetros. Com
o \ifstar, seleciona o comando de acordo com a existência do “*”. \ote que o primeiro é
xx” 123
versão com e o segundo é a versão sem
Depois define os comandos com “*”
e comandos sem “*” que foi usado anteriormente.
\ote o uso de “O” no nome destes comandos para proteger do uso indevido deles.
Assim, podemos usar a versão normal que enfatiza e versão “*” que sublinha. \eja o
Exemplo 14.1.
Exemplo 14.1: exl4-star.tex
\documentclass [12pt,a4paper] {article}
\usepackage [T1] {fontenc}
\usepackage [brazil] {babel}
\nakeatletter
\defnyemphfNeifstar \omyemphNCeomyemph+ % selecionando os comandos
\newcommandí \omyemphY+[1] fNunderlineí(tH1)) %Z versao “x''
\newcommandí \eemyemph+[1] {Nemphtt13} Z versao normal
\nakeatother
\beginf{document}+
Enfatizando palavras com wnyemph{Teste} e \myemph*{Teste}.
\endí{document}
Enfatizando palavras com Teste e Teste.
\ote que no caso de ambientes, a versão com “*” pode ser definido diretamente, sem a
necessidade do artifício dos comandos como em
\newenvironmentímypar+[1]% 1 argumento eh titulo
fipar \center
Tilpar \center
W Y% título e linha
W
\newenvironmentímypar*Y[1]% 1 argumento que eh titulo
fhpar \center -—-—-—-—--——————— — S$ E DESCCCICCCCOICCS W Y% título e linha
fhpar \center -——-—-—————————————————————————————— —— W
\nakeatother
Outra coisa que pode querer é criar comandos e ambientes que recebem os parâmetros na
forma chave=valor.
Para isso, usa-se o pacote keyval. para implementar o parâmetro do tipo chave=valor.
Inicialmente, precisa criar uma regra do que vai fazer quando tiver uma determinada chave
no parâmetro, usando o comando \def ineOkey.
O primeiro parâmetro é o grupo que o parâmetro pertence. Em geral, coloca o nome do
comando ou ambiente para evitar conflitos. Segundo parâmetro é o nome da chave e terceiro
é o que vai fazer. O t1 será o valor da chave.
Em geral, se tiver o nome da chave sem o valor, dará erro. Se quer aceitar a chave sem o
valor, poderá passar o valor padrão como parâmetro opcional.
O parâmetro será evaluado pelo comando \setkeys onde primeiro parâmetro é o grupo
que o parâmetro pertence.
\ote que, se o parâmetro for definido pelo comando, precisará expandir antes, ou seja,
retardar o \setkeys. Para isso, usa-se o comando \expandafter, mas retardar o comando
para expandir o segundo argumento, em vez do primeiro não é simples. Neste caso, define
um comando auxiliar com um único argumento que chama o \setkeys com nome do grupo
prefixado e aplicar \expandafter neste comando. \eja o Exemplo 14.2.
Exemplo 14.2: exl14-keyval
\documentclass [12pt,a4paper] farticley
\usepackage [T1] {fontenc}
\usepackage [brazil] f[babel]>
\{usepackageTkeyval}
\nakeatletter
4 O que voi fazer se encontrar "foo" no parametro do grupo "my".
\defineOkeyímyXlfookilfoo vale Hilpark % se receber foo sem o seu valor, dara
erro
\defineOkeyímyY{bar}[99] íbar vale Hilpark 4 com valor padrao "99" se valor
naãao for repassado.
\nakeatother
& Definindo o comando auriliar com um argumento
\ief nysetkeyst1{Nsetkeystmy}(t41))
/4 Comando associado ao argumento
\def nykeyvalueífoo=5)
\begin{document}
Testando o parâmetro chave=valor.
\setkeystmyYífoo=3,bar)
O argumento que esta " “armazenado'' no comando.
\nykeyvalue
/& expandindo o argumento primeiro para poder evaluar
\expandafter mysetkeysYexpandafterfWmykeyvaluel
\end{document}
Testando o parâmetro chave=valor.
foo vale 3
bar vale 99
O argumento que esta “armazenado” no comando.
foo=5
foo vale 5
Agora, veja o Exemplo 14.3 para exemplo de implementação do ambiente. Nele, foi
usado o \newif que cria um condicional. O comando \newifVWif<nome> cria o condicional
\if<nome> que torna verdadeiro ou falso quando chamar if<nome>true ou if<nome>false
respectivamente.
Exemplo 14.3: exl14-keyval-env
\documentclass [12pt,a4paper] farticley
\usepackage [T1] {fontenc}
\usepackage [brazil] ({babel}
\{usepackageTkeyval}
\nakeatletter
\newifWifmyparkeyvaltitle Z testar se tem titulo
%4 O titulo será associado ao comando para poder ser usado posteriormente.
\def ineOkey {myparkeyval}ítitleYt
\hrulefill1\fbox{tH1}\hrulefillNmyparkeyvaltitletrue
\def myparkeyvaltitle{t1})
\newenvironmentímyparkeyvalY[1] []€
\nyparkeyvaltitlefalse
\parWnoindent
\setkeysímyparkeyval (1)
\ifmyparkeyvaltitle
\else
\hrule
\i
\par+t
\parWnoindent
\ifmyparkeyvaltitle
\hrulefillNfboxífim do \myparkeyvaltitlekNWhrulefill
\else
\hrule
vNfi
\par+
\nakeatother
\beginí{document}
\beginí{myparkeyval}
Sem titulo.
\endímyparkeyval+>
\begin{myparkeyval} [title=Titulo]
Com titulo.
\end{myparkeyval}>
\endí{document}
m titulo.
Titulo
Com titulo.
fim do Titulo
14.2. Ambiente com parâmetro na finalização e aplicação
do comando no corpo
No caso de ambiente precisar usar o argumento na finalização, precisará associar a al
gum comando. Isto porque, o comando \newenvironmentí{ambiente} criará o par de
comandos \ambiente (chamado pelo \begin{ambientel}) e \endambiente (chamado pelo
\end{ambiente})) que funcionará em sincronismo. Os parâmetros do ambiente são passado
para o comando de inicialização, mas não para a finalização.
\eja o Exemplo 14.4 que usa o segundo parâmetro na finalização.
Exemplo 14.4: exl14-parametro-finilizacao.tex
\documentclass [12pt,a4paper] farticley
\usepackage [T1] ({ontenc}
\usepackage [brazil] ({babel}
\newenvironment {mypartwo} [2] €
\parWnoindentWhrulefil1/Z
\ifx H1\empty
\else % se naão for vazio, coloca com fbox
\fbox{t1}
vfi
\hrulefillpar
\de{ nypartwoargtwoTt2}XTZ agora eh finalizacao do ambiente
\parWnoindentWhrulefil1/Z
\ifx \nypartwoargtwoYempty
\else
\\{boxTimypartwoargtwo}
\fiz
\hrule{illlpar})
\beginfí{document}
\begint{mypartwokTlInicio}íFimy
Testando
\end{mypartwo}l
\end{document}
Inicio
Testando
Fim
\ote que no exemplo acima, foi usado o comando \ifx para verificar se o argumento
correspondente é vazio ou não. O comando \else é senão e \fi é fim se.
As vezes, queremos um ambiente que aplica um comando no corpo do ambiente. No
entanto, a chave aberta/fechada para indicar o parâmetro deve aparecer em par tanto na
inicialização, com na finalização, não podendo delimitar o corpo do ambiente.
Para casos como este, podemos usar um comando em vez da chave para inicializar/finalizar
o agrupamento. Para inicializar o agrupamento, usa-se o comando \bgroup e para finalizar,
usa-se o comando \egroup.
Como um exemplo, vamos supor que queremos um ambiente que sublinhe todo texto,
aplicando o \emph em todo corpo do ambiente (já existe tal ambiente que é em, mas aqui foi
construído como um exemplo). Exemplo 14.5.
Exemplo 14.5: exl4-comando-no-corpo-do-ambiente.tex
\documentclass [12pt,a4paper] {articley}
\usepackage [T1] {fontenc}
\usepackage [brazil] {babel})
\newenvironmentímyulbox-+í\emphWbgroupl{\egroup}
\beginf{document}
\begint{myulbox}
Testando o ambiente.
\end{myulbox}
\endí{document}
Testando o ambiente.
O uso de \bgroup/\egroup falham para vários comandos tais como \underline e \fbox.
Nestes casos, poderá usar o comando \collectObody do pacote amsmath. Exemplo 14.6
ilustra o uso do recurso de amsmath (observe que \collectObody vem antes do comando).
Exemplo 14.6: ex1l4-comando-no-corpo-do-ambiente-amsmath.tex
\documentclass [12pt,a4paper] {article}
\usepackage [T1] ({ontenc}
\usepackage [brazil] ({babel}
\usepackageTamsmath )
\nakeatletter
\newenvironmentímy{boxXfTYcollectebodyNfbox}T>
\nakeatother
\beginf{document}
\beginímyfboxy
Testando o ambiente.
\endímyfbox>
\endídocument )
Testando o ambiente.
\ote que \collectObody não pode ser usado para ambientes que recebem quebra de linhas
ou parágrafos e também não funciona para aplicar comandos com mais de um parâmetro.
Para tais casos, poderá recorrer ao pacote fora do base/required como o environ na qual
\BODY corresponde ao conteúdo do ambiente (Exemplo 14.7).
Exemplo 14.7: ex1l4-comando-no-corpo-do-ambiente-environ.tex
\documentclass [12pt,a4paper] {article})
\usepackage [T1] {fontenc}
\usepackage [brazil] {babel}
\usepackageTenviron)
\newcommandí\my{ramebox} [1] (\fboxtNparbox [\\columnwidth] (%1)))
\ewEnvironímyfbox+nyframeboxfNBODYYY 13
\beginí{document}
\beginímy{box}
Testando o ambiente.
\endímyfbox>
\endí{document}
14.3 Comandos definidos dentro do outro comando
As vezes, queremos modificar um comando dentro do outro. Por exemplo, comand \chapter
e \section modificam os comandos para exibir informações no cabeçalho. Outro caso é
os comandos que definem as informações da capa como \title e \author na qual define
comandos internos para armazenar informações para uso posterior. O Exemplo 14.8 ilustra o
uso de definição do comando dentro do comando para armazenar o parâmetro no comando
interno para o uso posterior.
Exemplo 14.8: exl4-comando-aninhado.tex
\documentclass [12pt,a4paper] {article}
\usepackage [T1] {fontenc}
\usepackage [brazil] ({babel}
\nakeatletter
\newcommandí \eomyCtitle)t)
\newcommandí\mytitle)[1] fNrenewcommandí \emyOtitle-+{it1})
\newcommandTWmyprinttitle)í\lemyetitle)
\nakeatother
\begin{document}
\nytitle{Teste}
O título armazenado é \myprinttitle
\endí{document}
O título armazenado é Teste
Como a cada chamada, o comando redefine o comando interno, o comando interno deve
existir antes.
Para redefinir um comando já existente, é interessante tirar uma cópia dele antes de
redefinir, o que permitiria usar ou restaurar o comando original, caso necessário. Para copiar
um comando, usa-se o \let. O Exemplo 14.9 ilustra o uso de \let.
Exemplo 14.9: ex1l4-comando-let.tex
\documentclass [12pt,a4paper] {article})
\usepackage [T1] {fontenc}
\usepackage [brazil] ({babel}
\newcommandíTWmythesectionk+í\roman{section}: |
\letWthesectionoriginal thesection
\begin{document}
\letVWthesectionWmythesection
\sectionfEnumeração nova)
\letWthesectionWthesectionoriginal
\sectioníEnumeração normal-
\endí{document}
i: Enumeração nova
2 Enumeração normal
Para desativar um comando, em geral associao ao comando \relax usando \let.
Para definir comando com parâmetro dentro da definição de comandos, o parâmetro do
comando aninhado (de dentro) deve ter dois “” em vez de uma para distinguir com o
parâmetro do comando externo. \eja o Exemplo 14.10.
Exemplo 14.10: exl4-comando-aninhado-com-parametro.tex
\documentclass [12pt,a4paper] {article})
\usepackage [T1] (ffontencY
\usepackage [brazil] {babel}
\newcommand{imytitledtext}[1] (1)
\newcommandfí\mytitlefortextY[1]1%
\renewcommand{imytitledtext}[1] (\textbfiH1:) HE1)/Z
d”
\nytitlefortextí\ota)
\begin{document}
\nytitledtextíTeste de aninhamento)
\endí{document}
\ota: Teste de aninhamento
Muitas vezes, usamos o comando de definição do TEX em vez do LaTeX, o que é mais
rápido de escrever (ou para di{erenciar}.
Os comandos TEX correspondentes ao newcommand do LaTeX são: \def, edef, gdef e
xdef.
Observe que \def redefine o comando caso já existir, o que requer cuidados para não
alterar o comando importante já existente. A diferença com o newcommand é a indicação dos
números de parâmetros.
Para definir comando com parâmetros, acrescenta-se o tt1t2,..., &<n>, onde <n> é o número
do parâmetro (no máximo 9). O Exemplo 14.11 ilustra o uso de definição do comando dentro
do comando para armazenar o parâmetro no comando interno para o uso posterior.
Exemplo 14.11: exl4-comando-def.tex
\documentclass [12pt,a4paper] {articley}
\usepackage [T1] {fontenc}
\usepackage [brazil] ({babel}
\nakeatletter
\defWmytitletifNgdefNOmyCOtitle{tH1}>
\newcommandTWmyprinttitle-í\lemyCetitle)
\oytitleí>
\nakeatother
\begin{document}
\nytitle{Teste}
O título armazenado é \myprinttitle
\endí{document}
O título armazenado é Teste
\ote que foi usado \gdef que é atalho para \globalVWdef, em vez de \def para que a
definição fique disponível globalmente, dai em diante. No caso de usar o \\def, a definição
só vale para dentro do ambiente que contém (caso definir comando usando \def dentro de
algum ambiente — entre \begin e \end — fora dele o comando não estará disponível. No caso
de \gdef, comando definido continua disponível {ora do ambiente}.
Existe o comando edef que expande os argumentos na hora de definir. Por exemplo,
\def wpagina{thepage} define comando que imprime a página na qual o comando \pagina
foi chamado, enquanto que \edefWpagina{thepage} define comando que imprime a página
na qual o comando \pagina foi definido. \ote que, xdef é um atalho para \globalVYedef que
mantém a definição dos comandos globalmente. No caso da definição de dentro ter parâmetro,
a indicação de parâmetro também leva dois “”. Outro caso é acrescentar algo no comando
já existente, como emWde{VWfoofYWfootl mais algo} que causa erros pela recursão infinita
e \edefYfoofVWfootl mais algol que funciona devidamente. \ote que, para adicionar algo
no comando ou ambiente existente, deverá usar o \AddToHook ou similar para funcionar
devidamente.
14.4 . Adicionando os código nos comandos e ambientes
existêntes
As vezes, queremos efetuar alteração no ambiente ou comandos existentes, adicionando co-
mandos a mais. Isto costumava ser feito pelo comando \addto do pacote babel ou similar,
mas atualmente, usa-se o comando \AddToHook.
Para exemplificar, considere o caso de definir o comando \foo e efetua a modificação
posterior com o \AddToHook.
\defYfootfum comandoy
\\AddToHookícmd/foo/beforelk% Adicionando no começo do comando
tEste é )
\AddToHookícmd/foo/a{ter}% Adicionando no final do comando
1 de teste)
A definição original do comando \foo é imprimir “um comando”. O primeiro \AddToHook
acrescenta “Este é ” antes dele, modificando para imprimir “Este é um comando” e o segundo
\AddToHook adiciona “ de teste” no final, para imprimir “Este é um comando de teste”.
No parâmetro de \AddToHook, inicia com cmd, indicando que é um comando e seguido do
separador do campo / e o nome do comando. Depois coloca-se o separador novamente e
coloca a posição que pode ser no início (be{ore} ou no final (a{ter}. Se o último campo for
omitido, será assumido \after
Para o caso de alterar o ambiente, especifica \env em vez de cmd e se a alteração for no
inicialização do ambiente, coloca-se before no último campo e se a alteração for na finalização,
coloca-se after no último campo do parâmetro.
\newenvironmentímyenvY{\beginfcenter})fVYend{center})
\AddToHookífenv/myenv/beforel%4 Adicionando no começo da inicializaçao do
ambiente
TiWbegin{bfseries})
\AddToHookífenv/myenv/a{ter}/, Adicionando no final da finalização do ambiente
TYlendíb{series})
Caso o primeiro campo for omitido, será assumido como cmd.
\ote que, o comando de inicialização e finalização do ambiente myenv são beginmyenv e
endmyenv respectivamente. Assim, podemos adicionar códigos diretamente nestes comandos
em vez do ambiente. Desta forma, para inserir comando no começo do documento (que tem
o atalho \AtBeginDocument) pode ser como no exemplo
\nakeatletter
\AddToHookTbegindocumentY% Adicionando no começo do documento
T \eifpackageloadedígraphicxYt
\defMlogofVincludegraphics [height=3ex] logo-u{scar})
