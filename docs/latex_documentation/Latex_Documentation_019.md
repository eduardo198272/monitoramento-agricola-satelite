A.4. Nome das funções e delimitadores no modo matemático 263
Setas
\\\es « o « « K >D MNDDINZ M
A seta dupla \Longleftrightarrow costuma ser usado para “se, e somente se”, mas com
pequeno ajuste no espaçamento. Para simplicidade, existe o comando \\iff que produz
<> . No pacote amsmath, define também o \implies para “implica” que tem mesmo
símbolo que \Longrightarrow, mas com espaçamento já ajustado devidamente.
Arpões
——
=
=2
Para produzir negação do símbolo longo como de “não implica”, poderá usar o \centernot
do pacote centernot(que não é da base nem do required) em vez do \not, como em
\centernotYimplies em vez de \wnotlimplies.
A.4 Nome das funções e delimitadores no modo mate-
mático
Os nomes das funções devem estar em \mathrm e tem vários comandos já defini-
dos. No caso de precisar definir um novo (como nome em português), use algo como
\newcommandí\sen+fWmathrmísent+) no preâmbulo. Se estiver usando o pacote AMS, po-
derá substituir por \eclaremathOperatorfí\senk{sen} no preâmbulo. No caso de de-
finir nomes do estilo limite na qual o índice fica embaixo no modo display, use em
conjunto com \mathop, como em \newcommandí\argmin+í\mathopí\mathrmíargN,min))Y.
\ote o uso de , para inserir espaço entre duas palavras. Com o pacote do AMS, po-
derá escrever como \eclaremathOperator*{\argmin}fargy,mink (usando a versão “*” do
\eclaremathOperator).
\eja o Exemplo A.8 para nome das funções pré-definidos.
Exemplo A.8: ex-a-nome-funcao.tex
$\arccos \arcsin \arctan \arg \bmod \cos \cosh \cot \coth \csc \\deg$
$\det \dim \exp \gcd \hom \\\inf \ker Mlg$
$\lim Miminf Mimsup Mn Mog \inax \wnin \Pr \sec \sin \sinh \sup \tan À
tanh$
Para indicar a congruência módulo $n$, podemo suar o comando \verb+\pmod+
como em $a \equiv b \pmodínIs.
A.4. Nome das funções e delimitadores no modo matemático 264
arccos arcsin arctan arg mod cos cosh cot coth csc deg det dim exp gcd hom inf ker lg
lim lim inflim sup ln log max min Pr sec sin sinh sup tan tanh
Para indicar a congruência módulo n, podemo suar o comando NYpmod como em a = b
(mod n).
Para delimitadores, veja o Exemplo A.9. Em geral, o tamanho dos delimitadores serão
ajustados automaticamente quando usar em conjunto com \left e \right.
O comando \left indica que o delimitador é do lado esquerdo e \right indica que o
delimitador é do lado direito. Além disso, poderá usar delimitador diferente para esquerda e
a direita como em
\left(\frac fxº2)12HXNright| 0 2=\frací2 2)412) - \\fracío 2H+12)=2
2/2 2 2 o
que produz (%, = % — % = 2. Quando usa o delimitador em apenas um dos lados, use
o
”"”para indicar que não há delimitador no outro lado, como em
\MleftWx+y=1 \atop x-y=OlWright.
x+y=l
que produz ízfy:º :
Para colocar delimitador ajustável no meio, poderá usar uniddle na variante do e-TEXcomo
no caso do TEFX atual. Por exemplo,
\leftWlangleWphiWmiddle| psiNrightirangle
insere delimitador
Exemplo A.9: ex-a-delimitadores.tex
Delimitador que pode ser usado independente ou como delimitador auto
ajustável (com \erbt+\left+ e \erbt+\right+).
$\\downarrow Mlangle Mlceil Mfloor ( /$
$\Downarrow \rangle \rceil \r{loor } \backslash$
$[ | \uparrow \updownarrow N ] \l \parrow \pdownarrow V.$
Símbolos de tamanhos variáveis grandes que só podem ser usados em conjunto
com \erb+\left+ e \erb+\right+.
$\left imoustachelright. Mleft.\rightWrmoustache$Z não tem no Latin Moden
Math
$\left M lgrouplyright. \Mleft.\rightWrgroup$
A.5. Outros símbolos 265
Delimitador que pode ser usado independente ou como delimitador auto ajustável (com
\left e \right).
\L DV E U
Símbolos de tamanhos variáveis grandes que só podem ser usados em conjunto com \left
e \right.
V. o
Os comandos \vert e \ert são mesmos que | e Xl, mas podem ser usados onde | causa
problemas como na entrada de índices remissivos.
Quando tiver quebra de linha no meio da equação (que pode ser efetuado pelos ambientes
do pacote amsmath), os delimitadores auto ajustáveis falham. Outro caso é ter um delimitador
dentro do outro de mesmo tamanho. Neste caso, poderá ajustar o tamanho manualmente
pelos comandos tipo “big” em vez de “left/right”. O especificador do delimitador grande na
ordem crescente são: \big, \Big, \bigg e \Bigg. \eja o Exemplo A.10.
Exemplo A.10: ex-a-big-delimitadores.tex
Exemplo de ajuste manual do tamanho doas delimitadores.
N
\Bigg(x+\bigg(y+\Big(z+\big(wtvlWbig)NBig)\bigg)NBigg)
yJ
Exemplo de ajuste manual do tamanho doas delimitadores.
<x+ (y+(z+(w+v))»
A.5 Outros símbolos
Símbolos que costuma ser usados como caracteres estão listados no Exemplo A.11.
Exemplo A.11: ex-a-tipo-letra.tex
$\bot \ell \exists NVforall \hbar NMIm \\\imath \in \jmath$
$\ni \partial \Re \top \wp$
Para produzir símbolo de negação, poderá usar \verb+\not+ antes do símbolo,
como em $\notlin$ ou $\notlexists$.
A.6. Acentuação no modo matemático 266
Le3\hIr E DORTÊ
Para produzir símbolo de negação, poderá usar not antes do símbolo, como em é ou À.
O Exemplo A.12 ilustra mais alguns símbolos adicionais.
Exemplo À.12: ex-a-simbolos-diversos.tex
Símbolos diversos
$\aleph \emptyset \angle \backslash \infty \nabla \neg \prime \surd À
triangle$
Símbolos musicais
$\flat \natural NVsharp$
Símbolos diversos
NAZYooVA' A
Símbolos musicais
dRF
Alguns autores preferem usar o \arnothing do amssymb em vez do \emptset para
representar o conjunto vazio.
A.6 Acentuação no modo matemático
Nas fórmulas, costuma usar vários tipos de acentuações para produzir símbolos novos que é
relacionado com outros já existentes (não acentuado). \eja o Exemplo A.l3para acentuação
no modo matemático.
Exemplo A.13: ex-a-acentuacao.tex
Acentuação no modo matemático
$\acute{a} \bar{a} \breveta) \checkla) \ddot{al} \dot{a}$
$iYgrave{a} \hat{a} \mathring{a} \tilde{al} \ec{ta}S$
Para i e j sem pontos, existem os comandos \erbt+\limath+ e \erb+\jmath+ que
podem ser usado como em $\hatí\limath)$ e $\hatí\jmath)$.
Acentos matemáticos extensíveis.
A.6. Acentuação no modo matemático 267
$\widetilde{abc}) \widehat{abc} \overleftarrowlabck$
$\overline{abc} \underline{abclk} \overbrace{abc}l f{n}$
$\underbrace{abc} {nk} \overrightarrow{abc} \sqgrt{abc} \sqrt[n] {abc}$
Pontuação no modo matemático
$\edotp \edots \colon Mldotp \ddots NMldots \vwdots$
\ote que vários símbolos de pontuação são usados como relações no modo
matemático.
Assim, quando precisar usar como pontuação, existem comandos para tal (a
diferença entre relação e pontuação está no espaçamento. Por exemplo, $a:
b$ é uma relação de proporção, enquanto que $alcolon b$ é uma pontuação.
Acentuação no modo matemático
áaaadaá àdâaad
Para i e j sem pontos, existem os comandos \imath e \jmath que podem ser usado como
em 4 e j.
Acentos matemáticos extensíveis.
abcabcabc \abcã;c abc abcx/í x/ã
Pontuação no modo matemático -
\ote que vários símbolos de pontuaçao são usados como relações no modo matemático.
Assim, quando precisar usar como pontuação, existem comandos para tal (a diferença
entre relação e pontuação está no espaçamento. Por exemplo, a : b é uma relação de
proporção, enquanto que a: b é uma pontuação.
\ote que, diferente do \bar, o comando \overline adjacentes ficam grudados, como
em AB. Para evitar isso, siga a instrução do [Pak17] para definir um comando apropriado
denominado de \\closure que não grudam. Para isso, basta colocar o seguinte código no
preâmbulo.
\newcommandfVclosureY[2] [3] %,
tINmkernttimuloverlinefNmkern-timutt2))
Alguns alfabetos matemáticos disponíveis por padrão estão listado no Exemplo A.14.
Exemplo A.l14: ex-a-alfabeto.tex
Alfabetos matemáticos
$\mathrm{ABCdef123} \mathitíABCde{123} \mathbfí{ABCdef123}$
$\mathnormal ({ABCdef123} \mathcalíABCY$
& \mathcal é somente para romana maiúscula
A.6. Acentuação no modo matemático 268
Alfabetos matemáticos
ABCdef123A BCdef1l 28 ABCdef123 ABCdefl123ABC
Caractere de extensão. Diferença com — = (relação) é somente o espaçamento. Quais são
os caso de uso?
O alfabeto \mathbb requer o pacote do AMS. No sistema de blog e moodle ou similar sem
a suporte ao pacote adicional, use o imathbf em vez de \mathbb.
B. Desenvolvendo Pacotes e Classes 269
Apêndice B
Desenvolvendo Pacotes e Classes
Aqui veremos como escrever seu próprio pacote, também chamado de arquivos de estilos.
Lembrando que, o arquivo de estilos, classes e similares não precisam ser instalados para
ser usado. O LaTeX dá preferência aos arquivos locais (o que está junto com arquivo .tex).
Assim, se quer testar um estilo ou classe mais nova que está instalado, basta manter o arquivo
novo junto ao arquivo .tex, o que costuma fazer para desenvolver arquivos de estilos e/ou de
classes.
B.1 Criando pacotes
Pacote é conjunto de configurações de documentos e definições de comandos ou similares para
ser aplicado no documento desejado. Pacote também é chamado de arquivo de estilos e tem
a extensão sty.
Um pacote começa com o cabeçalho. O comando \eedsTeXFormat {LaTeX2e} colocado no
começo do pacote indica que ele precisa do LaTeX 2.. Em seguida, costuma colocar o comando
\ProvidesPackageT<nome do pacote>Y[<data> <mensagem>]. onde <nome do arquivo> é
nome do arquivo, incluindo a extensão e o argumento opcional <data> <mensagem> é a data no
formato ano-mês-dia (ou ano/mês/dia) seguido da mensagem a ser emitido quando carrega
o pacote. Na data, o ano deve ser de 4 digitos. As informações adicionais tais como versões,
mensagens de advertência ou erros, etc pode ser emitido pelo comando \\typeoutí<mensagem>>
a qualquer momento.
Quando o pacote é uma classe de documento baseado num documento já existente, poderá
carregar a classe de documento pelo comando \LoadClass e efetuar ajustes necessários.
\ote que não precisa colocar imakeatletter e \makeatother (nem deve) no arquivo
de estilo para acessar comandos que usam “O”, pois já está com o uso de “O” ativado por
padrão. No caso de XeLaTeX/LuaLaTeX que usam pacotes mais modernos, usam “ ” e “” no
nome dos comandos protegidos. Para usar estes comandos no pramble, deverá colocar entre
NExplSyntaxOn e \ExplSyntaxOff. Também não é necessário no arquivo de estilos.
Era recomendado que use a acentuação no modo TEX, pois não saberemos a codificação
que o usuário final vai escolher no seu documento. Mas atualmente, o recomendado é usar a
B.1. Criando pacotes 270
codificação em utf-8, o que costuma ser padrão para editor dedicado para LaTeX.
Dentro do arquivo de estilos, o comando para carregar os pacotes é \equirePackage em
vez de \usepackage. Para testar se o pacote existe, cheque se tem o arquivo correspondente
com o \IfFileExists. Não esqueça da extensão do arquivo no nome. Se arquivo do primeiro
parâmetro existir, executará o segundo parâmetro. Caso não existir, executará o terceiro
parâmetro.
Também é bom checar se não está executando no modo de compatibilidade (modo antigo).
Para isso, usa-se o comando \ifOcompatibility que é da forma
\ifOcompatibility
<comando 1>
\else
<comando 2>
\fi
A mensagem de erro é emitido por
\eackageErrorí<nome do pacote>Yí<mensagem curta>)í<mensagem longa>).
Se for só a advertência, usa-se o comando \PackageWarningí<nome do pacote>)í<mensagem>).
Para saber se foi carregado a classe de documento compatível, usa-se o comando
\oifclassloadedí) que tem a forma \eifclassloadedí<classe>)í<cmdi>XYí<cmd2>].
Quando <class> for usado, executa o <cmd1> e caso não for a <classe>, executa o <cmd2>.
Com isso, podemos elaborar o cabeçalho do arquivo de estilo. O Exemplo B.1 é uma listagem
do exemplo de arquivos de estilos.
Exemplo B.1: ex-b-estilo.sty
% ex-b-estylo.sty
\eedsTeXFormat(LaTeX2e) % requer LaTeX 2e
% \eedsTeXFormat{LaTeX2e} [2020/10/01] % requer LaTeX 2e 2020-10-01 ou mais
recente
\PprovidesPackageíex-b-estilo[2021/07/14 vO.5 ex-b-estilo style (require
book, amsbook, or report as document class)]
% Para controle de versão
% \ersões anteriores, caso existam em paralelo
% \DeclareReleaseí)í<data>Yí<nome do arquivo com extensão>>
\eclareCurrentReleaseí+12025-08-08) % \ersão atual: Esta é versão de
2025-08-08
\typeoutífex-b-estilo style 0.6 <August/2025>.]>
% Para evitar a tentativa de usar no modo de
% compatibilidade com LaTeX antigo (documentstyle)
\ifecompatibility % modo de compatibilidade com LaTeX antigo?
B.1. Criando pacotes 271
\PackageErroríex-b-estilokí\ot support older compatible mode (documentstyle
)
íUse documentclass instead o{ documentstyle}
\endinput
\else
% OK
vfi
KVl lll llll lo la lo l lolo l lolo l lolo la lolo la lelolelololalolololololalolelolololo
%4 requer book, amsbook, ou report como classe de
% documento (enumeracao do teorema eh vinculado
% ao chapter)
1/A
\oifclassloadedíbooklY% Using book?
1% \ES (OK)
Tieifclassloaded{amsbook}% No, but are using AMS book?
1% \ES (OK)
fieifclassloadedíreportl% No, but are using report?
1% \ES (OK)
T % No! Then can'not apply this package
\PackageErrortex-b-estilolíRequire book, amsbook, or report as
document class)
íUse the required document {class}
%ZVendinput
Y
t
+
Rlhhh
% opcoes
% Aqui, opcoes ativa o if para efetuar configuracoes posteriormente
% \RequirePackage(i{then} % da base/required
\newifWifCexeblôestiloCusedsfont
% se usedsfont for usado como opcao
\eclareOption{usedsfont}í\CexObCestiloCusedsfonttruelf
CexOblestiloCuseds{ontfalse}
%% Fallback (opcoes nao declaradas)
\eclareOption*+t
\PackageWarningíex-b-estiloíUnknown option '\CurrentOption')
D
% Apos declarar todas opcoes, colocar este comando
\ProcessOptionsyrelax
B.1. Criando pacotes 272
llll llll la lolo lal lo l
% Pacotes necessarios
% Da base/required
\RequirePackageTamsthm, amssymb,amsmathy>
% \RequirePackage [brazil] {babel}
% pacotes nao obrigatorios do LaTeX
% \RequirePackage{geometry} %4 carregar sempre
ANIfFileExistsídsfont.sty)% carregar, se existir
%MNRequirePackagefíds{ont} )T%
% testando se tem o pacote instalado e providenciando o
% comando, caso pacote nao exista.
\IfFileExistsíhyperref.sty)%
T{iRequirePackageThyperref}Y/,
TfiPackageWarningíex-b-estilokíhyperref.sty not found. Using draft mode.)%
\providecommandWurl [1] \texttt HH1%
% definicao dos macros para ambiente de teoremas
%4 teoremas, lemas, proposilcícki-oes, etc
\theoremstyleíplainY
\newtheoremítheorem-{Teorema} [chapter]
\newtheorem{axiom} [theorem] fAxiomar
\newtheorem{corollary} [theorem] (CorolN'ario)
\newtheoremílemma+ [theorem] [lema)
\newtheorem{proposition} [theorem] (ProposilcíclN-ao)
\newtheorem{conjecture} [theorem] ({Conjectura}
%4 definilc ci-ao de definilc cy-oes, exemplos, etc.
\theoremstylefíde{inition}
\newtheoremíde{inition} [theorem] (DefinilcíckN-ao)
\theoremstyle{remark}
\newtheorem{remark} [theorem] (ObsercalcíckN-aoL
\newtheorem{note} [theorem] [\ota)
\newtheorem{example} [theorem] {Exemplo}
%
\newtheoremíquestionk [theorem] (Pergunta)
% alterando as penalidades (para corte de linhas em...)
\hyphenpenalty=5000 % hifenizalcíckN-falo
B.1. Criando pacotes 273
\exhyphenpenalty=500 % palavras com hifem
\binoppenalty=3000 % operador binario (+, - , etc)
\relpenalty=2000 % operador relacional ( = \cong \ne,)
\clubpenalty=1000 % ???
\brokenpenalty=1000 % ???
\sloppy % prefere underfull do que overfull
% conjunto numerico (evitando o real, complexo, etc,
\newcommandí \Rset H \mathbbíRJ>
\newcommandí \Cset Y \mathbb1C)y
\newcommandí \Zset H \mathbb{1Z})
\newcommandí\Iset í \mathbb{I1}>
\newcommandí \Qset Y( \mathbb1Q)>
\newcommandí\set í \mathbbíNJ>
% Funcoes em portugues (nome da {uncao deve ser em romano}
\eclareMathOperatorfíysenk+{sen}
\eclareMathOperatorí\arcsentk{arcsen}
\eclareMathOperatorí\senhl{senh}
\eclareMathOperatorí\arcsenh+(arcsenh)
RRl lll lolo o lolololelololo la la lo la lololo la lololo la lo lolo lolo lolo
% Reconfigurando de acordo com a opcao
% Usar dsfont
\ifCexebCestiloCusedsfont”, se usedsfont for usado como opcao
\IfFileExistsídsfont.sty)%
t%
\RequirePackageTds{ont})
\renewcommandí \Rset ) \mathds{RJ}
\renewcommandí \CsetIfNmathds{C}>
\renewcommandí \Zset f \mathds{1Z}>
\renewcommandí \IsetIYfNmathds{I}>
\renewcommandí \Qset Y f imathdsí1QY>
\renewcommandí \setYí\mathds{NJ})
H%
\PackageErroríex-b-estilokídsfont.sty not found.X%
tfInstall dsfont package.)%
)
vfiZ \ifCexeobCestiloCdusedsfont
% fim: ex-b-estilo.sty
Quando o arquivo de estilo usa opções, coloca o que vai fazer quando uma determinada
opção for especificada, com o comando \eclareOptioní<opção>Yí<comando>). Lembre-
se que não é permitido carregar o pacote dentro da declaração de opções, mas poderemos
testar se o pacote existe. Para evitar tais desconfortos e deixar o código mais fácil de ser
B.1. Criando pacotes 274
analisados, costuma colocar a declarações de opções no começo e nele, colocar ativação do
“if” previamente criado. O corpo da opção ficará mais adiante. Para criar “if” novo, utiliza
o \newif seguido de \if<nome> onde <nome> é um nome desejado. O “flag” associado pode
ser ativado ou desativado com o comando \nome>true e W<nome>false respectivamente. O
código
\if<nome>
comando 1
\else
comando 2
\fi
Executará comando 1 se “flag” associado a <nome> estiver ligado e comando 2 caso con-
trário. Quando não tiver o comando 2, \else pode ser omitido como em
\if<nome>
comando 1
vfi
Um dos problemas é que o “if” criado desta forma não funciona devidamente quando aninhado
(colocar um “if” dentro do outro). Isto pode ser contornado pelo pacote ifthen (da base)
para manipular condições de forma mais confortável do que criar “if”.
Também podemos passar opções para classe que será carregado posteriormente, pelo
comando \PassOptionsToClass ou para o pacote a ser carregado posteriormente, com o
comando \PassOptionsToPackage.
No caso de querer que alguma opção seja aplicada como padrão, poderá usar o comando
\ExecuteOptions.
Quando tem a declaração de opções, deve colocar \\ProcessOptions após terminar todos
\eclareOption e \ExecuteOptions para que opções sejam processados.
O Exemplo B.2 é um exemplo do uso do pacote do Exemplo B.1.
Exemplo B.2: ex-b-estilo.tex
\documentclass [a4paper,12pt] fbookY
\usepackage [T1] ({ontenc} % codificação da fonte em 8-bits
\usepackage [brazil]{babell} % em portugues brasileiro
\usepackagefex-b-estilol % arquivo de estilo definido pelo usuário.
% \usepackage [useds{ont} fex-b-estilol) % com opcao (se usar este, conjuntos
numéricos {icam como dsfont, caso dsfont estiver instalado}
\beginf{document}
\chapter{Teste}
\beginfíde{inition}\labelídef:triangulo:retangulo)
B.2. Criando classes 275
Um triângulo é dito retângulo se tiver um ângulo reto.
\endfídefinitiony
\begin{theorem} [Pitágoras] V.abelíthm:pitagoras)
Dado um triângulo retângulo $ABC$ com ângulo reto em $A$, temos que
\beginfequationkWlabelíeqg:pitagoras)
a 2=b"2+cO2
\end{equation}
\endítheoremy
\begin{proof})
Demonstração aqui.
\end{proof}y
Usando a definição do $\sen$ e $cos$ juntamente com o Teorema-\refíthm:
pitagoras), temos que
\beginf{proposition}
N
\forall t \in \Rset, \senº2 t + \cos”2t=1
\i
\endípropositionY
\end{document}
Capítulo 1
Teste
Definição 1.1. Um triângulo é dito retângulo se tiver um ângulo reto.
Teorema 1.2 (Pitágoras). Dado um triângulo retângulo ABC com ângulo reto em A,
temos que
a? =b?2+c? (1.1)
Demonstração. Demonstração aqui.
Usando a definição do sen e cos juntamente com o Teorema 1.2, temos que
Proposição 1.3.
\t E R,senºt + cosº t =1
B.2. Criando classes 276
B.2 Criando classes
Em geral, a classe é criado de mesma forma que um arquivo de estilo. Em muitos casos,
a classe criada consiste na reconfiguração da classe existente. Quando pretende aplicar o
ajuste sobre diversas classes base, é conselhável criar um arquivo de estilo. Quando o ajuste
é aplicado numa classe específica, é aconselhável criar uma classe sobre tal classe base.
Os comandos \ProvidesPackaget<nome do pacote>) [<mensagem>] será substituído por
\ProvidesClassí<nome da classe>) [<mensagem>].
Quando tem o parâmetro opcional, a “<mensagem>"” deve iniciar com data no formato
ano-mes-dia (ou ano/mes/dia onde ano é de 4 digitos.
A classe base é lido pelo comando \LoadClass{*} após declaração das opções, passando
as opções não processadas para classe base. Isto pode ser feito com o código do tipo
% Demais opções
\eclareOption*(T%
\PassOptionsToClassí\CurrentOptionkíbookY% repassar para book
)
\ProcessOptionsyrelax
% carrega a classe base
\oadClassíbooky
O \PassOptionsToClass é comando para agendar os parâmetros para a classe a ser lido
posteriormente. \ote que existe o comando \PassOptionsToPackage para pacotes, com
mesma finalidade.
O Exemplo B.3 é uma listagem do exemplo de arquivos de classe.
Exemplo B.3: ex-b-classe.cls
\eedsTeXFormat (LaTeX2e)
% \eedsTeXFormat {LaTeX2e} [2020/10/01] % requer LaTeX 2e 2020-10-01 ou mais
recente
\ProvidesClassíex-b-classe)[2021/07/14 vO.5 ex-b-classe class file (
implemented over book class)]
\typeoutíex-b-classe 0.5 <July/2021>.)
RVlh llll lalh lololololololololololololelololololololololololololololololololo
% Para evitar a tentativa de usar no modo de
% compatibilidade com LaTeX antigo (documentstyle)
\ifecompatibility %4 modo de compatibilidade com LaTeX antigo?
\olassErrorífex-b-classe-í\ot support older compatible mode (documentstyle)])
íUse documentclass instead o{ documentstyle}
\endinput
B.2. Criando classes 277
\else
% OK
\fi
RKh
% opções
TEAA
% Aqui, algumas opçoes ativa o if para efetuar configurações posteriormente
\RequirePackageti{then} % da base/required
\RequirePackage [english,brazilian] (babel) % da base/required (ultima é
idioma principal)
\newboolean{exObOclasseCusedsfont})
% se usedsfont for usado como opcao
\eclareOptionfusedsfontIílsetbooleanfexObOclasseOusedsfont{truel}H
setboolean{exebOclasseOusedsfont}+í{alse})
\eclareOptionfenglishYf % idioma principal como english
\nainClanguagetenglish)
% \selectlanguageftenglishy
D”
\eclareOptioníbrazilian+t % idioma principal como brazilian
\nainClanguagetbrazilian)
% \selectlanguagef{brazilian}
F
\eclareOptionfíbrazil+t % idioma principal como brazilian
\nainClanguagetbrazilian)
% \selectlanguage{brazilian}
D7
%% Fallback (opcoes nao declaradas)
\eclareOption*f
\PassOptionsToClassfí\CurrentOptionk)tbookY%
H
% Após declarar todas opções, colocar este comando
\ProcessOptionsyrelax
% lendo a classe base
\LoadClassíbook
RRl lal la lo la lo lelo la la la lo la lo la lo la lo la lo la lo lalo lolo lal
% Pacotes necessários (além de i{then}
% Da base/required
\RequirePackage(lamsthm, amssymb,amsmath>
B.2. Criando classes 278
% \RequirePackage [brazil] {babel}
% pacotes nao obrigatorios do LaTeX
% \RequirePackage{geometry} % carregar sempre
ANIfFileExistsídsfont.styl% carregar, se existir
ZNRequirePackageíds{ont}Y(Y%
% testando se tem o pacote instalado e providenciando o
% comando, caso pacote nao exista.
\IfFileExistsíhyperref.styl%
TNRequirePackageThyperref)Y%
fiClassWarningíex-b-estilokíhyperref.sty not found. Using draft mode.)%
\providecommandWurl [1] \texttt(tHtH1XX%
H
% Ambiente tipo teorema com Multi idiomas
% (ingles, portugues brasileiro)
% \addto do pacote babel adiciona comandos no final do macro existente.
\addtoYextrasenglisht
\engnames
P
\addtolextrasbraziliant
\brnames
F
\addtoVYextrasbrazilfí
\\brnames
T
\newcommandVYengnamesí % english names
\defyaxiomnameíAxiomY
\defWtheoremnameí{Theorem}
\defWcorollaryname{Corollary}
\def lemmaname{Lemma}
\def \wpropositionname{Proposition}
\de{ \conjecturenametConjecture}
\def definitionnameíDe{inition}
\defWnotenameíNote)
\defexamplenametExampley
\def questionname{Question}
\def remarknameí(Remark]>
\def \wproofnameíProofy
% %AAAh data abreviada: mes/dia/ano
% \defWtodayabreví%,
