\angí1;2;{3} NW % grau, minuto e segundo
\angt;;1) W %Z so o segundo
Números
// +- é substituido por + 1 + 2i
0.3 x 10%
1.654 x 2.34 x 3.430
R$27,37 e R$15,00
Ãngulos
10º
5.3º
—1.5º
102/3//
1//
O comando \unit produz unidade de medida de acordo com o seu parâmetro (o comando
da versão 2 equivalente \si também continua {uncionando}. A configuração de saída pode
ser efetuado pelo parâmetro opcional. O \unit, assim como \num e \ang, funciona tanto no
modo texto como no modo matemático.
Em geral, coloca-se pequeno espaço entre valor e medida. O comando \qty automatiza
isso. O comando da versão 2 equivalente é \SI que pode ser usado quando NVqgty não está
disponível como no caso de usar junto com o pacote physics, ou quer colocar símbolo antes
do valor.
Ele tem a forma \qtyLopção] fvalor+[simbolo anterior] {unidade} \eja o Exem-
plo 15.15.
Exemplo 15.15: exl5-si.tex
Entrada literal (Neste modo, não há opção de formatação).
\unitíkg.m/s"{2} W
\unitíg fpolymerl-mol {cat}.s"(-1))
Entrada pelo macro (permite configurar a formatação usando opção do comando
ou do parâmetro do pacote).
\unitT{NkiloNYgramperWsquareNsecond} NW
\unitílgram fpolymer+\mol fcatINperlsecondl
Mais exemplosWY
\unitTfNkiloNgramimetreNperisquareYsecond+ \V
\unitfNWgramiperVcubicyWcentiNWmetre-] N
\unit{\squareWvoltycubicWlumenWperNfarad}I N
\unitfimetreNsquaredWperWgrayWcubicWlux+ N
\unit{lhenryNsecond}
Medidas com valor
NVgtyt1.23H€J.mol f-13.K1-13) W Z modo textual
\gtyt.23e7H{Ncandela} N % como macros
\agty[locale = DE] (1.345){\coulombYperwmole} % Alemanha usa virgula como
decimal também
Medida não numérico
\qgty [parse-numbers = {alse} tx) \metreNYperWsecond)
é mesmo que
$xy, vjunit fWmetre {perWsecond}$
& Comando da versão 2 permite colocar elemento antes do múmero.
%4 Para este exemplo, está arredondando para duas casas decimais.
\SI [per-mode=symbol,locale=DE,round-precision=2,round-mode=places,round-
integer-to-decimal] 11.987) [RN$] (\perkilogram) N % com simbolo R$ antes
Colocar medida após valor usando \erb+\unit+ e
colocar valor já com medida usando \erb+\gty+
pode apresentar diferença no espaçamento. W
\unití{iOlcelsius} NW % valor concatenado com medida
\atyt10H{lcelsius} % valor e medida usando macro
Entrada literal (Neste modo, não há opção de formatação).
kg m/s?
gpolymcr InOlcat 371
Entrada pelo macro (permite configurar a formatação usando opção do comando ou do
parâmetro do pacote).
kgs ?
gpolymermOlcat/ E
Mais exemplos
kgms ?
gem*?
V. m? F
mº Gy * xô
Hs
Medidas com valor
1.23Jmol * K*!
0.23 x 107 cd
1,345 Cmol *
Medida não numérico
xms*!
é mesmo que
xms *
R$1,99/kg
Colocar medida após valor usando \unit e colocar valor já com medida usando \qty pode
apresentar diferença no espaçamento.
10ºC
10ºC
Alguma das medidas padrão são: \ampere, \candela, \kelvin, \kilogram, metre ou
meter, \wnole, \second, MNlitre, icelsius, \wpercent, etc que são muitas. Para saber mais,
consulte o manual do pacote.
Para conversão de medidas, \giga, mnega, \kilo, \\hecto, \deca, \deci, \\centi, umilli,
\mnicro, \nano, etc. são disponíveis.
Exemplo: \agty£20+{NkiloYgram} e mesmo que Mgty({20}{\kilogram}).
Para operar, tem o per, square, etc.
\agty 30 \kiloWmeter per squareNsecond+) é mesmo que
\gty 30 \kiloWmeter/Asecond”2) no modo padrão, mas o segundo não consegue
controlar a formatação por usar forma literal em “/” e ““2”.
A configuração geral de formatação pode ser feito pela opção do pacote ou pelo comando
\sisetup, mas também pode especificar localmente como no Exemplo 15.16.
Exemplo 15.16: exl5-sisetup.tex
\qgty [mode=text] [30)\kiloWmeter \per \squareNsecond]
\qgty [per-mode=power] 30 \kiloWmeter \per \squareNsecond]
\qgty [per-mode=symbol] 130( \kiloWmeter per squareNsecond]
\qaty [per-mode={raction} [30HNKkiloWwmeter perWsquareNsecond+
30 km s ?
30 km s ?
30 km/s?
30 &
A nova versão, apesar de continuar com os comandos da versão 2, separa o comando para
números complexos e com o produto, como pode ver no exemplo de ynum (Exemplo 15.14).
Se o documento já está escrita usando os comando da versão 2 (sem esta separação), poderá
carregar no modo de versão 2, com o comando \usepackagetsiunitx)[=v2].
15.11. Calculando o valor de uma função
Para efetuar cálculo de funções matemáticas no LaTeX, como no caso de tabelar funções nos
pontos dados, podemos usar o pacote xfp ou numerica. O pacote xfp evalua a expressão
matemática normalmente, enquanto que numerica evalua a expressão escrita na forma TeX,
permitindo que mesma expressão pode ser usado tanto para evaluar, como para exibir. Se
usar a opção “comma” no carregamento de numerica, o ponto decimal da saída será virgula
em vez de ponto. O numerica-tables permite tabelar funções rapidamente.
\eja o Exemplo 15.17.
Exemplo 15.17: exl5-xfp-e-numerica.tex
/ASupõe carregada seguintes pacotes: xfp, numerica e numerica-tables
Expressão a ser evaluada: $\sin(\frací\pi)t4))$
Valor pelo \\textttíx{p} é $\fpevalísin(pi/4))S$
Valor pelo \texttt{numerica} (com configuração padrão) é $\evalí\sin(\fracfí
pi)l4)))8,
Tabelando função com \\textttínumerica-tables)
\tabulate [rvar=x,rstep=(tNfrací\pi-(10H),rows=(10+1)]
{isin x} [x=0]
A partir da versão de 2024, o \\textttínumerica-tables) suporta transpor a
tabela.
\tabulate [rvar=x,rstep=TNfrací\pi-t7)),rows=t7+1),transpose] í\sin x) [x=0]
Expressão a ser evaluada: sin(Z)
Valor pelo xfp é 0.7071067811865474
Valor pelo numerica (com configuração padrão) é 0.707107,
Tabelando função com numerica-tables
E sinr
o o
A partir da versão de 2024, o numerica-tables suporta transpor a tabela.
x O 0.4 0.8 1.2 1.6 2 2.4 2.8
sinr O 0.389418 0.717356 0.932039 0.999574 0.909297 0.675463 0.334988
\ote que, o pacote numerica requerido pelo numerica-tables carrega o pacote mathtools
na qual pode apresentar problemas nos comandos \underbracefí) e \overbraceí) quando
diagramado com certas fontes. Para resolver tal problema, quando utiliza o pacote mathtools
diretamente ou indiretamente, como no caso de numerica, coloque o código (dica de https:
//github.com/latex3/unicode-math/issues/582)
\nakeatletter
\AtBeginDocumentt%
\oifpackageloadedímathtools+T
\oifpackageloadedíunicode-math)t
\let underbraceWLaTeXunderbrace
\MletYoverbraceWLaTeXoverbrace
H
1)
”
\nmakeatother
no preâmbulo para corrigir.
15.12  Controle das figuras e similares
As vezes queremos que o elemento flutuante ({iguras e tabelas} sejam inseridas exatamente
no lugar onde foi colocado. Para isso, existe o pacote float que fornece a opção extra “H”
nas figuras e tabelas na qual impede de auto posicionar (manter no lugar). Para usar, é só
carregar o pacote no preamble e usar o “H” como opção de posicionamento das figuras e
tabelas que querem que fiquem no lugar. Outro recurso do pacote float é alterar algumas
configurações do elemento flutuante (como colocar moldura nas {iguras}, e criar um novo
elemento flutuante. \eja o Exemplo 15.18
Exemplo 15.18: ex15-float.tex
\beginífigure+[H] & No lugar
\centering
\begin{tikzpicture}
\draw (0,0) -- (1,0) -- (0.5, 0.5) -- cycle;
\end{tikzpicture}
\captioníFigura no lugar onde {oi inserido}
\endí{igure})
Figura 1: Figura no lugar onde foi inserido
Para colocar subfiguras ou subtabelas, use o pacote subcaption. Tendo
\usepackage{subcaption} no preamble, podemos produzir subfiguras e subtabelas facil-
mente. \eja o Exemplo 15.19.
Exemplo 15.19: exl5-subcaption.tex
\beginífigureY [hbp!]
\centering
\beginísub{igure}[t] T10.45)]inewidth)
\centering
Sub figura aqui.
\captionísub título 1)
\endísub{igure}Z
\beginísub{igure})[t] (0.45)]linewidth)
\centering
Segunda sub figura aqui.
\captionísub título 2)
\endísub{igure}
\captioníUso de sub figural
\endí{igure})
Sub figura aqui. Segunda sub figura aqui.
(a) sub título 1 (b) sub título 2
Figura 2: Uso de sub figura
Se a classe/pacote conflitar com subcaption, poderá optar pelo pacote subfig.
Para que o texto contorne as figuras ou tabelas, poderá usar o pacote wrapfig ou floatflt.
O Exemplo 15.20 ilustra o uso de wrapfig.
Exemplo 15.20: exl5-wrapfig.tex
\beginfíwrap{igure}(1X10.3\linewidth)
\centering
\beginf{tikzpicture}
\draw (0,0) rectangle (3,1);
\endí{tikzpicture}
\captioníFigura com texto contornando)
\endíwrap{igure}
A figura deve ser colocado dentro do ambiente wrapfigure. No exemplo, ""1''
significa left (esquerda) que posiciona a figura a esquerda (e texto a
direita). Se colocar o “""r'' (right), a figura ficará a direita. O
próximo parâmetro é a largura reservada para figura que foi 30NZ% da
largura da linha.
\ote que são contadas junto as outras figuras.
Se pretende colocar tabela com texto em torno dele, use o ambiente \textttí
wraptable), também do pacote \textttíwrap{ig}.
A figura deve ser colocado dentro do ambiente wrapfigure. No
exemplo, “1” significa left (esquerda) que posiciona a figura a
esquerda (e texto a direita). Se colocar o “r” (right), a figura
ficará a direita. O próximo parâmetro é a largura reservada
Figura 3: Figura com texto para figura que foi 30% da largura da linha. \ote que são
contornando contadas junto as outras figuras. Se pretende colocar tabela
com texto em torno dele, use o ambiente wraptable, também
do pacote wrapfig.
Outra opção é usar o pacote vapstuff (Exemplo 15.21).
Exemplo 15.21: ex15-wrapstuff.tex
\beginíwrapstu{f}[c,top=2,type=table,width=\\\dimevalíMlinewidth/3)]
\colorletíshadecolorkígray!30) % cor do fundo
\begin{shaded*}
\captioníTabela com \\textttíwrapstu{f})
\begin{tabular}+{l1r}
primeira linha & 1 W
segunda linha & 2
\end{tabular}
\endíshaded*>
\endíwrapstu{f}
\lipsum[1]
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Ut purus elit, vestibulum ut,
placerat ac, adipiscing vitae, felis. Curabitur dictum gravida mauris. \am arcu libero,
nonummy eget, consectetuer ut leo. Cras viverra me-
id, vulputate a, magna. Do- — Tabela 1: “Tabela com  tusrhoncussem. \ulla et
nec vehicula augue eu ne- wrapstuff lectus vestibulum urna frin-
que. Pellentesque habitant gilla ultrices. Phasellus eu
morbi tristique senectus et primeira linha 1 tellus sit amet tortor gra-
netus et malesuada fames segunda linha 2 vida placerat. Integer sa-
ac turpis egestas. Mauris pien est, iaculis in, pretium
quis, viverra ac, nunc. Praesent eget sem vel leo ultrices bibendum. Aenean faucibus.
Morbi dolor nulla, malesuada eu, pulvinar at, mollis ac, nulla. Curabitur auctor semper
nulla. Donec varius orci eget risus. Duis nibh mi, congue eu, accumsan eleifend, sagittis
quis, diam. Duis eget orci sit amet orci dignissim rutrum.
Para saber sobre os parámetros do wrapstuff, veja o manual.
Quando tem figura ou tabela muito larga, precisará rotacionar a página. Isto pode ser
feito pelo pacote pdflscape.
Para que uma página fique rotacionada, coloque dentro do ambiente landscape. \ote que,
para rotacionar tabelas longas que pode ocupar mais de uma página, deverá usar o pacote
rotating. \eja o Exemplo 15.22.
Exemplo 15.22: exl15-pdflscape.tex
\begin{landscape})
\center
\beginífigureY[H]
\center
\begin{tikzpicture}
\draw[fill=gray!20] (0,0) -- (MWNlinewidth,0) -- (MNlinewidth,5) -- (O, 5) --
cycle;
\endítikzpicture
\captioníFigura larga {rotacionada}
\endí{igure})
\end{landscape}
Bepeuorsezo1 eSIer esnStg :em3tg
Para inserir figuras externas como parte de texto como o logotipo, poderá usar o pacote
inlinegraphicx que disponibilizará o comando \inlinegraphics que tem a mesma sintaxe
do \includegrahics, mas que ajusta a altura e posição à linha de texto. Se quer alterar a
escala, poderá usar a opção scale como em \includegrahics que faz ajuste relativa à altura
da linha de texto.
15.13 Criando ambientes tipo figuras e tabelas
O pacote float permite criar elemento flutuante do tipo figuras e tabelas. O novo elemento
flutuante é crido pelo comando \newfloat. O código
\newfloatíalgorithmY(tbplíloa-+%[section]
\floatnamefalgorithmY(fAlgor{tmo}
cria o ambiente algorithm que auto posiciona e aceita \\caption dentro dele para enumerar
e colocar o título. \eja o exemplo 15.23.
Exemplo 15.23: exl5-newfloat.tex
\beginfalgorithmy
\captioníPrimeiro algorítimoy
Algorítimo aqui.
\endfalgorithmy
Algorítmo 1: Primeiro algorítimo
Algorítimo aqui.
A lista do novo elemento flutuante é criado pelo comando \listof. Para listar algorítmos
criados acima, usa-se o comando MlistofíalgorithmYíLista de algor{tmos}
\ote que o elemento flutuante não pode dividir em páginas, sendo recomendado para
figuras ou elementos menores. No caso do exemplo, o algorítimo pode ser maior, sendo
recomendado dividir em páginas, como ocorre com a tabela longa. Para criar o ambiente do
estilo longtable (tabela longa) na qual pode quebrar entre páginas, mas ficam enumeradas
como os elementos flutuantes, usa-se o pacote caption que permite controlar títulos dos
elementos flutuantes e similares. O código
% definindo o tipo algorítimo
\eclareCaptionTypeítalgorithmtypel[Algor{timo} [Lista de algor{timos}
% ambiente algorítmo configura o caption para tipo algorítimo
\newenvironmentfíalgorithmYí\captionsetupttype=zalgorithmtype))t>
%MNcaptionsetupltype=zalgorithmtype, justification=centering)Y(>
% atalho para lista de algoritmos
\newcommand Ml istofalgorithmsNlistofalgorithmtypes
%4 contador subordinado a capítulo
\counterwithinfalgorithmtypek{chapter}
Cria o ambiente algorithm similar a longtable.
15.14 . Melhorando as tabelas
O pacote booktabs oferece comandos para traçar linhas horizontais com espaçamento ajustado
adequadamente. Use \toprule para linha acima da tabela, inidrule e \cmidrule para linhas
dentro da tabela e \bottomrule para linha abaixo da tabela. No caso de ABNT, encima e
embaixo da tabela é fechada, mas não no lado esquerdo e direito.
\eja a Tablea 15.24).
Exemplo 15.24: ex15-booktabs.tex
\boegin{table}[hbp!]
\begin{center})
\captioníTabela com \textttibooktabs-+\labelítab:booktabs)
\beginítabular+{11}
\toprule
produto & preço À
\nidrule
cenouras (500g) & RNA$0,50 W
cogumelos (vidro de 500g) & RA$5,00 W
batata (1\g) & RN$1,20 W \nidrule Z lhline
total & RN$6,70 W
\bottomrule
\endítabular+)
\end{center}
\end{table}
Tabela 2: Tabela com booktabs
produto preço
cenouras (500g) R$0,50
cogumelos (vidro de 500g) R$5,00
batata (1\g) R$1,20
total R$6,70
Para colorir linhas e ou células da tabela de forma simples, poderá carregar o pacote
xcolor com opção table colocando o código
\usepackage [table] (xcolor)
Se for usar pacote que carrega o xcolor automaticamente, coloque antes do pacote cor-
respondente. Se estiver usando a classe beamer, coloque a opção xcolor=table no beamer
como em
\documentclass [xcolor=table] [beamer]
Com a opção table no xcolor, o pacote colortbl será carregado com ajustes neces-
sários. \ote que pacotes tais como tikz e pdfpages carregam o xcolor. Logo, deve
colocar \usepackage [table] (xcolor] antes de tais pacotes para evitar erros. "Outra
forma de evitar erros é colocar \assOptionsToPackagettable-íxcolorllogo em seguida
do \documentclasst] para que, qualquer pacote que venha a carregar o xcolor passe opção
table para ele. Neste caso, yusepackagetxcolor] pode ser colocado sem preocupação.
Como exemplo,vamos colorir as linhas ímpares de cinza clara para para facilitar o acom-
panhamento das linhas. \eja a Tablea 15.25
Exemplo 15.25: exl5-xcolor-table.tex
\begin{table} [hbp!]
\begin{center}
\captiontíColorindo as linhaskMlabelítab:xcolor)
\rowcolorsí2+íwhitelígray!15)
\beginfítabular+(11)
\toprule
produto & preço À
\idrule
cenouras (500g) & RNA$0,50 \W
cogumelos (vidro de 500g) & RA$5,00 W
batata (1\g) & RN$1,20 N
beterraba (1\g) & RA$1,50 \W
alface (1 maço) & RN$0,50 W
\nidrule Z lhline
\rowcoloríblue!15>
total & RN$8,70 \W
\bottomrule
\end{tabular}
\endfí{center}
\endítabley
Tabela 3: Colorindo as linhas
produto preço
cenouras (500g) R$0,50
cogumelos (vidro de 500g) R$5,00
batata (1\g) R$1,20
beterraba (1\g) R$1,50
alface (1 maço) R$0,50
total R$8,70
Para configuração de cores mais sofisticada, veja o manual do pacote colortb1l.
Para implementação mais moderna da tabela, poderá usar o ambiente tblr do pacote
tabularray que permite incorporar recursos do tabularx como do colortbl, entre outros.
\eja o Exemplo 15.26. \ote que tblr funciona também dentro da fórmula, isto é, pode ser
usado como array. Para usar pacotes adicionais como booktabs, diagbox, etc., usa-se o
comando \seTblrLibrary para que seja configurado devidamente.
Colocando no preamble
\usepackage{xcolor}
\usepackagettabularray)
\seTblrLibrary{booktabs}
poderá usar o código como do Exemplo 15.26.
Exemplo 15.26: exl5-table-tblr.tex
\begin{table} [hbp!]
\begin{center})
\captioníTabela com \\texttt{tabularray})\Mlabelítab:tabulaary)
\beginítblrYt Zconfigurações
colspec = (rX), % alinhamentos/espaçamentos das colunas: l->left, r-> right,
c->center, X->automatic
row{lodd} = fgray!15), %4 cor da linha impar
Arowleven) = {uhite}, 4 cor da linha par
row{1i1} = ffont=\b{serieslsffamily}, % primeira linha
rowi2-Z) = ffont=\s{family}, % linha 2 até a última linhoa
row{Zz} = ffg=bluelk, % última linha
d”
%4 conteúdo da tabela
produto & preço À
\nidrule
cenouras (500g) & RA$0,50 N
cogumelos (vidro de 500g) & RN$5,00 W
batata (1\g) & RN$1,20 \W
beterraba (1\g) & RN$1,50 W
alface (1 maço) & RN$0,50 \W
\bottomrule
total & RN$8,70 N
\end{tblry}
\end{center}
\endítabley
Tabela 4: Tabela com tabularray
produto —preço
cenouras (500g) R$0,50
cogumelos (vidro de 500g) R$5,00
batata (1\g) R$1,20
beterraba (1\g) R$1,50
alface (1 maço) R$0,50
total! R$8,70
O tablarray implementa também a funcionalidade da tabela longa correspondente que
pode ser usado pelo ambiente longtblr, que é mesmo que tblr com a primeira opção opcional
como long, mas não consegue configurar perfeitamente para Associação Brasileira das \ormas
Técnicas (ABNT) somente com comandos padrão, por não conseguir saber se a tabela cabe ou
não em uma única página (2024) (Para ajustar como ABNT, use o pacote tabularray-abnt
explicado na Seção 19.5 do Capítulo 19, na página 250). Como um exemplo de ajuste de
tablas, segue uma configuração parecido com a ABNT no caso de tabela ocupar mais de uma
página.
\usepackage{url} % para endereço web, se hyperref não está carregado.
\usepackage{xcolor} % para colorir tabelas
\usepackagettabularray) % tabularray
\seTblrLibrarylbooktabs) % adiciona booktabs
% configurando
\efTblrTemplateífirsthead-textYíde{ault}í\par-\hfill(continua)) % primeira
página
\DefTblrTemplateflasthead-text ) ídefaultIí\par-\hfill(conclusão)) Súltima
página
\efTblrTemplatefconthead-textXídefaultIfNWpar-\hfill(continuação)) % páginas
do meio
% desativando os rodapés
\efTblrTemplateífirstfoot,middlefoot+ídefault+l>
% redefinindo o título da primeira página
\De{TblrTemplatetcaption}ídefaultYt
\seTblrTemplatefcaption-tagY-íde{ault}
\seTblrTemplateícaption-sep)íde{ault}
\seTblrTemplatefcaption-textXíde{ault}
\seTblrTemplatetfirsthead-textlIíde{ault} % acrescentar o firsthead-text
D”
% redefinindo o título das páginas do meio
\efTblrTemplatef{capcont}ídefaultYt
\seTblrTemplateícaption-tagY-íde{ault}
\seTblrTemplatefcaption-sepYídefaultY
\seTblrTemplatefcaption-text)íde{ault}
\seTblrTemplatetconthead-text)íde{ault}
% redefinindo o título da última página
\efTblrTemplateflasthead+ídefaultH+f
\seTblrTemplatefcaption-tag-íde{ault}
\seTblrTemplatetcaption-sepkíde{ault}
\seTblrTemplatetcaption-textlíde{ault}
\seTblrTemplatetlasthead-textkíde{ault} % acrescentar o lasthead-text
% último rodapé para inserir fonte
\efTblrTemplateflastfoot-textkíde{ault}l) Z inicialmente vazio
\efTblrTemplateflastfootH+ídefaultYl % rodapé da última página
\seTblrTemplateflastfoot-textIíde{ault} % colocar somente o lastfoot-text
% tamanho das fontes
\SetTblrStyleífirsthead-text,lasthead-text,conthead-textYlNW{ootnotesize}
\SetTblrStyleícaption,lasthead,capcontYí\normalsize)
\SetTblrStyleflastfootIíV{ootnotesize}
no preamble para que a tabela do Exemplo 15.27 fique similar ao ABNT. \ote que \legend
é um comando de memoir usado pelo ABNTeX2. Se não estiver usando o ABNTeX2 ou memoir,
deverá substituir com outra, ou providenciar algo como
\providecommand(\legendY [1] (\par \medskip %1 \smallskipy
no preamble.
Exemplo 15.27: exl5-table-longtblr.tex
\efTblrTemplateflastfoot-textIíde{ault }l NMlegendíFonte: \urlíhttps://blog.
nubank.com.br/ipca-2022/HWparWhspaceí3emkVWurlíhttps://brasilindicadores.
com . br/poupanca/]
D
J7
\beginflongtblr>
[
caption = fInflação (IPCA) e juro de poupança de 2022), % titulo
label=ftab:in{lacaol}, % rotulo para referências cruzadas
[
ÃL
%theme=default, % default é tema padrão
colspec = (XXX), % colunas de largura automatica
rowhead = 1, % primeira linha será repetida em todas páginas
row{1} = ffont=\b{series}, % linha de título
rowleven) = fgray!15), % página par em cinza
row{Z} = ffont=\b{series}, % última linha
1”
\toprule
Mês & Inflação & Poupança N
\nidrule
Janeiro & 0,54 & 0,5608 W
Fevereiro & 1,01 & 0,5000 W
Março & 1,62 & 0,5976 W
Abril & 1,06 & O0,5558 \W
Maio & 0,47 & 0,6671 W
Junho & 0,67 & 0,6491 W
Julho & -0,68 & 0,6639 \W
Agosto & -0,36 & 0,7421 W
Setembro & -0,29 & 0,6814 W
Dutubro & 0,59 & 0,6501 W
\ovembro & 0,41 & 0,6515 W
Dezembro & 0,62 & 0,7082 W
\bottomrule
Acumulado do ano & 5,79 & 7,8997 W
\endí{longtblr}
Observe que, nos argumentos dos comandos de configuração, o espaço serão eliminados,
exceto quando estiver dentro do outro comando. Isto melhor a precisão dos cálculos necessários.
Assim, usa-se o comando \space (ou o espaço não quebrável “-”, caso não precise quebrar em
linhas). O pacote tabularray também disponibiliza o ambiente tal 1tblr que pode ser usado
dentro do ambiente table, mas que aceitam os mesmos parâmetros do longtblr, permitindo,
por exemplo, colocar rodapé da tabela, entre outros.
Com o uso de siunitx, poderá lidar com tabelas que tem números flutuantes, como no
Exemplo 15.28.
Exemplo 15.28: exl5-siunitx-table.tex
%5 não funciona?
h
\beginítableY[hbp!]
\begin{center}
\captioníTabela com \\texttt{siunitx}Mlabelítab:siunitx)
\nedskip
\beginítblry
É
colspec = £ X X[r, si=flocale=DEX] |,
row{1} = ffont=\b{series}, % linha de título
rowleven) = fgray!15), % página par em cinzo
row{Zz} = ffont=\bfseries,whitek, % última linha
1”
\toprule
produto & \textípreço] N
\nidrule
cenouras (\qgty{500}í\gram+) & RA$0.50 N
cogumelos (vidro de \qgtyí500X{Ngram}) & RA$5.00 W
batata (\gty{1}{Nkilogram}) & RN$1.20 M
\idrule
total & RA$6.70 N
\bottomrule
\endítblry
\endfí{center}
\endítabley
Tabela 5: Tabela com siunitx
produto preço
cenouras (500 g) R$ 0,50
cogumelos (vidro de 500 g) R$ 5,00
batata (1kg) R$ 1,20
total R$ 6,70
No caso do ambiente tabular, use a especificação da coluna “S”. O exemplo anterior usa o
pacote tabularray, com o comando adicional \seTblrLibraryíbooktabs,siunitx) para
configurar o uso de booktabs e siunitx.
Nas colunas que usam o siunitx, deverá tomar cuidado quando tem o caractere “e” que
é uado para notação científica dos números (na qual tenta interpretar como número). Tais
colunas no ambiente tabular, basta colocar entre chaves para prevenir que seja interpretado
como número, mas no ambiente tblr e longtblr do tabularray, deverá ficar dentro do
comando \text, o que requer cuidados.
\ote que, com o uso de localidade “DE” (Alemão) na coluna de siunitx, os decimais serão
convertidos automaticamente para virgula em vez do ponto. Se quer alinhar devidamente nos
decimais, deverá usar mais opções para “si”, como no Exemplo 15.29, cuja saída foi omitida.
Casos como estes que requer vários parâmetros, poderá configurar com \sisetup antes da
tabela, lembrando que o efeito do \sisetup continuará até que seja reconfigurado novamente.
Exemplo 15.29: exl5-siunitx-long-table.tex
\sisetupt
