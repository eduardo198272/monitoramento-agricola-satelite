que, para ajuste somente de capítulos, existe o pacote fncychap que permite escolher um
modelo entre alguns prontos através da opção do pacote (Sonny, Lenny, Glenn, Conny, Rejne,
Bjarne, Bjornstrup) e ajustar as fontes com comandos tais como \hNumVar e \ChTitleVar.
Mas o pacote fncychap não consegue refazer o estilo como no titlesec.
Assim, para configuração mais refinada dos títulos de capítulos e seções, costumam usar
o titlesec. Este pacote, além de configuração refinada de títulos, também pode ser usado
para configurar o cabeçalho das páginas (apesar de, para o cabeçãlho, o recomendado é o
pacote {ancyhdr}. \eja o Exemplo 15.5.
Exemplo 15.5: exl5-titlesec.tex
\documentclass [12pt,a4paper] {article}
\usepackage [T1] ({fontenc}
\usepackage [brazil] fbabelY
\usepackage{calc} % para cálculo de medidas
\usepackage [pagestyles] (titlesec) % para formatar título do capítulo e seção
& formatando o titulo do capítulo
\titleformatílchapterk[display] % modo display
fibfseries|Large) & fonte usado no título do capíútulo
TNfilleft MakeUppercase{\lchaptertitlename} \HugeWthechapter) % Como colocar
o nome do capítulo
{4ex} % espaco entre nome do capítulo e titulo do capítulo
fititleruleWspace{2ex}\\{ilright} Z o que colocar antes do titulo do
capitulo
[\spacet2exkltitlerule] %Z depois do titulo do capítulo
% \titlespacing*t|chapter)íOptr{20pt}{16pt} % espacamento do titulo de
capitulos
& Exemplo ajustado da documentação
& formatando o título da seção
\newcommandí\sectiontitlenamel-íSeção)
\title{ormatfNsection} [{rame} Z colocar moldura
finormalfontYZ fonte normal
fNfilright footnotesize
\enspace \akeUppercasefWsectiontitlenamel-\enspace \thesectionVYenspace /%
Como colocar o nome/enumeracao da seção
T8pt)Y%Z espaço antes do titulo da seção
fiWLargeWbfseries {ilcenter}Z antes do titulo da seção (ajustando {ontes}
& \titlespacingtílsection+)íOptI{*2}1*2)
/4 definindo o estilo do cabeçalho usando titlesec
A para configuração mais sofisticada, use fancyhdr
\newpagestyleímain+t % Novo estilo de pagina
\headrule
\sethead [\\thechapter. \scshapeVWchaptertitle] [] [l \Y \thechapter. \slshapel
chaptertitle)
\setfoot[] [\\thepage] [] (\\{\thepage}T>
D”
\pagestyleíempty
\begin{document}
\pagestyleímain+ Z% inicia o cabeçalho personalizado
\chapteríUm Capítulol
Um capítulo novo.
\sectioníUsando \texttt{titlesec})
\idots
\endídocument y
CAPÍTULO 1
Um Capítulo
Um capítulo novo.
r SEÇÃO 1.1
Usando titlesec
\ote que a primeira página do capítulo será sempre do estilo plain. Então, se quer que a
primeira página do capítulo seja diferente do plain padrão, deverá redefinir ele.
Para configurações mais complicadas de títulos de capítulos e seções, use a opção explicit
na qual os textos de títulos só serão colocados se for referenciado diretamente.
Para usar o titlesec e fancyhdr ao mesmo tempo, deverá carregar o titlesec com
opção pagestyles e antes do fancyhdr.
Para configurar a saída de títulos dos elementos flutuantes como figuras e tabelas que
são produzidos pelo comando \caption, costuma usar o pacote caption que implementa o
comando \captionsetup para configurar o formato de títulos das figuras e tabelas. Este
pacote também implementa a versão “*”
o t{tulo}.
No Exemplo 15.6, está configurado o nome da figura no ambiente figure como sendo
do \caption que não será contabilizado (só coloca
Imagem. A fonte do nome será em negrito, título em itálico, formato do nome é modo simples
e nome com título será separado pelo ponto.
Exemplo 15.6: exl5-caption.tex
\documentclass [12pt,a4paper] {article}
\usepackage [T1] ({fontenc})
\usepackage [brazil]{babel}
\usepackage{caption} % para formatar titulo do float ({igura e tabela}
\captionsetup[{igure} fname=Imagem,labelfont=f1bfl, textfont=it, labelformat=
simple, labelsep=period)
\pagestyleíempty>
\begin{document}
\beginítfigureY [hbp!]
\center
Figura aqui.
\captioníNovo títulokMlabelífig:titulo:novo)
\endí{igure})
\clearcaptionsetuptfigurey
\beginí{igure}) [hbp!]
\center
Figura aqui.
\eaptioníTítulo normalMlabelífig:titulo:normal]
\endí{igure})
\endí{document}
Figura aqui.
Imagem 1. Novo título
Figura aqui.
Figura 2: Título normal
Para limpar as configurações, usa o comando \clearcaptionsetupí{igure}, onde figure
pode ser table, se for da tabela.
Para criar configurações complexas que é difícil de ser ajustado com comandos acima,
poderá usar o comando \eclareCaptionFormat.
Por exemplo, se quer que o nome da figura fique em maiúsculo negrito, separado por dois
pontos e titulo em itálico, basta criar o estilo novo com
\eclareCaptionFormat{meuestilo}(íTWMakeUppercaselb{series H1}H2\textit{tHa}
par]|
e usar como \captionsetup[{igure} (fformat=meuestilo, labelsep=colony.
15.4  Ajustando o sumário
Para ajustar o estilo de sumário e similares, costuma usar o pacote tocloft. Este pacote
também permite criar lista de objetos similares a de sumários (por exemplo, lista de algo-
r{timos}. Uma das coisas que ocorre com certa frequência é ter livro sem as seções e com
a ausência de linhas pontilhadas no capítulo do sumário, o que dificulta a localização da
página correspondente. Neste caso, é só acrescentar a linha pontilhada no capítulo, como no
Exemplo 15.7.
Exemplo 15.7: ex15-tocloft.tex
\documentclass [a4paper,12pt,oneside] (bookY
\usepackage [brazilian] {babel}>
\usepackageTttoclo{t})
\setcounterítocdepthY(1) % até nivel 1 (seção)
% Fontes do sumário
%ArenewcommandfVcfttoctitlefont Y \hfillNLarger
%ANrenewcommandí\c{taftertoctitle}í\hfilly
% linhas pontilhadas para capítulo no sumário.
\renewcommandí\cftchapdotsepYílc{tdotsep}
\begin{document}
\tableofcontents % sumário
\chaptert{Primeiro}
\sectioníSeção)
\chapteríOutro cap{tulo}
\sectioníOutra seçã{o}
\end{document}
na qual o sumário ficará algo como segue
é L)
Sumário
1  Primeiro....llllraareraa aaac aaeaa aaacA aaaaaao. 2
11 SeçãoO. .. iilA 2
2 Outro Capítulo....llllaaa aaaA 3
2.1 / Outra seção.....llllll.ll AAA 3
15.5 Links
Quando usa o pacote hyperref, sumário, índice remissivo, as referências cruzadas e citações
ganham link automaticamente. Além disso, poderá configurar informações gerais do docu-
mento PDF gerado, tais como titulo, autor, palavras-chave, etc relacionado com o documento
PDF.
A configuração do PDF pode ser feito por algo como segue.
\usepackage{Thyperref})
% configurando o PDF
\hypersetupt
bookmarks=true, % show bookmarks bar?
unicode=true, % non-Latin characters in 'Acrobats bookmarks
breaklinks=true, %break long url across lines
pdftoolbar=true, % show *Acrobats toolbar?
pdfímenubar=true, % show *Acrobats menu?
pdffitwindow=false, % window fit to page when opened
% pdfstartview=(FitH), % fits the width of the page to the window
pdftitle={Pacote hyperref}, % title
pdfauthor=(Sadao Massagol, % author
pdfsubject=(Uso do pacote hyperref), % subject of the document
pdfcreator=({Creator}, % creator of the document
pdfproducer=tProducer), % producer of the document
pdfkeywords=(keywordl, key2, key3k, % list of keywords
pdfnewwindow=true, % links in new PDF window
colorlinks=false, % false: boxed links; true: colored links
linkcolor=red, % color of internal links (change box color vith
linkbordercolor)
citecolor=green, % color of links to bibliography
filecolor=magenta, % color of file links
% urlcolor=cyan %4 color of external links
RXX
\ote que, apenas carregar o hyperref já é suficiente para maioria dos casos, mas em geral,
se estiver usando pacotes que ajustam os comandos de referências cruzadas ou citações, o
pacote hyperref deve vir depois deles para não perder os links.
Além do link automático, poderá inserir links para sites, etc, usando o comando \url.
\eja \urlíhttps://en.wikibooks.org/wiki/LaTeX/Hyperlinks) por exemplo.
Atualmente, o url (endereço de internet) é importante para ser colocado nas referências
bibliográficas, caso exista. O estilo moderno para BibTeX costuma usar o campo url na qual
o seu valor pode ser ser colocado no arquivo de BIBLaTeX, como em
url = fhttps://en.wikibooks.org/wiki/LaTeX/),
urldate = 12018-06-11),
onde urldate é a data da última consulta.
Para estilos um pouco antigo que não tem o campo urldate, poderá colocar a data de
último acesso no campo note como em
url = fhttps://en.wikibooks.org/wiki/LaTeX/]),
note = f(\isited on 2018-06-11)),
No caso de estar usando o estilo antigo na qual ignora o campo url, poderá colocar o
endereço no campo note, usando o comando \url.
note = "URL: \urlíhttps://en.wikibooks.org/wiki/LaTeX/) (\isitado em
2018-06-11)",
mas cuidado para não colocar em note e url ao mesmo tempo, para evitar duplicações nos
estilos que suportam url.
Para quem deseja um estilo clássico com suporte a url, o pacote urlbst dispõe de
alphaurl, plainurl, abbrvurl e unsrturl correspondentes a alpha, plain, abbrv e unsrt
respectivamente. \ote que, para estes estilos, a data de último acesso é no campo lastchecked
e não no urldate. Para que funcione tanto nestes estilos quanto no estilo mais moderno,
poderá colocar ambos os campos.
Obviamente, o arquivo tex correspondente ao estilo bibliográfico com URL deve usar o
pacote hyperref ou o url.
Quando quer acrescentar o link com texto onde clicar é diferente do endereço do link,
poderá usar o \href como em
\hrefíhttps://en.wikibooks.org/wiki/LaTeX/Yíwikibooks, \LaTeXí\y
Também poderá criar os links manualmente, dentro do documento. Para isso, define a che-
gada do link com o comando \hypertarget e cria link para ele, com o comando \hyperlink.
\eja o https://en.wikibooks.org/wiki/LaTeX/Hyperlinks para detalhes.
Quando usa as fórmulas nos títulos, aparece “lixo” no indicador (bookmarks) do PDF. Isto
porque, no indicador, só o texto é aceito. Para evitar isso, existe o comando \\texorpdfstring
que coloca conteúdo de LaTeX ou texto, dependendo de estar no documento ou no bookmarks.
Por exemplo,
\sectionfVWtexorpdfstringí$E=mc 2$1E = mc ** 2)>
Usará E = mc? para o documento, mas E = mc ** 2 para o indicador (bookmarks).
Alguns comandos pode não funcionar no bookmarks do PDF, como o caso de
\MakeUppercase. O pacote hyperref dispõe de comando \pdfstringdefDisableCommands
para redefinir estes comandos dentro do bookmarks. Por exemplo, para desativar o
\MakeUppercase ou redefinir W dentro do bookmarks do PDF, coloque
\pdfstringdefDisableCommandsí%,
\let MakeUppercaselrelax/desativando
\defWNWWt Y% em vez da nova linha, será espaço
\defyandf e >
d”
no preamble do documento.
Quando adiciona um item manualmente no sumário através do comando
\addcontentsline, o link do sumário pode não posicionar na página correta. Para
o funcionamento correto (posicionamento correto) do link no sumário requer que o
\addcontentsline deve ser chamado logo em seguida da mudança de capítulo ou seção.
Caso não esteja, é só colocar \wphantomsection oferecido pelo pacote hyperref antes do
\addcontentsline.
.'lev
\ote que “"|” na entrada do índice remissivo para inserir o símbolo não funciona em
«”
conjunto com o pacote hyperref. AÀ forma de contornar isso é definir um comando para
e usar na entrada do índice remissivo.
15.6 Controle das listas e listas inline
O pacote enumerate permite controlar as enumerações das listas. Mas as vezes queremos
efetuar controle mais refinado ou controlar o rótulo de listas não enumeradas também. O
pacote enumitem permite formatar a lista de forma similar ao pacote enumerate, mas com
recursos adicionais.
Existe também os casos que queremos as listas que coloquem vários itens na mesma linha,
denominado de listas inline. Existem vários pacotes que permitem criar listas inline, mas
esta tarefa também pode ser feita pelo pacote enumitem.
A opção shortlabels no pacote enumitem ativa o modo de compatibilidade com o pacote
enumerate, permitindo formatar enumeração da lista enumerate via modelos. AÀ opção
inline criará a versão “*” dos ambientes de lista que são listas inline (não muda de linha
X”
entre os itens). Para alinhar os itens das listas versão , poderá usar o pacote tabto.
\eja o Exemplo 15.8 que usa os pacotes enumitem e tabto.
Exemplo 15.8: ex-d-enumitem.tex
\documentclass [12pt,a4paper] {article}
\usepackage [T1] ({ontenc} %& codificação da fonte em 8-bits
\usepackage [brazil]{babel} %Z em português brasileiro
\usepackagefamssymbl Zpara comando lsquare
\usepackage [inline,shortlabels] {enumitem}
\usepackageTtabto)
\usepackagetxcolor) % para mudar de cor
\beginfí{document}
/4 Em vez de indentar, cria espoço extra entre parágrafos
\parindent=0em & indentação nula
\parskip=\baselineskip % um linha entre parágrafos
%& No parâmetro opcional, aceita a formatação de enumeração como do pacote
enumerate (ativado pela opção shortlabels)
& Tombém poderá configurar as fontes
/& As opções são separados pela vírgula
\begin{enumerate}) [1),font=\color{blueY}
\item Item 1
\item Item 2
\\\item Item 3
\end{enumerate}
%& Nas listas como o enumerate e itemize, poderá configurar o \\\label que
rotula os itens. Neste exemplo, será colocado um circulo na enumeração.
4 O "*" no label será substituido pelo enumi, enumii, etc dependendo do seu
nível.
\begin{enumerate} [label=fMlargelprotecttextcircledí\normalsizeVarabic*))]
\\\item Item 1
\item Item 2
\item Item 3
\end{enumerate}
/4A versão "“*'' produz lista inline que não efetua mudança de linhas quando
muda o item.
\begin{enumerate*}[a)]
\\\item Item 1
\item Item
\\\item Item
\\\item Item
\item Item
\item Item
O MP OMN
15.6. Controle das listas e listas inline
\item
\item
\item
\item
Item
Item
Item
Item
o o N
\endí{enumerate*}
/4 Poara alinhas os ítens, use em conjunto com tabto.
/& Quantas "colunas" vai ter na tabulação (que será usada na lista versão
UP n)
\unmnTabsít5>
%4 Na lista versão *, poderá indicar o que colocar entre itens consecutivos
com itemjoin
& No caso, o \ltab será usado para alinhar itens em colunas.
\begin{enumerate*}[1.,itemjoin={\tab}]
\item
\\\item
\item
\item
\item
\item
\item
\item
\item
\item
Item
Item
Item
Item
Item
Item
Item
Item
Item
Item
O O 2N O UP OMN
\endí{enumerate*}
AWumTabst4) %4 poderá mudar o número de colunas, se desejar
% Ítens longas podem ocupar dois ou mais "colunas" automaticamente
\begin{itemize*} [label=$lsquare$, itemjoin={Ntab}]
\item
\item
\\\item
\item
\item
\item
\item
\item
Item
Item
Item
Item
Item
Item
Item
Item
e longa, com espaço maior
2 O 0P OMNM
\endí{itemize*}
\endí{document}
1) Item 1
2) Ttem 2
3) Item 3
(D Item 1
( Item 2
& Item 3
a) Item 1 b) Item 2 c) Item 3 d) Item 4 e) Item 5 £f) Item 6 g) Item 7 h) Item 8 i) Item 9
j) Item 10
1. Item 1 2. Item 2 3. Item 3 4. Item 4 5. Item 5
6. Item 6 7. Item 7 8. Item 8 9. Item 9 10. Ttem 10
Item 1 Item 2 Item 3 Item 4 Item 5
Item 6 e longa, com espaço maior Item 7 ITtem 8
15.7 Trocando as fontes — parte 2
LaTeX dispõe de diversas fontes gratuitas para diagramar o documento. Em geral, para
versão impressa, costuma usar o Latin Modern que é uma extensão do Computer Modern
para derivados de latim que tem letras acentuadas. Outra opção é MLModern que é fonte
compatível com Computer Modern e Latin Modern, mas um pouco mais grossa, adequado
para livros eletrônicos. Para usar o MLModern, carregue o pacote mlmodern e para usar a fonte
Latin Modern, carregue o pacote lImodern no preamble do documento, como em
\usepackage{mlmodernY} % MLModern, com espessura Book.
% \usepackage(lmodern) % Latin Modern, com espessura igual a Computer Modern
tradicional.
Além de variantes do tradicional Conputer Modern, diversas combinações de fontes podem
ser escolhidas usando pacotes correspondentes. Aqui, veremos algumas entre muitas outras.
Fonte Times pode ser escolhido com
\usepackageTnewtxtext,newtxmath]>
A fonte Palatino com
\usepackageínewpxtext,newpxmath)
A fonte matemático em sans serif, compatível com o computer modern, ideal para
poster e slides.
\usepackageTlmodern) % computer modern com extensão para derivados ee latin
\usepackagetsansmath{onts} %fonte compatível com computer modern sans para
fórumulas matemáticas
\renewcommandí\familydefault+í\sfdefaultl% sans serif como padrão
Outra opção para poster e slides (tcxto e fórmulas em sans serif). Por ser espessura
“Book”, é mas legível do que uso de Imodern+sansmathfonts.
\usepackage [s{default} {notomath} % sffamily as \notosans
\ote que, o conjunto de fontes \oto ainda não tem fontes matemáticos serifados para
matemática (2024). Se não precisar de fórmulas matemáticas, poderá usar o pacote noto
para usar fontes noto.
Se quer usar a fonte sans serif na fórmula matemática (para uso em slides e poster),
poderá carregar o pacote sfmath ou similar para forçar a usar a fonte sans serif pra fórmulas,
mas nem todas fontes tem símbolos necessários em sans serif. Por isso, sífmath permite
usar fontes diferentes do texto na fórmula, através de opções.
Fonte Schoolbook L pode ser escolhdo por
\usepackage{mlmodern} % para complementar
\usepackageTtfouriernck % schoobook L: Serifa grossa?
A fonte stix (estilo compatível com Times \ew Roman)
\usepackagetnewtxtextl % para complementar
\usepackage{stixl} % compativel com \ew Times Roman
A versão nova da fonte stix pode ser carregado pelo pacote stix2 .
\ote que, para complementar a fonte com a outra, como do amssymb, deve carregar
o complemento antes do pacote de fonte desejado. Quando vários pacotes de fontes são
carregados e tiver conflitos, o que vale é do pacote carregado por último.
Também existem pacotes de fontes que acrescentam comandos para fontes adicionais. Por
exemplo, o pacote dsfont adiciona o comando \mathds para usar a fonte “negrito de quadro
negro” alternativo dentro das fórmulas. Da forma análoga, o pacote calligra acrescenta o
comando \textcalligra para textos na fonte caligráfica.
Para ver as fontes livres do BTFX e os pacotes correspondentes, veja o site http://www.
tug .dk/FontCatalogue/.
15.8 Texto somente com contorno, sombreado e degradê
No caso de cartazes e folhetos, as vezes usamos texto somente com contorno para títulos na
qual usa-se a letra grande. Uma forma fácil de fazer isso é usar o pacote contour que permite
criar um contorno no elemento. \eja o Exemplo 15.9.
Exemplo 15.9: exl5-contour.tex
\documentclass [12pt,a4paper] {article}
\usepackage [brazil] ({babel}
\usepackageTcontour+)
AlcontourlengthtoO.Spt) % controle da espessura do contorno
\beginfí{document}
TiHuge \contouríredH+í\lcolor{whitel}\scshape Atenção: )>
\endídocument )
ATENÇÃO:
Para sombrear o texto, costuma usar o pacote shadowtext. \eja o Exemplo 15.10.
Exemplo 15.10: exl5-shadow.tex
\documentclass [12pt,a4paper] {article}
\usepackage [brazil] {babel})
\usepackageTshadowtext]
\shadowcoloríblue!40!white)
Alshadowoffset{2ptr} % deslocamento da sombra
\begin{document}y
fiHuge \\shadowtextí\sffamily Atenção))
\endí{document}
Atenção
Para produzir o texto em degradê, existe o pacote novo chamado gradient-text
(https://www.ctan.org/pkg/gradient-text)que implementa a aplicação do gradiente li-
near no texto. Caso ele não for instalável pelo gerenciador de pacotes e não souber instalar
manualmente, basta abaixar o arquivo gradient-text.sty e deixar junto com o documento
TEX.
O gradient-text suporta somente o modelo de cor em RGB. Para usar outros modelos de
cores como pelo nome, poderá criar um novo comando com auxilio do \convertcolorspec do
pacote xcolor. \ote que, para que letras acentuadas sejam aceitas, requer XgLaTeX/LuaLaTeX.
\eja o Exemplo 15.11.
Exemplo 15.11: exl5-gradient.tex
\documentclass [12pt,a4paper] farticle>
\usepackage [brazil] {babel}
\usepackaget{xcolor}
\usepackageTgradient-{text}
/4 comando que aceita cor pelo nome
\nakeatletter
\newcommand{ \invertedOgradientRGB} [3] (\gradientRGBTtH3)(t1)(%2))
\newcommandfWgradienttextY[4] [named] (%
\convertcolorspec{t1}(t3)RGBYí\gradienttextOstartcolorYZ
\convertcolorspec{t1} t4) (RGBY) T \gradienttextOôendcolor) Z
\edef gradienttextOcolorsíflgradienttextOstartcolor-í\gradienttextOendcolor
-)
\expandafterVinvertedOgradientRGByWgradienttextecolors{t2}
º
\nakeatother
\beginfí{document}
Com cor em RGB: fWHuge \gradientRGBíTexto em degradê)to,255,0X10,0,255))
Com comando criado: fNHuge \gradienttextíTexto em degradêlfíorange!50!redkt
yellow-
\end{document}
Com cor em RGB: LEeXxto em degradê
Com comando criado: TGXtO em degradê
15.9 Circulando o texto
O ETEX implementa o comando \\textcircled para números/letras com círculos. O comando
básico é \textcircled que coloca circulo no seu argumento. \eja o Exemplo 15.12.
Exemplo 15.12: exl5-textcircled.tex
\documentclass [12pt,a4paper] {article}
\usepackageTtenumitem)
\beginf{document}
\textcircledílsmal112+H+\quadVWtextcircledílsmal1(A)Y
\begin{enumerate})
[1abel=Mlargelprotect \textcircled{lsmallVarabic*}]
\item First item
\item Second item
\\\item Third item
\end{enumerate})
\endídocument y
&SS
(D First item
(D Second item
(& Third item
Para controle mais sofisticado, existe um pacote novo circledtext (https://www.ctan.
org/pkg/circledtext).Caso ele não for instalável pelo gerenciador de pacotes e não sou-
ber instalar manualmente, basta abaixar o arquivo textcircled.sty e deixar junto com o
documento TEX.
\eja o Exemplo 15.13.
Exemplo 15.13: exl5-circledtext.tex
\circledtextsetíwidth=1em)
\documentclass [12pt,a4paper] {article}
\usepackageTtcircledtext) % tem o comando \lcircledtext
\ecircledtextsetíresize={real}
\usepackageTenumitem]y
\begin{document}
\circledtextsetíwidth=1em)
\circledtextí8kNquad
\circledtext{888}\quad
\circledtext*(8XNWquad
\eircledtext*(888)
Algumas alterações da configuração
\circledtext [boxtype=0] 112XYquad
\circledtext [boxtype=oo ]188INquad
\circledtext [boxtype=0o ]188)\quad
\circledtext [boxtype=00 ]í88SH+\quad
\circledtext*[boxtype=0oo ]{S8S}\quad
\circledtext* [boxtype=0o ]{8S}\quad
\circledtext* [boxtype=00 ]{8S}\quad
Alcircledtexrt [yscale=0.5] 1157
\circledtext [width=3em,height=1l1em] {abc}
\begin{enumerate}
[1label=AWprotect circledtextí\arabic*)]
\item First item
\item Second item
\\\item Third item
\end{enumerate})
\end{document}
Oooo
Algumas alterações da configuração
B F
7 0 E E o e
D First item
& Second item
& Third item
15.100 Escrevendo medidas internacionais
Para escrever medidas, requer alguns cuidados tais como usar letra romana reta (por ser
abreviatura da palavra), ter pequeno espaço entre valor e medida, entre outros. Por exemplo,
10kg e não 10kg, 5L e não 5! e assim por diante.
Para facilitar a escrever unidades de medidas corretamente no documento, o siunitx
providencia comandos para escrever na unidade internacional. \ormalmente (siunitx) usará
formatação usando a fonte do modo matemático, mas pode converter para usar a fonte do
modo texto com o comando \sisetupíunit-mode=text].
Para produzir o número rapidamente, tem o comando \num. O comando \ang gera ângulos
rapidamente. Para exemplos a seguir, será assumido que foi carregado o pacote siunitx no
preamble \eja o Exemplo 15.14.
Exemplo 15.14: exl5-num.tex
Números
\numí12345.67890) W % espacando de 3 em 3 casas
\numí12345,{67890} NW % ““,'' também pode ser usado para decimal
// +- é substituido por $\pm$
\complexnumíi +- 2i) W % t é núnmero complexo
\numí . 3e45) W % notacao cientifica
\numproductí1i.654 x 2.34 x 3.430) % ““x'' vira $l)times$
%4 valor monetaria costuma ser arredondado em duas decimais
& DE (Alemão) usa virgula para decimais também
RV$\num [locale=DE,round-precision=2,round-mode=places] £27 . 3671)
e
RA$\num [1ocale=DE,round-precision=2,round-mode=places] £15)
Ângulos
\ang{10} N % grau
\angí5.{3} NW % grau com decimal
\angí-1,5] NW % ““,"" também pode ser usado como decimal
