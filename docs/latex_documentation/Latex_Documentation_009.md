HHNdefWlogoíUFSCar >
U”
\nmakeatother
que checará se o pacote graphicx foi carregado através do comando \eifpackageloaded
e caso positivo, define o comando \logo para inserir imagem de logotipo. Caso não for
carregado, define o comando para apenas inserir o texto. Checar pacotes carregados para
decidir o que fazer é uma técnica utilizada pelos desenvolvedores de pacotes.
Dependendo da necessidade, os desenvolvedores podem inserir código em enddocument
({inal do documento} e shipout (gerar página) também, para ajustar parâmetros, se necessário.
Para acessar o parâmetro do comando ou ambiente, use \\\ddToHookWithArguments em
vez de \AddToHook.
Para mais detalhes, veja o [Mit25].
14.5 Usando \NewDocumentCommand e \NewDocu-
mentEnvironment
Para melhor controle e uso dos parâmetros, foram desenvolvidos o \ewDocumentCommandí+>
para substituir o \newcommandí+ e \\\ewDocumentEnvironmentí) para substituir o
\newenvironmentí). Com o uso destes comandos, poderá criar comandos e ambientes efe-
tuando especificação mais precisa dos seus parâmetros. A versão de TEX anterior ao ano de
2022, pode precisar usar o pacote xparse para este recurso.
O novo comando podem ser definidos pelo
\ewDocumentCommandí<comando>Yí<especificação>Yí<corpo>)
Também existem \RenewDcoumentCommandfí] (recria, caso existir — erro, se não exis-
tir), \ProvideDocumentCommand (cria somente quando não existir — ignora, se existir),
\eclareDocumentCommand (cria independente de existir ou não),
A “<especificação>” é uma lista que especifica como será cada parâmetro que podem
ser
m Parâmetro obrigatório
o Parâmetro opcional
Of<valor>*) Parametro opcional. Se omitido, será assumido como *<valor>'
r<> Paramétro obrigatório delimitado pelo '<' e "> em vez de chaves. Poderá usar outro
pares de caracteres em vez de "< e '>* como em r()
R<>f<valor>) Paramétro obrigatório similar a r<>, mas assume o valor '<valor>' caso
omitido (após indicar erro devidamente).
d<> Paramétro opcional delimitado pelo "< e > em vez de chaves. Poderá usar outro
pares de caracteres em vez de "< e "> como em d()
D<>Tf<valor>> Paramétro opcional similar a d<>, mas assume o valor '<valor>' caso for
omitido.
s Para verificar a existência de "*”. \ormalmente será o primeiro parâmetro quando presente.
É usado para implementar a versão com e sem **º.
v Parâmetro tipo verbatim, delimitado pelo primeiro caractere do parâmetro. Usar com
cuidado.
Ainda existem “t”, “e” e “E” que não será explicado neste texto.
Para testar os  parâmetros que foram  passados, tem os  comandos
\IfValueTí<par>Yí<cmd>) (executa o comando <cmd> se o parâmetro <par> for pas-
sado), \IfValueFí<par>Yí<cmd>) (executa o comando W<cmd> se o parâmetro <par> não
{or passado} e \IfValueTFí<par>Yí<cmdi>Y(T<cmd2>) (executa o comando <cmdi> se for
passado o parâmetro <par> e o comando <cmd2>, se o parâmetro não {or passado}. Para
facilitar, existe o comando para checar se os parâmetro não foram passados, que são
\IfNoValueT, \IfNoValueF e \IfNoValueTF que funciona de forma similar. Mesmo que o
parâmetro for passado, pode ser parâmetro vazio ou formado somente pelos espaços. Para
testar, usa se os comandos \IfBlankT, \IfBlankF e \IfBlankTF. \ote que o espaço do tipo
\space não é considerado “blank”.
exX*”»
Para verificar a existência de (parâmtro do tipo “s”), existe o comando \IfBooleanT,
\IfBooleanF e \IfBooleanTF. \eja o Exemplo 14.5.
exl4-newdocumentcommand.tex
\documentclass [12pt,oneside,a4paper] {article}
& Comando sem parâmetro
\ewDocument ConmandNconjuntoRíYí\mathbb{RY}
h mé parâmetro obrigatório
\ewDocumentCommandí V.ormulaBhaskara}{mmm}
TVlensurematht
\frací-t2pmNsqrtít27 2-4H1H43))(241)
-)
%5 Otlvalor padrãor-
% o -> sem valor padrão (poderá testar se foi passado o valor com À
IfNoValueTFíparametrotTse não foi passadotíse foi passador
\ewDocumentCommandí\derivadaParcial-í OffYox
n
\ensuremathfVWfrací\partial H1)fNWpartialNIfValueT{t2}1 (t2))
+
\verbt+\ensuremathf)+ coloca entre *“N$'' caso ainda não estiver, para tornar
fórmula mesmo no modo texto.
” star, nostar version
h s is used to detect star
& from https://www. texdev.net/2010/05/23/from-newcommand-to-
newdocumentcommand/
\ewDocumentCommand \ithStarArgísmY(%
\IfBooleanTFH1 % se tem ““x''
tComando versão *, com parâmetro t2)
tComando versão sem *, com parâmetro t2X/%
D”
/& Comando que usa o parâmetro, já mo próprio parâmetro
\eclareDocumentCommandWmeuTituloí(O{t2} +my
tTíulo curto: H1; Título: t2)
\begin{document}
Testnado os comandos
$\conjuntoR$
\formulaBhaskaraí{a}{bXtc}
\derivadaParcial % sem argumentos
\derivadaParcial[g] [2,3] % com argumentos
\ithStarArg{Teste}
\ithStarArg *íTeste 2)
\neuTituloíTeste do comando)
\neuTitulo [Teste] (Teste do comando)
\endí{document}
\ensuremathf* coloca entre “$” caso ainda não estiver, para tornar fórmula mesmo no
modo texto.
Testnado os comandos
R
—b+vVb?—4ac
9f
&a
D(2,3)
Comando versão sem *, com parâmetro Teste
Comando versão *, com parâmetro Teste 2
Tíulo curto: Teste do comando; Título: Teste do comando
Tíulo curto: Teste; Título: Teste do comando
Para refinar a especificação dos parâmetros, existem os modificadores que especificam
algumas alterações no argumento. Ele é colocado antes do especificador de parâmetro.
+ O argumento não pode conter parâgrafos.
! Não pode ter espaço antes do argumento.
= Parâmetro é uma lista de elementos do tipo 'chave=valor”. =(chave) coloca o parâmetro
como sendo o valor da chave chave.
Por exemplo,
\\ewDocumentCommandYderivadaParcial(+1+01f) +o)
impede que os seus parâmetros contenham parâgrafos.
Para usar o parâmetro como lista do tipo chave=valor, deverá implementar o processa-
dor de chaves. Inicialmente, especifica o que fazer para cada chave encontrada através do
\eclareKeys e depois chama o processador \etKeys dentro do comando.
O primeiro parâmetro opcional do \eclareKeys é “família” que deve ser único e deve co-
incidir com a “família” especificado no \setKeys. Para configurar o valor inicial (.initial:n)
e/ou valor padrão quando aparece somente o nome da chave no parâmetro (.default:n),
deverá colocar o \eclarekeyst] entre \ExplSyntaxOn e VEXxplSyntaxOff, caso for no pre-
amble.
\eja o Exemplo 14.5
exl4-keyvalparameter.tex
\documentclass [12pt,oneside,a4paper] {article}
\nakeatletter
\newiflifOtemSinalizadore
\etemSinalizadorCfalse % valor inicial
4 O que fazer para cada chave
AVErplSyntazcOn
\eclareKeys [meuComando] €
% valor padrão, para caso não for fornecido
/& nome .initial:n = 1), % antes da chamada de SetKeyst) (vazio já é padrão)
/Anome .default:n = 1), /& se tiver somente nome da chave, assume este valor
% parametro .default:n = (),
/ armazenar o valor no comando (caso encontrar)
nome .store = \meuComandoCnome,
parametro .store = \meuComandoCparametro,
/ coaso encontrar, liga (não altera, caso contrário)
sinalizador .if = OtemSinalizadore,
mensagem .code=(Mensagem: ""H1'') Z erecutar o código, caso encontrar a
chave. 'H1" é o valor associado a chave
D”
AVExplSyntacOff
/& Comando que usa chave=valor declarado anteriormente
\ewDocument ConnandWmeuComandoChaveValorím o
t % valor padrão para casos omissos
AVdef meuComandoOnometr
/Alde{imeuComandoCOparametrot}
/AV)0temSinalizadoreOfalse
% \begingroup/lendgroup protege o bloco para restaurar valor alterado
/h senão, na proxima chamada, terá valor da chamada anterior, caso não tiver
chave
\begingroup % protege
\IfValueT{t2}(Z
\SetKeys [meuComando] (%2)
t
% Excecutando, usando os valores
t1: Nome: \mneuComandoCnome, paramêtro: \meuComandoCparametro; sinalizador
: (\ifetemSinalizadore LigadolYelse DesligadoVW{i}
\endgroup
d”
\nakeatother
\beginf{document}+
Testnado o comando
\neuComandoChaveValorítestel
\neuComandoChaveValortíteste 2) [nome=(Testandol], sinalizador, mensagem=(
Somente um testeY]
\neuComandoChaveValoríteste 3Y%4[nome=1Testando), parametro=tTestando)]
\end{document}
Testnado o comando
teste: Nome: , paramêtro: ; sinalizador: Desligado
Mensagem: “Somente um teste” teste2: Nome: Testando, paramêtro: ; sinalizador:
Ligado
teste 3: Nome: , paramêtro: ; sinalizador: Desligado
O \begingroup/\endgroup no corpo do comando é para proteger os valores do comando,
pois não há mecanismo de resetar os valores. Os valores alterados após \begingroup pelo
comando \SetKeyst+ volta ao valor original após \endgroup.
Para copiar comandos, costuma usar o \let, mas ele nem sempre funciona quando o co-
mando tiver parâmetros. Para resolver este problema, no conjunto de \ewDocumentCommand,
foi implementado os copiadores. \ewCommandCopyt<dest>Yí<orig>] (copiar <orig> para
o destino <dest>, caso destino ainda não existir), \RenewCommandCopy (copiar se destino
existir) e \DeclareCommandCopy (copiar independente do destino existir).
Os parâmetros podem ser processados antes de serem usados no corpo do comando,
pelo comando denominado de processador de parâmetros. O Processador é acrescen-
tado antes do parâmetro correspondente com >(í<processador>). Neste texto, será visto
dois dos processadores pré-definidos que são \SplitArgumentí<num>Yí<separador>) e
\SplitListí<separador>)
O processador Sp1itArgumentí<num>Yí<separador>) toma <num>+1 primeiros elementos
da “lista” separada pelo <separador> e converte em sequencia de argumentos. Caso, tenha
menos do que <num>+1 elementos na lista, será completada pelo "-\oValue-”. Caso tiver mais,
dará erro.
O converte o parâmetro “lista” numa lista real. Para processar a lista, o comando
\ProcessList{tli}í<comando>) pode ser usado, onde <comando> é o comando de um argu-
mento.
\eja o Exemplo 14.5.
exl4-parameter-processor.tex
\documentclass [12pt,oneside,a4paper] {article}
%4 Exemlo de processar lista em CSV
\ewDocumentCommandVWimprimirItem{m}(O item é 'H1'\par)
%& \{SplitListt} converte CSV em lista
%& \ProcessList aplica a função a cada elemento da lista
\ewDocumentCommandVWimprimirLista (>ANSplitListí;)) my
ftLista:\par \ProcessList{ti}í\limprimirItem))
%4 Converter lista em parâmetro
\ewDocumentCommandWimprimirTresParametrosímmmY(Os 3 parâmetros são: 'H1';
'H2'; 'H3'\pary)
\ewDocumentCommandVimprimirListaComoArgumento f>fNSplitArgumentí2H1,)) rO)
hnum = numargs-1 = 2 pora 3 argumentos
% rO especifica que vai usar () em vez de chaves
{\imprimirTresParametrostt1} % não colocar chaves em 'k1'
\begin{document}
\imprimirListaítabc;def;123;456)
& No seguinte comando, o delimitador do parametro foi definido como sendo
parenteses em vez de chaves.
\imprimirListaComoArgumento(123,abc,def) % correto
\imprimirListaComoArgumento(1,2) Zeste é aceito
AlimprimirListaComoArgumento(a,b,c,d,e) % este, dará erro por ter elementos
demais
\endí{document}
Lista:
O item é 'abc
O item é 'def'
O item é *123'
O item é *456'
Os 3 parâmetros são: *123'; 'abc'; 'def'
Os 3 parâmetros são: *1º; *2'; -\oValue-'
,
Caso tiver mais de um processador de parâmetro indicado, será aplicado da direita para a
esquerda.
\ote que o processador deve ser comando com um argumento. Se for de mais de um
argumento, deverá ter os parâmetros preenchidos, exceto o último.
Para os ambientes, usa-se o \ewDocumentEnvironment, \enewDocumentEnvironment,
\ProvideDocumentEnvironment e \eclareDocumentEnvironment cuja especificação dos pa-
râmetros é mesmo que o caso dos comandos. No entanto, ambientes permite uma especificação
adicional 'b' que é o corpo do ambiente. Com isso, poderá usar o corpo do ambiente várias
vezes, ou passar para o comando ou outro ambiente, sem complicações. \eja o Exemplo 14.5.
exl4-documentenvironment.tex
\documentclass [12pt,oneside,a4paper] {article}
\ewDocumentEnvironment{saidaDupla} {OTVlitshape} +b)
Ttfinoindent fboxfNparboxt1O. 99 textwidth)(H2)HNpartiH2) 1)
\obegin{document}
\begin{saidaDupla} [litshape]
Bom dia!
\endísaidaDuplal
\endí{document}
Bom dia!
Bom dia!
Mais sobre este assunto, veja o [LaT25].
15. Usando Pacotes Fora do base e required 123
Capítulo 15
Usando Pacotes Fora do base e
required
Até agora, só estudamos os pacotes disponíveis em qualquer distribuição TEX, usando somente
os pacotes do conjunto denominado de base e required. No entanto, maioria das distribu-
ições LaTeX instala uma grande quantidade de pacotes adicionais para incrementar a sua
funcionalidade. Assim, neste capítulo, vamos aventurar em alguns destes pacotes adicionais
para facilitar o nosso trabalho.
15.1. Ajustando a configuração das páginas e similares
Para ajustar as margens, tamanho de papeis, espaçamento entre cabeçalho e texto, etc, usamos
o pacote geometry. AÀs configurações podem ser feitas, passando no parâmetro opcional do
pacote, a lista dos itens na forma chave=valor, separado pela virgula. Também pode usar o
comando \geometry após carregar o pacote.
Para ajustar margem superior (tmargin), margem inferior (bnargin), margem esquerda
(Imargin, será de dentro se for frente/verso), margem direita (rmargin, será de fora se for
frente/verso), basta colocar algo como
\usepackage [tmargin=2cm,bmargin=2cm,lmargin=2cm,rmargin=2cm] ({geometry}
ou
\usepackageTgeometryY
\geometry(ítmargin=2cm,bmargin=2cm,lmargin=2cm,rmargin=2cm)
no preamble do documento.
Para ajuste de espaçamento entre linhas, usamos o pacote setspace que tem os coman-
dos \singlespacing (espaçamento simples), \onehalfspacing (espaçamento um e meio)
e \doublespacing (espaçamento duplo), além do ambiente spacing que permite qualquer
espaçamento dentro dele.
Para que o documento fique em espaçamento um e meio, coloque
\usepackageTsetspace
\onehalfspacing
no preamble do documento.
Usuário da classe memoir devem colocar \isemulatePackage{setspace} antes de carre-
gar o setspace.
Para desabilitar a hifenização em todo documento ou ativar hifenização na fonte mono
espaçado (\tt{amily}, poderá usar o pacote hyphenat.
\usepackage [none] {hypenat})
no preamble desabilita hifenização em todo documento. Se não quer usar o pacote e quer
desativar a hifenização, coloque
\hyphenpenalty=10000
\exhyphenpenalty=10000
no preamble do documento.
Para melhorar o ajuste de espaços, poderemos usar o pacote microtype que usa o recurso
de micro tipografia. Um desses ajustes é reduzir ou ampliar levemente o tamanho da fonte
para melhorar o espaçamento. Por exemplo, podemos colocar
\usepackage [stretch=10] {microtype}
no preamble.
Cabeçalho no estilo de página headings coloca o título do capítulo e seção no cabeçalho
em maiúsculo. Para tanto, usa-se o comando \MakeUppercase que não funciona para letras
acentuadas diretamente (funciona para acentuação no modo TEX). Além disso, ele tenta
converter inclusive as fórmulas, o que pode causar problemas. O pacote textcase permite
sobrescrever o \akeUppercase para evitar tais problemas, além de mais alguns recursos
adicionais. Coloque
\usepackage [overload] {textcase}
no preamble.
\ormalmente, a referência bibliográfica e índice remissivo não costumam ficar no sumário.
Para que eles constem no sumário, use o pacote tocbibind. Usando a opção adicional, pode
impedir que o sumário, lista de figuras e de tabelas fiquem fora do sumário.
\usepackage [nottoc,notlof,notlot]ítocbibindY
no preamble efetua esta tarefa.
\ote que no LaTeX, o texto é justificado por padrão, mas não existe comando para justificar
um trecho dentro do outro alinhamento. Uma saída é usar o minipage, mas minipage não
permite quebrar entre páginas. Para resolver este problema, existe o pacote ragged2e que
providencia o ambiente justify (e comando \justi{y} que pode ser usado como outros
comandos de alinhamento de texto no parágrafo.
15.2 Estilo europeu
Em Alguns países da Europa, um parágrafo é separado pela outra com o espaçamento maior
entre linhas em vez de indentação. Remover a indentação é feito, ajustando o valor de
\parindent para zero, mas ajustar o espaçamento antes do parágrafo por \parskip e acertar
alguns detalhes requer conhecimento extra. Para facilitar, existe o pacote parskip que, ao
ser usado, ajustam de forma apropriada. Se não quer usar o pacote, coloque
\setlength{\parindent}íOptY
\setlengthfWparskipkílex plus O.5ex minus O.2ex)
no preamble, mas isto não ajustará tudo que o pacote faz.
Para produzir o estilo literário francês na qual a primeira letra do parágrafo ocupa mais de
uma linha, tem o pacote lettrine. O uso comum nos livros de literatura é usar o lettrine
no primeiro parágrafo do capítulo e manter o restante como normal. \eja o Exemplo 15.1 na
qual é assumido que tem o \usepackage{lettrinel} no preamble do documento.
Exemplo 15.1: exl5-lettrine.tex
\chapteríUm Cap{tulo}
\lettrinefEl{xistel} um pacote chamado \texttt{letrinel} que oferece o estilo
literário francês (estilo b{blico} na qual a primeira letra do parágrafo
ocupa varias linhas.
Alguns livros literários usa este estilo somente para o parágrafo do
primeiro capítulo, mantendo outros parágrafos como sendo normal. O
primeiro parâmetro é a letra (primeira letra) que ocupará várias linhas,
e o segundo parâmetro é a continuação dele até finalizar a palavra, que
será escrito em maiúsculo. O comando ainda aceita parâmetros opcionais
para ajustar quantas linhas vai ocupar, etc.
Capítulo 1
Um Capítulo
XISTE um pacote chamado letrine que oferece o estilo literário francês (estilo b{blico}
E na qual a primeira letra do parágrafo ocupa varias linhas. Alguns livros literários
usa este estilo somente para o parágrafo do primeiro capítulo, mantendo outros parágrafos
como sendo normal. O primeiro parâmetro é a letra (primeira letra) que ocupará várias
linhas, e o segundo parâmetro é a continuação dele até finalizar a palavra, que será escrito
em maiúsculo. O comando ainda aceita parâmetros opcionais para ajustar quantas linhas
vai ocupar, etc.
\ote que, em muitos casos do usos de lettrine, costuma usar a fonte enfeitada (fonte
para iniciais) na primeira letra como no exemplo ?? que supõe o uso do pacote yfonts com
codificação T1, colocando o código
\usepackage [T1] {fontenc})
\usepackagety{onts}
no preamble.
Exemplo 15.2: exl5-lettrine-b.tex
\chapterfUm Cap{tulo}
\lettrine[lines=3] (\initfamilyNsmall EX{xistel} um pacote chamado \textttfí
letrine) que oferece o estilo literário francês (estilo b{blico} na qual
a primeira letra do parágrafo ocupa varias linhas.
Alguns livros literários usa este estilo somente para o parágrafo do
primeiro capítulo, mantendo outros parágrafos como sendo normal. O
primeiro parâmetro é a letra (primeira letra) que ocupará várias linhas,
e o segundo parâmetro é a continuação dele até finalizar a palavra, que
será escrito em maiúsculo. O comando ainda aceita parâmetros opcionais
para ajustar quantas linhas vai ocupar, etc.
Capítulo 1
Um Capítulo
UG
ª X XxISTE um pacote chamado letrine que oferece o estilo literário francês (estilo
GQ; b{blico} na qual a primeira letra do parágrafo ocupa varias linhas. Alguns livros
id literários usa este estilo somente para o parágrafo do primeiro capítulo, mantendo
outros parágrafos como sendo normal. O primeiro parâmetro é a letra (primeira letra) que
ocupará várias linhas, e o segundo parâmetro é a continuação dele até finalizar a palavra,
que será escrito em maiúsculo. O comando ainda aceita parâmetros opcionais para ajustar
quantas linhas vai ocupar, etc.
Para mais fontes para iniciais, veja o https://tug.org/FontCatalogue/.
15.3 Ajustando o cabeçalho, títulos de capítulos e de
figuras
Ajustar o cabeçalho diretamente não é simples. Assim, costumamos usar o pacote fancyhdr
que permite personalizar o cabeçalho das páginas. \eja o Exemplo 15.3 usado para produzir
estilo de cabeçalho deste documento.
Exemplo 15.3: exl5-fancyhdr.tex
\documentclass [12pt,a4paper] {article}
\usepackage [T1] {fontenc}
\usepackage [brazil] {babel}
\usepackage{calc} % para calculo de medidas
\usepackageít{ancyhdr} % personalizar o cabeçalho
CPAALAL inicio da redefinicao do cabecalho %%%/44%
% Ajustando o chaptermark e sectionmark
\nakeatletter
%iaddtolpsCfancy (%
\renewcommandfíTVchaptermarkY[1] 1%
\markbothfVifemainmatterNthechapter. \\{i 1}%
TVNifemainmatterNthechapter. \fi $1))
\renewcommandfí \sectionmark+[11]1%
\narkrightTVWifemainmatterNthesection. \fi $1))
%-
\nmakeatother
\setlengthí\headheightIYT15pt) % enlarge heade height
% linha horizontal entre cabecalho e corpo do documento
\renewcommandTVWheadrulewidthYtO.5pt)
% sem linha horizontal entre corpo de texo e rodape
\renewcommandí \\{ootrulewidth}{Opt}>
% redefinindo o estilo da pagina "fancy"
% Redefinido o estilo fancy
\fancypagestyleífancyY(%
\fancyhft % limpa o cabecalho
% redefine o cabcalho. \nouppercase foi usado para eliminar conversao para
maiusculo do sumario/bibliografia
\fancyhead[LE,RO] {Nbfseriesthepage}
\fancyhead[LO] \bfseries nouppercaselrightmarky
\fancyhead [RE] (\bfseriesWnouppercaseWleftmark>
) % NVfancypagestyleífancyY(%
% redefine o "plain" (usado na primeira pagina do capitulo).
\fancypagestyle{plain} t%
\fancyheadí) % get rid of headers
\fancyhead[LE,RO] fNbfseriesWthepagel % colocar enumeracao
% \renewcommandfVWheadrulewidthY(O.5pt) % com linha horizontal
D7
% Ajustando a primeira página do capitulo
\naKkeatletter
%\letipseplainCoriginal psêplain %4 copia do original, se necessário
\\AddToHookícmd/psefancy/afterMetWpsôplainlpseê{ancyplain}
\AddToHookícmd/psCempty/after i \letlpsCplain|psCempty]
\nakeatother
LPAALAA fim da redefinicao do cabecalho %4%4%%%/
% iniciar com estilo empty
\pagestyle{empty})
\begin{document}
\pagestyleí{ancy} % inicia o cabeçalho personalizado
\end{document}
\ote que o comando \\fancypagestyle permite definir/redefinir estilo de páginas.
O comando \AddToHookí\T] foi usado para adicionar o código no comando já existente.
No LaTeX, \psôestilo é o comando correspondente ao estilo de páginas “estilo”.
Para documento em um lado, poderá usar a configuração um pouco mais simples. O
Exemplo ?? efetua configuração similar ao Exemplo 15.3 para caso de impressão em apenas
um lado, mas coloca o nome do capítulo no cabeçalho da página, em vez da seção.
Exemplo 15.4: exl15-fancyhdr-oneside.tex
% ajustando o \chaptermarkí) e desabilitando o NVsectionmarkí>
\nakeatletter
\renewcommandí \chaptermark+[1]1% suppress string 'Chapter'
\narkboth
TlifomainmatterNWthechapter. \\{i H1}(\ifemainmatterVthechapter. \\{i H1})
\renewcommandfWsectionmark*[1] 1X%
% \markrightilifemainmatterNthesection. \\{i HH1}>
\nakeatother
% aumenta o espaco do cabecalho superior
\setlength{\headheight}{T15pt}
% linha horizontal entre cabecalho e corpo do documento
\renewcommandí\headrulewidthYTO.5pt)
% sem linha horizontal entre corpo de texo e rodape
\renewcommandí\footrulewidthfOptx
% Redefinido o estilo fancy
\fancypagestyleífancyYt%
\fancyhftY% limpando as configuracoes
% redefinindo o cabecalho superior
% \nouppercase foi usado para eliminar conversao
% para maiusculo do sumario/bibliografia
\fancyhead[R] {Wbfseries thepage}
\fancyhead[L] {NbfseriesWnouppercaseleftmark}
) %4 fim do \fancypagestyleí{ancy}
% estilo plain (usado na primeira pagina do captulo).
\fancypagestyleífancyplain+í
% limpando as configuracoes
\fancyhft>
\renewcommandfWheadrulewidthYTtO.5pt) % com linha horizontal
\fancyhead[R] (\bfseriesWthepagel% colocar enumeracao
) % fim do \fancypagestylelfancyplain+t
% mais ajustes
\nakeatletter
% MetiWpsêplainêoriginal psêplain, cópias do original, se necessário
vWAddToHookícmd/psCfancy/a{ter}
TiMletipseplainlpsC{ancyplain}
\AddToHookícmd/psCempty/a{ter}
TWletWpsOplainpsCempty|
\nakeatother
Para configurar o formato de título do capítulo e seções, usamos o pacote titlesec. \ote
