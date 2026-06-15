LaTeX 2- Via Exemplos
Sadao Massago
07 de março de 2026
DFQM-UFSCar - Campus de Sorocaba, SP (http://dfqm.sorocaba.ufscar.br/)
Copyright 2018-2025 por Sadao Massago. Todos os direitos reservados. Este documento
é software livre; podendo ser redistribuído e/ou modificado de acordo com os termos da
Licença Pública do Projeto LaTeX (LPPL); versão 1.3c da Licença, ou (se for sua opção)
qualquer versão posterior. \eja http://www.latex-project.org/lppl.txt.
A versão atual deste documento está disponível em
https://ctan.org/pkg/latex-via-exemplos
“\inguém é tão pobre que nada possa dar e ninguém é tão rico que não precise receber”
(Alvaro Granha Loregian)
Sumário
1 Introdução 1
1.1º Uma breve história
1.2 Como usar LaTeXc ccecc 0 1
2 Iniciando um Documento 3
2.1º Primeiro documento. 3
2.2 Mensagem de erro e COrreçãoc e00 0AA 5
2.3 Caracteres especiais 5
3 Introdução às Fórmulas Matemáticas Á
3.1º Fórmula textstyle edisplaystyle ./00// /. 7
3.2 Modo displaystyle no meio do texto .. 9
3.3 Equação enumerada e referências cruzadas
4 Estrutura de Texto 11
4.1º Alinhamentos
4.2 \otas de rodapé e ênfase de texto
4.3 Listas. 13
4.4 Tabelas
4.5 Ambiente de tabulação .c.000000 20
4.6 Textos de citações, versos e verbatim
4.7 Caixaminipage. A 24
4.8 Colunas múltiplas de texto
5 Aprofundando nas Fórmulas Matemáticas 29
5.1/ Usando algumas fontes matemáticas ..0/ .2 Texto, função por partes e matrizes . 3l
5.3  Delimitadores, chaves e integrais
5.4  Quebrando fórmulas em várias linhas .
5.5º Nome sobre setas e delimitador empilhados
5.6 Subequações.7 Acentuação no modo matemático
6 Definindo Comandos e Ambientes
6.1º Definindo comandos
6.2 Criando ambientes
6.3  Quebrando o código em várias linhas .
7 Divisão Lógica de Documentos
7.1 Capítulos, seções e similares .
7.2 Capa, conteúdo frontal e principal
7.3 Limpando o verso das páginas .
7.4 Efetuando pequenos ajustes ..0 .
8 Teoremas e Similares
8.1 . Criando ambiente para teoremas .0c 000 A
8.2 Parâmetros Opcionais .
9 Figuras, Tabelas e Imagens Externas
9.1º Figuras flutuantes.
9.2 Tabelas flutuantes
9.83 Tabelaslongas
9.4 Imagem externa.c.0000
9.5 Desenhando sobre a imagem externa0.000
9.6 Caixasgráficas
10 Ajuste das Fontes
10.1 Seleção da família de fontes ..
10.2 Seleção de formas e peso das fontes .
10.3 Tamanho das fontes
10.4 Ajuste de fontes no modo matemático/0. .
11 Referências Bibliográficas e Índice Remissivo
11.1 Referências bibliográficas
11.2 Usando o BibTeX .
11.3 Indice remissivoc A
12 Medidas e Contadores
12.1 Unidade de medidas e espaçamentos
12.2 Medidas
12.38 Contadores
13 Mais Alguns Cuidados e Ajustes 94
13.1 Comandos frágeis
13.2 Babel enomes
13.3 Espaçamento entre linhas .
13.4 Sobre hifenização
13.5 Trocando fontes .
3.6 Trocando marcador da lista itemizada
13.7 Cores no LaTeX
13.8 Uso de Caixas
14 Algumas Dicas Para Criar Comandos e Ambientes 105
14.1 Comandos com “” e LLc AA 105
14.2 Ambiente com parâmetro na finalização e aplicação do comando .
14.3 Comandos definidos dentro do outro comando ..
14.4 Adicionando os código nos comandos e ambientes existêntes
14.5 Usando \ewDocumentCommand e \ewDocumentEnvironment .
15 Usando Pacotes Fora do base e required 123
15.1 Configuração das páginas
5.2 Estilo europeu
5.3 Cabeçalho e títulos .
15.4 Ajustando O sumário .
15.5 Links.
15.6 Controle das listas e listas inline
15.7 Trocando as fontes — parte 2. 139
15.8 Texto somente com contorno, sombreado e degradê
5.9 Circulando o texto
15.10Escrevendo medidas internacionais
15.11Calculando o valor de uma função
15.12Controle das figuras e similares .
15.13Criando ambientes tipo figuras e tabelas . 153
15.14Melhorando as tabelas
15.15Moldura, enumeração das linhas e marca dágua.. o 161
15.16Algorítmo e código fonte .
15.17Ênfase modo antigo e cancelamento .
5.18Mais sobre referências bibliográficas
15.19Siglas e glossários .
16 Gráfico e Diagramas 182
16.1 Misturando cores. 182
16.2 Criando ilustrações gráficas
6.3 Mais um pouco sobre sobreposição
17 Produzindo Poster e Slides 202
17.1 Poster.
17.2 Slides Usando XeLaTeX e LuaLaTeX 214
18.1 LuaLaTeX e XATEX
18.2 Fontes no XeLaTeX/LuaLaTeXc e 218
18.3 Usando em conjunto com BiblBTKEX .
19 Diagramando na \orma ABNT 225
19.1 Documentos em ABNT Luc ccccc cccA 225
19.2 Documento ABNT usando ABNTexto .
19.3 Usando o estilo ABNT no BibTeXe c 243
9.4 Usando o estilo ABNT no BibLaTeX
9.5 Tabelasem ABNT ..c cce cc 250
A Símbolos Básicos de LaTeX 255
A.1 Caracteres especiais e acentuação no modo TEX .2 Símbolos no modo texto
A.3 Símbolos matemáticos
A.4 Nome das funções e delimitadores no modo matemático0
A.5 Outros símbolos .
A.6 Acentuação no modo matemático .
B Desenvolvendo Pacotes e Classes 269
B.1 Criando pacotes.
B.2 Criando classes
B.3 Preenchendo o documento para teste .c.000000 282
B.4 Observação
C Usando o Editor LyX 284
C.1 \isualização do documento final
C.2 Antesdeusar o LyX
C.3 Acertando a configuração do documento .c.c0000 00 286
C.4 Inserindo o comando de LaTeX .
C.5 Formatando textos .
C.6 Lista, sublista e similares
C.7 Matemática
C.8 Observação adicional .
D Para Organizadores do Evento
D.1 Certificado com mala direta no LaTeX
D.2 Gerando crachá pela mala direta.
D.3 Caderno deresumosc.00000 AAA
D.4 Folhetos
D.5 Poster soisticado, revistas e brochuras
E Para Professores
E.1 Cancelando ou anotando equações. .. A
E.2 Lista de exercícios € provas
E.3 Comesemrespostas .cA
F Para Projetos
F.1 Pacote standalone . A
F.2 Dividindo o documento em vários arquivos .
F.3 “ºTodo” (tare{as} ..c
G Alguns Aplicativos Auxiliares para Usuário de LaTeX
G.1 Editor para LaTeX ..c
G.2 Editor gráfico .
G.3 Gráfico científico
G.4 Alguns convertores .
G.5 Outras ferramentas . .000000
G.6 Algumas alternativas a LaTeX/.
Alguns Comentários Finais
Referências Bibliográficas
Indice Remissivo
Lista de Exemplos
2.1
2.2
2.8
3.1
3.2
3.3
3.4
4.1
4.2
4.3
4.4
4.5
4.6
4.7
4.8
4.9
4.10
4.11
4.12
4.13
4.14
4.15
4.16
4.17
4.18
4.19
4.20
4.21
4.22
5.1
5.2
5.8
exO2-minimal.tex .
exO2-inicial.tex
ex0O2-caracteres.tex .
exO3-formulas.tex .
exO3-simbolos.tex .
exO3-displaystyle.tex
exO3-ref.tex
exO4d-alinhamento.tex .
exO4d-nova-linha.tex .
EexO4d-rodape.tex .
exO4d-enfase.tex.0. 00 13
EeXO4-listas.tex .
exO4-sublistas.tex
exO4d-enumerate.tex .
exO4d-tabular.tex
exO4d-multicolumn.texexO4d-cline.tex
exO4d-deolumn.tex .
exO4-tabularx.tex
exO4-tabbing.tex
EexO4d-quote.tex
exO4d-quotation.tex
EXOA-VEISE LLL A A 23
exO4d-verbatim.tex. .
exO4d-verb.tex
exO4d-minipage.texc
exO4-minipage-fbox.tex ..
EXO4-ParboxX.tex .
exO4d-multicols.tex. .. 27
exO5-mat-fontes-basico.tex .
exO5-mat-text.tex .l
EeXOS-Matriz.tex
5.4
5.5
5.6
5.7
5.8
5.9
5.10
5.11
5.12
5.13
5.14
5.15
5.16
5.17
5.18
6.1
6.2
6.3
6.4
T.5
7.6
8.1
8.2
9.1
9.2
9.3
9.4
9.5
9.6
9.7
9.8
9.9
9.10
9.11
9.12
10.1
exOS-delimitador.tex
exO5-delimitador-grande.tex ./0/0/ / 33
EXOS-bracos.tex
EexXOS-integrais.tex .
EXOS-SPplit.tex
exOS-cases-aligned.texc . 35
exOS-gather.tex
exOS-multiline.tex .
exOS-align-star.tex
exOS-intertext.tex .
exOS-stackrel.tex
exO5-binom.tex, parte €
exOS-subequacao.tex
EXOS-acentos.texc e A A A 41
EXOS-NEegacao.texc e R 41
exO6-newcommand.tex .
exO6-parametro-opcional.tex .
exO6-ambiente.tex
exO06-comando-multlinhas.texc ///A 47
exOT-capitulo.tex
exOT7-capitulo-star.tex
exOT-mMatter.tex .
exO7-maketitle.tex
exOT7-article.tex
exO7-clearpage.tex
EXO8S-teorema.tex .
ex0O8-teorema-parametro.tex .
exOI-figura.tex
exO9I-figura-fbox.tex .
exO9-tabela-flutuante.tex . ..0. /A 62
exOI-tabela-tabular.tex. .
exO9-longtable.tex
EXOOD-iMmMagem.tex
exO9-imagem-rotacao.tex.
ex09—imagem—Íado.teX
exO9-imagem-sobreposicao.tex .
EXOI-PiCture.tex .
exOI-scale.tex
exOI-rotate.texc 7TO
exlO-family.tex
10.2 exlO-Series.tex. .B
10.3 exlO-Size.tex.
10.4 exlO-fontes-mat.tex .
10.5 EX1IO-Mnegrito.tex .c T7
11.1 exll-bib.tex
11.2 exll-cite.tex.c
11.3 exll-bibtex.bib
11.4 Exll-index.tex. .2. . e 85
12.1 exl2-espacos.tex
12.2 exl2-contadores.tex ..
12.3 exl2-newcounter.tex
13.1 exl3-fragil.tex . 94
13.2 exl3-babel.tex. ..c
13.3 exl3-babel-caption.tex
13.4 exl3-Color.tex .
13.5 exl3-Caixa-fDox.tex .
13.6 exl3-CaixaSs.tex
13.7 exl3-rule.tex
14.1 exldstar.texc
14.2 exldkeyval ..c
14.3 exld-keyvalenv .
14.4 exl4-parametro-finilizacao.tex .
14.5 exl4-comando-no-corpo-do-ambiente.tex .. . 111
14.6 exl4-comando-no-corpo-do-ambiente-amsmath.tex0 111
14.7 exl4-comando-no-corpo-do-ambiente-environ.tex
14.8 exl4-comando-aninhado.tex .c
14.9 exl4-comando-let.tex .
14.10exl14-comando-aninhado-com-parametro.tex ..0.0. /. 113
14.11exl4-comando-def.texc ../ 114
15.1 exl5-lettrine.texc // A 125
15.2 exl5-lettrine-b.tex
15.3 exl5-fancyhdr.tex.
15.4 exl5-fancyhdr-oneside.tex
15.5 exló-titlesec.tex . ..c
15.6 exl5ó-caption.tex ..c
15.7 exl5-tocloft.tex .
15.8 ex-d-enumitem.tex
15.9 exl5-cContour.tex
15.10exl5-shadow.texc e A 141
15.1lexl5-gradient.tex ..
15.12exl5-texteireled.tex
15.13exl5-circledtext.tex
15.14exl5-mum.texc
15.15exI5-SLtEX .
15.16ex15-Sisetup.tex .
15.17exl5-xfp-e-numerica.tex
15.18exl5-float.tex
15.19exl5-subcaption.tex
15.20exl15-\wrapfig.tex
15.21lexl5-wrapstuff.tex
15.22ex15-pdflscape.tex
15.23exl5-newfloat.tex .
15.24exl5-booktabs.texc .// /. 154
15.25exl5-xcolor-table.tex .
15.26exl5-table-tblr.tex
15.27exl5-table-longtblr.tex
15.28exl5-siunitx-table.tex. .
15.29exl5-siunitx-long-table.tex .
15.380ex15-fancyboxX.tex.
15.8lexl5-framed.tex .
15.32ex15-postit.tex
15.383exl5-lineno.tex
15.34exl15-alg.tex
15.35ex15-listings.tex .
15.36Bhaskara
15.37exl5-Showexpl.tex.c ./. A 170
15.1 exl5-showexpl-completo
15.2 exl5-ulem.texc .// A A 172
15.3 EXxl5-Soul.tex
15.4 exl5-natbib.texc /// A 174
15.5 exl5ó-biblatex.tex
15.6 EXx15-acro.tex ..c
15.7 exl5-glossaries.texc
16.1 exIO-XCcolor.tex
16.2 exl6-tikz-preamble.tex
16.3 exl6-tikz:basico.tex .
16.4 exl6-tikz-draw.tex
16.5 exl6-tikz-parametro.texc 2
16.6 exl6-tikz-coordenadas.tex
16.7 exl6-tikz-Cirele.texc .// 187
16.8 exl6-tikz-foreach.tex
16.9 exl6-tikz-intersection.tex .c.c0000.
16.10ex16-tikz-grafico.tex
16.11ex16-tikz-funcao-tabelada.tex/// 191
16.12ex16-tikz-intersection-plot.tex .
16.13exl6-tikz-pintar.tex .
16.14exl16-tikz-Brid.tex
16.15ex16-tikZz-CUrve.texc
16.16ex16-tikz-SCOpe.tex
16.17exl6O-tikz-Clip.tex
16.18ex16-tikz-region.tex .
16.19exl6-tikz-matriz.tex
16.20ex16-tikz-diagrama.tex .
16.21exl16-imagem-sobreposicao.tex .
16.22exl6-imagem-sobreposicao-tikz.tex
17.1 EXl 7-poster.tex
17.2 exl7-Slides.tex.
18.1 exl8-lualatex.texc ..// A 215
18.2 exl8-fontsetup.texc ..// A A A 220
18.3 exl8-biblatex.bib
18.4 exl8&-biblatex.texc
19.1 exl9-abntex2.tex
19.2 exl9-abntexto.tex .
19.3 exl9-abntex2Cite.texc . 243
19.4 exl9-biblatex-abnt.tex .
19.5 exl9-abnt-table.tex
19.6 exl9-abnt-quadro.tex
A.l ex-a-especiais-acentuacao.texc ../ 255
A.2 ex-a-simbolos-texto.tex .
A.3 EX-A-CONSPYUCao.tex ..
A.4 ex-a-simbolos-basicos.tex ..
A.5 EXA-Brega.tex .
A.6 ex-a-simbolo-binario.tex
A.7 EXx-a-Setas.tex
A.8 ex-a-nome-funcao.tex.
A.9 ex-a-delimitadores.tex
A.10 ex-a-big-delimitadores.tex
A.11 ex-a-tipo-letra.tex.
A.12 ex-a-simbolos-diversos.tex
A.13 ex-a-acentuacao.tex.44 . A 266
A.l4dex-a-alfabeto.tex
B.1 ex-b-estilo.sty
B.2 ex-b-estilo.tex
B.3 Eex-b-classe.els
B.4 Ex-b-classe.tex.
B.5 ex-b-lipsum.tex .
B.6 ex-b-blindtext.tex.
D.1 ex-d-lista-nomes.esv
D.2 ex-d-certificado.tex
D.3 ex-d-cracha.tex
D.4 ex-d-conferencial.tex .
D.5 ex-d-caderno.tex
D.6 exl7-folder.tex
D.7 exl7-fliowfram.tex.
E.1l exce-ccancel.tex
E.2 ex-e-annotate-equations.tex
E.3 ex-e-exsheets.tex
E.4 EX-e-answers.tex
F.1 ex-fstandalone-fig.tex
F.2 ex-Estandalone.tex
F.3 ex-fsubfiles-principal.tex.
F.4 ex-fsubfiles-capitulol.tex
F.5 extftodonotes.texPrefácio
O LaTeX 2- é um sistema de processamento de documentos implementados sobre o TEÊEX.
O objetivo deste documento é apresentar o LaTeX 2- de forma gradativa, usando os exem-
plos. Assim, o documento contém muitos exemplos e suas saídas, o que aumentou considera-
velmente as páginas.
Este documento está dividido em 19 capítulos mais os apêndices.
Do Capítulo 1 até Capítulo 14 utilizam somente os pacotes da base e de required na
qual qualquer sistema LaTeX devem conter. Do capítulo 15 a 18 utilizam os pacotes que não
são da base e de required para incrementar a funcionalidade. Nos apêndices, serão tratados
alguns recursos extras que podem ser interessantes, mas que julgar que não sejam de interesse
de todos.
Capítulo 1 é uma breve introdução sobre o sistema.
Capítulo 2 trata do primeiro documento em LaTeX 2., incluindo introdução à escrita de
textos.
Capítulo 3 introduz sobre fórmulas matemáticas.
Capítulo 4 trata sobre estrutura de textos.
Capítulo 5 é uma continuação do Capítulo 3, tratando sobre fórmulas matemáticas.
Capítulo 6 trata sobre definições de comandos e ambientes.
Capítulo 7 discute sobre divisão lógica de documentos, conhecido como “seccionamentos”.
Capítulo 8 trata de definições e uso dos ambientes do tipo teoremas.
Capítulo 9 discute sobre a criação de figuras e tabelas flutuantes, tabelas longas e inclusão
de imagem externa.
Capítulo 10 trata sobre ajuste das fontes e espaçamentos.
Capítulo 11 trata sobre referências bibliográficas e índice remissivos. BILaTeX também será
introduzido neste capítulo.
Capítulo 12 trata sobre medidas e contadores.
Capítulo 13 e 14 exploram várias possibilidades dentro dos pacotes de base e required
que não foram discutidos nos capítulos anteriores.
Capítulo 15 discute o uso de pacotes fora do base e required para ajuste de documentos.
A partir deste capítulo, serão apresentados pacotes fora do base e required. Isto significa
que os pacotes indicados podem precisar de instalação a parte em alguns sistemas.
Capítulo 16 discute o pacote xcolor especial para cores, e tikz espacial para criar ilus-
trações.
Capítulo 17 ilustra a criação de poster e slides de apresentação.
Capítulo 18 apresenta o uso de XeLaTeX e LualTEX, considerado como a próxima geração
de ETEX.
Capítulo 19 apresenta a formatação no padrão de Associação Brasileira de \ormas Técnicas
(ABNT).
Apêndice A é sobre símbolos básicos do LaTeX.
Apêndice B é sobre como escrever um pacote (arquivo de estilos).
Apêndice C trata de editor LyX que permite elaborar documentos de forma mais visual
como os editores para escritórios, em vez de editar diretamente o código fonte em LaTeX.
Apêndice D trata da mala direta, criação do caderno de resumos, folhetos, etc que são
interessantes para organizadores de eventos.
Apêndice E trata de pacotes úteis para elaborar provas e lista de exercícios.
Apêndice F trata de pacotes interessantes para desenvolver projetos tal como escrever um
livro ou similar.
Apêndice G descreve alguns aplicativos livres interessantes que auxilia os usuários de
ELaTeX.
Sorocaba, março de 2026.
Sadao Massago <sadaoQOufscar.br>
1. Introdução 1
Capítulo 1
Introdução
LaTeX é um sistema de diagramação de documentos profissional largamente utilizados, desen-
volvido sobre o TEX. Para quem entende inglês, os livros impressos recomendados são [Lam94]
e [GMS04]. Outros textos recomendados que podem ser lidos gratuitamente são [OPHS25],
[Tut02] e [wik18]. \ote que a tradução em português brasileiro do [OPHS25] costuma estar
desatualizado em relação à versão original. Então prefira a versão em inglês.
1.1 Uma breve história
O TEX [\nu86] e a fonte padrão Computer Modern, foram desenvolvidos pelo Donald \unuth
em 1977 a 1985. Dos sistemas implementados sobre o TEX, o mas usado é o LaTeX [Lam86]
desenvolvido pela equipe de Leslie Lamport, concluido em 1985. A versão mais utilizada do
LaTeX foi concluído em 1994 que é o LaTeX 2- [Lam94]. Em 2004, o TEX começou a suportar
oficialmente o utf-8, facilitando a elaboração de documentos multi-idiomas. Em 2007, o
XeTEX que suporta o uso de fontes do sistema implementado inicialmente no Mac OSX foi
portado para linux e \indows. Em 2008, o recurso de sincronização do documento fonte com
o PDF tornou fácil e PDF foi substituindo a saída DVI do TEX na diagramação. Em 2010 foi
lançado a primeira versão estável do LuaTEX, considerado como o sucessor do PDFTEX. O
LuaTEX, além de poder usar as fontes do sistema como o XeTEX, também pode estender a
funcionalidade com a linguagem script Lua. Em 2018, o LaTeX passou a adotar a codificação
utf8 como padrão, eliminado a necessidade de especificar explicitamente.
1.2 Como usar LaTeX
O TeX é um sistema de compilação de documentos e o LaTeX é um conjunto de macros
(instruções) para automatizar e facilitar a diagramação de documentos.
O documento é preparado como arquivo texto num editor de texto, compilado pelo LaTeX,
visualizado e corrigido e compilado novamente, até obter o resultado desejado. O arquivo
fonte do documento costuma ser editado no editor próprio para LaTeX tais como TeXMaker
(http://www.xmimath.net/texmaker/) e TeXStudio (https://www.texstudio.org/), am-
bos disponível livremente em várias plataformas. Além de recursos para facilitar a escrever
documentos, eles contam com botões de compilação e visualização, assim como sincronismo
de PDF com o código fonte. Para quem quer a funcionalidade mais próxima dos aplicati-
vos de escritórios que permite visualizar como vai ficar enquanto escreve e quer elaborar
o documento usando botões e menus em vez de digitar comandos, poderá optar pelo LyX
(https://www.lyx.org/) que também é livre e suporta várias plataformas. Para evitar erros
de escrita, é recomendável que ative o corretor ortográfico com idioma desejado, o que depende
de cada editor. Para compilar, deverá instalar alguma distribuição de TEX. Em geral, o mais
recomendado é o TeXLive para Linux, MacTeX para Mac OS e MikTeX para \indows, todos
são livres.
Evite usar o espaço no nome de arquivos para LaTeX, pois o sincronismo do código fonte
com o PDF (posicionar PDF na posição correspondente à linha de código fonte e vice-versa)
pode tornar parcial.
2. Iniciando um Documento 3
Capítulo 2
Iniciando um Documento
Neste capítulo, vamos tratar do básico de como começar um documento LaTeX.
2.1.º Primeiro documento
Um documento em LaTeX inicia-se com o comando \documentclass que especifica qual tipo
de documentos será diagramado. Em seguida, será especificado os pacotes (conjunto de
instruções) adicionais a serem carregados e também será realizada algumas configurações.
Esta parte do documento é chamado de preamble (preâmbulo) do documento. Depois inicia
o conteúdo do documento com \begin{document}, escreve o corpo do documento e finaliza
o documento com \end{document}.
O código minimal do documento e sua saída em pdf (que está dentro da moldura) seria
como do Exemplo 2.1.
Exemplo 2.1: ex02-minimal.tex
\documentclass{article}
\beginfí{document}
Alô pessoal.
\end{document}
Alô pessoal.
Para gerar o arquivo PDF, deverá processar com o LaTeX. Salve o arquivo e clique no botão
de Compilar no caso de TeXMaker e botão LaTeX no caso de TexStudio (na versão mais nova,
é um triângulo verde).
Para documento ser mais funcional, precisará adicionar algumas especificações no docu-
mento, como o tamanho de letra, idioma, etc. Assim, ficaria commo no Exemplo 2.2.
Exemplo 2.2: ex02-inicial.tex
