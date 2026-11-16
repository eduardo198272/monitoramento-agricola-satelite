# Auditoria de normalização acadêmica — quinta rodada

> **Complemento bibliográfico final — 16/11/2026:** a auditoria individual
> vigente está em [`AUDITORIA_REFERENCIAS.md`](AUDITORIA_REFERENCIAS.md), com
> evidências em `evidencias/revisao_bibliografica_final/`. Foram corrigidas oito
> entradas (EOSDA, UPF, NASA Parameter Dictionary, BIPM, três páginas QGIS e
> páginas de Rouse), sem alterar seções, resultados ou template. BIPM passa a
> 2026 por recomendação expressa da instituição; QGIS passa a 3.44 LTR.
> O adaptador apenas escapa percentuais na projeção TeX da URL da UPF.
> Este complemento sucede os estados de acesso e o PDF descritos abaixo,
> sem apagar as limitações históricas ou reabrir a apresentação institucional.

**Autor:** Eduardo Steffens Hoppen. **Orientador:** Prof. Rafael Rieder.
**Data:** 16 nov. 2026. **Defesa prevista:** dezembro de 2026.
**Comparação:** versão local da quarta rodada, preservada antes dos ajustes.
**PDF desta entrega:** 32 páginas, papel Letter, duas colunas, 22 figuras,
cinco tabelas e **14 expressões numeradas**.

## Estado vigente — acabamento final com template definitivo

O template encaminhado pelo professor foi declarado pelo pesquisador como
**padrão oficial definitivo de apresentação**. A configuração ativa foi
preservada integralmente nesta etapa, incluindo autoria/orientador, filiação,
`dcu`, conjunções das citações, ordem dos resumos, legendas e identidade visual.
Não foi reaberta a escolha do modelo nem reaplicada normalização geral da ABNT.
O registro operacional é `TEMPLATE_INSTITUCIONAL.md`, com hashes em
`evidencias/acabamento_definitivo/template.json`.

Esta etapa alterou apenas dados/projeção bibliográfica, o PDF recompilado e
documentação interna. O texto dos arquivos científicos e os arquivos de
apresentação permaneceram intactos. A referência operacional é o conjunto
ativo de arquivos; não se afirma obtenção de outro pacote independente
durante este acabamento.

### Ajustes bibliográficos pontuais

| Ocorrência | Decisão e evidência | Resultado |
|---|---|---|
| DOI e URL idênticos | Se `url` for exatamente `https://doi.org/` + `doi`, omitir somente a repetição na nota e manter a URL nativa do dcu | 13 ocorrências na base, das quais 11 citadas. Nenhum campo DOI/URL apagado; endereços diferentes continuam distintos. |
| `GITHUB_SDD` | Última alteração do arquivo `spec-driven.md`: 23/06/2026, commit `3cfc81ff316b3ccdca2aa80500b300787d20212e`; arquivo atual e versão datada com hashes idênticos | Ano bibliográfico 2026, identificado como atualização do arquivo-fonte, não como data de criação ou de acesso. |
| `NOMINATIM_POLICY` | Última alteração de `policies/nominatim.md` no repositório oficial indicado pelo próprio site: 11/05/2026, commit `fd6937012a5b2d8f4c0255148342b97191c840e7`; conteúdos atual/datado idênticos | Ano 2026 com nota de atualização; sem inferir a data a partir do ano de acesso. |
| `SENTINELHUB_NDMI` | Última alteração do README da documentação: 04/06/2026, commit `eec561588a5c5dcee3b7f25da6b2e39355f5c4eb`; conteúdos atual/datado idênticos | Ano 2026 com nota de atualização; não se confundem datas de imagens usadas como exemplo com a data da documentação. |
| `BJARNASON2015` | Registro Crossref do DOI confirma local editorial Cham e ISBN eletrônico do livro `9783319186122` | Local e ISBN preenchidos; autores, título, ano, série, volume e páginas preservados. |
| `VAITHILINGAM2022` | Registro Crossref distingue local da editora, New York, NY, USA, do local do evento, New Orleans | Local editorial preenchido sem confundir os dois; demais dados preservados. |
| `GOTEL1994` | Registro DOI novamente consultado; metadados prévios preservados, sem importar automaticamente abreviações divergentes de autoria | Nenhuma substituição de autor ou título por dado não confirmado no texto primário. |

### Datas que continuam sem confirmação exata

As dez referências com datas genéricas foram investigadas individualmente;
três foram resolvidas pelas versões datadas acima. Permanecem sete:

- `USGS_NDMI`: consulta atual terminou em timeout; não foi estabelecida data
  editorial exata a partir das evidências disponíveis.
- `NIST_OUTLIERS` e `NIST_LOCATION`: as páginas específicas não informam data.
  A página inicial do Handbook informa criação em 2003 e atualização em 2022,
  mas isso não comprova a data de cada seção; não foi propagado o ano de 2022.
- `NASA_POWER_METHOD` e `NASA_POWER_PARAMETERS`: não foi localizada data de
  edição da página/dicionário. Datas de cobertura das séries e anos das versões
  dos produtos não foram convertidos em datas dessas páginas.
- `EOSDA_GUIDE`: acesso atual respondeu HTTP 403, sem data verificável.
- `ONESOIL_PLATFORM_DETAIL`: página acessível, sem data editorial identificada.

Nesses casos, a indicação aproximada anterior permanece explicitamente
incerta; não se inventou um ano para eliminar visualmente a pendência.
Datas de acesso efetivamente registradas foram preservadas.

### Validação e preservação

O artigo foi recompilado e todas as páginas foram inspecionadas por IA.
Foram conferidos o uso efetivo de `dcu`, as citações, referências cruzadas,
as 22 figuras, cinco tabelas, 14 expressões numeradas e a base de 32 respostas.
O conteúdo científico, a declaração de IA e os arquivos de template foram
comparados ao estado anterior, sem alteração. A inspeção não é aprovação
humana ou prova física de impressão.

Compilação, evidências bibliográficas, diferenças e preservação ficam em
`evidencias/acabamento_definitivo/`. Não houve alteração do código funcional,
dos dados, dos resultados, commit ou push.

## Registro anterior — revisão de fidelidade ao template UPF

**Registro da revisão anterior, complementado pelo acabamento definitivo acima.**
A normalização geral da ABNT passa a ser complementar à apresentação do
modelo do curso, conforme a nova orientação expressa do pesquisador.
Foram confrontadas a classe local, sua primeira versão no Git (`f4c46a7`),
o backup anterior à quinta rodada e o estado da quinta/sexta rodadas.

`CC-EC_TF-TC.cls` permanece **idêntica à versão introduzida no Git**.
Ela seleciona explicitamente `natbib` com `dcu` na opção `alpha-refs`
(linhas 472–474), define legendas centralizadas com dois-pontos e fontes
9/9 pt (linhas 455–460). O backup anterior à quinta rodada coloca as
legendas de figuras abaixo das imagens. A classe, isoladamente, não impõe
a ordem dos ambientes Abstract/Resumo nem a posição física de cada
`\caption`; por isso, a sequência dos exemplos/backup e a determinação do
pesquisador são distinguidas das definições literais da classe.

### Comparação e decisão por divergência

| Elemento | Modelo local / anterior à quinta rodada | Alteração da quinta/sexta rodada | Restauração necessária e decisão vigente |
|---|---|---|---|
| Fonte, peso e entrelinha do corpo | Merriweather, corpo 9 pt/10,5 pt; matemática com mathastext | Não houve sobrescrita global desses atributos | Preservados. Não se introduziu fonte nova, ajuste artificial de peso ou espaçamento entre letras. |
| Papel, margens e colunas | Letter; margens e `columnsep=18pt` na classe | Não foram substituídos por A4 ou margens de monografia | Preservados literalmente; duas colunas mantidas. |
| Títulos e autoria | Títulos 16/27 pt, autor 13/18 pt, filiação 9/13 pt | Sexta rodada preparou opção de coautoria | Fontes/espaçamentos da classe preservados; Rafael permanece orientador no PDF entregue. |
| Ordem dos resumos | Abstract, Keywords, Resumo, Palavras-chave no backup | Quinta rodada antepôs Resumo; sexta restaurou o inglês primeiro | Mantida a restauração da sexta rodada, conforme orientação institucional informada pelo pesquisador; textos e descritores intactos. |
| Filiação com dois autores | Um mesmo indicador de filiação para pessoas da mesma instituição | Opção condicional acrescentada na sexta rodada | `autoria.tex` mantém a opção 0; a opção 1 foi testada em cópia isolada com os dois nomes e apenas UPF, Instituto de Tecnologia, Ciência da Computação. Não se presume coautoria confirmada. |
| Cabeçalho e URL | Identidade verde, logotipo, mês/ano e repositório da classe | Ajustes técnicos de contêiner e altura já existiam antes da quinta rodada | Mantidos esses ajustes prévios que evitam corte/avisos; nenhum endereço, margem ou identificador substituído. |
| Seções, parágrafos e recuos do corpo | Hierarquia, cores e recuo de 12 pt definidos na classe | Sem nova hierarquia científica ou sobrescrita global do corpo | Preservados; não foi aplicado `raggedbottom` nem reduzido espaçamento para forçar páginas. |
| Posição dos títulos de figuras | Legendas inferiores no backup; configuração compatível com a classe | Quinta rodada moveu as legendas para cima | Restauradas abaixo das imagens, preservando integralmente seus títulos, fontes, notas e rótulos automáticos. |
| Separador e fonte das legendas | Dois-pontos, centralização, negrito no rótulo, 9/9 pt; intervalos próprios de figura/tabela | Travessão e `skip=6pt` introduzidos em `normalizacao.tex` | Overrides removidos; configurações originais da classe voltaram a atuar. |
| Tabelas e bordas | Títulos superiores, tabelas abertas e regras verdes | Fontes acrescentadas e notas separadas dos títulos | Melhorias de atribuição preservadas; bordas e valores não alterados; separador e espaçamento seguem a classe. |
| Fontes e notas das ilustrações | Parte das fontes integrava a legenda; algumas tabelas não tinham fonte explícita | Quinta rodada criou blocos próprios, alinhados à esquerda, 9/10,5 pt | Fontes/notas mantidas em blocos inferiores, agora centralizadas e em 9/9 pt, acompanhando a legenda; extensão editorial, não regra institucional inventada. |
| Bibliografia e citações | `natbib/dcu` selecionado na classe e usado antes da quinta rodada | Quinta rodada substituiu a saída por `bibitem` personalizados e macros de separadores/sufixos | `\bibliography{referencias_institucionais}` restaura o BibTeX/dcu original; macros de citação, ordenação e aparência bibliográfica da quinta rodada desativadas. A conjunção nativa `and` volta a ser gerada pelo estilo, sem exigir caixa alta nas citações. |
| Alinhamento e recuo da bibliografia | Padrão do natbib/dcu | Recuo zero, `bibsep` explícito e alinhamento à esquerda impostos na quinta rodada | Overrides removidos; recuos, alinhamento e destaques voltam ao estilo original. |
| Metadados bibliográficos | Base científica consolidada e correções de autoria, anos, DOI, URL e acessos | Quinta rodada produziu uma base estruturada com 63 entradas | Todos os campos dessa base são preservados em `referencias_institucionais.bib`; os nove itens não citados continuam na base, sem remoção. Não se restauram os anos incorretos ou notas internas antigas. |
| Campos que o dcu não lê | O estilo original lê URL e note, mas não DOI, urldate, versão ou eid; também não exibe edição/editora de entradas misc | Gerador anterior formatava diretamente esses dados | Adaptador de dados expõe esses campos em `note` sem apagá-los nem gerar autores, citações ou verbetes. Siglas e nomes próprios recebem apenas proteção de caixa por chaves BibTeX, sem mudar caracteres do título. O `.bst` continua intacto. |
| URLs e datas entre colchetes | Limitações técnicas do dcu/natbib | Base revisada contém URLs longas e datas aproximadas | Mantidos apenas dois ajustes técnicos: URL clicável/quebrável com o rótulo nativo URL; proteção de datas entre colchetes no argumento do natbib. Sem alteração visual da pontuação do estilo ou dos anos. |
| Unidades e porcentagem | Apresentação tipográfica do texto e classe, sem redefinição global de `%` | Quinta rodada redefiniu `\%` e padronizou unidades compostas | Redefinição global de `\%` removida; notação de unidades por expoentes permanece, pois não altera a identidade do template nem valores científicos. |
| “Palavras-chave” | Classe escreve “Palavras-Chave” | Correção ortográfica de capitalização na quinta rodada | Mantida a grafia solicitada “Palavras-chave”, sem trocar fonte ou espaçamento. |
| Gerador personalizado de referências | Não integrava o template | Criado na quinta rodada | `gerar_referencias_normalizadas.py` e sua saída `.tex` ficam preservados como histórico, mas não são executados nem incluídos na compilação institucional atual. |

### Trabalhos publicados indicados — limite de acesso

As três referências fornecidas foram consultadas:

1. `https://repositorio.upf.br/items/3540a7da-a6df-4004-990e-f0211ce98f87`
2. `https://repositorio.upf.br/bitstreams/2c41199c-5c1c-42f2-8b9c-2f4eb97b4651/download`
3. `https://repositorio.upf.br/server/api/core/bitstreams/9d81667e-fc72-4b60-ab67-e9c3deee32e6/content`

Todas retornaram **HTML de verificação antirobô Anubis, não o conteúdo dos
trabalhos**, inclusive a URL de conteúdo e as tentativas pelos endpoints
canônicos da API. O status HTTP 200 não foi confundido com obtenção de PDF.
Assim, não se afirma ter observado características recorrentes desses três
trabalhos, nem se certifica comparação visual externa completa. A restauração
executada se apoia na classe local, no histórico, no backup e na instrução
do pesquisador; a comparação externa permanece **pendente de acesso aos PDFs**.

### Resultado da revisão e distinção normativa

- Os defaults verificados do modelo local foram restaurados, sem alegação
  de que escolhas individuais de artigos publicados seriam regras obrigatórias.
- Os estados anteriores de ABNT-01, ABNT-04–05, ABNT-06/09–12 e ABNT-20
  devem ser lidos à luz desta decisão institucional, não como autorização
  para reaplicar os overrides desativados.
- A ordem dos resumos permanece uma **particularidade do template informada
  pelo pesquisador**, não uma exigência geral da NBR 6022.
- A apresentação `dcu` não é certificada como implementação da NBR 6023:2025
  ou da NBR 10520:2023. A fidelidade ao estilo e a qualidade dos metadados
  são critérios distintos; as lacunas de datas/metadados já registradas
  continuam explicitadas, sem criar novas datas nesta revisão.
- Corpo científico, SDD, resumos, discussão, conclusão, 32 respostas,
  14 expressões numeradas, gráficos e declaração de IA preservados.
- Compilação, comparação e inspeção desta revisão ficam em
  `evidencias/fidelidade_template_upf/`; os relatórios anteriores não são
  sobrescritos. O PDF tem 32 páginas; a prévia de coautoria foi apenas um teste.
- A inspeção de todas as páginas é assistida por IA, não aprovação humana
  ou institucional. Sem commit ou push.

## Resultado e limites

**Registro histórico da quinta rodada e do primeiro ajuste pré-textual:**
as descrições abaixo documentam decisões anteriores, substituídas pela
seção vigente quando houver conflito de apresentação.

### Correção pontual posterior — ordem institucional e autoria

Por solicitação expressa do pesquisador, foi restaurada a sequência
**Abstract, Keywords, Resumo e Palavras-chave**, preservando literalmente os
dois textos e os descritores. A sequência é registrada como **particularidade
do template institucional informada pelo pesquisador**, após sua comparação
com TCCs publicados pela Ciência da Computação da UPF. Não se trata de uma
ordem imposta pela NBR 6022. Os trabalhos comparados e o pacote original
independente não foram fornecidos nesta correção; portanto, não se apresenta
essa informação como verificação documental independente pelo assistente.

Foi acrescentado `autoria.tex`, com a opção
`\TCCIncluirRafaelComoCoautor` **desativada por padrão (0)**. A versão entregue
mantém Eduardo Steffens Hoppen como único autor e Rafael Rieder identificado
como orientador, sem presumir coautoria. Somente após confirmação explícita,
o valor 1 inclui os dois autores com o mesmo indicador de filiação e usa
apenas **Universidade de Passo Fundo, Instituto de Tecnologia, Ciência da
Computação** na filiação. Os metadados PDF e o cabeçalho autoral acompanham
essa opção; a alternativa não é uma confirmação de autoria.

A composição da primeira página mantém as definições da classe local:
Merriweather, títulos em 16 pt, autoria em 13 pt, filiação em 9 pt, cores,
espaçamentos e identificação institucional. Não foi introduzida expansão
manual entre letras nem alterada a classe. As demais melhorias da quinta
rodada permanecem. Compilação, inspeção e preservação desta correção são
registradas junto à revisão em `evidencias/fidelidade_template_upf/`, sem
sobrescrever as evidências anteriores.

Foram aplicadas correções de apresentação, citações, geração bibliográfica,
fontes/legendas e unidades. Foram inventariadas individualmente as **63 entradas
bibliográficas**; as **54 citadas** são publicadas, e as nove não citadas
permanecem na base. Não houve exclusão de fontes, nova revisão científica,
nova análise das respostas ou alteração de resultados.

**Esta entrega não satisfaz ainda todos os critérios de aceite integral.**
Inventariar e normalizar uma entrada não equivale a confirmar todos os seus
metadados. A proveniência oficial do modelo final, o levantamento completo
de versões corrigidas/emendas e algumas datas/metadados bibliográficos não
foram encerrados. As lacunas são indicadas abaixo e em
`evidencias/quinta_rodada/referencias.json`; não há certificação de conformidade
integral com a ABNT nem aprovação institucional presumida.

O conteúdo dos dois resumos foi preservado; mudou sua ordem. A declaração
de IA, a classe, os resultados e as imagens foram preservados. A contagem
“12 equações” da solicitação não correspondia à base: ela já numerava **14**,
em oito ambientes `equation`/`align`. Nenhuma foi removida ou renumerada
para forçar aquela contagem.

## 1. Base normativa e institucional consultada

| Documento | Evidência obtida | Alcance e limitação |
|---|---|---|
| NBR 6023:2025 | PDF da terceira edição, 21 maio 2025, disponibilizado em domínio de armazenamento do Centro Paula Souza; substitui a edição anterior e sua emenda | Consultados, entre outros, §§6.3, 6.6, 6.7, 7 e 8.4–8.6. A extração tem glifos corrompidos; usou-se também decodificação auxiliar. Não foi confirmada a inexistência de correções posteriores no catálogo oficial. |
| NBR 10520:2023 | PDF disponibilizado pela Casa de Oswaldo Cruz/Fiocruz | §§6.1.1.1, 6.1.2, 6.1.3, 6.1.4 e 6.1.8: caixa mista, autores, narrativa e citações simultâneas. O servidor apresentou cadeia TLS não validável; download realizado sem validação de certificado e conteúdo identificado pelo documento. Essa limitação de transporte não é omitida. |
| NBR 14724:2024 | PDF da quarta edição, 16 dez. 2024, disponibilizado em site do TPP/UFF | Subsídio geral; não foi usada para converter o artigo em monografia. Situação de versão corrigida posterior não confirmada. |
| IBGE, Normas de apresentação tabular | PDF obtido na Biblioteca do IBGE | Conferência de fonte, título e estrutura aberta; tabelas descritivas foram distinguidas da estatística, sem reclassificação indiscriminada. |
| SI, 9ª edição de 2019 | PDF oficial do BIPM, versão 4.01 de junho de 2026 | §§5.4.3, 5.4.4 e 5.4.7; produto/quociente de unidades e espaço entre valor e símbolo. |
| NBR 6022:2018, 6024:2012 e 6028:2021 | Requisitos indicados na solicitação; buscas de texto primário sem resultado utilizável nesta execução | Não se afirma leitura integral dessas três normas, nem se inventam números de cláusulas. As correções compatíveis e expressamente solicitadas foram realizadas; conferência normativa direta permanece necessária. |
| Modelo final UPF | Leitura integral de `CC-EC_TF-TC.cls`, entrada, macros e histórico Git | A classe local declara desenvolvimento por Marcelo Trindade Rebonatto e atualização por Rafael Rieder. Comentário: v1.1, 26/06/2026; `ProvidesClass`: 24/07/2025. Introduzida em `f4c46a7`; sem alteração posterior identificada na classe. Não se obteve cópia oficial independente para comparação de origem. |
| Curso/UPF | Página pública do curso no Instituto de Tecnologia | Confirma unidade, curso e campus Passo Fundo; não foi encontrado ali o pacote final nem regra expressa impondo ordem dos resumos, `dcu` ou legendas inferiores. O antigo modelo de proposta em `docs/modelo_latex/` não foi tratado como modelo original do artigo final. |
| Catálogo ABNT | Página principal acessível; tentativa de busca sem ficha normativa conclusiva | Não permite declarar que inexistem emendas ou versões corrigidas. |

URLs, hashes e limitações constam de `evidencias/quinta_rodada/fontes_normativas.json`.
Os PDFs normativos ficaram em cache privado, sem republicação no repositório.

## 2. Achados ABNT-01–22 — registro histórico da quinta rodada

Os números de página abaixo correspondem ao PDF desta rodada. “Corrigida”
identifica a ocorrência específica, não constitui certificado de conformidade
integral do item ou do documento. Evidências comuns: `antes_depois.diff`,
`compilacao.json`, `renderizacao.json` e relatório visual na pasta desta rodada.

| ID | Norma / localização verificada | Página | Problema e estado anterior | Correção / decisão | Arquivos | Evidência / validação | Status |
|---|---|---|---|---|---|---|---|
| ABNT-01 | Template institucional segundo comparação comunicada pelo pesquisador; NBR 6022:2018 como referência geral, sem impor sua ordem à exceção local | 1 | A quinta rodada havia anteposto o Resumo ao Abstract | Restaurados Abstract, Keywords, Resumo e Palavras-chave; textos e descritores intactos; coautoria preparada, não ativada | `final_0_resumo.tex`, `autoria.tex`, `Relatorio_Final.tex` | Orientação expressa do pesquisador; comparação literal dos blocos e inspeção do PDF; confirmação documental independente do template ainda não disponível | Pendente de confirmação institucional |
| ABNT-02 | NBR 6028:2021, cláusula não conferida diretamente | 1 | Rótulo “Palavras-Chave” da classe | Ajuste local para “Palavras-chave”; parágrafos únicos, descritores e resultados das 32 respostas preservados | `normalizacao.tex`, `final_0_resumo.tex` | Leitura dos resumos e p.1; sem reformulação científica | Não conformidade corrigida |
| ABNT-03 | NBR 10520:2023, 6.1.1.1 | 2–5, 7–12, 15, 27–32 | Risco de introduzir regra antiga de caixa alta nas citações | Caixa mista mantida nas citações; caixa alta apenas nos sobrenomes/autorias da lista bibliográfica | `normalizacao.tex`, gerador e produtos bibliográficos | Fontes e PDF: Gao, Davis, Patrício/Rieder e autores institucionais | Conforme |
| ABNT-04 | NBR 10520:2023, 6.1.3 e 6.1.4 | 2–5, 7–12, 27–29 | `harvardand=e` compartilhado entre narrativa e parênteses | Separadores dependentes do contexto: “Patrício; Rieder” versus “Patrício e Rieder”; três autores explicitados, abreviação para quatro ou mais | `normalizacao.tex`, `scripts/gerar_referencias_normalizadas.py` | Leitura visual de exemplos parentéticos e narrativos | Não conformidade corrigida |
| ABNT-05 | NBR 10520:2023, 6.1.2 e 6.1.8 | 2–5, 7–12, 27–32 | Espaços relatados nas auditorias e risco de sufixos incoerentes | Geração de pontuação por natbib; ordenação das citações simultâneas pela lista alfabética; sufixos autor/ano coerentes; `et al.` tipograficamente uniforme | Configuração e gerador | PDF não apresenta citações indefinidas; os exemplos de extração não foram presumidos erros visuais | Não conformidade corrigida |
| ABNT-06 | NBR 6023:2025, seções 7 e 8 | 30–32 | `dcu`: ano após autor, formato internacional e estruturas heterogêneas | Estruturas distintas para artigo, livro, capítulo, evento, trabalho acadêmico, relatório e documentação; sobrenomes em caixa alta, autores separados por ponto e vírgula, periódico/obra em negrito; identificadores de artigo separados de páginas | Gerador, `referencias_normalizadas.bib/.tex` | 63 entradas inventariadas, 54 publicadas; lacunas individuais explícitas, sem atestar metadados completos | Pendente de confirmação institucional |
| ABNT-07 | NBR 6023:2025, 6.6 | 30–32 | Notas com “Acessado em”, falta de dois-pontos e comentários internos | Campos URL, DOI e acesso separados; “Disponível em:” / “Acesso em:”; meses abreviados; datas antigas preservadas e novas somente quando houve consulta documentada | Gerador e produtos bibliográficos | `links.json`; falhas HTTP não são declaradas consultas bem-sucedidas; ainda há entradas sem acesso registrado | Pendente de confirmação institucional |
| ABNT-08 | NBR 6023:2025, 8.6.1.1 e 8.6.1.3 | 4–5, 7–8, 10, 29–32 | Documentação sem ano, gerando `n.d.` e sufixos | Datas verificadas do Google/QGIS; copyright identificado como tal em NumPy/Streamlit; edição e revisão do SI separadas; dez fontes com século provável, não com ano inventado | Gerador e `datas.json` | Cada alteração e incerteza discriminada; século provável é indicação de incerteza, não data exata certificada | Pendente de confirmação institucional |
| ABNT-09 | NBR 6023:2025, 6.3 e 6.7 | 30–32 | Recuo francês, alinhamento e destaque heterogêneos | Recuo zero, alinhamento à esquerda, espaço simples, linha simples entre entradas e destaque uniforme por tipo | `normalizacao.tex` | PDF renderizado; nove entradas não citadas preservadas na base, não incluídas artificialmente na lista | Não conformidade corrigida |
| ABNT-10 | Configuração editorial; NBR 6023/10520 | 2–32 | Estilo `dcu` não implementa a apresentação pretendida | Geração determinística de `bibitem` natbib a partir de dados estruturados; sem biblatex, sem edição de `.bbl`, sem alterar a classe; arquivo de origem preservado | `Relatorio_Final.tex`, gerador, requisitos editoriais e produtos | Compilação efetiva; instruções de reprodução na pasta de evidências | Recomendação editorial implementada |
| ABNT-11 | NBR 6022:2018, cláusula não conferida diretamente | 6, 9–10, 12, 14, 16, 18–22, 24–26 | Títulos abaixo das 22 figuras | Identificação/título acima de todas as figuras; fonte e notas abaixo; nenhum conteúdo visual refeito | `figuras_relatorio.tex`, `fig/conceitos.tex`, seções com figuras | Todas as páginas contendo figuras inspecionadas | Não conformidade corrigida |
| ABNT-12 | NBR 6022 / apresentação tabular, cláusula não atribuída | Mesmas páginas e 8, 13, 25, 27–28 | Separador global “:” da classe | Separador automático “–” nos títulos de figuras e tabelas, sem editar números | `normalizacao.tex` | 22 figuras e cinco tabelas; numeração automática preservada | Não conformidade corrigida |
| ABNT-13 | NBR 6022 / atribuição científica | Páginas com figuras | Fonte e explicações integradas à legenda | Fonte em bloco inferior; notas separadas quando cabíveis; origem própria, aplicação e catálogo diferenciados | Macros e seções com figuras | Conferência de 22 fontes sem atribuição fictícia | Não conformidade corrigida |
| ABNT-14 | IBGE; NBR 6023 quando há citação da fonte | 8, 13, 25, 27–28 | Três tabelas sem fonte explícita e notas excessivas em títulos | Fontes em todas; notas das tabelas geradas separadas do título. Laterais já eram abertas, sem grades fechadas: não se registrou correção de borda inexistente | `final_2_fundamentacao.tex`, `final_3a_implementacao.tex`, `final_5_discussao.tex`, gerador de tabelas | Conteúdo e valores comparados; tabela 3 estatística; 1, 2 e 5 textuais; 4 mista com frequências | Não conformidade corrigida |
| ABNT-15 | Legibilidade editorial | 6, 9–10, 12–16, 18–22, 24–26 | Risco de textos pequenos nas capturas escuras | Mantidos os vetores nos diagramas e gráficos; inspeção das capturas sem alteração artificial de contraste, valores ou enquadramento | PDF; imagens intactas | Não houve corte de títulos/fontes. Textos pequenos nas capturas 18–21 e eixo ausente na captura da série continuam limitações dos originais; não se certifica legibilidade de impressão sem prova física | Pendente de confirmação institucional |
| ABNT-16 | NBR 6024:2012, texto primário não obtido | 2–29 | Conferência de hierarquia e numeração | Hierarquia e estrutura científicas preservadas; nenhum ponto ou hífen introduzido entre indicativo e título; declaração e referências sem número | Seções preservadas | Inspeção de títulos e referências cruzadas; conferência normativa direta pendente | Pendente de confirmação institucional |
| ABNT-17 | NBR 14724:2024, aplicação subsidiária ao artigo | 3–4, 8–10, 15 | Solicitação menciona 12; base possui 14 números | Todas as 14 expressões e oito ambientes preservados literalmente; identificação à direita e referências automáticas mantidas | Fórmulas sem alteração | `preservacao.json`; números (1)–(14), não “12 equações preservadas” | Conforme |
| ABNT-18 | NBR 14724 / revisão terminológica | 2–5, 9–13 | IA sem expansão na primeira ocorrência do corpo; formatos apresentados somente pelas siglas | Expansão de IA; identificação de PDF/CSV e caracterização de XLSX/ZIP sem inventar expansões; NIR/SWIR/MSI/API/CRS/UTM/UTC/LST já definidos | `final_1_introducao.tex`, `final_2_fundamentacao.tex` | Leitura das primeiras ocorrências; QA60 mantido como identificador de banda, sem lista artificial de siglas | Recomendação editorial implementada |
| ABNT-19 | Critério editorial, não regra universal de ABNT | 5–16, 17, 23, 27–29 | Estrangeirismos e identificadores com usos distintos | Itálico em `toolkit` e em ocorrências ilustrativas de raster/snapshot; identificadores literais e nomes próprios preservados; não foi feita substituição indiscriminada em excertos e diagramas | Seções e legenda pontualmente ajustadas | Uniformização não esgotada: permanecem usos não destacados de raster, tiles, snapshot, viewport e tracer; não se declara revisão terminológica integral | Pendente de confirmação institucional |
| ABNT-20 | SI, §§5.4.3, 5.4.4 e 5.4.7 | 1, 10, 23–29 | Unidade de radiação com duas barras; símbolo de porcentagem junto ao número | Radiação em MJ m⁻² d⁻¹ e kWh m⁻² d⁻¹; espaço entre número e % no texto/tabelas; espaços inseparáveis em medidas selecionadas; vírgula PT e ponto EN mantidos | `normalizacao.tex`, métodos e resultados | Nenhuma conversão de valor ou precisão; textos internos das imagens preservados, não uniformizados artificialmente | Recomendação editorial implementada |
| ABNT-21 | Revisão editorial e preservação do modelo | 1–32 | Flutuantes, títulos, fontes e possíveis excessos de caixa | Legendas/fontes mantidas com o elemento; nenhuma redução de margens ou fontes. PDF sem `Overfull`/referências indefinidas | Fontes e PDF | 32 páginas inspecionadas por IA; permanecem espaçamento vertical elástico na p.10 e páginas de figuras com branco, sem impor limite artificial de páginas | Pendente de confirmação institucional |
| ABNT-22 | Identificação confirmada pelo autor; modelo local | 1–32 | Conferência de identidade, orientador, data e endereço | Eduardo Steffens Hoppen, Prof. Rafael Rieder, Itec/UPF, Ciência da Computação, dezembro de 2026 e URL do repositório preservados; cabeçalho indica 1–32 | Entrada e classe preservada | PDF e hashes; nenhuma afiliação, assinatura ou identificador criado | Conforme |

## 3. Particularidades preservadas — sem alegar confirmação indevida

- Duas colunas, papel Letter, Merriweather, fontes, margens, identidade verde,
  logotipo, cabeçalhos, paginação e estrutura de identificação da classe local.
- Endereço `https://repositorio.upf.br/handle/123456789/8754` mantido.
- Nenhuma capa, folha de rosto, ficha catalográfica, sumário ou lista de siglas.
- A ordem **Abstract antes de Resumo** foi restaurada como particularidade
  institucional informada pelo pesquisador. Como os exemplos comparados não
  foram disponibilizados nesta correção, o status documental permanece
  **“Pendente de confirmação institucional”**, sem questionar ou contrariar
  a decisão de apresentação fornecida.
- Não foi usado o status **“Particularidade institucional confirmada”** para
  `dcu`, legendas inferiores ou qualquer regra cuja obrigatoriedade não foi
  demonstrada em documento oficial independente.
- Elementos textuais 1, 2 e 5 foram reconhecidos como potenciais quadros,
  mas mantidos como tabelas: a reclassificação não é automática nem necessária
  para corrigir fonte e apresentação, e não há regra específica do curso
  confirmada para impor outro nome.

## 4. Datas bibliográficas e lacunas

A investigação foi individual, não uma substituição de `n.d.` por 2026.
As páginas do Google exibiram atualizações em 2023, 2024 e 2026; QGIS 3.40
exibiu atualização em março de 2026. O SI confirma a edição de 2019 e a
revisão 4.01 de junho de 2026. Copyright aparece com prefixo `c`, não como
ano editorial certificado.

Para `USGS_NDMI`, `NOMINATIM_POLICY`, `SENTINELHUB_NDMI`,
`NIST_OUTLIERS`, `NASA_POWER_METHOD`, `NASA_POWER_PARAMETERS`,
`NIST_LOCATION`, `GITHUB_SDD`, `EOSDA_GUIDE` e `ONESOIL_PLATFORM_DETAIL`,
não se obteve data editorial exata. A indicação **[20--?]** é de **século
provável**, possibilidade prevista no §8.6.1.3, e permanece uma aproximação
editorial a validar, não uma confirmação de data. Os anos 2026 anteriormente
atribuídos a outras páginas dinâmicas também não são certificados apenas
porque o acesso ocorreu nesse ano.

Há ainda localidades não identificadas, entradas sem data efetiva de acesso
registrada, detalhes dos eventos e do trabalho acadêmico a conferir na fonte.
Não foram inventados páginas, graus, números de evento, cidades ou editoras.
As abreviações de ausência não equivalem a preenchimento de metadados reais.
Comentários internos removidos dos verbetes permanecem no inventário.

## 5. Aceite e próximos encaminhamentos

1. Confirmar com o orientador/curso o pacote oficial e suas exceções obrigatórias.
2. Encerrar a consulta das versões corrigidas/emendas e das três normas cujo
   texto primário não foi obtido, preferencialmente pelo acesso da biblioteca.
3. Conferir os metadados ainda ausentes, as dez datas aproximadas e os anos
   anteriores não demonstrados; registrar acessos efetivos, sem reconstruí-los.
4. Encerrar a uniformização terminológica e avaliar os espaços verticais e
   uma prova de impressão das capturas antes de declarar acabamento integral.
5. Submeter a apresentação ao autor e ao orientador. A inspeção de IA não é
   aprovação humana, aprovação institucional ou validação de conteúdo científico.

Esses encaminhamentos não reabrem as decisões já fornecidas sobre as
32 respostas, orientador, defesa, imagem ilustrativa e declaração de IA.
Sem commit ou push.
