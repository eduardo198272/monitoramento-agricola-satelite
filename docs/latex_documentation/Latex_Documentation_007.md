12. Medidas e Contadores 87
Capítulo 12
Medidas e Contadores
Neste capítulo, veremos medidas e contadores.
12.1 Unidade de medidas e espaçamentos
As vezes o espaçamento ajustado automaticamente não está bom e queremos fazer pequenos
ajustes.
Para aumentar espaçamento entre parágrafos em um determinado ponto, como entre texto
e equações altas, poderá usar o \smallskip, wnedskip e \bigskip para ter espaçamentos
maior que o padrão. \ote que, se quer ter espaçamento maior entre texto e equações em todo o
documento, deverá efetuar ajustes de parâmetros \abovedisplayskip e \\belowdisplayskip.
Para espaço horizontal e vertical, usa-se o \hspace{medida} e \spaceí{medida} respecti-
vamente. Caso estiver inserindo o espaço vertical no começo das páginas, ou espaço horizontal
no começo das linhas, use a versão com “*” \hspace*{medida} e \space*ímedidaL.
Medidas comumente usados são:
pt (point - unidade grá{ica} = -55sin (polegada) ou 0.351mm
mm (milimetro) = 2.845pt
pc (pica) = 12pt ou 4.218mm
cm (cent{metro} = 2.371pc
in (polegada) = 25.4mm ou 72.27pt ou 6.022pc
U”
x
ex altura da letra minusculo da fonte corrente
em largura da letra “M” maiúsculo da fonte corrente
mu (math unit) = -s<em
\stretchí{peso} espaço esticável com peso especificado.
Existem ainda várias ouras medidas menos usadas que foram omitidos aqui.
O \stretch{pesol} produz medida que preenche o espaço. Existem alguns comandos
deste tipo que são úteis: \hfill (equivale a \hspaceístretch{t1})), \fill (equivale a
\spacef{Tstretcht1})), \\arulefill (similar a NVh{ill, mas preenche com linha}, \dotfill
(similar a \h{ill, mas preenche com pontos}.
Ainda existem comandos para inserir pequenos espaços, que são \quad (insere espaço
de lem = 18mu), \gquad (insere espaço de 2quad=2em), \enspace ou \enskip (insere
espaço de %quad). Estes comandos costumam ser usados para inserir pequenos espaçamentos
para melhora a aparência das fórmulas matemáticas. No modo matemático, ainda existem
comandos de inserção de espaços menores que são
> (Équad = 3mu),
N: (quad = 4mu),
N; (fgquad = 5mu),
V! (FEquad = —ômu).
\eja Exemplo 12.1.
Exemplo 12.1: exl2-espacos.tex
palavra a esquerda \hfill palavra a direita.
palavra a esquerda \hrulefill palavra a direita.
palavra a esquerda \dotfill palavra a direita.
primeiroWhfill segundoWhrulefillNhrulefill terceiroNdotfillNdotfillNdotfill
quarto
\oigskip
$x NVin \mathrmíIV!IR), \enspace x>0$.
palavra a esquerda palavra a direita.
palavra a esquerda palavra a direita.
palavra a esquerdalllllvlc AAAA palavra a direita.
primeiro segundo - terceiro... llll lll o quarto
TER r>O0.
\ota: O \wnathbffR* construído acima é apenas como ilustração. Deverá usar a fonte
apropriada tal como \vnathbb do AMS.
Outra coisa que as vezes usamos para alinhamento dos elementos de fórmulas é o comando
\phantom que, em vez de produzir elementos da fórmula, reserva o espaço usado por ele. Por
exemplo, L. ; te F,'; foram produzidos respectivamente por $\Gamma ({ij} fNphantom{ij}+k)$
e $\Gamma {ij} k$.
12.2 Medidas prédefinidas ou definidos pelo usuário
Existem algumas medidas pré-definidas como comandos, relacionadas à configuração das
páginas e similares que costuma ser usados com certa frequência. Aqui, vamos citar algumas
delas.
\textwidth Largura de texto atual.
\linewidth Largura da linha atual. Por exemplo, dentro da lista, será menor que o
\textwidth.
\columnwidth Largura da coluna. Se for em uma coluna, coincide com \textwidth.
\columnsep Distância entre colunas no modo multi colunas.
\columnseprule Largura da linha que separa colunas no modo multi colunas (Opt para
desabilitar).
\textheight Altura do texto atual.
\parindent Indentação (quanto deixa no lado esquerdo) do parágrafo.
\parskip Quanto deixa de espaço antes do parágrafo.
\paperwidth Largura do papel.
\paperheight Altura do papel.
\unitlength Medida de unidade usado no ambiente picture.
Dentro do minipage, \textwidth, \linewidth e \columnwidth assumem a largura do
minipage, mas no \wparbox, somente \linewidth assumirá a largura da caixa.
Para imprimir estas medidas, coloque o comando \the antes do comando de medidas. Por
exemplo, para imprimir o valor de \textwidth, use \theYtextwidth.
Para definir uma nova medida, usa-se o comando \newlength{\minhamedida}. Este
comando criará a medida \ninhamedida. Para definir ou altera o valor da medida, use
\setlengthfWminhamedidal{medida} onde medida é a medida da \minhamedida.
O valor da medida pode ser configurado a partir de box (caixa) existente (como texto,
fórmulas, etc). Uma caixa (de elemento) tem altura (height), largura (width) e a distância
da parte inferior até a linha base (depth).
\settoheight(\minhamedidalí<conteúdo>), \wsettowidthfWminhamedidal-í<conteúdo>)
e \settodepthfWminhamedida-+í<conteúdo>) configuram o valor da \minhamedida para
essas medidas correspondentes ao seu parâmetro.
\ote que, pela facilidade, as vezes usamos o modo TEX para configurar as medidas como
E”
em \minhamedida=3.0Ocm ou até mesmo, omitir e escrever como \minhamedida 3.Ocm
Para facilitar os cálculos das medidas, normalmente usa-se o pacote calc.
O pacote calc, além de permitir calcular medidas com facilidade, ainda acrescentam alguns
novos comandos tais como \settototalheightí\algumamedidal-í<conteúdo>) que confi-
gura \algumamedida para width+depth e \idthofí<conteúdo>]), \\heightofí<conteúdo>],
\depthofí<conteúdo>) e \totalheightofí<conteúdo>) que retornam width, height,
depth, e width+depth, respectivamente.
\ote que o calculo efetuado pelo pacote calc pode não funcionar em alguns parâmetros
como medida de largura do \parbox e de minipage. Neste caso, coloque a expressão dentro
do \dimexpr(). \ote que expressão deve ficar dentro de parenteses e não chaves.
Por exemplo,
\parboxfWdimexpr (\linewidth-lcm)X{texto}
efetuará calculo da largura da caixa como sendo 1cm menor do que a largura da linha.
12.3 Contadores
LaTeX usa diversos contadores para efetuar enumeração automática, tais como páginas, equa-
ções enumeradas, capítulos e seções, figuras, etc.
Estes contadores podem ser controladas, tanto na contagem como na sua aparência.
Em geral, o costume é nomear contador com mesmo nome do ambiente e o que precede
\the será usado para imprimir o seu valor. Por exemplo, a impressão de enumeração da
página usa o \thepage e enumeração do capítulo usa \thechapter e assim por diante.
Os principais contadores pré definidos no LaTeX são: part, chapter, section, subsection,
subsubsection, paragraph, subparagraph, page, figure, table, footnote, mpfootnote
(rodapé dentro do minipage) e equation.
Então, alterando o \the<contador>, alterará como será impresso estes contadores.
Por exemplo, yrenewcommandí\thepageYfVWromant{page}) alterará a enumeração das pá-
ginas para 1, ii, ill, etc.
O estilo de enumeração \roman acima, podem ser
\\\arabic que é 1,2,3..
\alph queé a, b,c
\Alph que é A, B, C
\roman que é , ii, ii
\Roman que é 1, II, IMI
\fínsymbol que é sequencia de símbolos (pode ser usado no rodapé, se {or pouco}.
\eja Exemplo 12.2.
Exemplo 12.2: ex12-contadores.tex
A página atual é \thepage.
Seção atual em romano minúsculo é \roman{section}.
A página atual é 91.
Seção atual em romano minúsculo é iii.
As vezes, precisamos ajustar valores iniciais dos contadores, tais como das páginas,
listas enumeradas, etc. Para isso, usamos os comandos \setcounter, \stepcounter e
\addtocounter. Para decrementar, use o valor negativo no parâmetro de \addtocounter.
No caso de listas enumeradas, os contadores são enumi, enumii (sub lista), enumiii
(subsub lista), enumiv (subsubsub lista).
Para que estes contadores sejam impressos na fonte reta, mesmo no ambiente em itálico
(enunciado do teorema, por exemplo), acrescente
\renewcommandí \labelenumi-í\textuplVWtheenumi .))
\renewcommandí\labelenumiil)í\textupt(\theenumii)))
\renewcommandí\labelenumiii-fWtextupíltheenumiii.))
\renewcommandfWlabelenumivYí\textupí\theenumiv.))
no preamble do documento.
Ajuste adequadamente como ficará o rótulo (label) de cada ítem (no exemplo anterior,
no nível 2, ficará entre parenteses e outros níveis será seguido pelo ponto).
Além disso, o contador novo pode ser criado por inewcounter, útil para ser usado no
ambiente/comando novo a ser criado.
Aqui, vamos criar um contador para testá-los. \eja o Exemplo 12.3.
Exemplo 12.3: ex12-newcounter.tex
\newcounter{testel} % cria e inicializa com o valor zero.
\setcounter{teste}(1) % novo valor
O contador é \theteste.
O contador em \textttiAlph) é \Alphítestel.
Adicionando 1 e usando.
\refstepcounterítestelNlabelícount:teste).
Novo valor é \theteste.
Adicionando por 1 de novo \addtocounter{teste}(1)
Novo valor é \theteste.
O valor atribuído no rótulo \textttícount:testel) após o \\textttí
re{stepcounter} é \refícount:teste).
Agora, a lista enumerada começando de $3$
\begin{enumerate}\setcounterfenumiY(2)
\item Um item.
\item Outro item.
\end{enumerate}
O contador é 1.
O contador em Alph é A.
Adicionando 1 e usando. . Novo valor é 2.
Adicionando por 1 de novo Novo valor é 3. O valor atribuído no rótulo count:teste
após o refstepcounter é 2.
Agora, a lista enumerada começando de 3
3. Um item.
4. Outro item.
Para que o Mlabelí) pegue o valor atual do contador, use o \refstepcounter que
incrementa o contador por um e atualiza o valor para \label.
Para pegar o valor de um contador (para ser usado como argumento para \setcounter,
por exemplo), use o comando \alue.
Muitas vezes, um contador está vinculado no outro e quando outro for incrementado,
ele será reinicializado. Além disso, contadores vinculados aos outros imprimem dois valores
(contador do outro mais dele).
Este vínculo pode ser criado pelo comando \counterwithinfí<contador>Yí<pai>).
Quando o <pai> for incrementado, o <contador> é reinicializado. Por exemplo, para que a
enumeração da equação seja da forma <no. do capítulo>.<no da equação>, basta colocar
\counterwithin{equation}í{chapter} no preamble do documento. Observando que, para
LaTeX versão anterior a 2018/04/01, requer o pacote chngcntr.
Para eliminar um vínculo, usa-se o comando \counterwithout. Outra forma é usar o
comando Yêremovefromreset. Por exemplo, para remover o vínculo do contador da equação
com o contador da seção, coloque o código
\counterwithout{equationYtsectiony}
%" makeatletter
% \oremovefromresetíequationk+{section}
12.3. Contadores
%\makeatother
no preamble do documento.
Mais sobre manipulações dos contadores, veja o [wik18, Capítulo 3, Seção 3].
13. Mais Alguns Cuidados e Ajustes 94
Capítulo 13
Mais Alguns Cuidados e Ajustes
Neste capítulo, veremos mais alguns ajustes e incrementos no documentos.
13.1. Comandos frágeis
Existem comandos denominados frágeis por poder causar problemas quando é passado como
parâmetros de alguns comandos ou ambientes. Por exemplo, o argumento do \\chapter e
\section costumam ser usado no sumário também. Se colocar comando que tem contadores
ou o \\\footnote, causará problemas, pois incrementará contadores duas vezes, ou tentará
colocar rodapé também no sumário.
Assim, quando colocar comandos no argumento da função que usam o seu parâmetro
em mais de um lugar, requer cuidados. Além dos comandos de seccionamento (chapter,
section, etc), caption, thanks, comandos que produz saída do cabeçalho como \markboth,
etc, também usam o seu argumento em mais de um lugar.
Os comandos que causam problemas quando é passado para argumento destes comandos
são chamados de comandos frágeis e deve ser precedido de \wprotect para prevenir problemas.
Alguns comandos frágeis são: comandos com argumento opcional, ambientes, fórmula
no modo displaystyle, fórmula no modo textstyle delimidado por Y( e ) (no entanto,
delimitado por “$” não é frágil), \phantom, “AW”, \item e \footnote.
\eja Exemmplo 13.1.
Exemplo 13.1: ex13-fragil.tex
\sectionfíSublinhando textoWprotectNWfootnoteíForma antiga de enfatizar o
textol)) %Z footnote é frágil: usar \protect
\idots
\sectioníSobre a famosa fórmula $a 2=b"2+cP2$8Y % delimitado por "$" não é
frágil
\idots
\beginfífigureY [hbp!]
\center
Figura aqui.
\captioní$\Gamma {ij} fNprotectWphantom{ij}+2)$Y % \phantom é frágil
\endífigurey
\ldots
1.1 . Sublinhando texto!
1.2 Sobre a famosa fórmula aº = b? + c?
Figura aqui.
Figura 1.1: 1';-]-2
9Forma antiga de enfatizar o texto
13.2 Babel e nomes
O pacote de internacionalização babel oferece regra de hifenização e nomes dos elementos
tais como capítulo, figura, tabela, sumário, etc em vários idiomas. Para carregar mais de
um idioma, coloque os idiomas separado pela vírgula no parâmetro do babel. O idioma do
último será considerado padrão e outros são opcionais que podem ser ativados quando quiser.
Mas, se preferir, poderá usar “main=<idioma>” na lista de parâmetros para indicar o idioma
padrão.
Seleção de idiomas pode ser alterado por \selectlanguageí<idioma>). Para demarcar
somente um trecho como outro idioma, usa-se o ambiente otherlanguage. Para trecho bem
curto, poderá usar também o comando \\foreignlanguage. \eja Exemplo 13.2.
Exemplo 13.2: ex13-babel.tex
\documentclass [12pt,a4paper] {article}
\usepackage [T1] {fontenc}
\usepackageTamsmath,amssymb]>
\usepackage [english,brazil] {babel})
%& Dados para títulos
\title{Exemplo}
\authoríSadao Massagol % caso de mais de um autor, separe com o comando \and
\dateíFevereiro, 2018
\obegin{document}
\naketitle
\begin{abstract}
Resumo aqui.
\end{abstract}
\begin{otherlanguage})fTenglishy
\begin{abstract})
Abstract here.
\end{abstract}
\end{otherlanguage}
& \tableofcontents & so se for artigo longo
\sectioníMudando o idioma de um trecho)
O trecho curto pode ser no outro idioma como em *"\foreignlanguagetenglishYí
This is english)''.
Para trechos maiores, use o ambiente \textttiotherlanguagek como em
\beginí{quote}
\begin{otherlanguagelTtenglish}
This environment switches all language-related definitions, like the
language specific names for figures, tables etc. to the other language.
\end{otherlanguage}
\end{quote}
\ldots
” referência biliográfica
\end{document}y
Exemplo
Sadao Massago
Fevereiro, 2018
Resumo
Resumo aqui.
Abstract
Abstract here.
1 Mudando o idioma de um trecho
O trecho curto pode ser no outro idioma como em “This is english”. Para trechos maiores,
use o ambiente otherlanguage como em
This environment switches all language-related definitions, like the language
specific names for figures, tables etc. to the other language.
H “ Z ” .« H ” « E&riPº
Para escrever o nome tais como “Capítulo”, “Figura”, “Sumário”, etc, tem os comandos
que produz estes nomes. Redefinindo apropriadamente estes comandos, podemos alterar a
sua saída.
Alguns nomes pré definidos são: NVabstractname (somente article e report),
\appendixname, \bibname (somente book e report), \\chaptername (somente book e
report), \contentsname, \figurename, \indexname, \listfigurename, \listtablename,
\partname, \refname (somente article), \tablename.
\ote que o nome para referência bibliográfica no livro e relatório são \bibname enquanto
que no artigo, é ywrefname.
Alguns pacotes definem o nome usado para seus pacotes. Por exemplo, amsthm que define
o ambiente proof, define também \proofname.
Para alterar ou definir novos nomes quando usa o babel, requer usar o recurso do babel,
pois nomes pré definidos, quando usa o babel, são redefinidos dinamicamente quando altera
os idiomas.
Assim, deverá definir/redefinir os nomes dentro do comando \captions<idioma> onde
<idioma> é o nome do idioma. Mas, se redefinir o captions, perderá as definições anteriores
feitas pelo babel. Logo, utiliza o comando \addto do babel que acrescenta porções de código
no final do comando especificado.
Por exemplo,
\addtoWcaptionsbrazilt%,
\renewcommandWrefnameíReferências Bibliográ{icas}%
D
no preamble altera o nome da referência bibliográfica no caso de artigos quando usa o
idioma brazil.
\ote que, no caso de português brasileiro, tanto pode usar o brazil como o brazilian.
Assim, se estiver implementando um pacote na qual não sabe qual opção o usuário final vai
usar, precisará redefinir em ambos idiomas. Neste caso, define um comando auxiliar e coloca
em cada um dos idiomas.
\providecommandí\theoremname)tTheorem) % Providenciando novo nome com valor
padrão
\necommandí\braziliannamesYT%,
\renewcommandNWrefnameíReferências Bibliográ{icas}/
\renewcommandí \theoremname|{Teorema}%
D7
\newcommandfVenglishnames+tT%
\renewcommandf \theoremname+{Theorem}%,
F
\addtoWcaptionsbrazilí\braziliannames)
\addtoVWcaptionsbrazilian{\braziliannames}
\addtoYcaptionsenglishí\englishnames)
\addtoWcaptionsamericanfí\englishnames)
\newtheorem{theorem}í\theoremname]+ [section]
no preamble após carregar o pacote babel habilita suporte para português brasileiro e
inglês. \ote que no mewtheorem, está usando o comando \theoremname que será redefinido
automaticamente quando o idioma muda. \eja o exemplo 13.3.
Exemplo 13.3: ex13-babel-caption.tex
\documentclass [12pt,a4paper] {articley}
\usepackage [T1] {fontenc}
\usepackageTamsmath,{amssymb}
\usepackage{amsthm}
\usepackage [english,brazil] íbabely
\providecommandí\theoremnameY{Theorem} % Providenciando novo nome com valor
padrão
\newcommandfí\braziliannamesYT%
\renewcommandyrefnameíReferências Bibliográ{icas}%
\renewcommandí\theoremname(íTeoremal%
J”
\newcommandfVenglishnamesY1%
\renewcommandf \theoremname+{Theorem}'%,
D
\addtoVWcaptionsbrazilí\braziliannames)
\addtoWcaptionsbrazilianí\braziliannames)
\addtoYcaptionsenglish{\englishnames}
\addtoWcaptionsamerican{\englishnames}
\newtheorem{theorem}(\theoremname+ [section]
\title{Exemplo}
\authoríSadao Massago)
\dateíFevereiro, 2018
\begin{document}
\naketitle
\begin{abstract})
Resumo aqui.
\end{abstract})
% \tableofcontents % so se for artigo longo
\sectioníTeoremas multi lingue)
\begin{otherlanguageltenglish}
\beginf{theorem}
\ldots
\end{theorem}
\end{otherlanguage}
\begin{theorem}y
\ldots
\endttheorem)
\beginfthebibliographyYf99Y
\bibitem[GMSO04] ([Goossens : 2004
Michel Goossens and Frank Mittelbach
\emphíThe {NLaTeX} companion (second edition)), Adilson--\esley, 2004.
\endíthebibliographyY
\endí{document}
FExemplo
Sadao Massago
Fevereiro, 2018
Resumo
Resumo aqui.
1 Teoremas multi lingue
Theorem 1.1. ..
Teorema 1.2.
Referências Bibliográficas
[GMSO04 ] Michel Goossens and Frank Mittelbach The LaTeX companion (second edition),
Adilson-\esley, 2004.
\ote que, se usar a opção de idiomas como opção de documentos (no \documentclass,
o pacote babel reconhece este idioma e vai usar, mesmo que não tenha passado opções no
babel.
13.3  Sobre espaçamentos entre linhas e “estouro de li-
nhas”
O espaçamento entre linhas é definido pelo comando \l inespread onde \l inespreadí1!.3) é
o espaçamento um e meio e \linespreadt1.6) é o espaçamento duplo, o que atuará a partir
do próximo parágrafo.
\ote que o LaTeX deixa “estourar” as linhas (Overfull \hbox) quando não consegue
acomodar devidamente o conteúdo nas linhas. Para que ele use o espaçamento grande entre
elementos (Underfull \hbox) em vez de “estourar linhas”, coloque \sloppy (para voltar, use
\\{ussy}. \ote que, independente de linha estar “estourando” ou “espaçando demais”, deverá
checar cada um deles para ver se não está prejudicado visualmente e se for o caso, resolver o
problema.
13.4 Sobre hifenização
O pacote babel carrega a regra de hifenização para o idioma selecionada, mas as vezes
encontramos as exceções na qual a regra do babel não funciona devidamente. Neste caso,
poderá indicar na palavra de texto, a posição que pode ser hifenizada por "N-” como em
rel-felW-rên-\lcia.
Este comando é ignorado quando não há necessidade de hifenização. Quando precisar,
será hifenizada somente nestes locais.
Em geral, quando encontra uma palavra hifenizada indevidamente, poderemos querer acres-
centar regra de hifenização para tal palavra em vez de indicar localmente. Para tanto, coloque
o comando \hyphenation onde seu argumento é a lista de palavras separados pelo espaço,
“ »
onde cada palavra contém na posição de hifenização. \ote que, para colocar regra de hifeni-
zação das letras acentuadas pelo comando \hyphenation, requer \vusepackage [T1] {fontenc}
ou similar para ativar fontes que suportam acentuações.
o seguinte trecho de código colocado depois do carregamento do pacote babel no preamble,
acrescenta hifenizações das palavras correspondentes.
% regra de hifenização das palavras não acentuadas:
% não requer \usepackage[T1] ({fontenc})
\hyphenationíli-vro tes-te cha-ve bi-blio-te-cal
% regra de hifenização das palavras acentuadas:
% requer \usepackage [T1] ({ontenc}
\hyphenationfíco-men-tá-rio re-fe-rên-cia)
Para que ele não hifenize, é só colocar dentro de uma caixa, o que pode ser feito pelo
comando \mbox. O código do tipo \nboxínão hi{enizar} não pode ser quebrado em li-
nhas, mesmo na posição de espaços. Este recurso permite proibir hifenização das palavras
localmente.
Para que não use a hifenização no documento inteiro, costuma aumentar o valor da
penalidade de hifenização no preamble do documento, como em
\\hyphenpenalty=10000
\exhyphenpenalty=10000
13.5 Trocando fontes
Fonte padrão do LaTeX é Computer Modern desenhado especialmente para ele, mas existem
outras fontes incluídos no TEX que podem ser usados.
Em geral, selecionar fontes manualmente requer cuidados e conhecimento sobre tipografia
para não combinar fontes incompatíveis. Portanto, recorremos aos pacotes desenvolvidos
pelas especialistas no assunto.
Vamos ver como usar a fonte Times que é uma das fontes populares. Para selecionar a
fonte times, usa o pacote mathptmx. Basta colocar yusepackage{mathptmx} no preamble
para que fontes fiquem como Times.
Para o Palatino, use o pacote mathpazo com o comando \usepackagetmathpazo].
Ainda existem várias outras fontes que vem em qualquer distribuição TEX, assim como
fontes adicionais do TEX mais completo.
13.6 Trocando marcador da lista itemizada
A marca de itens da lista itemize também pode ser redefinidas. Por exemplo, o código
\renewcommandí\labelitemi)í$\bullet$
\renewcommandí\labelitemii)í$\cdot$)
\renewcommandí \labelitemiii)(í$\diamond$>
\renewcommandí\labelitemivXí$yYast$>
ajustado adequadamente no preamble faz isso.
13.7 / Cores no LaTeX
O pacote color (carregado automaticamente pelo pacote graphicx) oferece recur-
sos básicos para trabalhar com cores no LaTeX. Aqui, vamos supor que oO
\usepackage{Tgraphicx} já está no preamble. Para poder referenciar cores pelos nomes,
coloque \usepackage [usenames] fcolor+ no preamble também.
Os comandos de cores usam o parâmetro opcional para indicar o modelo. Se for omitido,
será assumido o que foi especificado na hora de carregar o pacote color. Como estamos
supondo que vai usar a opção usenames na opção do pacote color, se o modelo for omitido
nos comandos de cores, será assumido como named (por nomes).
A cor é especificado pelo comando \color [modelo] {cor}, mas lembre-se de proteger
o trecho pelas chaves para que a cor retorne ao padrão fora dele. Para a cor do fundo
(das páginas), usa-se o comando \pagecolor [modelo] í(cor). No caso do trecho de tex-
tos, podemos usar os comandos \textcolor [modelo] fcor+{texto} (texto com cor especi-
{icado}, \colorbox [modelo] fcork{texto} (caixa de texto com cor do fundo especi{icado}
