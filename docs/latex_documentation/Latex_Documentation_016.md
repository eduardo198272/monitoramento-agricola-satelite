No caso de querer usar as fontes da MicroSoft no MS \indows, coloque
\setmainfont [Ligatures=TeX] (Cambria)
\setsansfont{Calibri}Y
\setmonofont{Consolas}
\setmathfontíCambria Math)
no preamble.
Uma das dificuldades de usar fontes não padrão é saber as combinações adequadas (en-
tre romano, sem serifa, mono espaçado, etc), o que requer o conhecimento de tipografia e
diagramação. Para resolver este problema em XeLaTeX e LuaLaTeX, foi desenvolvido o pa-
cote fontsetup. O padrão deste pacote é usar a fonte \ew Computer Modern na espessura
Book adequado para livros eletrônicos e similares, mas existem muitas opções deste pacote
que configura para outras combinações das fontes pré estabelecidas. Por exemplo, a opção
stixtwo carrega a fonte STIX 2 que é do tipo times. \eja o documento do pacote fontsetup
para mais detalhes. Para usar fonte de espessura Book compatível com Computer Modern
no PDFLaTeX em vez de XqalATEX/LualTEX, carregue o pacote mlmodern para usar a fonte
MLModern.
O Exemplo 18.2 é um exemplo usando a fonte compatível com “Computer Modern”, mas
com espessura Book. Para PDFLaTeX, usa a fonte MLModern e para XeLaTeX/LualTEX, usa-se
a fonte \ew Computer Modern. À opção para tornar espessura compatível com o Conputer
Modern tradicional (para impressão em papel) está comentada.
Exemplo 18.2: ex18-fontsetup.tex
\usepackageTti{tex} % Para detectar o motor de TeX utilizado
% Fontes, de acordo com o motor do TeX
\ifPDFTeX % PDFLaTeX
\usepackage[T1] ({ontenc} % codificação da fonte em 8-bits
\usepackage{mlmodern} % fontes MLModern que é mais escura que Computer
Modern tradicional (espessura de letra de Book)
%\usepackagetlmodernk) % fontes Latin Modern: espessura tradicional do
Computer Modern
\else % XeLaTeX/LuaLaTeX
\usepackageí{ontsetup} % \ew Computer Modern com espessura da letra de Book
% \usepackage [oldde{ault} ({ontsetup} % espessura tradicional do Computer
Modern
vNfi
Para poster e slides, é recomendado que use a fonte sans serif. Para escolher o \ew
Computer Modern no estilo sans serif pelo pacote fontsetup, use a opção sansdefault.
Para PDFETEX, carregue o pacote sansmathfonts.
18.3  Usando em conjunto com BiblATEX
O documento em vários idiomas pode precisar também de referências bibliográficas em vários
idiomas. O BibLaTeX permite internacionalizar a referência bibliográfica (mesmo sem usar
XqLaTeX/LuaLaTeX).
Para especificar o idioma da referência bibliográfica no arquivo bib para BibllTEX, coloca-
se o idioma no campo langid de cada item. O “* romanized” é a escrita em alfabeto
romano caso o campo esteja em carácter que não seja alfabeto romano. Ele será usado para a
ordenação e similar. O campo “* translated <idioma>” é a tradução para o <idioma> se
as referências forem formatados para <idioma>. \eja o Exemplo 18.3.
Exemplo 18.3: ex18-biblatex.bib
Obookíwikibooks:latex,
LANGID = fenglishl,
author=í{wikibooks},
title=(1NLaTeX)),
publisher=fwikibooksk,
url = fhttps://en.wikibooks.org/wiki/LaTeX),
date = 12018),
urldate=12018-03-05)
1”
OBookí\awasaki,
LANGID = fjapanesel,
TITLE = (7S5 LT D KE RÉ LI,
TITLE romanised = íbara to origami to sugaku tol,
TITLE translated english = fíRoses, Origami N& Math),
AUTHOR = ()IIEBITOS,
AUTHOR romanised = fKawasaki, Toshikazuk,
PUBLISHER = (AILHIRHAEADBDA, Japank,
PUBLISHER translated english = (Morikita Syuppan Co. Ltd, Japan),
year=(1998),
ISBN = f4-627-01671-9)
D”
O comando de configuração para BibLaTeX é algo como
\usepackage [
% backend=biber, % padrão
language=auto,
% autolang=other, % for <otherlanguage> environment from babel and
polygrossia
% autolang=langname, /& only for polygrossia <language> env.
% bibencoding=utf8, % padrão
style=authoryear,
]{biblatex}
\addbibresourcefexi8&-biblatex.bibl) % arquivo bib
A opção language=auto indica que é para selecionar automaticamente o idioma (pelo
campo LANGID). Obviamente, onde quer que apareça a referência bibliográfica, coloca-se o
\phantomsection % se estiver usando hyperref
\printbibliography [heading=bibintoc]
\ote que, até agora, não usamos nada que não funcione no LaTeX normal. Mas como
a referência bibliográfica contém caracteres em japonês, precisará definir o uso de japonês
em algum trecho. Isto será facilitado se estiver usando X4LaTeX ou LualTEX em vez do
PDFLaTeX. Assim, vamos supor que está usando o XglLaTeX/LualáTEX para prosseguir com a
explicação. Para definir comandos para texto em japonês, coloque o comando
\usepackage [Ligatures=TeX] ({fontspec}
\usepackage{Tiffonty}
\def W jafontlistí\oto Serif CJK JP, MS Mincho, TakaoMincho, IPAexMincho,
IPAMincho, Hiragino Mincho Pro, [Imromani2-{regular} % último da list anão
é japonês
\def V.jagothicfontlistí\oto Sans CJK JP, MS Gothic, TakaoGothic, IPAexGothic,
IPAGothic, Hiragino Maru Gothic Pro)
\settofirstfoundífVjafontYí\ja{ontlist}
\settofirstfoundí\jagothickí\jagothic{ontlist}
% Se cair no último, fonte japonês não encontrado.
\\ifdefstringí\jafontYt[lImroman1i2-regular] \NWPackageWarningí\jobname)íFonte
japonês Mincho não encontrada.)íInstale um dos seguintes: \jafontlistk
newcommandfí\textja)[2] [] (41))
t%
\ifdefstrequalí\jagothickí\jafont Y \PackageWarningí\ljobnamek+íFonte japonês
Gothic não encontrada.YíInstale um dos seguintes: \jagothic{ontlist};)t>
\newfontfamilyí\ja{amily} [BoldFont=\jagothic] (\ja{ont})
\newcommandí\textja)[2] []€f€\ja{amily t2}>
H
O comando \jafamily será definido quando encontrar alguma fonte da lista. Também
será definido o comando \textja para trecho pequeno.
Agora, basta usar o comando para trocar de fontes padrão para a fonte japonês onde
aparece o texto em japonês. \eja o Exemplo 18.4.
Exemplo 18.4: ex18-biblatex.tex
Figura contendo texto em japonês.
\beginíffigure [hbtp!]
\center
\begin{tikzpicture}
\draw (0,0) circle(2) (0,1) nodefltextjatRÊ));
\draw (0,-0.5) circle(1) (0,-0.5) nodefltextja(úloARSr);
\end{tikzpicture}
\captioníFigura com texto em japonês)
\endí{igure})
Sobre uso básico do \texttt{biblatex}, veja o \citeíwikibooks:latex).
Agora, citando o livro em japonês \textjaflWciteí{lKkawasaki}).
Figura contendo texto em japonês.
Figuraq 1: Figura com texto em japonês
Sobre uso básico do biblatex, veja o wikibooks 2018. Agora, citando o livro em japonês
JNBAA 1998.
Como a referência bibliográfica contém texto em japonês, colocamos o comando de seleção
de fonte japonês.
\phantomsection % se estiver usando hyperref
fijafamily \printbibliography [heading=bibintoc] )
e a saída será
Referências Bibliográficas
[1] wikibooks (2018). BIKX. wikibooks. URL: https://en.wikibooks.org/wiki/
LaTeX (acesso em 15/03/2018).
[2] JTA (1998). 13 LÍ DAKE RÉ E . BPALEIRAABtE, Japan. ISBN: 4-627-
01671-9.
\ote que, no exemplo acima, a fonte de todo trecho da referência bibliográfica foi trocada.
Assim, se tiver letras acentuadas na referências bibliográficas que não existem nas fontes
japonesas escolhidas, terá problemas. Para contornar o problema, ou acentuar no modo TEX,
ou especificar o uso de japonês dentro do arquivo bib a cada trecho, em vez de aplicar no
\printbibliography.
No caso de escrever o documento em japonês ou similar, deverá carregar o pacote apropri-
ado que configurará para ambiente do idioma correspondente, ajustando os parâmetros para
particularidade daquele país. Além disso, com o uso do tal pacote, a troca de fontes para
japonês e vice versa será automática, sem a necessidade de estar especificando a família de
fontes a ser usadas a cada trecho.
Como observação final sobre XeLaTeX/LualTEX, os comandos protegidos dos pacotes de
XeLaTeX/LuaLaTeX costumam usar “ ” e “:”, em vez de “O” (ou ests caracteres em conjunto
com “O”). Isto foi introduzido no LaTeX pelo equipe de desenvolvimento LaTeX 3 e aparecem
nos pacotes mais recentes. Assim, para acessar estes comandos e ambientes protegidos no
preamble, deverá colocar entre \ExplSyntaxOn e \ExplSyntaxOff.
19. Diagramando na \orma ABNT 225
Capítulo 19
Diagramando na \orma ABNT
Neste capítulo, vamos estudar duas classes de documentos e suporte para a referência bi-
bliográfica, para diagramar de acordo com a exigência de Associação Brasileira das \ormas
Técnicas (ABNT).
19.1/ Documentos em ABNT
A classe padrão para diagramar os documentos como trabalho de conclusão de cursos, mo-
nografias em geral, teses e dissertações em ABNT é a classe abntex2 que foi implementado
sobre a classe memoir, herdando diversas funcionalidades. Para saber estas funcionalidades
adicionais, consulte o manual do memoir.
Para usar a classe abntex2 ([{Aral6a}, inicie com a linha como em
\documentclass [12pt,a4paper,openright,oneside,english,brazil]{abntex2}
onde 12pt é usado para ajustar o tamanho das letras, a4paper para papel A4 e oneside para
criar impressão de somente um lado para versão eletrônica. Se quer gear a versão impressa em
frente/verso no papel, coloque twoside e openright para ficar como frente/verso seguindo
a recomendação do ABNT (recomendação não é obrigatoriedade). Por último, english e
brazil foi colocado para ser repassado no pacote babel, pois ABNT requer que tenha resumo
na língua estrangeira (por exemplo, em inglês) além do resumo em português.
A classe abntex2 implementa diversos comandos para produzir elementos de acordo com
a exigência ou recomendações do ABNT. Alguns desses comandos possuem equivalência para
comandos da classe memoir e estão mapeados para poder usar tanto os comandos do memoir
como da própria classe abntex2 (por exemplo, \autor e \author, \titulo e \\\title, \data
e \date, etc), enquanto que existem comandos que equivalente do memoir produz estilo
diferente do exigido ou recomendado pelo ABNT (por exemplo, \inprimecapa e wnaketitle,
\apendices e \appendix). Assim, requer cuidados. Via das dúvidas, opte pelo comando em
postuguêns, implementado na classe abntex2.
A classe abntex2 faz a chamada de \frontmatter (ou \pretextual) no início do docu-
mento. Assim, não é necessário colocar este comando no começo do documento.
O Exemplo 19.1 ilustra o uso desta classe (com referências em BibLaTeX), com alguns
comentários importantes. AÀ sua saída será omitida aqui.
Exemplo 19.1: ex19-abntex2.tex
% \documentclass[12pt,a4paper,openright,twoside,english,brazil]{abntex2} %
impressão no papel
\documentclass [12pt,a4paper,oneside,english,brazil]{abntex2} % digital em
pdf
% Atenção: para compilara a referência bibliográfia, use biber e não o
bibtex
% latex
% biber
% latex
%
%ou
%
%lualatex
%Abiber
%Alualatex
\usepackageTi{tex} % Para detectar o motor de TeX utilizado
% Fontes, de acordo com o motor do TeX
\ifPDFTeX
\usepackage [T1] ({fontenc} % codificação da fonte em 8-bits
\usepackage{mlmodern} % fontes MLModern (espessura Book)
%\usepackagetlmodern) % fontes Latin Modern (espessura normal)
% \usepackage [ut{8} {inputencl} % acentuação direta em UTF-8. Não é mais
necessário
\else
\usepackageí{ontsetupl} ZÁ\ew Computer Modern com espessura Book
% \ote que a fonte padrão para XeLaTeX/LuaLaTeX é Latin Modern
\i
% pacotes matemáticas de acordo com o motor TeX
\\\ifPDFTeX
\usepackagefTamsmath,amssymbl % para matematica
\else
% para matematica
\usepackageTunicode-math>
\ifLuaTeX
\usepackageTlualatex-math>
\fi
\fi
%
\usepackage [overload] {textcasel} % para poder ter comandos de LaTeX/fórmula
no titulo
\usepackageTtmicrotypel % micro tipografia para ajuste refinado de
espaçamento
\usepackageThyperref) % para link automático no PDF
% Desabilitando ou redefinindo comandos que causa erros no bookmark do PDF
\pdfstringdefDisableCommandsí%
\let \MakeUppercaselrelax%, desabilitando
%Z W evand já é tratada adequadamente em ABNT2
D”
\usepackageíTpd{pages} % para incluir documento PDF (ex.: folha de aprovação)
\usepackage{tindentfirstl} % se quer que o primeiro parágrafo seja indentada
\usepackagef{csquotes} % biblatex recomenda quando usa babel ou proligrosia
% Com BibLaTeX (recomendado)
\usepackage [backend=biber, language=auto, style=abnt] (biblatex)
\addbibresourceímodelo-biblatex.bib) % arquivo bib
% para compatibilidade com documentos que usam com abntex2cite
% (compilar o documento que usa abntext2cite com biblatex sem alterar
comando de citação da referência biliográ{ica}
\nakeatletter
\eifpackageloaded{biblatex}t
MetWciteonlineltextcite
\letyapudonlineYtextapud
1)
\nakeatother
%% Se for criar o índice remissivo (opcional)
%\usepackage{makeidx}
%Amakeindex
%
\nakeatletter
% resolvendo o problema de gerar cabeçalho da página no sumário quando
tiver mais de uma página
\letWpsCabntheadingsoriginal psCabntheadings % copia do original
% Quando chamar \pretextual, configurar como empty
\AddToHookícmd/pretextual/be{ore}
ficlearpagelaliaspagestylelabntheadings+temptyl)
% Quando chamar \\textual, restaurar o estilo
\AddToHookícmd/textual/be{ore}
T{iclearpagelaliaspagestylefabntheadings}tabntheadingsoriginal))
%
% no cabeçãlho da página, fica "Capítulo no. nome". %4 deixar somente como "
no. nome" (sem o termo cap{tulo} para economizar espaço
% ajustando o \\chaptermarkí) e desabilitando o \sectionmarkíy>
\renewcommandí\chaptermarkY [1]1% remove o string 'Capítulo'
\narkbothfVWifemainmatter thechapter. \\{i H1}(\ifemainmatter thechapter. À
{i H1})
% Se dois lados, reativar o sectionmark
\ifetwoside%r
\renewcommandfí\sectionmarkY[111%
\narkright1\ifemainmatterNthesection. \\{it1})%
\fi
%
% ficha catalográfica não deve ser contada ABNT NBR 14724 (2024)
% caso de somente anverso ({rente} parece ser contada
\ifetwoside
\AddToHooktenv/fichacatalografica/a{ter}ílYaddtocounter{page}t-1XX %
retornar uma página
\i
\nakeatother
% linha orizontal na primeira página do capitulo também (caso não quer tal
comprtamento, comente)
\makeheadrule{abntchapfirst}í\textwidth)í\normalrulethickness)
% Para evitar o Overflow \hbox, podera usar \sloppy
\sloppy
% enumeração subordinado a capítulo
\numberwithinfequationY{chapter}
% permite quebrar equacoes entre linhas
\allowdisplaybreaks
% reduzindo o espaço entre numeração e titulo no sumário
% (para caso de ter somente capitulo e seção)
\setlengthfVYcftlastnumwidth+(2.5em) % do sumário de ABNTeX
% Dados para capa, folha de rosto, etc
\title{Exemplo de ABNTeX2} % ou NVtituloíy
% caso de mais de um autor, separe com o comando \and
\authoríSadao Massagol % ou \autoríy
\dateíDezembro de 2024) % ou \dataí)
\instituicaofDFQM-UFSCar) % Instituição
\localf{Sorocabal} % Local.
% Tipo de trabalho pode ser usado no preambulo e na ficha catalográfica
% "Tese (doutorado)", "Dissertação (mestrado)", "Trabalho de conclusão de
curso (graduação)", etc.
%ANtipotrabalhotMonogra{ia}
% Texto do tipo "Monografia apresentada à, como requisito parcial para a
obtenção do título de" impresso na folha de rosto e folha de
aprovação.
% Consultar a sua instituição para saber o texto correto.
%ipreambuloíTexto do tipo "“\imprimirtipotrabalhof) apresentada'' que
depende da instituição)
\preambuloíTexto do tipo ""Monografia apresentada'' que depende da
instituição)
\orientadoríNome do orientador)
%£\orientador [DOreintadora:] íNome da orientadora)
%£AVcoorientadoríNome dos coorientadores) % caso existam
%£Acoorientador [Coorientadora:]íNome das coorientadoras) % caso existam
% (Opcional): informações para PDF
% Precisa ajustar o pdfkeywords (palavras-chave) de acordo com o trabalho.
\hypersetupípdftitle={limprimirtitulo},
pdfauthor={\imprimirautor},
pdfsubject=(\{mprimirpreambulo},
pdfkeywords=(1ABNT, LaTeX, ABNTeX2)
”
% INICIO DO DOCUMENTO
\beginf{document}
\imprimircapa % Capa é obrigatória no ABNT (não use \maketitle)
% Observação: Se a capa não correspnder ao exigido, deverá criar manualmente
usando o ambiente 'titlepage'
\begin{titlepage}
capa formatada manualmente
\end{titlepage}
[X XNX
% Observação: Lombada (parte de trás do livro impresso) é opcional no ABNT e
não tem comandos específicos para ele no abntex2.
% Folha de rosto é obrigatório no ABNT
% versao ""*'' não pula página, permitindo adicionar ficha catalográfica no
verso
Se não tiver a ficha catalográfica (e se for impressão frente/verso), use
a versão sem *“*''
\imprimirfolhaderosto* % pule uma linha em branco (parágra{o} antes da ficha
catalográfica.
==
% Observação: Se a folha de rosto não correspnder ao exigido, deverá criar
manuaçmente (sem usar 'titlepage')
% \newpage
% folha de rosto formatado manualmente
% \newpage
% Ficha catalográfica, caso existir, deve ficar no verso da folha de rosto
\begin{fichacatalografica}
Ficha catalográfica provisória.
% Quando tiver versão definitiva, inserir aqui
% \includepdfífichacatalograficafinal.pdf)
\endí{ichacatalografica}
% Errata, caso existir
%begin{errata}
%úCaso exista errata. Opcional no ABNT.
%end{errata}
% Folha de aprovação é obrigatório no ABNT
\beginfí{olhadeaprovacao})
% provisória: \eja o código no manual do abntex2.
% quando tiver a folha de aprovação devidamente assinada, incluir aqui
% \includepdfífolhadeaprovacaofinal.pdf)
\endí{olhadeaprovacao})
% Dedicatória
%begin{dedicatoria}
%Dedicatória é um elemento opcional para ABNT.
19.1. Documentos em ABNT
%vend{dedicatoria}
% Agradecimentos
\begin{agradecimentos}
Agradecimentos é opcional no ABNT, mas boa educação é agradecer aos que
contribuíram para realização do trabalho.
\end{agradecimentos}
% Uma mensagem bonita e autor da mesnagem
%begin{epigrafe}
%Uma mensagem que é opcional no ABNT.
%vend{epigrafe}
% Resumo
\begin{resumo}Y
Resumo em português, obrigatório no ABNT.
\noindent
\textbfíPalavras-chave): ABNT, LaTeX, ABNTeX2.
\end{resumo}
% Resumo em linguagem estrangeira
\begin{resumo} [Abstract]
A I[{NMakeUppercasetAbstract}]
\begin{otherlanguagelfTtenglish}
Resumo em língua estrangeira (obrigatório no ABNT).
\noindent
\textbfí\eywords): ABNT, LaTeX, ABNTeX2.
\end{otherlanguage}
\end{resumo}
%ZiclearpagelthispagestylefemptyVWVcleardoublepage
% \phantomsectionWpdfbookmark [chapter] \l ist{igurename}(lofy
% Mistoffigures /& opcional no ABNT
%clearpagelWthispagestyletfempty H \cleardoublepage
%\phantomsectionlpdfbookmark [chapter] (\listfigurename+í(lot)
%listoftables % opcional no ABNT
%begin{siglas} % Lista de siglas é opcional no ABNT.
%\item[ABNT] Associação Brasileira de \ormas Técnicas.
%end{siglas}
Avbegin{simbolos}% Lista de Símbolos é opcional no ABNT
Aitem[$\pi$] Razão entre circunferência e raio.
r%end{simbolos}
% Sumário é obrigatório no ABNT
% A versão ""*'' remove a entrada "sumário" do bookmark do PDF e do sumário
\clearpageWthispagestylefempty+\cleardoublepage
\phantomsectionWpdfbookmark [chapter] fVcontentsnamel{tock} % adicionando ao
bookmark
\tableofcontents*
% CONTEÚDO PRINCIPAL
\clearpageWthispagestyle{empty}\cleardoublepage
\nainmatter % ou \\textual
% Como já é conteúdo textual, capítulos serão enumerados.
\chapteríPrefácio) % % prefácio (ou apresentação) é opcional no ABNT
Prefácio aqui. Se preferir, pode incorporar na introdução.
\clearpageWthispagestyletempty+\cleardoublepage
\chapteríIntrodução)
Introdução aqui.
\clearpageWthispagestylefemptyIYcleardoublepage
\chapteríCitações)
\begin{citacao}
As citações diretas, no texto, com mais de três linhas, devem ser destacadas
com recuo de 4 cm da margem esquerda, com letra menor que a do texto
utilizado e sem as aspas.
No caso de documentos datilografados, deve-se observar apenas o recuo
\apud[5.3] (NBR10520 : 2002 (book:abntex2:araujo)
% \eite[5.3] (NBR10520:2002].
\end{citacao}
\erb+\paudíl+ é para citação das citações.
% Em \apudíNBR10520:2002)íbook:abntex2:araujo)
% NBR10520:2002 é onde está escrito, enquanto que book:abntex2:araujo é quem
citou.
\beginf{citacao} [english]
Text in English with correct hyphenation and in italic.
\endí{citacao}
Observação: ""Citações simples, com até três linhas, devem ser
incluídas com aspas. Observe que em \LaTeX, as aspas iniciais são diferentes
das finais'' \citeíbook:abntex2:araujo).
Citações indiretas (reescritas) é formatado normalmente como um texto, mas
também precisam estar com fontes citadas.
Para citaçao de referências bibliográficas que faz parte do texto, use \verb
+itextcitell+ como em *"Segundo \textcitelbook:abntex2:araujol,''.
Análogo para \erbt+\lapudí)+ que deve usar \erb+\textapudíl+ quando faz
parte do texto.
\clearpageWthispagestyletlempty+\cleardoublepage
\chaptertAlí{neas}
Alíneas é uma subdivisão enumerada alfabeticamente para assuntos de texto,
pequeno demais para criar uma seção/subseção.
\isualmente, é uma lista enumerada alfabeticamente.
Cada alínea deve terminar em ponto e virgula, com excessão de últmo que é
ponto.
Uma subalíneas são divisões de alineas, mas não são enumeradas.
No ABNTeX2, alíneas e subalíneas são criados pelos ambientes \texttt{alineas}
e \texttti{subalineas} respectivamente, sendo seus elementos
especificados pelo comando \erbtVYitem+t como na lista.
\begin{alineas}
\item Primeira alínea;
\item Segunda alínea:
\beginf{subalineas}
litem alinea é enumerada alfabeticamente.
\item subalínea não são enumeradas.
\end{subalineas}
\endí{alineas}
\clearpageWthispagestylefemptyIVYcleardoublepage
\chapteríFonte de tabelas e {iguras}
A fonte de tabelas e figuras são colocadas embaixo, pelo comando \verb+y
fonte+
\beginífigureY [hbp!]
\center
\captioníImagem exemplo contido no pacote \\textttímwekWlabelífig:simples))
\includegraphics [width=O0.35)linewidth] lfexample-image)
\fontefCTAN -- \urlíhttps://ctan.org/))
\notafExemplo do pacote \textttímwell % nota é opcional no ABNT
\endí{igure})
No caso de subfiguras e sub tabelas, colocar fonte em cada uma delas, com À
verb+\fonte+.
Para tabelas curtas, use o comando \erb+\IBGEtabt+ do \\textttiABNTeX2)] como
na Tabela-\refítab:simples).
\beginíftableY[hbp!]
\IBGEtabí
\captioníTabela pequenaMlabelítab:simples))
H
\beginftabularY+fl1ry
\toprule
primeira coluna & segunda coluna N
teste & 123 W
\bottomrule
\endítabularY%\center
H
\fontefElaboração do autor)
\notaíTabela {luturante em conformidade com o ABNT} % nota é opcional no
ABNT
\lend{table}
\ote que o \erb+\IBGEtab+ não funciona na tabela longa ainda (2024). Além
disso, \textttTABNTeX2) ainda (2024) não tem o ambiente de \textttí
quadros) do ABNT.
Quem precisar de tabelas e quadros longos (e curtos), use o pacote como o À
textttitabularray-abnt) do \urlíhttps://ctan.org/pkg/tabularray-{abnt}.
\clearpageWthispagestylefemptyIYcleardoublepage
\chapteríConsiderações Finais)
Conclusão do trabalho.
% PÓS TEXTUAL
\clearpageWthispagestylefemptyIYcleardoublepage
\backmatter % ou o comando \postextual
4% Referencias bibliográficas é obrigatório no ABNT
%% Em geral, usa-se o BibLaTeX (ou BibTeX)
\printbibliography %& Com BibLaTeX
% Glossário é opcional no ABNT.
%clearpagelphantomsectionVladdcontentslinefttocl{chapter}+íGlossário) %
adicionando no sumário
% inserir glossário pelo comando de acordo com o pacote usado: pacotes mais
usados são acro e glossaries
% Apêndice é opcional no ABNT.
% Caso existir, inicio de apêndices será marcado com o comando \apendices
\clearpageVWthispagestylefemptykYcleardoublepage
\apendices % não usar o \appendix
\chapteríPrimeiro Apê{ndice}
Conteúdo do primeiro apêndice.
\clearpageWthispagestylefemptyIVYcleardoublepage
\chapteríSegundo Apêndice)
Conteúdo do segundo apêndice.
% Anexos são opcionais no ABNT
% Caso existir, inicio de anexos será marcado com o comando \anexos
\clearpageWthispagestylefemptyIYcleardoublepage
\anexos
\chapteríPrimeiro Anexo)
Conteúdo do primeiro anexo
\chapteríSegundo Anexo)
Conteúdo do segundo anexo
% Índice remissivo (opcional)
% NVelearpageVWthispagestylefempty+\cleardoublepage
% \printindex % Índice remissivo é opcional no ABNT
\endídocument y
onde o arquivo de referência bibliográfica usado modelo-biblatex.bib é como segue.
Obookíbook:abntex2:araujo,
author=(Lauro César Araujol,
title=(A classe abntex2: Documentos técnicos e científicos brasileiros
compatíveis com as normas ABNTJ,
url=fhttps://ctan.org/pkg/abntex2/),
lastchecked=(£2018-06-11),
urldate=12018-06-11),
year=2016
