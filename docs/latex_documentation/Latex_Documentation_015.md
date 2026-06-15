O tema (modelo) de slides é escolhido pelo comando \usetheme. Tema que vem como
padrão são: AnnArbor, Antibes, Bergen, Berkeley, Berlin, Copenhagen, Darmstadt,
Dresden, Frankfurt, Goettingen, Hannover, Ilmenau, JuanLesPins, Luebeck,
Madrid, Malmoe, Marburg, Montpellier, PaloAlto, Pittsburgh, Rochester,
Singapore, Szeged, \arsaw, boxes, default e CambridgeUS.
Para cada tema, ainda podemos escolher o tema de cores, ou combinação de cores
a serem usados, escolhidos pelo comando \usecolortheme. Tema de cores padrão que
vem são: default, albatross, beaver, beetle, crane, dolphin, dove, fly, lily,
orchid, rose, seagull, seahorse, whale e wolverine.
Para ver como ficará a combinação do tema e tema de cores, poderá consultar o https:
//hartwork.org/beamer-theme-matrix/.
É pouco usado, mas ainda podemos alterar as combinações das fontes com o co-
mando \usefonttheme. Tema de fontes padrão são: default, serif, professionalfonts,
structurebold, structureitalicserif, structuresmallcapsserif. Muitas vezes, usa-
se o comando \\setbeamerfont para configurar fontes de seus elementos em vez de escolher
um tema para fontes (combinação de {ontes}.
A classe beamer carrega o pacote hyperref por padrão. Então podemos configurar alguns
aspectos sobre informações do PDF com o \hypersetup, mas isto não é obrigatório.
Para criar slide de títulos ou quando estiver usando tema que usa títulos, autores, etc,
precisará informar o titulo, autor, instituição e data, respectivamente pelos comandos \title,
\author, \institute e \date. Quando tiver mais de um autor, separe com \and. O comando
\inst dentro do \author e \institute faz a ligação de autor com o instituto correspondente.
Os elementos do slide pode ser alterado pelo comando \setbeamertemplate. Se desejar
criar degrade no fundo do slide, costuma usar o recurso do pacote tikz. \ote que xcolor
é carregado pelo beamer por padrão. O comando \setbeamertemplate também pode ser
usado para desativar os botões de navegação.
Os comandos \maketitle e \tableofcontents funcionam normalmente. \ote que o
sumário é construído a partir de section e não pelo frame. Assim, para ter o sumário,
deverá colocar \ysection entre os frame's no local desejado.
Cada slide (tela) é criado pelo ambiente frame ou comando \\frame. O ambiente frame
aceita o comando \frametitle para colocar títulos.
O comando \note serve para inserir notas adicionais que não são colocados no s1lide, mas
podem ser gerados e impressos com a opção notes ou notesonly na opção da classe, para
auxiliar na apresentação.
O beamer também permite gerar pdf para aplicativos de apresentação “dual screen” (tela
dupla), exibindo o slide no projetor e notas na tela do notebook.
Para tanto, coloque o comando
\setbeameroptioníshow notes on second screen=rightl
no começo do documento para que a nota seja colocada a direita do slide no PDF. Este
pdf pode ser aberto no aplicativo como o pympress para a exibição correta.
As notas adicionadas fora do frame será assumido que do frame anterior.
O Exemplo 17.2 ilustra um slide e uma das telas do slide gerado pelo código listado. Nele,
foi usado o pacote lipsum para preencher alguns slides.
Exemplo 17.2: exl7-slides.tex
\documentclass [12pt] (beamer) % para apresentação.
% para usar com o visualizador de pdf de tela dupla, para apresentaçãocomo o
pympress (https://github.com/Cimbali/pympress) de código aberto e
multiplataforma.
% posiçao do conteúdo (notas) da segunda tela podem ser: left, right (padrão
), top, bottom
% Descomente para dual screen mode com pympress
%%vsetbeameroptioníshow notes on second screen=right)
\usepackage [T1] ({ontenc} % codificação da fonte em 8-bits
% \usepackage [ut{8} {inputenck} % acentuação direta (padrão)
\usepackage [brazil]{babel} % em portugues brasileiro
% tema (modelo)
% \usethemeí\arsaw)
%AVusethemetAnnArbor)
%AVusetheme{Boadilla}
eAusethemeí{Singapore}
\usethemeí{SimplePlus}
%usethemeí{ocus}
%\usetheme{metropolis}
% Tem muitos temas em
% https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/
themes
% tema de cores (Esquema de cores)
\usecolorthemeídefaultY
%4 para ver como fica as combinacoes de algumas temas e esquema de cores,
% veja o site https://hartwork.org/beamer-theme-matrix/
%%vsetbeamerfont{title}family=\rm) % titulo em romano
\usepackageTamssymb,amsmathl) % para incrementar fórmulas
\usepackage{tikz} % para cria degrade no fundo
% \usepackageThyperref) % ja eh carregado pelo beamer
\usepackageísansmath{onts} % fontes sans para fórmulas
%\usepackage [s{default} {notomath} % Mudando fontes
\usepackage{lipsum} % para gerar texto, para teste
\usepackage [bibencoding=utf8,backend=biber,style=authoryear-comp] {biblatex}
\addbibresourceítlatex-via-exemplos.bib)
\hypersetupt% informacoes do PDF
pdftitle={Slide beamer},%
pdfauthor=íSadao Massago),
pdfsubject=TExemplo de Slide),
pdfkeywords=(LaTeX, Slide)
) %4 \hypersetup
% Informacoes para criar titulo
\title[Exemplo de Slidel {Exemplo de Slidey}
\authorí%
Sadao MassagoVYinst{1} % \and ???\inst{2}
+
\institute [DFQM-UFSCar] (
\instí1Y%
Departamento de Física, Química e Matemática N
Universidade Federal de São Carlos
% \and
% \inst{2} ?7??
+
\date[Março 2018] (\LaTeXí) Via Exemplos, 2018)
% fundo em degrade
\setbeamertemplate{background canvas}í%
\begin{tikzpicture} [remember picture,overlay]
%ishade[top color=red!10,bottom color=blue!10, middle color=white!10]
\shade[top color=red!10,bottom color=blue!10]
(current page.north west) rectangle (current page.south east);
\end{tikzpicture}%Z
Asetbeamertemplateínavigation symbolskí) % desativa botao de navegacao que
temem alguns temas
\beginídocument+
\\{ramefiWtitlepagel} % slide de titulos
\\{ramefVWtransdissolveWtableofcontents} % slide de sumario
% Fora do frame,só pode usar um note (será considerado soment eo último note
)
\notefEm torno de 1 minuto para cada tópicos deste slide.) % notas para
slide anterior
% \ota dentro do slide são acumulados e pode especificar o "“overlay'', se
desejqr.
% também pode usar opção como 'item' para criar lista de notas
% Observação: quando tem notas como item e sem ser como item, os que não são
itens fican no começo.
\sectioníOverlay (apresentando por etapas)) % section será usado no sumário
e similares
% ""overlay'' é recurso de apresentar em etapas (especificado pelo parametro
opciuonal delimitado por <>)
\beginí{rame} % slide
\frametitleíSlides de apresentação)
\begin{itemize}
\item <1->\alert<1>íUsar letras grandes)
% notas vinculado ao slide "1-"
\note<1->[{tem} fNalert<1>fNo beamer, só não reduzir o tamanho das letras.
Recomendável usar a fonte não seri{ada})
\item <2->\alert<2>íCor do {undo deve criar contraste com texto}
% notas vinculado ao slide "2-"
\note<2->[{tem} fNalert<2>ffundo, caso usar, não pode reduzir a legibilidade
++
\item <3->lalert<3>fContraste pode ser pela cor ou claro/escurol
\end{itemize}
\only<4->flalert<4>{Escrever pouco e falar muito})
\endí{rame}y
% lista permite *“overlay'' automático
\beginí{rame} % slide
\frametitlefíAlgumas dicas)
\begin{itemize} [<+->]
\item \alert<.>{Organizar em listas ou blocos}
\note<.->[{tem} fNalert<+>(Se possível, dividir em blocos ou itens de listas
-
\item \alert<.>{Apresentar lista ou blocos em etapas}
\note<.->[{tem} fNalert<+>fUsar o *“overlay'')
\item \alert<.>fEvitar conteúdo grande, dividindo em slides)
\endí{itemize}
\uncover<t+>fVlalert<.->fNão abusar do efeito de transição))
\endíframey
% ""bloco'' é uma ''caixa'' dentro do slide
\beginíframeY
\frametitle{BlocosY}
\beginfíblockY(X<1->
Este é um bloco sem título.
\endíblocky
\beginfblockYíSegundo blocol<2->
Este é um bloco com título.
\end{block}
% como este paragrafo não tem especificação de *“overlay'', aparecerá em
toda etapa
""bloco'' é uma ""caixa'' com ou sem título
\notefO ""bloco'' aceita o parâmetro de \texttt{overlay}.lk % nota
\endíframe>
\sectionfAmbiente \texttt{verbatim} no slide) % outra entrada de sumário
% Ambiente \\texttt{verbatim} e similar requer opção \textttí{ragile}.
\beginíframe+[{ragile} % outro slide
\frametitleí\erbatimY
Ambiente \texttt{verbatim} e similar requer opção \textttí{ragile}.
\beginf{verbatim}
program teste;
begin
writeln('Alô pessoal!');
end.
\endf{verbatim}y
\noteíNão pode usar * “\textttíoverlayl'' no ambiente \texttt{verbatim}. No
caso de listar o código do beamer, deverá criar o novo ambiente para
evitar conflito com o \\textbackslash endWí{rameW} .>
\endí{rame}>
% Para listar o código do beamer, deverá criar o novo ambiente para evitar
conflito de \endí{rame}.
%4h Crie um novo ambiente como segue, no preamble.
%4\newenvironmentíverbatimf{rame}
%MYVbeginí{rame} [fragile,environment=verbatim] )
%\endí{rame}y
%% Depois use ele
Abeginíverbatim{rame}
% \frametitleí\erbatim com código beamer+
%Para listar o código do \\texttt{beamer}, deverá criar o novo ambiente para
evitar conflito de \erbt+\endí{rame}+.
%% \pausel)
Abeginf{verbatim}
Abegint{rame}\frametitleíT{tulo}
o o o
%Zendí{rame}
%end{verbatim}
%vendíverbatim{rame}
\sectioníQuebra automática em {rames} % mais uma entrada para sumário
\beginí{rame} [allow{ramebreaks} % e mais um slide
\notef
Para que mude o frame automaticamente quando tornar cheio
coloque a opção \textttíallow{reamebreaks} no frame
D7
\lipsum[1-2]
\endí{rame})
\sectioníOpção plain)
\beginíframeY[plain]
\frametitleíOpção \texttt{plain})
17.2. Slides
\lipsum[1]
\endíframey
\notef
Opção \texttt{plain} desativa cabeçalho e rodapé do frame para ter mais
espaço.
Útil, por exemplo, para colocar figura ou tabela maior.
P
% colocar somente os mais relevantes para não ficar longo
\sectiontreferêcnias)
\beginíframeY [allow{ramebreaks}
\frametitleíBibliogra{ia}
\nocitel*) % todas referências
\printbibliography [heading=none]
CANbibliographystyle{amsalphal} % estilo não faz efeito
Abibliographytflatex-via-exemplos)
\endíframe>
\endí{document}
Slides de apresentação
* Usar letras grandes
€ Cor do fundo deve criar contraste com texto
3/10
\ote que, nos itens de listas, aceitam o parâmetro opcional de “overlay” delimitado por
“<” e “>”. Com o uso de overlay, o slide será apresentado por etapas. Em cada etapa do
overlay, será mostrado uma parte do slide. O mais usado é ir mostrando cada vez mais
elemento na medida que etapa avança (andar no slide).
A especificação do overlay são:
<n> indica que será mostrado somente na etapa n.
<m-n> é mostrado somente nas etapas m até n.
<n-> é mostrado nas etapas n em diate.
<-n> é mostrado até as etapas n.
Os comandos de formatação de textos do tipo \texts{t}, \textb{1}, \emph, etc, também
aceitam a opção de overlay. Também foi acrescido o comando \alert neste conjunto para
deixar o texto em vermelho.
Para criar overlay nas partes desejadas que não é necessariamente itens da lista ou
formatação de texto, existe o comando \only que mostra o conteúdo somente no overlay
indicado.
Também tem o ambiente chamado de block que produz “bloco” com ou sem títulos e
aceita “overlay”.
No frame, alguns parâmetros opcionais podem ser usados. Alguns dos mais importantes
são
fragile \ecessário quando usa o ambiente verbatim ou similar.
allowframebreaks Ativa a quebra automática de frame's quando o conteúdo não cabe no
frame atual.
plain Limpa as configurações (cabeçalhos e rodapés) do frame para caber mais conteúdos.
Útil para figuras e tabelas grandes.
shrink Reduz o tamanho do conteúdo para caber no frame atual, se necessário. Isto pode
reduzir o tamanho da letra e por isso, deve ser usado com muita cautela. Use em
conjunto com plain para ampliar a área de slide.
Dependendo do estilo usado, o slide em textttbeamer pode precisar ser compilado duas
vezes para acertar detalhes.
18. Usando X7lATEX e LuaLaTeX 214
Capítulo 18
Usando X4IlATEX e LualATEX
Neste capítulo será tratado sobre XeLaTeX e LuaLaTeX, considerado as próximas gerações de
LaTeX.
18.1 . LualATEX e XeLaTeX
O LualáTEX foi designado para ser o sucessor do PDFETEX e por isso, deve ser o LaTeX
padrão no futuro, mas pode ser um pouco mais lento do que o XaATEX. Lua(La)TEX permite
estender a funcionalidade do (La)TEX usando a linguagem script Lua (Lua foi desenvolvido
no PUC-Rio, aqui no Brasil).
Já existem pacotes especiais para LualáTEX como o módulo de diagramação automática
de grafos no pgf/tikz. O suporte ao recurso de microtipografia (efetuar pequenos ajustes no
tamanho das letras e espaçamento para que o texto acomode melhor) pelo pacote microtype
também funciona melhor com LualáTEX do que em XaLaTeX.
A maioria dos documentos de ELaTeX devem funcionar sem modificações no
XqALaTeX/LualTEX, mas para usar as fontes adicionais em “Open Type”, ou as fontes do
sistema, devem usar a forma própria de selecionar as fontes.
A forma de ajustar a codificação de documento fonte no LaTeX, XeLaTeX e LualATEX dife-
rem, mas como XalATEX e LualáTEX usam uft8 como padrão (e atualmente LaTeX também),
não vamos preocupar com isso.
Embora babel funcione no XgLaTeX/LuaLaTeX também, no Exemplo 18.1 foi usado o
polyglossia feito especialmente para XeLaTeX/LualTEX.
Embora maioria dos pacotes de fontes do LaTeX funcione no XeLaTeX/LuaLaTeX, no Exem-
plo 18.1, foi usado o método próprio deles que permite selecionar fontes adicionais, inclusive
as fontes do sistema.
Se a fonte usada contiver símbolos matemáticos, use unicode-math em vez do
amssymb/amsmath. Se precisar dos símbolos ou comandos de amssymb e amsmath, carregue
eles antes do unicode-math.
\ote que os pacotes e comandos do LaTeX padrão, exceto o inputenc costumam funcionar
no XeLaTeX e LuaLaTeX, mas não o contrário. Assim, para que o documento possa ser
compilado tanto em PDFILaTeX como em X47LaTeX/LualATEX, poderá usar o pacote iftex
para detectar a engenharia do TEX em uso.
Exemplo 18.1: exl8-lualatex.tex
\documentclass [a4paper,12pt]t{article}
\usepackageíti{tex} % Para detectar engenharia de TeX
\ifPDFTeX % Se (PDF)LaTeX
\usepackage [T1] ({fontenc} % codificação da fonte em 8-bits
\usepackage [english,brazil]{babell} % em portugues brasileiro (ingles como
secundario)
\usepackageTlmodern) % latin Modern (Computer Modern com extensao latin)
% \usepackage{notol} % fonte \oto patrocinado pelo Goggle
% \usepackage[{talic} {mathastext} %& A fonte \oto serifado nao possui fontes
matematicos ainda
\usepackage{Ttextcomp}
\usepackageTamssymb,amsmath+>
\else % Se XeLaTeX/LuaLaTeX
\usepackageTpolyglossia)
\setdefaultlanguage{brazil}
\setotherlanguagefTenglishk % secundario
% Estas fontes são padrões e não precisavam especificar. Foram colocados
somente para ilustrar
% No caso de XeLaTeX, se a fontes correspondentes não estiver isntalados no
sistema operacional, pode não funcionar. Comente.
\setmainfontíLatin Modern Roman)
\setsansfontíLatin Modern Sans)
\setmonofontíLatin Modern Mono)
% Se precisar do amssymb,amsmath, deverão carregar antes do unicode-math
% \usepackageí{amssymb,amsmath}
\usepackagefTunicode-math) % amsmath, amssymb equiv.
\ifLuaTeX % Somente LuaLaTeX
\usepackageTlualatex-mathk % alguns fix do amsmath/mathtools equiv. para
LuaLaTeX.
\fi
\setmathfontíLatin Modern Math) % Padrão e não precisava. Foi colocado
somente para ilustração
% Fonte \oto Serif não tem fontes matemáticos ainda
%setmainfont [Ligatures=TeX] (\otoSerify
%Zisetsansfontí\otoSansY
%setmonofontí\otoMono)
% Asana math (Palatino like)
% \setmathfontíAsana-Math)
% STIX (Times like {ont}
sAsetmainfont [Ligatures=TeX] (STIXY
£AsetmathfontísTIX Math)
%" XITS (Times like {ont}
%isetmainfont [Ligatures=TeX] (XITSY
AsetmathfontíXITS Math)
vfi
% Mais alguns pacotes
\usepackage [margin=2.5cm] ({geometry}
\{usepackageThyperref}
\hypersetupt
bookmarks=true
d”
\usepackage [stretch=10] {microtype} % microtipografia: funciona no PDFLaTeX e
LuaLaTeX (parcialmente em XeLaTeX)
\beginf{document}
O LualWLaTeXf) foi designado para ser o sucessor do PDFWLaTeXí) e por isso,
deve ser o \aTeXt) padrão no futuro. Por outro lado, XeLaTeX e mais
rápido.% e estável (2018).
\ldots
Se $F' (x)=f(x)$ for contínua,
NE
\int a“bf(x)dx = F(b) - F(a)
J
\endí{document}
O LualáTEX foi designado para ser o sucessor do PDFLaTeX e por isso, deve ser o LaTeX
padrão no futuro. Por outro lado, XebLaTeX e mais rápido.
Se F'(x) = f(x) for contínua,
b
/ f{x}da = F(b) — F(a)
O usuário de MS \indows devem ficar atentos pelo fato de que a fonte “Latin Modern
Math” usada no Exemplo 18.1 não vem instalado por padrão no MikTEX Básico. Como
XqLaTeX/LualTEX acessa as fontes diretamente sem usar os pacotes, pode precisar a instalação
manual do pacote Im-math usando o gerenciador do MikTEX.
Existem algumas fontes Open Type com suporte a matemática que podem ser usados no
XeLaTeX/LualTEX. O site
https://www.overleaf.com/help/193-what-otf-slash-ttf-fonts-are-supported-via-
fontspec lista algumas delas (com suporte aos símbolos matemáticos).
e Cambria Math (Microsoft, somente \indows).
* Latin Modern Math (Boguslaw Jackowski, Janusz M. \owacki). Padrão do
XeLaTeX /LuaLaTeX..
* TeX Gyre Pagella Math (Bogustaw Jackowski, Janusz M. \owacki).
* TeX Gyre Termes Math.
* Asana Math (Apostolos Syropolous), Estilo Palatino.
* \eo Euler (\haled Hosny).
* STIX (STI Pub).
* XITS Math (\haled Hosny).
\ote que a fonte vnathcal e \mathbb do unicode-math é diferente do amssymb. O
\mathbb é mais próximo do \wmnathds do dsfont e vmathcal é mais parecido com do pacote
eucal do que de amssymb.
Quem quer usar a versão do amssymb, poderá colocar
\letwmathcalirelax % remove the definition by unicode-math
\eclareMathAlphabetí\mathcalY(fOMSX{cmsy}im)tn)
\letWmathbbyrelax % remove the definition by unicode-math
\eclareMathAlphabetí\mathbb)fTUX{msb}{mIin}
no preamble, após carregar o unicode-math.
\ote que, nem todos os símbolos do unicode-math costumam estar presentes na fonte
utilizada. Quando a fonte utilizada não apresentar os símbolos correspondentes aos comandos
de unicode-math, o símbolo simplesmente não aparece, sem emitir mensagens de erro, o que
requer cuidados. Neste caso, deverá complementar com outras fontes, ou procurar símbolos
alternativos. Por exemplo, carregar o pacote amssymb antes do unicode-math complementa
com os símbolos de ANMS.
Observação 18.1. Além das melhores suportes das fontes, existem vários pacotes específicos
para XeLaTeX e LuallTEX, como no caso de luavlna (para LuallTEX) e xevlna (para XeLaTeX)
que impedem que as palavras de uma só letra ou similar, fiquem no final das linhas, o que
ajudam na finalização do livro, em conjunto com o microtype.
18.2 Mais sobre básicos das fontes no
XalaTEX /LualaATEX
No XgLaTeX/LualATEX, poderá redigir em qualquer idioma desde que esteja utilizando as
fontes que suportam tais idiomas. Assim, quando redige o documento multilingue, basta
definir qual fontes será usado em qual trecho. Para facilitar a especificação de fontes em
cada trecho de textos, costuma definir família de fontes usando \newfontfamily do pacote
fontspec. Ele define comandos para usar a fonte especificada com as configurações também
especificadas, que funcionam como outros comandos de seleção de famílias de fontes pré
definidos tais como \rmfamily, \sffamily, etc.
Por exemplo,
\newfontfamilyí\notormkí\oto Serify
\newcommandí\textnotorm[1] fí\notorm t1)
\new{ontfamilyfNnotosf}í\oto Sans)
\newcommandfNtextnotosf[1] ({Nnotosf t1}
definem comandos \notorm e \notosf para usar fontes \oto Serif e \oto Sans. O
\newcommand foi usado para criar a versão \textxx que são \\\textnotorm e \textnotosf
respectivamente. \ote o uso de chave dupla para que a configuração da fonte não “vaze” para
fora.
Para usar fontes não definidos anteriormente, poderá usar o comando \fontspec para
selecionar a fonte especificada.
Apesar de poder configurar a especificação da fonte com o parâmetro opcional dos coman-
dos de seleção das fontes e definições de família de fontes, isto também pode ser efetuado
separadamente pelo comando \defaultfontfeatures para especificar recursos das fontes.
O parâmetro opcional será usado para indicar o nome da fonte que está especificando. Por
exemplo,
\defaultfontfeatures[\oto Serif] íLigatures=TeX>
Especifica que no \oto Serif, será usado a ligadura no modo TEX. Além de indicar nome
das fontes, poderá indicar pelo comando de família das fontes como em
\defaultfontfeatures [\rmfamily,\s{family} (Ligatures=TeX)
especifica que na fonte romana e sans serif, será usado a ligadura padrão do TEÊEX.
Para limpar a especificação das fontes, basta usar como
\defaultfontfeatures [\\\rmfamily,\s{family} ()
O comando \defaultfontfeatures tem a versão “+” \defaultfontfeatures+ que acres-
centa a especificação em vez de substituir. O comando \addfontfeature pode ser usado
para ajustar localmente a especificação. Coloque entre chaves para especificação adicional
seja aplicado somente no trecho.
Quando lida com várias fontes no XgLaTeX/LualTEX, as vezes é importante checar se a
fonte existe. \IfFontExistsTF do pacote fontspec checa se a fonte do primeiro parâmetro
existe. Caso existir, executará o segundo parâmetro e caso não existir, executa o terceiro
parâmetro. O comando a seguir configura a fonte principal para \oto Serif caso ela existir.
\IfFontExistsTFí\oto Serif)ílsetmainjfontí\oto SerifXYY(%
\PackageWarningí\jobname.texXí\oto Serif not found. Using default {onts}
Ir testando várias fontes com este comando até achar uma disponível na lista é trabalhoso.
Assim, para procurar fontes na lista, costuma usar o pacote iffont. Ele implementa o
comando \settofirstfoundí\nomefonte+í<fontes>) onde <fontes> é lista de nome das
fontes, separado pela vírgula. Ele associa ao comando \nomefonte, o nome da primeira fonte
encontrada na lista, o que pode ser usado para selecionar ou definir família de fontes. Caso
nenhuma fonte existir, retorna o valor de \eiffontefirstfont que está como a última fonte
encontrada anteriormente (se ainda não existe a fonte encontrada, será a {onte Fira Sans}.
Em geral, coloca-se o nome de uma fonte existente no final da lista para evitar de cair no
\eiffontefirstfont que nem sempre é desejável.
Por exemplo, o código
\settofirstfoundí\mainfontkí\oto Seri{, Latin Modern Serif}
\setmainfontí\main{ont}
configura para usar o “\oto Serif” como fonte padrão caso existir. Caso ele não for encontrado,
usa-se a fonte “Latin Modern Serif” que deve estar presente na instalação padrão do TEX. No
caso de XgLaTeX, se a fonte “Latin Modern Serif” não estiver instalado no sistema operacional,
não vai encontrar. Assim, poderá colocar “[Imroman12-regular]” ou similar no lugar.
Se o que quer é saber se a fonte existe, o iffont também implementa os comandos
\iffontsexist e \iffontexists na qual executa o segundo parâmetro quando fonte existe
e terceiro parâmetro quando a fonte não existe. A diferença é que no \iffontsexist, o parâ-
metro é uma lista de nome das fontes separado pela vírgula (e executa o segundo parâmetro
se todas as {ontes da lista existirem} e no \iffontexists, o parâmetro é nome de uma única
fonte (igual a \IfFontExistsTF do {ontspec}. Por exemplo,
\iffontexistsí\oto SerifYílWsetmainjfontí\oto Serif)XY(%
\PackageWarningí\jobname.texkí\oto Serif not found. Using default {onty}
Configura para \oto Serif só quando ele for acessível.
As fontes Open Type que podem ser usados pelo XeLaTeX e LualáTEX podem estar no
diretório do documento, diretório de TEX ou instalado no sistema operacional. No LualATEX,
estas fontes podem ser acessadas pelo nome das fontes, mas no XqLaTeX, somente as fontes
instaladas no sistema operacional podem ser acessados pelo nome. Fontes encontradas em
outras localidades tais como junto ao documento TEX ou no diretório de TEX devem ser
indicados pelo nome do arquivo, incluindo a sua extensão (ou alguma especificação adequada ).
Assim, se os comandos do pacote fontspec ou de iffont não conseguirem encontrar as fontes
pelo nome no XeLaTeX, tente usar o nome do arquivo da fonte.
