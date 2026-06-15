E.2. Lista de exercícios e provas 308
\tikzmarknode{node3}ídxy
\end{equation*}
\annotate [yshift=1l1em] T)ínodel+íSímbolo de integral)
\annotate [yshift=-0.5em] fbelow,leftl-{node2}ífunção)
\annotate [yshift=-0.S5em] fbelow,rightlínode3+ídiferencial, indicando a
variável de integração)
Símbolo de integral
" diferencial, indicando a variável de integração
função
Observe que, para o posicionamento correto de anotação, requer duas compilações seguidas.
E.2 Lista de exercícios e provas
Nas provas ou listas de exercícios, os itens podem ser curtas. Neste caso, é aconselhável que
coloque mais de um item por linha, mas mantendo o alinhamento.
Existem vários pacotes para elaboração de lista de exercícios e provas. Aqui será apresen-
tado uma delas. O pacote xsim é sucessor de exsheets. Este pacote implementa o ambiente
exercise para produzir exercícios enumerados (e o ambiente solution para escrever soluções)
e o pacote tasks permite colocar vários itens enumeradas e alinhadas em uma única linha
(como é feito pela combinação dos pacotes enumitem e tabto).
\eja o Exemplo E.3.
Exemplo E.3: ex-e-exsheets.tex
\documentclass [12pt,a4paper] {article})
\usepackage [T1] ({fontenc}
\usepackage [brazil] ({babel}
\usepackage{tasks} % cria lista curta
\usepackage{xsim} % cria exercicios (e respostas)
% traduzindo
\eclareExerciseTranslationíbrazil-{exercise}(Exerc{cio}
\eclareExerciseTranslationíbrazil-{exercises}íExerc{cios}
% necessário se for colocar soluções também
\eclareExerciseTranslation{brazil}ísolutionYíSolução)
\eclareExerciseTranslationíbrazil-ísolutions+íSoluções)
\obegin{document}
% O ambiente exercise produz questões.
\begin{exercise}
Qual item não é metal?
% itens da questão será produzido pelo ambiente tasks
\eginttasks)(4) % 4 itens por linha
E.3. Com e sem respostas
\task ferro
\task carbono
\task cobre
\task mercúrio
\end{tasks}
\endfexercise
% Alterando a enumeração de tasks
\settasksí
label=(\alph*), % entre parenteses, em romano minusculo
label-width=4ex % largura reservada para rótulo
F
\begin{exercise}
O que é mamífero?
\begin{tasks}(2) % 2 itens por linha
\task Animais que botam ovos.
\task Animais que amamentam.
\task Animais que voam.
\task Animais com 4 patas.
\end{tasks}
\end{exercise}
\endídocument y
\endí{document}
Exercício 1
Qual item não é metal?
a) {erro b} carbono c) cobre d) mercúrio
Exercício 2
O que é mamífero?
(a) Animais que botam ovos. (b) Animais que amamentam.
(c) Animais que voam. (d) Animais com 4 patas.
EF.3 Com e sem respostas
As vezes, queremos gerar versões com resposta e outro sem, ou que resposta fique no final do
documento, mas que seja diagramado junto as questões. Neste caso, podemos usar o pacote
answers (existem vários pacotes para tal propósito). \ote que o pacote xsim pode fazer
mesma tarefa, mas o pacote answers pode ser combinados com ambientes diversos, como com
o ambiente gerado pelo inewtheorem. \eja o Exemplo E.4.
Exemplo E.4: ex-e-answers.tex
E.3. Com e sem respostas
\documentclass [12pt,a4paper] {article}
\usepackage [T1] {fontenc}
\usepackage [brazil] (babel)
\usepackageTanswers) % resposta no arquivo separado
Alusepackage [nosolution{iles}tanswers) 4 resposta no lugar
\usepackageT{amsthm}
% "sol" é ambiente a ser usado. "Solution" não deve ser modificada. A
resposta sera gravada no arquivo referenciado internamente por "ans"
\ewassociation{sol}íSolutionkífansY
/4 \renewcommandíf |solutionertensionttans)
\newtheorem{ex}fExercicíol[section] %Z ambiente de exercicios
\begin{document}
éh inicia a gravacao da resposta no arquivo "ans" cuja mnome externo e À
jobname-ans (\jobname e mnome do arquivo atual)
\\Opensolutionfile{ans} [NVjobname-ans]
\sectionfíProblemasY
\beginfex>
Primeiro exercício.
\begin{soly}
Solução do primeiro exercício.
\endí{sol}
\endíex>)
\beginfex>
Segundo exercício.
\beginísoly
Solução do segundo exercício.
\endísol+y
\endífex>
\elosesolution{ilefans} % finaliza a gravação das respostas
\sectioníSoluções)
\Readsolution{ilefans} % colocar solucoes do "ans" aqui.
\endí{document}
E.3. Com e sem respostas 311
1 Problemas
Exercicío 1.1. Primeiro exercício.
Exerciciío 1.2. Segundo exercício.
2 Soluções
1.1 Solução do primeiro exercício.
1.2 Solução do segundo exercício.
F. Para Projetos 312
Apêndice F
Para Projetos
Aqui será tratado de pacotes úteis ao desenvolvimento de documentos grandes como no caso
de livros.
F.1 Pacote standalone
Quando cria muitas ilustrações e diagramas, as vezes deixamos estas ilustrações como arquivo
separado para compilar e ajustar mais rapidamente. Por exemplo, cada ilustração em tikz
pode estar em um único arquivo para que o documento principal inclua eles. Neste caso,
não podemos usar \input, nem \include pois a ilustração tem a sua própria classe de
documento. Neste caso, podemos usar a classe standalone. Cada ilustração de tikz usará
a classe standalone em vez do article ou similar. Assim, podemos compilar e ajustar a
ilustração quando bem entender. No documento principal, use o pacote standalone e demais
pacotes que arquivos inclusos podem precisar. Para incluir a ilustração feito pela classe
standalone, basta usar \input ou similar.
A figura diagramado com a classe standalone é como do Exemplo F.1.
Exemplo F.1: ex-f-standalone-fig.tex
\documentclass [12pt,a4paper] f(standalone)
\usepackage{tikz}
\usetikzlibrary(patterns)
\begin{document}
\begin{tikzpicture}
\draw[pattern=north east lines] (-1,-1) rectangle(1,1) (0,0) circle(1);
\end{tikzpicture}
\endí{document}
F.2. Dividindo o documento em vários arquivos 313
O documento que usa a figura, usa o pacote standalone e usa o \input para incluir o
arquivo de figura, como no Exemplo F.2.
Exemplo F.2: ex-f-standalone.tex
\documentclass [12pt,a4paper] {articley}
\usepackage{standalonel} % para incluir arquivos diagramado com standalone
\usepackage [T1] ({ontenc}
\usepackage [brazil] (babel)
\usepackagetamsmath)
\usepackageí{amssymb}
% pacotes usados pelo arquivo a ser incluido
\usepackage{tikzy}
\usetikzlibrary{patterns}
\begin{document}
Para incluir o arquivo diagramado com classe \\texttt{standalone}, basta usar
o \erbt+\input+.
\beginffigureY [hbp!]
\center
\inputfex-f-standalone-fig>
\captioníInclusão de {iguras}
\endí{igure}
\end{document}
Para incluir o arquivo diagramado com classe standalone, basta usar o \input.
Z
F.2. Dividindo o documento em vários arquivos 314
F.2 Dividindo o documento em vários arquivos
Para dividir o documento em vários arquivos, poderá usar o \include, mas ele não é eficiente,
pois os pedaços de documentos não podem ser compilados separadamente. O pacote subfiles
resolve este problema. O uso de subfiles é similar ao do standalone, mas em vez de ignorar o
preamble dos arquivos inclusos, os arquivos a serem incluídos usam o preamble do documento
principal. Assim, como o standalone, o documento principal deve conter todos os pacotes
e definições que suas partes vão precisar, mas não há necessidade de colocar tais pacotes e
definições no arquivo de partes. À estrutura do documento principal com subfiles é algo
como do Exemplo F.3.
Exemplo F.3: ex-f-subfiles-principal.tex
\documentclass [12pt,a4paper,oneside] fbook>
\usepackageísub{iles} % para incluir partes do documento
\usepackage [T1] {fontenc}
\usepackage [brazil] {babel}
\usepackagefamssymb,amsmath+
\usepackage{Ttikz}
\usetikzlibrary(patterns)
\begin{document}
\subfilesífex-f-subfiles-pre{acio}
\subfilesfex-f-subfiles-capitulol)
\subfilesfex-f-subfiles-capitulo2)
\subfilesfex-f-subfiles-capitulo3y
\endí{document}
Exceto pelo uso do pacote subfiles e o comando \subfiles em vez do \include, tem nada
de especial. Cada pedaço do documento tem a forma como do Exemplo F.4.
Exemplo F.4: ex-f-subfiles-capitulo1 .tex
\documentclass [ex-f-subfiles-principal] (sub{iles}
\beginf{document}
\end{document}|
\ote que a classe de documento é subfiles e sua opção é o nome do arquivo principal.
Como o preamble será obtido do documento principal, não há preambles e já começa a
escrever o documento no ambiente document normalmente.
Com isso, podemos compilar partes do documento, assim como todo o documento.
F.3. º“Todo” (tare{as} 315
F.3 “OTodo” (tare{as}
Para inserir “todo” (tarefas a {azer} no documento LaTEX, existe alguns pacotes. Aqui,
veremos somente o todonotes. O comando básico deste pacote é o \\todoíl que insere
anotação de tarefas na área lateral do documento, correspondente a posição desejada. O
comando \\todo aceita opções adicionais. Por exemplo, \todo[{nline} 1) adiciona nota de
tarefa dentro do documento, em destaque, em vez da área lateral. Para criar lista de tarefas,
usa-se o comando Ml istoftodos. \eja o Exemplo F.5.
Exemplo F.5: ex-f-todonotes.tex
\documentclass [a4paper,12pt]{article}
\usepackage [ut{8} {inputenc})
\usepackage [portuguese] {todonotes}
\begin{document}
\istoftodos % listar todos todo's
\sectionfApresentação)
Tarefas a fazer ou *"todo'' pode ser anotados usando pacotes tais como
todotVerificar opções de pacotes). Neste texto, será apresentado o uso de
\texttt{todonotes}.
\sectioníDesenvolvimento
\todo[{nline} fElaborar conteúdos)
\end{document}
Documento com as notas de tarefas é como segue.
Lista de tarefas pendentes
\erificar opções de pacotes
Elaborar conteúdos .
1 Apresentação
Tarefas a fazer ou “todo” pode ser anotados usando pacotes tais como ar
Neste texto, será apresentado o uso de todonotes.
2 Desenvolvimento
G. Alguns Aplicativos Auxiliares para Usuário de LaTeX 316
Apêndice G
Alguns Aplicativos Auxiliares para
Usuário de LaTeX
Para melhor aproveitamento do LaTeX, costumam usar diversos aplicativos auxiliares para
melhorar o seu uso. Aqui, listaremos alguns desses aplicativos populares gratuitos.
G.1 Editor para LaTeX
TeXMaker/TeXStudio
site: https: //www.xmimath.net/texmaker/
site: https: //www.texstudio.org/
O TeXMaker é um editor de código fonte do LaTeX multiplataforma leve e eficiente. Ele
apresenta painel de inserção de símbolos matemáticos e visualizador de PDF integrado. Apesar
de não vir com o menu para chamar biber usado no BibLaTeX, pode ajustar a chamada de
BibTeX ou acrescentar no menu personalizado (menu “usuário”).
O TeXStudio, por sua vez, é um “fork” do TeXMaker, incorporando mais recursos. Isto
torna um pouco mais pesado, mas apresenta a capacidade de compilar um trecho do código
no tempo real, mostrando na janela de edição. Para isso, basta selecionar um trecho, e no
menu aberto pelo botão direito, escolher “Preview selection/parentheses”.
LyX
site: https: //www.lyx.org/
site: https: //sourceforge.net/projects/lyxwininstaller/
O LyX é um editor com aparência similar a aplicativos Office (MS Office/Libre O{fice},
mas que compila o documento em LaTeX. Ele também importa/exporta documentos LaTeX.
O instalador de LyX para MS \indows pode encarregar de instalar o MikTeX básico, caso
tenha conexão com a internet, mas também pode deixar o MikTeX pré-instalado. Ele também
instala automaticamente os pacotes adicionais necessários.
G.2. Editor gráfico 317
No menu de ajuda, encontrará o tutorial e guia de usuário. O LyX foi desenvolvido para
os usuários de LaTeX. Como o usuário de LaTeX ganha desempenho significativo em relação
ao usuário comum, é altamente recomendado que estude o LaTeX. Pra ativar o verificador
ortográfico no tempo real, entre em “tools->preferences”, e em “[language settings]->|[spell
checker]”, selecione “enchant” ou similar para “spell check engine” e cheque o “[ lspell check
continuouslly”.
Observação G.1. O \indows costuma não vir com visualizador de PDF instalados. Apesar de
editores para LaTeX costuma vir com visualizador de PDF integrados, é bom ter um visualizador
dedicado (por exemplo, LyX não vem com visualizador de pd{ dedicado}. Uma das opções
é instalar o Sumatr PDF (https://www.sumatrapdfreader.org/) que é muito leve. Ele não
tem recursos de preenchimento de formulários ou acrescentar notas como o Adobe Reader
(https://get.adobe.com/br/reader/), mas atende a maioria das necessidades.
TeXWorks e Gummi
https://www.tug.org/texworks/
https://alexandervdm.github.io/gummi/ (somente linux)
O TeXWorks é um editor multiplataforma, leve e simples para I1TEX. Apesar de ser
desenvolvido para facilitar o uso pelos inciantes, não inclui o painel de inserção de símbolos
matemáticos e navegação na estrutura dos docuumentos.
O Gummi é um editor leve para linux, com capacidade de compilação instantânea. Além de
mostrar o documento compilado enquanto digita, ele usa o diretório temporário para compilar,
mantendo a pasta do documento livre de arquivos intermediários que o TEX costuma criar
durante a compilação. Ele é indicado para documentos menores sem muita complexidade por
não conseguir desativar a compilação instantânea, assim como ausência do painel de inserção
de símbolos matemáticos e navegação na estrutura de documentos.
G.2 Editor gráfico
Editores gráficos ajudam a elaboração de ilustrações e similares.
InkScape
site: http://www. inkscape .org/
InkScape é um editor gráfico vetorial para criar ilustrações no estilo do Corel Draw
(comercial) ou Adobe Illustrator (comercial). Ele é bem mais leve e fácil de ser usado do
que os seus concorrentes. Pode ser usado para criar uma ilustração nova, ou retocar o arquivo
pdf já existente.
A versão atual permite instalar plugin para inserir fórmulas L1TEX diretamente na figura.
\ote que nem todo efeito pode ser salva no eps e também no pdf. Por isso, é necessário
checar o eps ou pdf quando criando.
G.2. Editor gráfico 318
O manual pode ser acessado pelo menu de ajuda, sem precisar ficar procurando na internet.
Quando salva como PDF, selecione “usar tamanho do objeto exportado” na opção “tamanho
da saída de página”. Também ajuste o “resolução para renderização (dpi)” para mínimo de
300 em ”[v] Efeitos de filtro de renderização”. Se quer deixar o tamanho do papel já ajustado
para tamanho da figura, selecione toda figura (<ctrl>A) e entre em "file->document propries”.
No ”custom size”, clique em [fit page to selection].
Para inserir fórmulas diretamente na figura, instale o textext (https://textext.github.
io/textext/).
Na versão atual, existe a opção de separar o texto para ser processado diretamente no
LaTeX. Para isso, basta escolher “Omitir texto no PDF e criar um arquivo LaTeX” na opção
de “Orietnação do teto”. Assim, ele criará um arquivo tex para cada pdf. No documento do
LaTeX, insere o arquivo tex com o comando \input. Com esta opção, o comando LaTeX pode
ser usado diretamente na figura que será processado quando gera o documento no LaTeX.
Dia
site: http://projects.gnome.org/dia/
Editor de diagramas, similar ao comercial Microsoft \isio. Diagramas costumam usar
peças prontas, assim como curvas que se quebram no meio, o que é recomendável usar um
editor próprio. O Dia é feito especialmente para editar diagramas, mas não há atualização
recente.
Se for o caso de criar ilustrações, use o InkScape.
GIMP
site: http://www.gimp.org/
É o editor de imagem como o Adobe Photoshop (comercial) ou Corel Photo Paint
(comercial). O “GIMP Help” é uma espécie de manual que precisa ser abaixado/instalado a
parte devido ao seu tamanho. Ainda não há versão traduzida para português deste manual.
Se for apenas fazer pequeno retoque e converter formato da imagem (para jpg e png, por
exemplo), poderá usar o aplicativo mais leve.
LaTeX Draw
site: http://latexdraw.sourceforge.net/
Editor escrito em java, especializado para pacote pstricks do LaTeX. Ele permite abrir
muitas figuras com pstrick, editado manualmente ou gerado pelo outro programa. Como vá-
rios programas tais como gnuplot, geogebra, inkscape, etc podem salvar no formato LaTeX
com pstrick, poderá usar este editor para retoques. \ote que o ajuste de tamanho da figura
deve ser feito no editor e não no documento, para ter espessura da linha inalterada, mas se
entender um pouco do pstrick, poderá editar o código da figura exportada para deixar escalá-
vel dentro do documento (sem alterar a espessura). Como pstrick é um pacote desenvolvido
G.3. Gráfico científico 319
para dvi/ps, precisará usar o pacote adicional pstool (não é pstools), pst-pdf ou similar,
quanto pretende compilar diretamente para PDF através do PDFETEX, XalATEX ou LuaLaTeX.
Uma maneira clássica de gerar PDF sem tais pacotes é usar o LaTeX=>dvips=>ps2pdf.
FlowFram Tk
site: http://www.dickimaw-books.com/apps/flowframtk/
O FlowFramTk, anteriormente conhecido como jpgf Draw é escrito em java e exporta
figura no formato LaTeX usando o pacote pgf (usado pelo pacote beamer). O pacote pgf tem
uma grande vantagem de poder ser compilado tanto para dvi como para pdf (por isso que o
beamer normalmente compilado pelo pdflatex pode ser compilado com latex quando não usa
o recurso especí{ico do PDF}. FlowFramTk armazena a figura no formato próprio e permite
exportar como pgf, mas parece que não tem recurso de importação.
Um dos recursos adicionais interessantes do FlowFramTk é a capacidade de gerar modelo
de poster e material publicitário usando o pacote consolidado flowfram. O pacote flowfram
permite criar caixas de texto com rótulo e diagramar dentro dele de forma simples (parece
ser um dos mais simples desta categoria). No entanto, criar layout complexo é um pouco
trabalhoso. O FlowFramTk permite desenhar o layout para usar com flowfram, o que simplifica
o trabalho.
TikZit
site: https://tikzit.github.io/
Editor gráfico que exporta para o formato tikz (parte do pacote pgf). Ele permite criar
facilmente os diagramas em tikz através da interface gráfica.
G.3 Gráfico científico
Asymptote
site: https : //asymptote.sourceforge.io/
O Asymptote é uma linguagem/interpretador gráfico 2D/3D inspirado em MetaPost que
permite produzir gráficos em Post Script, PDF e SVG.
Geogebra
site: http://www.geogebra.org/
Ele é um aplicativo de geometria dinâmica, mas permite incorporar gráficos de fun-
ções. — Além de exportar para ser colocado na página web, permite exportar para
eps/pdf/pstrick/tikz. Para retocar texto/fórmulas, exporte no formato LaTeX como
pstrick ou tikz.
G.3. Gráfico científico 320
gnuplot
site: http://www.gnuplot.info/
Este aplicativo permite gerar gráfico de boa qualidade a partir do dado armazenado no
arquivo texto, mas pode gerar gráfico a partir das expressões também. Poderá escolher
diversos formatos de exportação, dependendo do objetivo. Como ele é um interpretador,
precisará aprender alguns comandos básicos para gerar gráfico de boa qualidade.
Maxima
site: http://maxima.sourceforge.net/
Álgebra computacional como Maple (comercial) e Mathematica (comercial), implemen-
tando a linguagem MacSyma. Costuma ser usado com a interface gráfica \xMaxima (http:
//wxmaxima-developers.github.io/wxmaxima/) que permite efetuar diversas tarefas sem
saber a linguagem, inclusive gerar gráficos 2D e 3D das funções.
Observação: No caso de MS \indows, o instalador do Maxima instala o \xMaxima por
padrão.
GNU R
site: http://www.r-project.org/
GNU R é um aplicativo popular especial para estatística e implementa a linguagem R, bem
parecido com a linguagem S. Ele produz ótimos gráficos, mas requer conhecimento de um
pouco da linguagem R. Uma das interfaces gráficas recomendados é o RKWard e R Studio, mas
para quem quer usar com o menu como no MiniTab (comercial), poderá instalar o Deducer
(não testado).
site do RKWard: https://rkward.kde.org/
site do R Studio: http://www.rstudio.org/
site do Deducer: http://www.deducer.org/
GNU Octave e outros clones do MatLab
gnu octave: https://octave.org/
scilab: http://www.scilab.org/
Para quem entende um pouco da linguagem MatLab, o GNU Octave e SciLab podem ser
usados para gerar gráficos matemáticos no formato vetorial. O GNU Octave é mais popular.
LabPlot e outras imitações do Microcal Origin
LabPlot: https://labplot.org/
SciDAVis: https://github.com/SciDAVis/scidavis
RLPlot: http://rlplot.sourceforge.net/
G.4. Alguns convertores 321
O LabPlot é um aplicativo multi plataforma de código aberto para visualização (criar
grá{icos} e análise de dados.
O SciDAVis é programa multiplataforma para análise de dados e criação de gráficos como
o popular Microcal Origin (comercial). O gráfico é de boa qualidade e permite exportar em
diversos formatos, incluindo o formato vetorial eps. Como SciDaVis não é atualizado algum
tempo (2025), LabPlot que continua tendo suporte é mais recomendado.
O RLPlot é bem mais simples, mas tem recurso de adicionar texto e linhas poligonais no
gráfico gerado.
Observaçao: O aplicativo gratuito e multiplataforma FitYK (http://fityk.nieto.pl/)
é desenvolvido especialmente para o ajuste de curvas que é interessante, apesar de não ser
clone de Microcal Origin.
LibreCAD
site: http://librecad.org/
LibreCAD é un CAD 2D de código aberto e é multiplataforma.
Outros
Nem sempre os aplicativos matemáticos tem a habilidade de exportar gráficos vetoriais, como
no caso de MathMod (sucessor do k3dsurf). Isto ocorre devido a dificuldade ou impossibilidade
de criar gráfico vetorial de alguns tipos específicos de imagens matematicos obtidos. Neste
caso, exporte a figura com resolução de 600DPI quando tem os traços bem definidos (desenho
técnico) ou 300DPI no caso de traços estar menos definidos (como imagem no estilo de {otos},
o que é recomendado para impressão. Se for ampliar dentro do documento, a escala da
ampliação deve ser considerada, exportando para ter o mínimo de DPI após ampliação.
* MathMod (sucessor do k3DSurf para linux/win): Plotador de superfícies tanto a para-
métrica como a implícita, usando interface gráfica amigável.
Site: http://sourceforge.net/projects/mathmod/
* Fractint (multi plata{orma}: Um dos mais poderosos softwares para plotar fractais.
Por ser baseado em DOS, a interface gráfica não é amigável na versão estável. AÀ versão
de teste contém a implementação para \indows.
Site: http://www.fractint.org/
* Graphvis (multiplata{orma}. Especial para produzir grafos, usando a linguagen dot.
Site: https://www.graphviz.org/
G.4. Alguns convertores 322
G.4 Alguns convertores
Image Magick
site: http://www. imagemagick.org/
Se instalou o LyX, já deve ter instalado. Este convertor é para usuário mais avançado,
útil para conversão em lotes. Ele converte praticamente de qualquer formato. O comando é
convert, mas usuário de MS \indows deve tomar cuidado pois a ferramenta do MS \indows
para converter sistema de arquivo FAT para NTFS também se chama convert. Assim, deverá
assegurar de que está chamando convert do Image Magick, como chamar especificando o
caminho.
No Linux, a opção de conversão para EPS,PDF pode vir desativados por padrão, o que
requer ativação manual.
Exemplo:
convert img.jpg img.pdf
converterá no formato pdf e
convert img.jpg eps2:img.eps
Criará eps compactado.
sam2p
site: https : //github.com/pts/sam2p/releases
Converte imagem bitmap para eps ou pdf. Atualmente o InkScape pode ser usado para
converter para EPS/PDF, mas pode ser útil para usuários avançados.
sam2p figura.jpg figura.pdf
converterá para pdf.
TeX4ht, LaTeXML e Iwarp
site: https://ctan.org/pkg/tex4ht, https://math.nist.gov/-BMiller/LaTeXML/,
https://ctan.org/pkg/lwarp.
TeX4ht é um convertor de TEX/LaTeXpara HTML/XHTNML, similar a Hevea, TTH, e
LaTeX2HTML, que roda em diversas plataformas. \ote que todos 4 programas clássicos são
de multiplataformas e cada um tem vantagens e desvantagens. Hevea e TTH, não apresenta
suporte decente às fórmulas matemáticas. O Tex4ht é implementado como pacote para TEX
e o LaTeX2HTML é convetor escrito em perl. Ambos conseguem converter eficientemente os
documentos com equações, permitindo usar a imagem (GIF, PNG ou JPEG) ou MathML para
representar equações. Além disso, TeX4ht e LaTeX2HTML são de código aberto. Por estas
e outras razões, eles são os mais usados. O HTML gerado por Tex4ht é mais parecido com
o documento original e não consegue dividir documentos em pedaços (o que é interessante
para HTML grande, para acelerar o acesso na internet). O LaTeX2HTML produz documentos de
