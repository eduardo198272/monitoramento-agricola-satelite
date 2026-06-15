D.2. Gerando crachá pela mala direta 293
\w£fill
%4 corpo do certificado
\noindent
fiLarge
Certificamos que \\textití\MakeUppercaseWpersonname) apresentou o trabalho
intitulado \textitt""\worktitle'') no \\textscíNome do Congressol,
realizado no período de DATA, em LOCAL.Y
NW£fill
\begin{flushright})
TfiLarge LOCAL E DATA.Y
\endífflushrighty
\w£fill
% campo de assinatura, etc
\begin{minipage}tO.45\textwidth)
Realização: ORGANIZADORES
\end{minipage}
%
\begin{minipage}tO.45textwidthy
\centering \noindent
\underlinefVWhspace*f0.95 textwidth+] N
TfiLarge Comissão Organizadora)
\end{minipage}
\newpage
) % \DTLforeachflistar(%
\endí{document}
Um dos certificados gerados é como segue.
Universidade Federal de São Carlos
Centro de Ciências Tecnológicas e de Sustentabilidade
Departamento de Física, Quimica e Matemática
Certificado
Certificamos que NOME 1 apresentou o trabalho intitulado
“Trabalho 1º" no NOME DO CONGRESSO, realizado no período
de DATA, em LOCAL.
LOCAL E DATA.
Realização: ORGANIZADORES Comissão Organizadora
D.2. Gerando crachá pela mala direta 294
D.2 Gerando crachá pela mala direta
Crachá pode ser gerado pelo aplicativo de escritórios, mas aproveitando a mala direta visto na
seção de certificados, poderá gerar crachás usando o pacote ticket que gera cartão de visitas
e similares. Este pacote dispõe de dois comandos: \\ticketdefaultí) que determina o que
será colocado em todas crachás (por exemplo, nome do evento, logotipo, etc) e o comando
\ticket que determina como crachá será gerada. Como cada crachá é gerado pelo ambiente
picture, coloca os conteúdos pelo comando \put na posição desejada. \eja o Exemplo D.3.
Exemplo D.3: ex-d-cracha.tex
\documentclass [a4paper,11ipt]{article}
% cracha usando o pacote ticket e datatool
\usepackageTgraphicx>)
\usepackageíxcolor+)
\usepackagetrotating)
% paacote para gerar cartão de visitas e similares
\usepackage [rowmode,cutmark] {ticket}
% A4 = 210mmx297mm
%& lin = 24.5mm
%
% Definiçãao de dimensão e similares
\unitlength=1mm
% Cartão de visitaa internacional é 80mmx50mm (tamanho do cartão de credito)
Ahoffset=-0.5mm %42.5mm-1in
ANvoffset=-1mm %23.5mm-1in
ANticketNumbersí2Y+15)
AticketSizel80)(50) % in unitlength
AticketDistance(0)(o) Z% in unitlength
%44% Cartão de vista brasileiro é 90mmx5O0mm
ANhoffset=-9.5mm Zismm-1in
Avoffset=-I1mm %423.5mm-1in
%ticketNumbersí2+15)
ZticketSizel90)(50) % in unitlength
AticketDistance(o0)ToO) % in unitlength
%% Crachá CR-80 (internacional) é 8.6mmx5.4mm
\hoffset=-5.5mm Z1i9mm-1in
\offset=-11mm %13.5mm-1in
\ticketNumbers12Y(15)
\ticketSizeí8S6+(54) % in unitlength
\ticketDistance(0)TO0) % in unitlength
% Para todos (background/logo, etc)
% \ticketde{aulti} estará no ambiente picture
D.3. Caderno de resumos 295
\renewcommandí \ticketdefaultYT%
%\put (100, 5) flincludegraphics [width=35mm] logo)Y%
\put (20,45) íNome do EventoY%
\put (10,7) {Nbegintrotate} ( 90)\colorboxtblue! 50 fNWsffamilyNhuge Abrev.
EventolVendf{rotate})%
D”
% Cracha
% \ticketT) estará no ambiente picture
\newcommandfVconferencepinY[3] (\tickett%,
\put (20,15) fNWparbox(í7OVWunitlengthk{lcentering H1})%
\put (20,30) fNparboxt7OVunitlength+flcenteringí\bfseries larget2]NNt3)X%
+>
\usepackageí{datatool}
% Associa o nome 'namelist' ao arquivo
ADTLloaddb{namelist}í\jobname-dat.csv)
\DTLloaddbínamelistlílatex-via-exemplos-cracha-lista-participantes.csv)
\beginf{document}
% para cada linha do 'namelist'
\DTLforeach*fínamelistItZ Associar cada coluna do CSV no comando
\ame=\ame, \ountry=Country, \Institute=Institutelt%
\conferencepinfVInstitutel-lWame){NCountry}%Z gera cracha
d”
\endí{document}
Parte de cráchás gerados é como segue.
Nome do Evento Nome do Evento
Fulano de Tal
Brazil
Beltrano
Brazil
Instituto 1 Insituto 2
Nome do Evento Nome do Evento
Fulano 2
Brazil
Sicrano
Brazil
TInstituto 3 Instituto 1
D.3. Caderno de resumos 296
D.3 Caderno de resumos
Quando recebe vários artigos e quer “encadernar”, poderá usar a classe combine em vez de
gerar PDF de cada um e grudar. A classe combine agrupa os artigos automaticamente em um
único documento, gerando um “caderno” de artigos.
Para usar o combine, todos documentos que serão incluídos nele devem estar usando a
mesma classe que podem ser memoir, book, report, letter ou article. As classes não
suportadas oficialmente como o amsart pode precisar de ajustes manuais para funcionar
adequadamente.
\ote que wnaketitle ou titlepage é necessário. Se não existir, causa erros.
Para gerar sumário de artigos incluídos, carregue o pacote combinet. Para usar recursos
do natbib, carregue o pacote combnat no lugar de natbib.
O modo padrão é ignorar os pacotes carregados pelos artigos. Assim, todos pacotes
necessários devem estar carregados no arquivo mestre (arquivo do combine que vai incluir
artigos). É importante observar que na distribuição do TEX recente (2023), precisa efetuar
correção segundo https://tex.stackexchange.com/questions/591145/extra-endgroup-
error-when-using-the-combine-document-class que é colocar o código
\nakeatletter
\letWdocument cOladocument \begingroup
\makeatother
no preâmbulo do documento, após carregar todos pacotes desejados (após todos
\usepackage{T})). Para gerar o sumário com o pacote combinet que vem junto com a classe
combine, deverá ajustar o uso de \contentsline que agora tem 4 parâmetros. Para isso,
deve incluir o código
\nakeatletter
\renewcommandí \cOlaaddcontentsline)[3] 1%
\celaaddtocontents{t1}fNWprotectNcontentslineí(t2)(t3)(\thecolpage) ())
”
\nmakeatother
após \beginf{document}. \ote que o combine desativa a inserção de código em
\begin{document} e pacotes como geometry, babel, hyperref, etc não efetuam aplica-
ção de ajustes automáticos. Assim, deve aplicar os comandos adequados logo após o
\beginf{document}.
Vamos supor que artigos a serem incluídos são conferencial.tex, conferencia2.tex,
etc e têm a forma como no Exemplo D.4.
Exemplo D.4: ex-d-conferencial.tex
\documentclass [10pt,a4paper] {article}
% Este arquivo será processado automaticamente por um programa.
D.3. Caderno de resumos 297
% Por favor não altere nada no preamble (até \beginídocument+ ).
%\usepackage [english,brazil] {babel}
\usepackage [english] ([babel>
\usepackageTamsmath)
\usepackage{amssymb} % Ele carrega amsfonts também
\{usepackageTenumerate}
% Por favor não inclua outros "packages".
\beginf{document}
\itleíTítulo da Conferência 1)
\authoríAutor da conferência 1)
\naketitle
Texto da conferência 1
% Incluir bibliografia é opcional. Se decidir incli-lá, use o formato abaixo
%Zbeginfthebibliography+(99)
Abibitem{key1} Lamport, L. \emphíLaTeX: A Document Preparation System)k,
Addison-\esley, \textbf{11986}.
%endíthebibliography
\endí{document}
Então o caderno, pode ser criado como no Exemplo D.5.
Exemplo D.5: ex-d-caderno.tex
\documentclass [12pt,colclass=book] {combine}
% combine fixa o papel para a4paper
% combine suportam: memoir, book, report, and article
% Para criar o sumário automaticamente
\usepackageTcombinet]>
% Todos pacotes usados nos artigos a ser importados
\usepackageTamsmath)
\usepackage{amssymbl} % it's include amsfonts too
\usepackageTenumerate]
%ô\usepackage [english,brazil] {babel}
\usepackage [english] ({babel}
% packages usados somente no corpo de anais do congresso
\usepackageTgraphicx>)
% geometry pode ser usado, mas não consegue alterar o layout antes do \begin
tdcocument]
\usepackageTgeometry]
\usepackageThyperrefl/requer truque para funcionar no combine
% ATENÇÃO: aplicar este código de bug fix somente depois de incluir todos
pacotes desejados.
D.3. Caderno de resumos 298
% correção indicado em
% from https://tex.stackexchange.com/questions/655984/unable-to-combine-
multiple-documents-into-a-single-latex-document
\nakeatletter
\letWdocument \cOladocument \begingroup%/
\nakeatother
\sloppy % prefere underfull
% NVfussy %4 prefere overfull
% Mudar o nme do sumário
c%addtolcaptionsbrazilí\renewcommandí\contentsname|+íSumárioW (Contents))Y
\addtoWcaptionsenglishfWrenewcommandfí\contentsname-íSumárioW (Contents)))
% No combine, chamada de \maketitle é obrigatório.
% Assim, quando faz a capa manualmente, deverá desabilitar isto
\nakeatletterVcOlmtitlemptyWmakeatother
\beginí{document}
% início da configuração
% seleção de idiomas do babel não aplica automaticamente.no combine
%%iselectlanguaget{brazil}
\selectlanguage{tenglish}
% bugfix para combinet: adicona 40. parâmetro na chamada de \contentsline
% este código deve ficar depois do \begin{document}
\nakeatletter/ adjustando o comando de escrita do toc
\renewcommandf \cOlaaddcontentsline)[3] 1%
\ifxWecurrentHref \oempty
\cOlaaddtocontents{t1}+fNWprotectNcontentslineí(t2)(H3)(\thecolpage+ ())
\else % para uso de hyperref
\phantomsection
\cOlaaddtocontents{t1}fNprotecticontentslineí(t2)(H3)í\thecolpage+f
CcurrentHref))
\fi
d”
% hyperref (preparation)
\IfPackageLoadedTFíhyperrefYt/ require latex nov/2021
ANAfterBeginDocumentí%
\HyCAtBeginDocumentHookT|Y%
\let HyCAtBeginDocumentHookYOundefined
%X
H
\naKkeatother
% layout da página usando geometry (não consegue alterar o papel)
\newgeometryímargin=1.5cm)
% fim da configuração
% capa
\beginftitlepage
\begin{center})
D.3. Caderno de resumos 299
\thispagestyleífemptyl
\begin{flushleft}
\noindent
\unitlength=0.04 textwidth
\beginf{picture}(0,0)(2,33)
% \includegraphics [width=1.16textwidth] ({undo}
\end{picture}
\end{flushlefty}
fNLarge TÍTULO DO CONGRESSO) N
HOMENAGEM, ETC.
N£fill
Tflhuge Resumos de apresentações N
(Abstract o{ presentations} )
NW£fill
DATA
N£fill
LOCAL
NW£fill
\endf{center}
\end{titlepage}
% contra capa
\clearpage
\thispagestyle{empty}
\noindent
fibfseries Comitê Científico (Scienti{ic Comittee}) W
Membro 1 (Instituição 1) \W
Membro 2 (Instituição 2)
N
\noindent
Tlbfseries Comissão Organizadora (Organizing Comittee)) W
Membro 1 (Instituição 1) \W
Membro 2 (Instituição 2)
N
\begin{flushright})
\begintminipage)to. INtextwidth>
Realização (Hosted by): W
INSTITUIÇÕES
\end{minipage}
\endí{lushright}
\clearpage
\newpage
% Table of contents
D.4. Folhetos 300
% \pagestyleí{combine}
\pagestyle{plainy}
\tableofcontents
\clearpage
% Importa artigos de conferências
% Usar o comando \import em vez de \\\input ou \include
\beginf{papers}
\importícon{erencial}
\importícon{erencia2}
\endí{papers}
\endí{document}
\ote que combine fixa o papel em a4paper e \wnewgeometry não suporta alteraçao do
tamanho de páginas por estar após preâmbulo.
D.4 Folhetos
Poderá gerar os folhetos do tamanho A4 dobrado em três, usando a claasse leaflet que
pode ser usado como se fosse a classe article. O folheto é obtido, imprimindo frente/verso
virando ao longo da borda maior e dobrando em três.
No Exemplo D.6, foi usado o pacote l1ipsum para preencher o espaço com texto para ver
como fica a aparência do folheto. \ote que foi ativado a paginação para ver o fluxo.
Exemplo D.6: ex17-folder.tex
\documentclass [a4paper,12pt]ílea{let}
% Folheto tipo folder: imprimir frente/verso, virando na borda maior
\usepackagef{Thyperref} % para URL
\usepackageTtgraphicxl) % para incluir desenhos
\usepackagetqrcodel % para QR code
\usepackage{lipsum}
% Dados do titulo
\eitlel
% \unitlength=\linewidth
% \beginf{picture}(0,0)
% \put(-0.1,0)flincludegraphics [width=0.25)linewidth] (logo))
% NVendípicturelN
\textbfTUFSCar-So))
\authoríSadao Massago
\dateí2023>
D.4. Folhetos 301
\pagestyle{plain} % paginação ativa para ver o fluxo
\beginf{document}
\naketitle
Athispagestyle{empty}
\sectioníPrimeira seção)
\lipsum[5]
\sectioníSegunda seção)
\lipsum[1-2]
\sectioníTerceira seção)
\lipsum[3-4]
\sectioníQuarta seção)
\lipsum[1-2]
\sectioníQuinta seção)
\lipsum[4]
\sectioníSexta seção)
\lipsum[1-3]
\grcode [hyperlink] fhttps://ctan.org/pkg/lea{let})
\hreffhttps://ctan.org/pkg/lea{let}íhttps://ctan.org/pkg/lea{let}
\endí{document}
tesque à n is natoque penati-
bus
UFSCar-So
\icula. curs
tincidunt tris Sadao Massago
a formentum felis.
Sexta seção
pellentesque ante. Phasel 2023
us adipiscing semper elit. Proin fermentum
massa ac quam. Sed diam turpis, molestic
Maece-
vitae, placerat a, molestie nec, leo.
\am arcn libero,
cctetuer id, vulputate a,
Jouec vebicula augue eu -
habitant morbi tristique
malesuada
Primeira seção
nauris. \estibuloim luctus níbli at ec
. d bibendum. nulla & fancib
na. Integer non
u purus. Donec
eus quam, in hendrerit risus eros e
set erat in sapien mattis port-
porttitor. \ulla facilisi. Sod
icus comunodo facilisis. Morli
cibus. Morbi dolor nulla, m
inar at, mollis ac. nulla. Cur
per uulla,
diguissim
\aim dui euisinod sodales,
sollicitudin vel, wisi. Morbi auctor lorem non
justo. \am lacus libero, protium at. lobortis .
vitae, ultrícies ev, tellus. Donec aliq Segunda seção
tor sed accmmsan bibendum, erat H : s
q maa v Lorem ipsum dolor sit amet, conscetetuer
Morbi ac orei et nisl hendrerit mollis. Sus-
pendisse nt massa. Gras noc ante. Pellen-
adipiscing elit.
placerat ac, adipiscing v
D.5. Poster soisticado, revistas e brochuras 302
y & z
1o1paadum 10 resaodçd ueouoy su vm 19 snaoauas onbiastn iqfiom menqer onbsomua| 'TT9] timquatIO] PLIONÃ SNTAA “02aquy “onbiy
"T "onbon na antne vpanas somoq “eniem sin vmpronm e jedinjos mom antírios “quia
“g ozemndfna “pi tomogoo S119J 29M0( “Ureip 094110d Bpensofen elmo
ou5as va99I9],
mmproury o
SRA Cumsdi yessoejd sod
09 am s dojop umsdi
ov5os eumo oe59s exrend idm mmpnquiso:
'sumem sraony snsmo mo
a aodoourem am suteata, s
em «
u qu assipuad
tm v sam o
- e o
Jstmgorp vogud
3TdIpe : Tônogaos
t03 “aonbife 29u0( Snio4 “1 sotatnim “oena Top umsdi was07  soounm
SIn0qo[ "Y vmposd “osaqu snve{ rexy coisnf JMproUT} t98 aENA OISNf fan IMIOIN aqra
mon mo ame IMoJy “ISta “Joa TpGANTOS Serg  omsdh jersoed tadioomegm on
'sotepos pousmmo "é eMTu, ma
mp ex
S119J onbsogottod mnpngnsoa “unmio
aaegmdua mex T do 9900( Cstuao] avera
md gnsimo mogmy csnfos m on mmpasqi
jn 208 pro
01 A1fo 1odumos Susidipe snf v omemdina “pr sonTaasos 1989 Aurmaou
tozaqu 2M UN san upiaerÊ umorp
STM9UM BLIOAIA SEI) 00l e tumuonos
ÉG D SouVg \puNSSfUEI 19 Sugou PeSTHR o oubsogajiad Áumummon 2omog
D.5 Poster soisticado, revistas e brochuras
Para elaborar poster sofisticado, revistas ou brochuras que requrem disposição de elementos
de forma específica, poderá usar o pacote flowfram que permite definir uma espécie de “caixa
de textoo” nas páginas e diagramar dentro dele. Estas “caixas” são chamadas de frame.
O pacote fornece três tipos de frames. O primeiro delas é o frame estático (“static frame”)
que tem o contúdo fixo que pode ser colocado em todas páginas, ou nas páginas indicadas.
Por exemplo, o logo, o nome do trabalho e/ou da instituição, etc. podem ser colocados em
todas páginas com o frame estático. O segundo frame é o frame dinâmico (“dynamic frame”)
que é similar ao frame estático. A diferença é que no frame estático, o conteúdo é armazenado
dentro da caixa TÊEX, enquanto que o frame dinâmico, será armazenado dentro do macro
(comando), permitindo que o conteúdo possa refletir o contexto de cada página. Por exemplo,
se usar o comando \thepage dentro do conteúdo do frame dinâmico, poderá exibir a página
atual. Isto permite, por exemplo, criar um cabeçalho personalizado.
Tendo os elementos “fixos” pelo frame estático ou dinâmico, agora precisrá acrescentar o
conteúdo em si. Os conteúdos do documento são colocados dentro do frame denominado de
flow frame, que é uma “caixa” disposto igualmente em todas páginas ou nas páginas indicadas.
O Exemplo ?? é um exemplo simples do uso do pacote flowfram, mas que diferencia a
primeira página do restante.
Exemplo D.7: ex17-flowfram.tex
\documentclass [12pt] {articley}
% para cálculo das medidas
\usepackageíTcalc
% Paginas absoluto (página fisica e não a enumeração de 'page')
\usepackage [pages=absolute] {flowfram}
D.5. Poster soisticado, revistas e brochuras 303
% papel e margens
\usepackage [a4paper, margin=1lcm] {geometry}
% moldura diveros
\usepackageTtfancybox>
% para preencher o espaço
\usepackage{Tlipsum}
% titulo do trabalho
\newcommandí\worktitleY1%
\begin{minipage}[b] £O.7\textwidthy
fiHuge Exemplo de {lowfram} \par
TNLARGE por \emphíSadao Massagol)
\endíminipageY
º
% Medida de altura do frame de titulo
\newlength{\titleFrameHeight})
\setlengthfWtitleFrameHeightIYTVWheightofí\worktitlel)) % altura do titulo
% espaço entre frames na primeira página
\newlength{\firstFrameSep}
\setlengthfNWfirstFrameSep+(0O.5Scm)
% largura da frame lateral da primeira página
\newlengthfWsideFirstFrameWidthy
\setlengthfWsideFirstFrameWidthY{5cm}
% largural da frame pprincipal da primeira página
\newlength{\mainFirstFrameWidth}
\setlengthfWmainFirstFrameWidthkfNtextwidth - \sideFirstFrameWidth - À
{irstFrameSep}
% altura do frame lateral e principal da primeira página
\newlength{NWfirstFrameHeight})
\setlengthfVWfirstFrameHeightWtextheight-\titleFrameHeight - \V.irstFrameSep}
% definindo os frames
% syntaxe para staticframe (para dynamicframe e flowframe são análogas)
Anewstaticframeí<largura>í<altura>Yí<x0>Y(<y0>) [<rótulo>]
% (xO0, y0) é deslocament a partir do canto infeiror esquerdo
% frames fixos (da primeira página)
% staticframe será de conteúdo fixo e será colocado em todas páginas (ou nas
páginas indicadas)
% frame de titulos
\newstaticframe(\textwidthY(\titleFrameHeightYTOptHYí\textheight - À
titleFrameHeight)[titleFrame]
% frame lateral (da primeira página)
% versão star coloca moldura no frame
\newstaticframe*fWsideFirstFrameWidth+í\\{irstFrameHeight}{Opt}{opt}L[
sideFirstFrame]
% dynamicframe é similar a static frame, mas em vez de conteúdo ser
D.5. Poster soisticado, revistas e brochuras 304
armazenado em box, será armazenado em macros (isto pode ajustar ao
contexto).
% flowframe
% flowframe é para colocar o conteúdos principais
% pode ter mais de um flowframe por página
% versáão star, coloca moldura no frame
\new{lowframe*fWmainFirstFrameWidth}(í\firstFrameHeight Y \sideFirstFrameWidth
+ \firstFrameSepY+íOpt+[mainFirstFrame]
% versão star coloca moldura no frame
\newflowframefVtextwidthYfWtextheightíOptIíOptl[mainMajorFrame]
% conteúdo do staticframe
% versão star permite usar rótulo (nome) do frame em vez de índice (versão
sem star, usará o índice que inicia de 1)
\begin{staticcontents*}{titleFrame}
\iorktitle
\end{staticcontents*}
% Para que seja somente na primeira página (em vez de todas páginas),
configure o 'pages'. Poderá configurar a moldura também
\setstaticframe*ítitleFrame-ípages=(1),border=shadowbox)
% conteúdo do frame alteral da primeira página
\beginfstaticcontents*X{sideFirstFrame}
\lipsum[1]
W£fill - % para emppurrar teto para cima
\endí{staticcontents*}
% somente na página 1
\setstaticframe*(sideFirstFramelípages=11)>
% especificando as páginas que serão usados os flowframe's
% somente na página 1
\setflowframe*tmainFirstFrame-(pages=(T1),border=doublebox)
% somente na página 2 em diante
Zsetflowframe*{mainMajorFrame}ípages=(>1)>
\setflowframe*ímainMajorFrame-fexcludepages=tT1),border=doublebox)
% Alem de especificar páginas onde usar cada frames, poderá ativar/desativar
frame, atribuindo true/false no hide
% Poderá desabilitar os frames manualmente
Asetstaticframe*{mainMajorFrame}íhide={alse}
\beginí{document}
% os conteúdos digitados normalmente será colocado no flowframe, na ordem
que aparece. Quando todos flowframe de uma página ficarem cheios, será
criado nova página e segue normalemnte.
\lipsum[1-2]
% Para ir na próxima flowframe
% NVframebreak
% Para ir na próxima página manualmente
D.5. Poster soisticado, revistas e brochuras
\newpage
% Poderá habilitar os frames manualmente
%%setstaticframe*{mainMajorFrame}íhide=true)
\Mlipsum[1-2]
\endí{document}
Exemplo de flowfram
por Sadao Massago
Lorem ipsum dolor sit amet,
consectetuer adipiscing elit
Ut purus elit, vestibulum
ut, placerat ac, adipiscing
vitae, felis. Curabitur dic-
tum gravida mauris. \am
arcu libero, nonummy eget,
consectetuer id, vulputate
a, magna. Donec vehicula
augue eu neque. — Pellen-
tesque habitant morbi tris
tique senectus et netus et
malesuada fames ac turpis
egestas. — Mauris ut leo.
Cras viverra metus rhon-
ceus sem. \ulla et lectus
vestibulum urna fringilla ul-
tric Phasellus eu tel
lus sit amet tortor gravida
placerat. — Integer sapien
est, iaculis in, pretium quis,
viverra ac, nunc. Prae-
sent eget sem vel leo ultri-
ces bibendum. Aenean fau-
cibus. Morbi dolor nulla,
malesuada eu, pulvinar at,
mollis ac, nulla. Curabitur
auctor semper nulla. Donec
varius orci eget risus. Dui
nibh mi, congue eu, aceum-
san eleifend, sagittis quis,
diam. — Duis eget orci sit
amet orci dignissim rutrum.
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Ut purus elit,
vestibulum ut, placerat ac, adipiscing vitae, felis. Curabitur dictum gravida
mauris. \am arcu libero, nonummy eget, consectetuer id, vulputate a,
magna. Donec vehicula augue eu neque. Pellentesque habitant morbi tris-
tique senectus et netus et malesuada fames ac turpis egestas. Mauris ut leo.
Cras viverra metus rhoncus sem. \ulla et lectus vestibulum urna fringilla
ultrices. Phasellus eu tellus sit amet tortor gravida placerat. Integer sapien
est, iaculis in, pretium quis, viverra ac, nunc. Praesent eget sem vel leo
ultrices bibendum. Aenean faucibus. Morbi dolor nulla, malesuada eu, pul-
vinar at, mollis ac, nulla. Curabitur auctor semper nulla. Donec varius orci
eget risus. Duis nibh mi, congue eu, accumsan eleifend, sagittis quis, diam.
Duis eget orci sit amet orci dignissim rutrum.
\am dui ligula, fringilla a, euismod sodales, sollicitudin vel, wisi. Morbi
auctor lorem non justo. \am lacus libero, pretium at, lobortis vitae, ul-
tricies et, tellus. Donec aliquet, tortor sed accumsan bibendum, erat ligula
aliquet magna, vitae ornare odio metus a mi. Morbi ac orci et nisl hendrerit
mollis. Suspendisse ut massa. Cras nec ante. Pellentesque a nulla. Cum
sociis natoque penatibus et magnis dis parturient montes, nascetur ridicu-
lus mus. Aliquam tincidunt urna. \ulla ullameorper vestibulum turpis.
Pellentesque cursus luctus mauris.
D.5. Poster soisticado, revistas e brochuras 306
Lorem ipsum dolor sit amet, consectetuer adipis
adipiscing vitae, felis. Curabitur dictum gravida mauris
id, vulputate a, magna. Donec vehicula augue eu neque. Pellentesque habitant morbi tristique sene
et netus et malesuada fames ac turpis egestas. Mauris ut leo. Cras viverra metus rhoncus sem. \ulla
et lectus vestibulum urna fringilla ultrices. Phasellus eu tellus sit amet tortor gravida placerat. Integer
sapien est, iaculis in, pretium quis, viverra ac, nunc. Praesent eget sem vel leo ultrices bibendum. Aenean
faucibus. Morbi dolor nulla, malesuada eu, pulvinar at, mollis ac, nulla. Curabitur auctor semper nulla.
Donec varius orci eget risus. Duis nibh mi, congue eu, accumsan eleifend, sagittis quis, diam. Duis eget
Orci sit amet orci dignissim rutrum.
\am dui ligula, fringilla a, euismod sodales, sollicitudin vel, wisi. Morbi auctor lorem non justo.
\am lacus libero, pretium at, lobortis vitae, ultricies et, tellus. Donec aliquet, tortor sed accumsan
bibendum, erat ligula aliquet magna, vitae ornare odio metus a mi. Morbi ac orci et nisl hendrerit mollis.
Suspendisse ut massa. Cras nec ante. Pellentesque a nulla. Cum sociis natoque penatibus et magnis dis
parturient montes, nascetur ridiculus mus. Aliquam tincidunt urna. \ulla ullamcorper vestibulum turpis.
Pellentesque cursus luctus mauris.
cing elit. Ut purus elit, vestibulum ut, placerat ac,
\am arcu libero, nonummy eget, consectetuer
us
Para criar layout complexos para o uso do pacote flowfram que inclui caixas não retangu-
lares, ou disposição complexas, poderá usar o programa livre e multi plataforma flowframtk
disponível no site http: //www.dickimaw-books.com/latex/admin/html/flowfram.shtml
E. Para Professores 307
A º
Apêndice E
Para Professores
Agora será apresentado alguns pacotes úteis aos professores.
E.1 Cancelando ou anotando equações
Para cancelar parte das equações, use o pacote cancel.
\eja o Exemplo E.1 para ver o uso.
Exemplo E.1: ex-e-cancel.tex
\renewcommandfT \CancelColorYí\coloríredl+) Zcor de cancelamento pode ser
alterado
\\lx+\cancel12y) = z M
\lx+\bcancel(2y) = z N
\\lx+\xcancel(2y) = z NM
\lxtNWcancelto{o0X12y} = z NM
x +/?/Ú =2z
x +Ég( =z
E +M =z
o
t+ ?/f: z
Para efetuar anotações sobe equações, usa-se o pacote annotate-equations. \eja o
Exemplo E.2 para o uso.
Exemplo E.2: ex-e-annotate-equations.tex
\beginfequation*+y
\eqgnmark [blue] fnodei+í\intY
\egnmarkbox [red] {node2}(f (x))
