B.2. Criando classes 279
% \ifnum \month < 10 OVNfi%Z
% \numberNymonth/
% \ifnum \day < 10 ONfi%
% \numberVday/
% \numberVyear]
\defWseename{see}
) % engnames
\newcommandWbrnamesí % Brazilian names
\def \axiomnameíAxiomaY
\def theoremnametTeorema]
\def \corollarynameíCorolY'{akrio}
\def lemmaname{Lema}
\def \propositionnameíProposiVlcíckN-Talo)
\def \conjecturenametConjectura)
%
\def definitionnametíDefiniVlcícHN-t{alo}
\defWnotenameí\ota)
\def \examplename{Exemplo}
\def questionnamefExercV'fí\ilcio)
\def remarknameífObservaWcícYkN-{aloL}
\def wproofnameíDemonstraYcícYN-farol
%444 data abreviada: dia/mes/ano
% MdefWtodayabrevílifnum \day < 10 ONfi%Z
% \numberNday/\ifnum \month < 10 OVfi%
% \numberWymonth/\{numberNyear}
\def \seenametíveja
% \typeoutíbrnames chamado)>
) % brnames
lll lo l o lolololololololololololololololololololololo lal ol lo l lo la lollode lolalolalole
%4 definicao dos macros para ambiente de teoremas
%4 teoremas, lemas, proposicoes, etc
\theoremstyle{plain}
\newtheorem{theorem}í\theoremname] [chapter]
\newtheorem{axiom} [theorem] (\axiomname*)
\newtheoremícorollary [theorem] fNcorollaryname
\newtheoremílemmaY [theorem] (\lemmaname]
\newtheoremípropositionY [theorem] (\propositionname]Y
\newtheorem{conjecture} [theorem] (\{conjecturename}
% definicao de definicoes, exemplos, etc.
\theoremstylefíde{inition}
B.2. Criando classes 280
\newtheoremíde{inition} [theorem] \de{initionname}
\theoremstyle{remark}
\newtheorem{remark} [theorem] f(\\\remarkname]
\newtheorem{note} [theorem] (\notename]
\newtheorem{example} [theorem] (\examplename]
,
%
\newtheoremíquestionY [theorem] (\questionname]
% alterando as penalidades (para corte de linhas em...)
\hyphenpenalty=5000 % hifenizalcíckN-tfato
\exhyphenpenalty=500 % palavras com hifem
\binoppenalty=3000 % operador binario (+, - , etc)
\relpenalty=2000 % operador relacional ( = \cong \ne,)
\clubpenalty=1000 % ???
\brokenpenalty=1000 % ???
% redefinição de sloppy
\defWsloppyfiWtolerance=9999 \hfuzz=.5pt \fuzz=.5pt)
\sloppy % prefere underfull do que overfull
% conjunto numerico
\newcommandí \Rset | \mathbbíRJ>
\newcommandí \Cset | \mathbb1C)>
\newcommandí \Zset Y { imathbb1Z}>
\newcommandf \IsetIí\mathbb{1}>
\newcommandí \Qset Y \mathbb1Q>
\newcommandí\\set Y \mathbb{N}>
% Funcoes em portugues (nome da {uncao deve ser em romano}
\eclareMathOperatorí\senk{sen}
\eclareMathOperatorí\arcsentk{arcsen}
\eclareMathOperatorí\senhYífsenhy
\eclareMathOperatorílarcsenhk{arcsenh}
% Reconfigurando de acordo com a opção
% Usar dsfont
\ifthenelsefí\booleanfexObOclasseOusedsfontlI+iZ se usedsfont for usado como
opcao
\IfFileExistsídsfont.sty)%
tZ
\RequirePackagefíds{ont})
\renewcommandí \Rset Y (\mathds{RI}
\renewcommandí \Cset ) \mathds{C}>
\renewcommandí\Zset ) \mathdsí{iZ}>
B.2. Criando classes 281
\renewcommandí \IsetIYfWmathds{I}>
\renewcommandí \Qset Y \mathds1Q)Y
\renewcommandí\set Y í \mathds{NJ}
H%
\olassErroríex-b-classekídsfont.sty not found.X%
fInstall dsfont package.Y%
»
Hrelse
Y% \ifthenelsefWbooleanfexObeêclasseQuseds{ont})
% fim: ex-b-classe.cls
\ote que alguns comandos de mensagem foi trocado da versão Package para a versão Class
a fim de emitir mensagem correta.
O Exemplo B.4 é um exemplo do uso do pacote do Exemplo B.3.
Exemplo B.4: ex-b-classe.tex
% Usando a classe definida pelo usuário
\documentclass [a4paper,12pt] fex-b-classe)
%idocumentclass [a4paper,12pt,english] fex-b-classel) Zidioma inglês
% \documentclass [a4paper,12pt,useds{ont} fex-b-classe) % com dsfont
\usepackage [T1] {fontencl} % codificação da fonte em 8-bits
\beginfí{document}
\chapterí{Teste}
\beginfíde{inition}\labelídef:triangulo:retangulo)
Um triângulo é dito retângulo se tiver um ângulo reto.
\endíde{inition}
\beginf{theorem} [Pitágoras] \Mabelíthm:pitagoras)
Dado um triângulo retângulo $ABC$ com ângulo reto em $A$, temos que
\beginfequationkWlabelífeg:pitagoras)
a 2=b"2+c72
\end{equation}
\end{theorem}
\beginfíproofy
Demonstração aqui.
\endíproofy
Usando a definição do $\sen$ e $cos$ juntamente com o Teorema-\refíthm:
pitagoras), temos que
\begin{proposition}
NE
\forall t NVin \Rset, \senº2 t + \lcos”2t=1
\i
B.3. Preenchendo o documento para teste 282
\end{proposition}
\endí{document}
A saída foi omitida por ser mesmo do Exemplo B.2.
B.3 Preenchendo o documento para teste
Para testar estilo de formatação, as vezes queremos preencher rapidamente o espaço.
Para isso existe o pacote lipsum que permite gerar parágrafos de texto em grego sem
sentido.
O comando \lipsum gera em torno de uma página de texto. O comando \lipsum[<n>]
gera n-ésimo parágrafo de texto. O comando \lipsum[<a>-<b>] gera o a-ésimo até b-ésimo
parágrafo de texto. \eja o Exemplo B.5.
Exemplo B.5: ex-b-lipsum.tex
& \lipsum % em torno de uma página
\lipsum[5] % quinto parágrafo
%& \ipsum[2-3] % de parágrao 2 até parágrafo 3
Fusce mauris. \estibulum luctus nibh at lectus. Sed bibendum, nulla a faucibus semper,
leo velit ultricies tellus, ac venenatis arcu wisi vel nisl. \estibulum diam. Aliquam
pellentesque, augue quis sagittis posuere, turpis lacus congue quam, in hendrerit risus
eros eget felis. Maecenas eget erat in sapien mattis porttitor. \estibulum porttitor. \ulla
facilisi. Sed a turpis eu lacus commodo facilisis. Morbi fringilla, wisi in dignissim interdum,
justo lectus sagittis dui, et vehicula libero dui cursus dui. Mauris tempor ligula sed lacus.
Duis cursus enim ut augue. Cras ac magna. Cras nulla. \ulla egestas. Curabitur a leo.
Quisque egestas wisi eget nunc. \am feugiat lacus vel est. Curabitur consectetuer.
\ote que lipsum gera somente parágrafos de textos. Para testar fórmulas e listas também,
poderá usar o pacote blindtext que tem o comando de mesmo nome que gera um texto.
O comando \blindtext[<n>] gera o texto nº vezes. O comando \Blindtext gera um
parágrafo. O parâmetro opcional pode ser usado para repetir n vezes.
Tem o comando \blindmathtrue que ativa as fórmulas no texto gerado, mas ele só
funciona em inglês (idioma selecionado pelo babel). Assim, se não estiver em inglês, use o
comando \blindmathpaper que gera parágrafos de textos e fórmulas. \eja o Exemplo B.6.
Exemplo B.6: ex-b-blindtext.tex
%& \olindmathtrue % funciona somente em ingles
& \olindtext & texto
& \Blindtext & Gera vários parágrafos
\lindtext[1] Z um parágrafo de textos
B.4. Observação 283
Alblinditemize % lista de itens
Alblindenumerate % lista de enumeração
Alblinddescription 4 lista de descrição
/Alblindmathpaper %4 texcto e fórmulas.
/Alblinddocument % documento com seção, subseção, listas, etc. Não inclui
fórmulas
& \Blinddocument % documento longo, com texto com seção, subseção, listas,
etc. Este inclui fórmulas
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam lobortis facilisis sem.
\ullam nec mi et neque pharetra sollicitudin. Praesent imperdiet mi nec ante. Donec
ullamcorper, felis non sodales commodo, lectus velit ultrices augue, a dignissim nibh lectus
placerat pede. \ivamus nunc nunc, molestie ut, ultricies vel, semper in, velit. Ut porttitor.
Praesent in sapien. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Duis fringilla
tristique neque. Sed interdum libero ut metus. Pellentesque placerat. \am rutrum augue
a leo. Morbi sed elit sit amet ante lobortis sollicitudin. Praesent blandit blandit mauris.
Praesent lectus tellus, aliquet aliquam, luctus a, egestas a, turpis. Mauris lacinia lorem
sit amet ipsum. \unc quis urna dictum turpis accumsan semper.
B.4 Observação
Para o desenvolvimento dos pacotes e classes, o LaTeX atual dispõe de uma camada de
programação sofisticada de LaTeX 3, além de permitir usar os caracteres “:” e “ ” no nome
dos comandos e ambientes. Neste documento, não será tratado sobre tais interfaces, mas se
precisar acessar no preâmbulo do documento, os comandos protegidos dos pacotes modernos
que usam tais caracteres no nome, deverá colocar entre \ExplSyntaxOn e \ExplSyntaxOff.
C. Usando o Editor LyX 284
Apêndice C
Usando o Editor Ly X
Neste apêndice, será explicado o básico sobre o editor LyX. LyX é um editor do similar a
\\\SIWYG (o que você vê é o que você obtém) e poderá editar o documento de forma similar
ao aplicativo de escritório, mas processando o documento final com o LaTeX.
C.1 \isualização do documento final
Para compilar/ver o documento, poderá usar o formatos comumente suportados pelo LaTeX.
O botão de “visualizar” (botão de olho, que {ica no lado esquerdo} é usado para visualizar o
documento em PDF.
Para exportar em PDF ou similar, basta acessar o menu arquivo->exportar. Lembre-se
que o IyX permite exportar/importar arquivos fonte em LaTeX, além de vários outros formatos
na qual existem conversores gratuítos do/para LaTeX.
Se estiver usando o pacote que precisa ser compilado para dvi como o pacote gráfico
pstrick e o psfrag, poderá escolher outro formato de visualização em “visualizar outros
formatos” (botão que {ica mais a direita, com olho dentro do quadrado}.
O uso do pacote hyperref é recomendado para que o LaTeX crie links automáticos
e bookmarks (indicadores). Os usuários de \indows, deve considerar em evitar o uso
do Adobe Reader na fase de elaboração, por ser pesado e apresentar dificuldade de in-
teragir com os editores de LaTeX. Uma boa opção é o freeware SumatraPDF (https:
//www.sumatrapdfreader .org/).
Depois de tudo pronto, “file->export” permite criar arquivo final no formato desejado.
\ote que a maioria dos editores de 1TEX salva o documento antes de compilar, mas o
LyX não faz isso. É necessário salvar manualmente sempre que convém.
Dicas:
* Para facilitar a navegação do documento em elaboração, é bom ativar o “Exibir->Painel
de estrutura de tópicos”.
e Se usar o código LaTeX inserido no documento com frequência, como o do pacote tikz,
seria bom ativar a pré-visualização na “Ferramentas-> Preferências” e em “Aparências
C.2. Antes de usar o LyX 285
& Comportamento”, ítem “Exibição”, na “Pré-visualização Instantânea”, escolher “sem
matemática”, e colocar pré-visualização no bloco que contém a caixa de INTEX que julgar
conveniente, com “Inserir->Pré-visualização”. Se quer que toda fórmula matemática
tenha pré-visualização automática, poderá escolher “ligado” em vez de “sem matemática”.
No entanto, as equações no modo “Instant Preview"” ficará com a mesma cor do texto,
tornando mais difícil de efetuar identificação rápida, o que não é recomendável.
e Para ver como ficaria o código 1TEX em edição, poderá ativar o “\iew->\iew source”.
* Seotexto todo ficar sublinhado em vermelho, ou não sublinha a palavra errada, mesmo
que o idioma em “Documento->Configurações: idioma” esteja correta, pode ser que o
corretor ortográfico não está selecionado corretamente. V. em “Ferramentas->Prefe-
rências” e em “Configurações de Idiomas”, item “\erificador Ortográfico”, escolha um
verificador em “verificador ortográfico”. Também certifique de que botão de “verificar
ortografia continuamente” (Botão ABC sublinhado em vermelho) está ativa.
C.2 Antes de usar o LyX
O tutorial e guias do usuário do LyX pode ser acessado pela “Ajuda->Tutorial” e “Ajuda-
>Guia dde Usuário” respectivamente.
Também é importante notar que copiar/colar padrão funciona somente entre trechos de
documentos do LyX. Caso de colar trecho de código do outro aplicativo como navegador de
internet ou editor de texto para o campo de comando LaTeX (botão TEX ou <ctrl>L), use
o colar especial (editar->colar especial->texto simples) ou ctrl+shift+v, para não perder a
quebra de linhas.
No lado esquerdo da barra de ferramentas, poderá escolher o tipo de texto (parágra{o}.
Alguns dos mais importantes são:
Standard texto normal.
Itemize lista não enumerada.
Enumerate lista enumerada.
Chapter Título do capítulo
Section Título da seção.
Subsection Título da subseção.
Lyx-code O texto como foi escrito, inclusive quebra de linhas (para colocar algoritmo, código
{onte do programa, etc}.
C.3. Acertando a configuração do documento 286
Esta lista aumenta, dependendo do módulo que for ativado. Por exemplo, se ativar o módulo
do ambiente de teoremas nas configualções do documento, terão entradas adicionais para
teoremas, definições, provas, etc.
Uma das formas de colocar comentário no documento é através da nota inserido por
“insert->note” (ou botão amarelo no painel de {erramentas} que é adequado para notas mais
longas por poder “fechar” a “caixa de notas”.
As “caixas” como de notas, TEX, Figure, etc tem um botão junto a “caixa” e clicando nele,
poderá abrir ou fechar, para facilitar a editoração. O fato de caixa estar fechada ou aberta
não influencia no processamento do documento final.
Como notas não serão impressas, também serve para desativar temporariamente o trecho
do documento, selecionando e clicando em “insert->note” (ou no botão amarelo). Para
desfazer a caixa de notas ou similares, use o “disolve->inset” acessível pelo botão direito sobre
caixa de notas ou similares.
Apesar de LyX efetuar conversão automática de imagens, quando pretende exportar
o código para LaTeX, é bom deixar convertido para pdf/jpg/png (para PDFLaTeX usado
atualmente) ou eps (para LaTeX antigo) a fim de evitar problema de compatibilidade de
imagem com o código fonte em (PDF)LaTeX.
C.3 Acertando a configuração do documento
No “Documento->Configurações”, escolha a classe de documento, margens e tamanho das
fontes, assim como idioma do documento. Certifique de que o idióma está de acordo com o
idioma usado no texto do documento para que as palavras corretas não sejam sublinhadas (o
que indica o erro ortográ{ico}.
Quando compila um documento, o LyX costuma colocar uma opção de usar o pacote
amsmath, mas no caso de inserir o comando de TEX diretamente, pode não ser detectado a
necessidade de amsmath.
Para resolver este caso, entre em “Document->settings” e no “math Package”, tire o check
do “use amsmath package automatically” e cheque em “use ams package”. O problema similar
pode acontecer quanto inclui figuras, usar cores, etc dentro da caixa de LaTeX, sem estar
usando fora dela. Neste caso, carregue os pacotes necessários, colocando o comando LaTeX
\usepackage no preamble (Document->Settings, [LaTeX {Preamble}.
Configuração do documento como estilo, margens, etc podem ser alterado pelo “Document-
>Settings” em qualquer momento.
Quando colar trecho de um documento para outro, pode ficar com a especificação da
linguagem diferente e começar a ser sublinhado. Neste caso, selecione este trecho e no “text
style” (botão com letras “abc”), escolha o “reset” na opção de [linguagem].
C.4. Inserindo o comando de LaTeX 287
C.4 Inserindo o comando de LaTeX
Para colocar pacotes adicionais, definições, configurações adicionas, etc que ainda não está
disponível no LyX (ou que não tem paciência de descobrir como {azer}, deverá ser colocado
no campo de “preamble” em “Document->settings, [LaTeX Preamble]|”, usando o comando
de LaTeX.
Quando precisar colocar um comando extra de LaTeX no documento, clique no botão
“TEX” ou pressione <ctrl>L na qual insere uma caixa de comando LaTeX, podendo colocar
qualquer comando válido de LaTeX. Caso finalizar com o comando LaTeX, coloque um espaço
(ou par de chaves) no final do campo de comandos de I2TEX para evitar problemas.
O comando ETEX pode ficar divididos. — Por exemplo, uma caixa pode conter
\begin{ambiente} e outra caixa pode conter \end{ambiente}, para colocar trecho do código
no ambiente desejado.
\ote que o campo de fórmulas também aceitam diretamente os comandos de ETEX.
C.5 Formatando textos
Para alterar o tipo de fontes do texto, selecione o trecho e clique no botão “abc”. Nele tem a
opção de escolher a família, forma e peso.
O emph fica na opção misc e language permite escolher idioma neste trecho. \ote que
<cntrol>+B é atalho para negrito e <cntr1>+E é atalho para enfatizar.
A opção “reset” de cada item restaura o item correspondente como padrão do documento.
Para saber o que cada botão faz, posicione o mouse sobre o botão e deixe parado para
aparecer o texto informativo.
Para criar um novo parágrafo ou linhas:
<ENTER> cria um novo parágrafo
<control>+<ENTER> quebra de linha (sem parágrafo que é W de LaTeX)
<control>+<space> espaço forçado (- de LaTeX).
\ote que, para inserir linhas vazias extras, deve alterar (quebras de linhas ou parágra{o}
com o espaço forçado.
C.6 Lista, sublista e similares
O texto como padrão, lista enumerada ou itemizada, pode ser escolhido pelo seleto superior
esquerdo da barra e ferramentoas, ou pelos botões na barra de ferramenta. Para cira sublista,
ou seja, um ítem seja sublista, clique no botão de aumentar profundidade. Para desfazer ou
finalizar sublista, clique no botão diminuir produndidade.
Se o módulo de demonstação estiver ativa na comfiguração do documento, aparecrá
teoremas, definições, etc. na seleção do tipo de texto (que fica na parte superior esquerdo da
barra de {eramenta}, mas se quer ter uma definição seguida da outroa, ou teoremas seguida da
C.7. Matemática 288
outra, precisaraá usar o menu que aparece quando clica com o botão direito do mouse. Com
ele, poderá inserir definição (ou similar) encima/embaixo da definição atual. Isto também
permite adicionar nome no teorema e similar com “texto adicional do teorema”.
C.T7T Matemática
Fórmulas matemáticas dentro do texto denominado de inlinestyle (textstyle) pode ser
inserido, clicando no ícone de somatório X” na barra de ferramentas, ou com o menu “insert-
>math->inline formula” ou com a tecla <control>+M. \ote que <ctrl>+M dentro da fórmula
matemática torna localmente como modo texto (aplicará \textt do amsmath).
Para inserir símbolos e fórmulas, podemos usar o painel matemático ativado embaixo,
quado o cursor está dentro da caixa de fórmulas. Para criar fórmulas de maneira rápida, é
recomendado memorizar alguns comandos básicos de LaTeX que podem ser digitados (em vez
de clicar no mouse).
\ote que o LyX tem dificuldade em lidar com o parâmetro opcional no modo matemático,
dificultando o uso da forma \sqrt[n] (x). Para contornar, foi definido o comando \root no
LyX que não é definido por padrão no LaTeX.
Para descobrir nomes de comandos LaTeX que estão no “Painel Matemático”, posicione o
mouse sobre os símbolos no “Math Panel” (mostrado quando o cursor está na fórmula) que
exibirá o nome do comando.
Uma fórmula numa linha independente denominado de “displaystyle” pode ser criado com
<Control>+<Shift>+M ou pelo menu “insert->math->Display formula”.
Para sair rapidamente de uma fórmula, pressione o “ESC” que posicionará o cursor logo
após a fórmula em edição.
Para converter tipo de fórmulas já digitadas, clique o botão direito sobre a fórmula e
escolha o novo tipo de fórmula. Também pode posicionar o cursor na fórmula e use o “edit-
>math->change formula type”.
A função por partes pode ser criado com “cases”, inserido com botão direito do mouse
sobre a fórmula, ou pelo menu “insert->math->cases”.
Nas fórmulas multi linhas, <control>+ENTER abre uma nova linha.
As fórmulas que ocupam uma linha independente tais como “Display fórmula” (fórmula no
modo “displaystyle”), “AMS align environment”, etc podem ser enumerados automaticamente.
Para ativar/desativar enumeração na equação com linha independente, clique no botão
direito do mouse sobre a fórmula, ou use o menu “edit->math->toggle numbering”.
Para referenciar equações ou elementos enumerados, use o botão de etiqueta para inserir
rótulo e referência cruzada (que {ica no lado da etiqueta} para inserir referências.
C.8 Observação adicional
Em geral, o estilo ABNTeX2 não costuma vir instalado no LyX.
C.8. Observação adicional 289
Para instalar, siga as instruções do site oficial https : //github.com/abntex/abntex2/
wiki/LyX.
D. Para Organizadores do Evento 290
Apêndice D
Para Organizadores do Evento
Aqui, veremos alguns pacotes úteis para organizadores de eventos. Um deles é o pacote para
mala direta no LaTeX, útil para emitir certificados. Outro é para criar caderno de trabalhos
apresentados.
D.1 Certificado com mala direta no LaTeX
Certificados de congressos científicos pode conter fórmulas nos títulos, o que complica a mala
direta nos aplicativos de escritórios. Assim, costumamos efetuar a mala direta no LaTeX.
A mala direta pode ser efetuada pelo datatool que lê os dados de um arquivo CSV. Após
carregar o datatool, comece configurando o separador de colunas e delimitador de campos.
\DTLsetseparatorí,) % Separador de campos
\DTLsetdelimiterí") % delimitador de celulas
Para acessar o arquivo CSV, usa-se o comando \DTLloaddbílistalífex-c-lista-
nomes . csv) para associar o arquivo ex-c-lista-nomes.csv no atalho lista. Assim, ao
referenciar lista, estará referenciando o arquivo ex-c-lista-nomes.csv
A primeira linha do arquivo ex-c-lista-nomes.csv é assumido que é título, isto é, contém
nome das colunas. Caso não tenha linha de título, poderá providenciar como em
\\DTL10oaddb [noheader,keys=tNome,Trabalho)]ílista-ílista.csv).
Neste caso, está indicando que não há linha de título no arquivo e está nomeando a
primeira e segunda coluna do arquivo de dados como Nome e Trabalho.
Agora podemos efetuar um laço de repetição que é algo como
\DTLforeachílista+t%s
\personname=Nome, \worktitle=TrabalhoY(%
+ % \DTLforeach
O primeiro parâmetro do comando \DTLforeach é o atalho para arquivo CSV que foi
criado pelo comando \DTL1oaddb. O segundo parâmetro é a lista de associação de comandos
com valor do campo. \personname=Nome e \worktitle=Trabalho associa o campo (dado da
D.1. Certificado com mala direta no LaTeX 291
coluna) Nome para o comando \personname e o campo Trabalho para o comando \worktitle.
O terceiro parâmetro são comandos a serem executados. O arquivo de entrada e como do
Exemplo D.1
Exemplo D.1: ex-d-lista-nomes.csv
"Nome" , "Trabalho","Observacao"
"Nome 1","Trabalho 1'",
"Nome 2","Trabalho 2",
"Nome 3","Trabalho 3",
Agora, o certificado pode ter enfeites como molduras, logotipos, etc.
Ele será diagramado para papel A5, para ser impresso no papel A4, ampliando-o. Fonte
também será alterado para bookman que é uma serifa grossa, ideal para letras maiores como
este. \eja o Exemplo D.2.
Exemplo D.2: ex-d-certificado.tex
\documentclass [12pt,a5paper,landscape] {article}
\usepackage [ut{8} {inputenc}
\usepackageTgraphicx) % para inlcuir logo
\usepackage{xcolor} % para cor
\usepackageTbookman) % Fonte bookman
\usepackage{datatool} % para mala direta
\usepackage [Imargin=1cm,tmargin=1cm,bmargin=1.8cm,rmargin=1.8cm] tgeometry) %
margens
\usepackageí{ancybox} % para colocar moldura na pagina
\usepackage{shadowtext} % texto sombreado
\usepackage [skins] {tcolorbox} % para moldura sombreada na página
\usepackage [none] {hyphenat} % sem hifenização
\sloppy % prefere underfull do que overfull
% para texto sombreado
\shadowoffsetí{2pt}
\shadowcolorfblack!30]
% veja o uso de tcolorbox em
% https://tex.stackexchange.com/questions/223694/how-"to-draw-a-text-box-with-
shadow-borders-in-latex
\newcommandí\certificateboxY[1]1%
\tcbox [enhanced, boxsep=8pt, boxrule=2pt, colback=white, , shadow=(2ptYí-2pt
D.1. Certificado com mala direta no LaTeX 292
IiOptlkíblack!30!whitelk, sharp corners] (%41)>
\fancypagefWsetlengthfWfboxsep+iSptIVcerti{icatebox}T)
\pagestyle{empty}
\begin{document}
\DTLsetseparatorí,) % Separador de campos
\DTLsetdelimiterí") % delimitador de celulas
% associa lista para o arquivo CSV
% \DTL10addb [noheader,keys=(Nome,Trabalho)] {lista}llatex-via-exemplos-lista-
nomes .. csv)
\DTLloaddbílista-ílatex-via-exemplos-certificado-lista-nomes.csv)
\DTL{oreachflista}l% processa cada item da lista
\personname=Nome, \worktitle=TrabalhoY(%
% certificado
incluindo a imagem de fundo (marca d'agua)
\begin{flushleft}
\noindent
\unitlength O.O04)textwidth
\beginfpictureY(0,0)(0,15)
\includegraphics [width=1.OWtextwidth] ({undo}
\end{picture}
\endí{lushleft}
Ex a
==
\sffamily
% timbre
\begin{center})
sAincludegraphics [width=0.1iNYtextwidth] flogo-esquerda)
\hfill
\beginí{minipage}[b] £O.7\textwidthy
\center
Universidade Federal de São Carlos W
Centro de Ciências Tecnológicas e de Sustentabilidade N
Departamento de Física, Quimica e Matemática
\endí{minipage}
ANREil1
%Cincludegraphics [width=0.1iYtextwidth] flogo-direita)
\hfil1-
\w£fil1
\end{center}
% titulo do certificado
\begin{center}
\shadowtextí\scaleboxt2)[NLARGE Certi{icado})
\endf{center}
