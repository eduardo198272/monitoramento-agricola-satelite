1”
Ocommentínote="URL: flurlíhttps://ctan.org/pkg/abntex2/X)",)
COmanual(íNBR10520 :2002,
Org-Short = T{ABNT},
Organization=(fAssociação Brasileira de \ormas Técnicas),
Title = (TABNT NBR) 10520:{2002},
subtitle=fInformação e documentação -- Citações
em documentos -- Apresentaçã{o},
address=(Rio de Janeiro)k,
pages=7,
year=2022,
”
\ote que a folha de aprovação provisória costuma estar presente no documento (é será
substituída pela {olha definitiva quando for aprovado}. Para criar uma folha de aprovação
provisória adequada, sugerido no manual do abntex2 [Aral6a] é
\beginfí{olhadeaprovacao}
% provisória
\begin{center})
TNABNTEXchapterfont {largeVimprimirautor}
\space*fNfillH+\vspace*fNfilly
\begin{center})
VABNTEXchapterfontWbfseries LargeVimprimirtitulo
\endf{center}
\space*fNfilly
\hspaceí.45\textwidth]y
\beginíminipagekt.SVWtextwidth)
\imprimirpreambulo
\endíminipagel%
\space*fNfilly
\end{center}
Trabalho aprovado. \imprimirlocal, 24 de novembro de 2012:
\assinaturafNWtextbfi{limprimirorientador} W Orientador)
\assinaturafNWtextbfíPro{essor} W Convidado 1)
\assinaturafNWtextbfíPro{essor} W Convidado 2)
\assinaturafNVtextbfíPro{essor}] W Convidado 3)
\assinaturafNWtextbfíPro{essor} W Convidado 4)
\begin{center}
\wspace*t0.S5Scm)
{MlargeVYimprimirlocal}
\par
{ilargeVimprimirdata}
\space*{1cm}
\end{center}
% quando tiver a folha de aprovação devidamente assinada
% NVincludepdfífolhadeaprovacaofinal .pdf)
\endí{olhadeaprovacao})
Após ter a folha de aprovação devidamente assinadas, digitalize e converta no formato PDF.
Em seguida, inclua diretamente no documento como uma página (e não como um desenho)
usando o comando \includepdf do pacote pdfpages.
ÀA classe abntex2 aceita a opção article para diagramar artigos, mas na maioria dos casos,
não é exigido que artigos sigam a norma ABNT, podendo ou não, requerer suas referências
em ABNT.
19.2 Documento ABNT usando ABNTexto
A classe ABNTexto ([{Abr24} que está na fase de desenvolvimento é uma alternativa leve para
ABNTeX2, para diagramar em ABNT. Enquanto que ABNTeX2 usa a classe memoir e diversos
pacotes para maior flexibilidade, ABNTexto usa a classe article e muitos poucos pacotes,
tornando mais leve. Caso não tenha a última versão instalada e queira usar sem instalar,
abaixe o arquivo abntexto.cls do CTAN (https://ctan.org/) e mantenha junto ao arquivo
.tex.
Um exemplo de ABNTexto com uso de BibLaTeX é como no Exemplo 19.2, cuja a saída é
omitida.
Exemplo 19.2: ex19-abntexto.tex
% Padrão para abntexto 2025-07-17 ou posterior
% Classe base: article
% pacote adicional: geometry, graphicx
% font size: 12pt
% twoside=true
%
% neste modelo, usa o layout de um lado
\documentclass [a4paper] labntexto)
\usechapters% ativar o uso de capítulos (ajuste ao sumário)
% O padrão é dois lados. Para um lado, ou modo eletronico (um lado com
margem menor), requer pequeno ajuste
% Em um lado somente
\letWtwosidelayout=\onesidelayout
% No formato eletronico (suas margens parece não ser de ABNT)
%ANletlonesidelayout=leletroniclayout% pretextual
ANletitwosidelayout=leletroniclayout% textual
\usepackageTi{tex} /% Para detectar o motor de TeX utilizado
% Fontes, de acordo com o motor do TeX
\ifPDFTeX % PDFLaTeX
\usepackage [T1] ({fontencl} % codificação da fonte em 8-bits
\usepackage{mlmodern} % fontes MLModern que é mais escura que Computer
Modern tradicional (espessura de letra de Book)
%usepackagetlmodernk) % fontes Latin Modern: espessura tradicional do
Computer Modern
%\usepackage [ut{8} {inputencl} % acentuação direta em UTF-8. Não é mais
necessário
\else % XeLaTeX/LuaLaTeX
\usepackageT{ontsetup} % \ew Cmputer Modern com espessura da letra de Book
% Padrão do XeLaTeX/LuaLaTeX
vNfi
% idiomas
\usepackage [english,main=brazil]íbabelY/ópadrão é brazil.
% pacotes matemáticas de acordo com o motor TeX
\ifPDFTeX
\usepackagefTamsmath,amssymbl % para matematica
\else
% para matematica
\usepackageTunicode-math]>
\ifLuaTeX
\usepackageTlualatex-math>
\fi
\fi
%Outros pacotes
\usepackageThyperref) % para link automático no PDF
% Desabilitando ou redefinindo comandos que causa erros no bookmark do PDF
\pdfstringdefDisableCommandsí%
\let \MakeUppercaselrelax%, desabilitando
\defNWt 3%
\deflandf e >
DP
\usepackageíTpd{pages} % para incluir documento PDF (ex.: folha de aprovação)
\usepackage{tindentfirst} % se quer que o primeiro parágrafo seja indentada
%% Se for criar o índice remissivo (opcional)
%\usepackage{makeidx}
%makeindex
\usepackageímicrotypel % micro tipografia para ajuste refinado de
espaçamento
\usepackageíxtabl % para tabela longa configurável xtabular
% Para linhas horizontais com espaçamento melhorado: NVtoprule, \midrule, À
bottomrule, \cmidrule
\usepackageTbooktabs)
% BibLaTeX
\usepackage{tcsquotes} % biblatex recomenda quando usar o pacote de idiomas
babel /poligrossia
\usepackage [backend=biber, language=zauto, style=abnt] {biblatex}
\addbibresourceímodelo-biblatex.bibl % arquivo bib
%Zvaddto{lcaptionsbrazil}+f
% \renewcommandfVWrefnameYíReferências)
%>
% Mesmo com \usechapters do ABNTexto, tamanho das fontes do título da
referências bibliográficas e similares ficam como seção. Para ser de
capítulo, precisa de ajustes usando comando de abntexto.
\defbibheading{bibliography} [\re{name} (\\\chapter*+{t1}>
\nakeatletter
% Índice remissivo
\AddToHookítenv/theindex/begin)í\beginf{corrprint})
\AddToHookfífenv/theindex/endkYfYend{corrprint})
% referências bibliográficas
\AddToHookífenv/thebibliography/beginYí\begint{corrprint})
\AddToHookíTenv/thebibliography/endk(í\end{corrprint})
% Glossário com pacote glossaries
\AtBeginDocumentíVNCifpackageloaded{glossaries}í
\AddToHookícmd/printglossary/before+í\begin{corrprint}Y
\AddToHookícmd/printglossary/after+í\end{corrprint}Y
J) /NCifpackageloaded ZNAtBeginDocument
% Glossário com pacote acro
\AtBeginDocumentTVNCifpackageloaded{acro}t
\\AddToHookícmd/printacronyms/be{ore}{\beginfcorrprint})
\AddToHookícmd/printacronyms/a{ter}fVYend{corrprint})
) ZNCifpackageloaded /NAtBeginDocument
\nakeatother
% versão * do capítulo/seção não tem no ABNTexto.
% No ABNTexto, será \\clearpageWnonuminotocWchapterfVYcentering |) ou \nonumy
notoclsectionflcentering
% Providenciando versão * pela praticidade em usar no conteúdo pretextual (
ABNT: deve ser centralizada)
\nakeatletter
\letWchaptereênostarWchapter% copiando o original
\def |chapter T NCi{starNchapterOstarWchapterCnostar})
\defWchapterOstart11% com *
\cleardoublepage
\nonuminotocYchapterOênostarílcentering t1)
+
% Para artigos
%ZNletisectionOnostarlsection% copiando o original
Adefisectionfleifstar|sectionôstar sectionCônostar)
%\defisectioneOstarti1(TZ com *
% \nonuminotocysectionônostarfílcentering t1)
.
\nakeatother
% informação do documento (requer o pacote hyperref)
\hypersetupípdftitle={Exemplo de ABNTexto},
pdfauthor=(Sadao Massago),
pdfsubject=(íExemplo do documento em ABNT com a classe ABNTexto),
pdfkeywords=(1ABNT, LaTeX, ABNTextol
”
\sloppy % preferência a underfull (muito espaço entre palavras)
% enumeração subordinado a capítulo
\numberwithin{equation}í{chapter}
% permite quebrar equacoes entre linhas
\allowdisplaybreaks
% INICIO DO DOCUMENTO
\begin{document}
\begin{titlepage}
UNIVERSIDADE FEDERAL DE SÃO CARLOS NW
CENTRO DE CIÊNCIAS E TECNOLOGIAS PARA SUSTENTABILIDADE
\begin{center})
N£ill
\Large SADAO MASSAGO
\w£fill
TNHugeVWbfseries EXEMPLO DE ABNTEXTOY
\f£il1l
SOROCABA NV
AGOSTO DE 2025
\end{center}
\end{titlepage}
\pretextual % pretextual é iniciado automaticamente?
% Folha de rosto é obrigatório no ABNT
\begin{center})
N£fill
Sadao Massago
\w£fill
{iLargeWbfseries Exemplo de ABNTexto}
N£ill
\begin{flushright}\begin{minipage}tO.SYtextwidth)
\noindent% sem indentação
\singlesp % espaçamento simpoles, usando o comando de ABNTexto
Texto do tipo ““Monografia apresentada que depende da instituição
\endíminipage-\endí{lushright})
\f£il1l
Universidade Federal de São Carlos N
Centro de Ciências e Tecnologias para Sustentabilidade
\w£fill
Orientador(a): Nome do(a) orientador(a)
\w£fill
SorocabaWY
Agosto de 2025
\endícenter+
%h% Ficha catalográfica, caso existir, deve ficar no verso da folha de rosto
%inewpage /& Quando tiver versão definitiva, inserir aqui
%Zincludepdfífichacatalograficafinal.pdf)
%
%úCaso exista errata. Opcional no ABNT.
%AVchapter*{Errata}
%
\newpage
Folha de aprovação é obrigatório no ABNT
%% Quando tiver a folha de aprovação devidamente assinada, incluir aqui
%44 NVincludepdfiífolhadeaprovacaofinal.pdfy
%
%chapter*t1>
%CóDedicatória é um elemento opcional para ABNT
%
\chapter*(]>
Agradecimentos é opcional no ABNT, mas boa educação é agradecer aos que
contribuíram para realização do trabalho.
%
%Achapter*(>
%epigrafe (uma mensagem) que é opcional no ABNT. Deverá colocar o autor da
mensagem, alinhada a direita.
%
\chapter*(Resumo]
\noindent Resumo em português, obrigatório no ABNT.
\noindent
\textbfíPalavras-chave): ABNT, LaTeX, ABNTexto.
%
\chapter*í{Abstract} %Resumo em língua estrangeira (obrigatório no ABNT).
\begin{otherlanguagelTtenglish}
\noindent Abstract in foreign language is required in ABNT.
\noindent
\textbfí\eywords): ABNT, LaTeX, ABNTexto.
\end{otherlanguage}
%
%iclearpagephantomsectionWpdfbookmark [chapter] [\l ist{igurename}Tlofy
%AVchapter*íLista de Figuras)% opcional no ABNT
%"makeextílofy
%
%Ziclearpagephantomsectionlpdfbookmark [chapter] [\l ist{igurename}Tlot)
%ichapter*íLista de Tabelas) % opcional no ABNT
%" makeext{lot}
%
% \clearpage
sAchapter*(Siglas) / Lista de siglas é opcional no ABNT.
Avbegin{description}
%CVitem[ABNT] Associação Brasileira de \ormas Técnicas.
%vend{description}
%end{siglas}
%
% \clearpage
%ichapter*{Simbolos}% Lista de Símbolos é opcional no ABNT
%\begin{description}
Aitem[$\pi$s] Razão entre circunferência e raio.
%Aitem[ABNT] Associação Brasileira de \ormas Técnicas.
%vend{description}
%
\clearpage
% \section*íSumário) % artigo
\chapter*íSumário)
\naketoc % produz sumário. Não use \tableofcontents
% CONTEÚDO PRINCIPAL
\clearpage
\textual MetlWtextual=\relax%4 iniciando o textual e desativando o comando
%
% Como já é conteúdo textual, capítulos serão enumerados.
\chapterfPrefácio) % prefácio (ou apresentação) é opcional no ABNT
Prefácio aqui. Se preferir, pode incorporar na introdução.
\clearpage
\chaptertIntroduçã{o}
Introdução aqui.
\clearpage
\chaptertAl{neas}
Alineas é criado pelo ambiente \textttí{topics}.
\begin{topics}
\item MVlabelfalinea:1) ítem 1
\begin{topics})
\item subítem a
\item subítem b
\end{topics}
\item MVlabelfalinea:2) ítem 2
\endí{topics}
\clearpage
\chapter{Legenda}
O comando \verb+\legend+ especifica se vai ser figura ou tabela e cria a
legenda (t{tulo}.
Deve respeitar a ordem dos comandos \verb+\legend+, \verb+\src+ e \verb+
beginíplacelt+. A opção de posicionamento é mesmo de figuras/tabelas
flutuantes \\textttí{igure}/\texttt{table},adicionado de uma opção 'here'
que fixa no lugar como a opção 'H' do pacote \\textttí{loat}).
\legendífigurelíUma {igura}
\srcíCTAN: \urlíhttps://ctan.org/X)
\labelífig:teste)
\beginfíplace+[hbp!] % opção de posicionamento é mesmo de figure/table
\includegraphics [width=0.4)]linewidth] fexample-image)
\end{place}
\er \refífig:teste).
Poderá usar subfiguras nativamente como na Figura-\refífig:teste2) (Figura-
refífig:teste2:a) e \refiífig:teste2:b)).
\legendífigurekíDuas {iguras} Mlabelífig:teste2)
% \srcíCTAN: \urlíhttps://ctan.org/))
\beginímultiplaceY% [here] % 'here' (padrão) fixa no lugar como 'H' do
pacotee float
\sublegendí{igure}{Normal}
\subsrcíCTAN: \urlíhttps://ctan.org/))
\labelífig:teste2:a)
\begin{subplace}
\includegraphics [\idth=0.4)]linewidth] fexample-image-a)
\end{subplace}
% figura 2
\sublegendfí{igure}{Rotacionada}
\subsrcíCTAN: \urlíhttps://ctan.org/X)
\labelífig:teste2:b)
\beginí{subplace}
\includegraphics [width=0.4)linewidth,angle=45] fexample-image-a)
\end{subplace}
\end{multiplace}
A tabela pequena pode ser inseridas de forma análoga a da figura, mas deve
usar o comando \erb+\legend+ devidamente com opção 'table'.
\begin{center}
\legendítable+íiUm títulolkNMlabelítab:primeira)
\srcíElaboração do autor.)
\beginf{place} [here]l% 'here' (padrão) fixa no lugar como 'H' do pacote float
\beginftabular+(11)
\toprule ZWhline
produto & preço N
\wnidrule ZNhline
cenouras (500g) & RNA$0,50 W
cogumelos (vidro de 500g) & RN$5,00 W
batata (1\g) & RN$1,20 W \midrule % \hline
total & RA$6,70 \W
\bottomrule /\hline
\end{tabular}
\endí{place}
\end{center}
Não há suporte para tabelas longas (2025). Também não há suporte para
quadros ainda (2025).
Quem precisar de tabelas e quadros longos (e curtos), use o pacote como o À
textttítabularray-abnt) do \urlíhttps://ctan.org/pkg/tabularray-abnt).
\clearpage
\chapteríCitações)
Para citações curtas, use \erbt+\enquotefítextokYcite{key}+.
Para citações longas (mais de 3 linhas), use
\verb+\lEnquotefttextolcitef{key})+ (com ""E'' maiúsculo).
Por exemplo,
\\\Enquotet
As citações diretas, no texto, com mais de três linhas, devem ser destacadas
com recuo de 4 cm da margem esquerda, com letra menor que a do texto
utilizado e sem as aspas.
No caso de documentos datilografados, deve-se observar apenas o recuo
\apud[5.3] (NBR10520:2002)fbook:abntex2:araujo)
% \eite[5.3] (NBR10520:2002].
) %Enquote
\verbt+lpaudíl+ é para citação das citações.
% Em \apudíNBR10520:2002)íbook:abntex2:araujo)
% NBR10520:2002 é onde está escrito, enquanto que book:abntex2:araujo é quem
citou.
\enquotetíCitações simples, com até três linhas, devem ser
incluídas com aspas. Observe que em \LaTeX, as aspas iniciais são diferentes
das {inais} \citefbook:abntex2:araujo).
Citações indiretas (reescritas) é formatado normalmente como um texto, mas
também precisam estar com fontes citadas.
Para citaçao de referências bibliográficas que faz parte do texto, use \verb
+\textcitell+ como em * "Segundo \textciteíbook:abntex2:araujok,''.
Análogo para \erb+\apudíl+ que deve usar \erb+\textapudíl+ quando faz
parte do texto.
\clearpage
\chaptertConsiderações Finais)
Conclusão do trabalho.
% PÓS TEXTUAL
%% Referencias bibliográficas é obrigatório no ABNT
\clearpageWphantomsectionVaddcontentslineítockY{chapter}flWprotectNtoclabelbox
TINrefnameY%
\printbibliography/sem opção, para devido funcionamento em ABNTexto
%h glossário é opcional no ABNT
%clearpagelphantomsectionVladdcontentslinefítoclíchapter+í\protect
toclabelboxtHNglossaryname)%,
% inserir glossário pelo comando de acordo com o pacote usado: pacotes mais
usados são acro e glossaries
%4hóApêndices são opcionais no ABNT
%iclearpage
%appendixíPrimeiro Apê{ndice}
%Conteúdo do primeiro apêndice.
%iclearpage
%vappendixíSegundo Apêndice)
%Conteúdo do segundo apêndice.
%% Anexos são opcionais no ABNT
%clearpage
%vannexíPrimeiro Anexo)
%Conteúdo do primeiro anexo
%vannexíSegundo Anexo)
%Conteúdo do segundo anexo
%% Índice remissivo (opcional no ABNT)
% \clearpageWphantomsectionladdcontentslineftock{chapter}fNprotect
toclabelboxtí\indexname),
% \printindex
\endídocument
onde o arquivo de referência bibliográfica usado é mesmo do Exemplo 19.1 que é modelo-
biblatex.bib.
O ABNTeX2 é mais completo, mas por basear na classe memoir e carregar diversos pacotes,
torna mais pesado. Por outro lado, abntexto é baseado na classe article e depende de
poucos pacotes, o que torna leve, apesar de ter menos recursos. Outra observação é que
ABNTeX2 implementa comandos e ambientes em português, enquanto que abntexto imple-
menta comandos e ambientes em inglês.
19.3 Usando o estilo ABNT no BiILaTeX
\ote que, o recomendado é usar o BibLaTeX em vez de BibTeX para o caso do estilo ABNT,
pois a versão em BibTeX não implementa atualizaçao recente do ABNT e não tem plano para
que isto seja feita. Mas será apresentado aqui para quem pretende usar com o BibTeX mesmo
assim.
Quando as referências bibliográficas devem seguir a norma ABNT, e pretende usar o
BibTEX, use o pacote abntex2cite que pode ser usado separadamente da classe abntex2. É
importante lembrar que este pacote requer que o pacote hyperref seja carregado antes dele.
Caso contrário, pode produzir erros, mas não costuma ser avisado de que hyperref precisa
ser carregado antes.
A citação entre parentes deve ser feito com o comando \cite, enquanto que a citação como
parte de texto deve ser feito com o comando \citeonline. As citações de citações (citações
indiretas) são feitas pelos comandos \apud ou \apudonline para colocar entre parenteses ou
fazer parte do texto, respectivamente.
\ote que o pacote abntex2cite requer a codificação do documento em utf8, o que é
padrão no sistema TEX atual.
\eja o Exemplo 19.3.
Exemplo 19.3: ex19-abntex2cite.tex
\documentclass [12pt,a4paper,english,brazil]í{article}
\usepackage{tiftex} % Para detectar o motor de TeX utilizado
\ifPDFTeX% Fontes, de acordo com o motor do TeX
\usepackage [T1] {fontenc} % codificação da fonte em 8-bits
\usepackage{mlmodern} % fontes MLModern
%\usepackagetlmodern) % fontes Latin Modern
%\usepackage [ut{8} {inputencl} % acentuação direta em UTF-8 % não é mais
necessário
\else
\usepackageT{ontsetup}/4 \ew Computer Modern
%\usepackageí{ontspec} % pacote para configurar fontes
%defaultfontfeaturesíLigatures=TeX)
% seleção de fontes, se desejar
E
vfi
% pacotes matemáticas de acordo com o motor TeX
\ifPDFTeX
\usepackage{amsmath,amssymbl} % para matematica
\else
% para matematica
\usepackageTunicode-math]>
\ifLuaTeX
\usepackageTlualatex-math>
\fi
\fi
\usepackage{babel} % idiomas da opção da classe será usado aqui
\usepackageThyperref)/ abntex2cite requer hyoerref carregado antes dele
% Opção "alf" é para alfabetico. "num" para numérico.
\usepackage[alf] {abntex2citel} % Para citação no formato ABNT
\pdfstringdefDisableCommandsí/ desabilitando comandos proibidos no bookmarks
\let MakeUppercaselrelax%
\defWWt Y%
d”
\begin{document}
Este modelo foi baseado no documento de \texttt{abntex2} \citeíbook:abntex2:
araujok.
Para citações textuais, deverá usar o comando \erbtWciteonlinet+ como
descrito em \citeonlineíbook:abnt2cite:araujo).
Para citações de citações, usar o comando \erb+\apud+ ou \verbt+\lapudonline+.
Também poderá usar o \texttt{biblatex}. \eja o \citeonlineíbook:biblatex-
abnt:marques) para detalhes.
% Especificacao de formatacao (\bibliographystyle) não será necessário, pois
o pacote anbtex2cite já fez isso.
\bibliographyfexi9-abntex2cite)
\endídocument
Para os documentos disponíveis na internet, complete os campos ur1l (endereço eletrônico)
e urlaccessdate (data de última consulta). Os campos isbn (identi{icador de livros} e issn
(identificador de periódicos) também estão disponíveis.
Também observe que no ABNT, foram acrescentados categorias adicionais e por conta
disso, o estilo abnt adicionou essas categorias que podem ser ignorados nos outros estilos de
formatação. \eja [Aral6b] para detalhes.
O arquivo ex1i9-abntex2cite.bib é como segue
Obookíbook:abntex2:araujo,
author=(Lauro CVY'esar Araujo),
title=(fA classe abntex2: Documentos tY'ecnicos e cientí\V'\ilkficos
brasileiros compatíVW'\ilveis com as normas (TABNTJ)),
url=fhttps://ctan.org/pkg/abntex2/]),
urlaccessdate=12018-06-{11},
year=2016
D”
Obookíbook:abnt2cite:araujo,
author=(Lauro CY'esar Araujol,
title=(O pacote abntex2cite: Estilos bibliogrV'aficos compatíV'\ilkveis com a
TABNTY ÍNBRY 6023),
url=fhttps://ctan.org/pkg/abntex2/),
urlaccessdate=12018-06-11%,
year=2016
”
Obookíbook:biblatex-abnt:marques,
author=íDaniel Ballester Marques),
title=(fbiblatex-abnt 3.3),
url=fhttps://ctan.org/pkg/biblatex-abnt/]),
urlaccessdate=12018-06-{11},
year=2018
D”
No exemplo, foi usado a acentuação pelo comando TEX para a compatibilidade com o
sistema TEX antigo (anterior a 2018).
A saída do Exemplo 19.3 e algo como segue.
Este modelo foi baseado no documento de abntex2 (ARAÚJO, 2018a).
Para citações textuais, deverá usar o comando \\citeonline como descrito em Araújo
(2016b). Para citações de citações, usar o comando \apud ou \apudonline.
Também poderá usar o biblatex. \eja o Marques (2018) para detalhes.
Referências
ARAUJO, L. C. A classe abntex2: Documentos técnicos e científicos brasileiros compatíveis
com as normas ABNT. |s.n.], 2016. Disponível em: <https://ctan.org/pkg/abntex2/>.
Acesso em: 2018-06-11.
ARAUJO, L. C. O pacote abntex2cite: Estilos bibliográficos compatíveis com a ABNT
NBR 6028. |s.n.], 2016. Disponível em: <https://ctan.org/pkg/abntex2/>. Acesso
em: 2018-06-11.
MARQUES, D. B. biblatex-abnt 3.3. [s.n.]), 2018. Disponível em: <https://ctan.org/
pkg/biblatex-abnt/>. Acesso em: 2018-06-11.
19.4 Usando o estilo ABNT no BiblkTEX
Para elaborar a referência bibliográfica no estilo ABNT, é recomendado usar o BibLaTeX
([{Mar18}.
Para isso, coloque a opção style=abnt na opção de chamada do pacote biblatex.
A data de último acesso ao material disponível na internet será colocado no campo
urldate do arquivo .bib no formato ano-mes-dia onde ano será com 4 dígitos. \ote que
urlaccessdate usado pelo BibTeX também funciona no BibLaTeX, mas urldate podem ser
usados em vários estilos e não somente no estilo abnt. Caso queira usar tanto o BibTeX,
assim como BiblKTEX, poderá especificar ambos os campos (e usar a acentuação no modo
TEX, caso queira usar o sistema TEX anterior a 2018).
No estilo ABNT de BibTeX do pacote abntex2cite, usa o \citeonline para citações
textuais, mas no estilo ABNT de BibLaTeX, usa o comando \textcite já existentes no
BibLaTeX. Se no documento estiver usando o comando \citeonline, basta criar um atalho
no preamble do documento com MletYciteonlineVWtextcite. Por outro lado, se quiser usar
o \textcite com abntex2cite, prevendo a futura transição para BiBLaTeX, basta colocar
\letYtextcitelciteonline no preamble do documento.
\ovamente, use a codificação em utf8. \ote que o BIiblTEX aceita a acentuação direta
no arquivo de BibTeX. O uso de hyperref é opcional, mas recomendável.
Como referências bibliográficas no estilo ABNT do BibLaTeX está projetado para poder ser
usado fora da classe abntex2, a formatação do título da referência bibliográfica não costuma
aparecer de acordo com o ABNT mesmo na classe abntex2 devido a algumas questões técnicas.
Isto pode ser acertado sem problemas com alguns códigos no preâmbulo como segue (supondo
que está usando “brazil” na opção do pacote babel).
%& BibLaTeX com estilo abnt
\usepackage [style=abnt] (biblatex)
\addbibresourcefex1i9-biblatex-abnt.biblk) Z arquivo bib
& Consertando o titulo que biblatex redefiniu
\efineBibliographyStrings{brazil}íbibliography=(Referências))
/4 Consertando para Referências ficar em maiusculo no sumário
\defbibheading{bibliography} [\bibname] 1%
\chapter*íft1>
\bibmark
\ifnobibintocYelse
\phantomsection
\addcontentslineí(tock{chapter}fWuppercaseí(t1))
\fi
\prebibhook
O Exemplo 19.4 ilustra como ficará o documento.
Exemplo 19.4: ex19-biblatex-abnt.tex
\documentclass [12pt,a4paper,english,brazil]í{abntex2}
\usepackageTtiftexl/, Para detectar o motor de TeX utilizado
% Fontes, de acordo com o motor do TeX
\ifPDFTeX
\usepackage [T1] {fontencl} % codificação da fonte em 8-bits
\usepackage{mlmodern} % fontes MLModern
%usepackage{lmodernk} % fontes Latin Modern
% \usepackage [ut{8} {inputencl} % acentuação direta em UTF-8 % não é mais
necessário
\else
\usepackageT{ontsetup} % fontes \ew Computer Modern
%usepackaget{ontspecl} % pacote para configurar fontes
%defaultfontfeaturesíLigatures=TeX)
% comandos de seleção das fontes, se desejar
%ee
\fi
% pacotes matemáticas de acordo com o motor TeX
\ifPDFTeX
\usepackageT{amsmath,amssymbl} % para matematica
\else
\usepackagefTunicode-math)
\ifLuaTeX
\usepackageTlualatex-{math}
vfi
\i
% babel ou poligrossia é carregado automaticamente pelo abntex2
\usepackage{Thyperref} % recomendável
\pdfstringdefDisableCommands(/desativar alguns comandos no bookmark
\let MakeUppercaselWrelax%
