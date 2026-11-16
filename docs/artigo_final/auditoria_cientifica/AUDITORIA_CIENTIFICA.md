# Auditoria científica — versão de trabalho

## Relatório vigente — quarta rodada, 16/11/2026

**Ajustes pontuais concluídos sobre a versão de32 páginas; demonstração complementar do detector aguardando evidências do pesquisador.** O artigo continua com32 páginas,22 figuras e cinco tabelas, sem alteração da estrutura, da classe, do código funcional ou dos parâmetros. Não houve commit/push/deploy. A nova redação permanece sujeita à leitura e aprovação substantiva do autor.

### Conjunto definitivo e reprocessamento

O pesquisador confirmou32 respostas. Durante a execução, a planilha pública já continha33 elegíveis, fato comunicado antes de qualquer seleção. Na pergunta de esclarecimento, escolheu **“Snapshot de 32 respostas”**. Foi recuperada a exportação pública anterior, hash `c9c267230e803a8aa09073c438ff6264de3a597a3e7478aacfd979026c245a34`, e conferido que todas as32 linhas, incluindo carimbos, integram a exportação atual. Não se excluiu arbitrariamente uma linha da fonte atual para forçarN=32.

As31 respostas do original privado correspondem ao snapshot sem alteração das respostas; as sete diferenças históricas de carimbo coincidem com a retificação documentada. Nenhuma retificação nesta rodada. O conjunto32 está preservado privadamente e ignorado pelo Git; não foi republicada planilha individual. A antiga pendência31/32 foi resolvida pela inclusão do registro e definição explícita da versão dos dados.

| Indicador | Terceira rodada | Quarta rodada |
|---|---:|---:|
| Respostas elegíveis |31|32|
| Nota média |7,74193548|7,71875|
| Mediana / moda |8 /9|8 /9|
| DP amostral |1,80679720|1,78224894|
| Q1 /Q3 |7 /9|7 /9|
| Demarcação sem ajuda |18/31|19/32|
| Conclusão de demarcação entre tentativas |23/25|24/26|
| Séries/anomalias: conclusão entre tentativas |23/28|24/29|
| Intenção de uso (4–5) |24/30|24/31|
| Consulta por pixel útil/muito útil |20/23|21/24|
| Mediana da utilidade dos índices, demais áreas |5 (n13)|4,5 (n14)|
| Mediana da nota, experiência poucas vezes/nunca |8 (n13)|7,5 (n14)|
| Células discursivas preenchidas /temas |142 /13|142 /13|

Todos os40 itens,191 categorias, seis cruzamentos, nota geral, contagens por perfil e qualitativo foram reprocessados. As32 submissões foram examinadas;31 contêm texto aberto. A incluída tem os cinco campos vazios: nenhum texto, interpretação ou tema foi imputado. São18 ausências entre160 campos, incluindo14 no comentário opcional. Os13 temas mantêm as contagens anteriores, com percentuais por32 submissões. O rótulo do gráfico temático explicita “n analisado”, evitando confundir32 unidades examinadas com31 unidades contendo texto.

Os nove gráficos foram regenerados em PDF/SVG/PNG, as tabelas/macros refeitas e todos os números narrativos revistos. Corrigida também a afirmação de que os gráficos temporais teriam a menor proporção de utilidade4–5: a tabela não sustenta esse superlativo; o texto agora apresenta diretamente21/30. Não houve seleção somente de resultados favoráveis.

### Ajustes científicos e editoriais

- **Metodologia:** coleta concluída,32 elegíveis, participação voluntária, consentimento/maioridade autodeclarados e tratamento agregado. A fonte é um snapshot fixo, não uma promessa de que o endereço público continuará contendo32.
- **Narrativa:** resultados sob perspectiva científica do pesquisador, sem suspeitas especulativas ou interlocução de auditor no artigo. Autorrelato, amostragem e ausência de validação agronômica permanecem limites do desenho.
- **Ética:** eliminadas repetições no resumo, discussão e conclusão; informação material preservada uma vez nos métodos. Não se afirmou submissão, aprovação, dispensa ou regularização.
- **IA:** declaração específica mantida integralmente no alcance das atividades; retiradas menções redundantes nos resumos, repetição final nos procedimentos de desenvolvimento e legenda temática. Permanecem os usos metodologicamente necessários no desenvolvimento e na codificação.
- **SDD:** dois parágrafos de complemento e uma associação na discussão, com Gotel/Finkelstein1994 (requisitos/rastreabilidade), Bjarnason et al.2015 (critérios/testes/contexto) e Vaithilingam et al.2022 (geração de código/compreensão/verificação humana). Três entradas adicionadas, nenhuma removida ou substituída;63 entradas e54 chaves citadas. Textos primários e metadados conferidos, com limites registrados. Não se atribuiu BDD/ATDD, especificação formal ou ganho medido.
- **Demonstração complementar:** não disponibilizada nesta execução. Preservada a distinção entre regra verificada com dados controlados e demonstração real anterior de duas aquisições. Nenhum novo experimento, observação ou sinalização foi produzido.

### Validação técnica, estatística e visual

O validador independente reproduziu frequências, percentuais, médias, medianas, quartis e DP, além dos nove denominadores de tarefas,13 contagens temáticas e seis cruzamentos (12 grupos). Os nove testes da rotina de análise passaram, incluindo tratamento de campos abertos vazios. São verificações do processamento estatístico, **não nova execução dos710 testes da aplicação**.

Tectonic compilou artigo e declaração sem erros, citações/referências indefinidas, caixas `Overfull` ou aviso de bloco inicial `twocolumn too tall`. Permanecem avisos de caixas pouco preenchidas, substituição de tamanhos de fontes matemáticas da classe e compatibilidade epstopdf/driver, sem corte observado. Classe, equações, algoritmos, parâmetros, capturas e evidências anteriores preservados.

As32 páginas foram renderizadas a1500px e inspecionadas individualmente porIA. Após a última correção pontual de redação, somente as páginas24 e27 mudaram e foram reexaminadas; as30 restantes permaneceram idênticas à inspeção inicial desta rodada. As duas páginas da declaração independente também foram inspecionadas. Não houve aprovação visual humana.

| Páginas | Conferência visual |
|---|---|
|1|Cabeçalho,32 respostas, média7,72/mediana8 e equivalência entre resumos; sem bloco alto|
|2–4|Objetivos, conceitos, bandas e equações preservados; títulos acompanhados|
|5–8|Novo fundamento de SDD, citações, esquemas e tabela documental, sem corte ou sobreposição|
|9–10|Fluxos, fórmulas e unidades legíveis; espaçamento vertical elástico da classe permanece, sem reduzir medidas institucionais|
|11–12|Metodologia32, ausência de campos, consentimento/ética em um único trecho e arquitetura; sem texto órfão|
|13–16|Componentes, persistência, consulta local e exportação preservados|
|17–22|Capturas/QR e legendas preservados; a imagem59,00 permanece apenas ilustrativa|
|23|Resultados técnicos e demonstração histórica de dois pontos sem valores alterados|
|24–27|Perfil32, tarefas, experiência, tabela de utilidade, nota7,72/DP1,78 e temas; denominadores por item não confundidos comN total|
|28–29|Objetivos, discussão, limites e conclusão32/intenção24 de31 válidas|
|30–32|Declaração deIA e referências, incluindo as três novas entradas; última coluna residual sem excesso|
|Declaração1–2|Campos institucionais e prompt desta rodada; assinatura em branco|

Todos os nove gráficos foram conferidos por regeneração e correspondência com os CSV; os complementares não incluídos no artigo também foram examinados. Os manifestos de preservação, compilação, fontes e dados estão em `../evidencias/quarta_rodada/`. A comparação da rodada é contra `2ca848a` e o PDF de32 páginas, não contra a antiga base38.

### Encaminhamentos e preparação de defesa atualizados

1. **Qual conjunto foi analisado?** As32 respostas do snapshot público definitivo escolhido pelo pesquisador; a fonte dinâmica passou a conter33, sem mudar automaticamente a versão analisada.
2. **Por que ainda aparecem denominadores31 ou30?** Porque “Não consegui avaliar” e ausências são excluídos conforme cada item;N total32 não é o denominador de todas as perguntas. Os31 textos abertos não significam31 participantes totais.
3. **O que mudou?** Média7,72, DP1,78, intenção24/31 e distribuições atualizadas; algumas medianas dos cruzamentos também mudaram. Não se presumiu estabilidade dos resultados.
4. **Como as ausências foram codificadas?** Não receberam tema; a submissão adicional tem mapa vazio. As142 células preenchidas permanecem efetivamente analisadas, sem criar novas respostas.
5. **A fundamentação prova superioridade do SDD ou da ferramenta deIA?** Não. Apoia os conceitos de especificação, rastreabilidade, verificação e supervisão; o TCC não contém ensaio comparativo do processo.
6. **Há nova demonstração real do detector?** Ainda não: aguardam-se área/período, série integral, índices, parâmetros e arquivos/capturas correspondentes fornecidos pelo pesquisador. Com esses dados, será possível conferir média móvel, dispersão, escore e marcações sem atribuir eficácia agronômica.

Permanecem as decisões institucionais e a revisão humana final registradas em `PENDENCIAS_AUTOR.md`, além dos limites bibliográficos anteriores. **As seções seguintes são históricas**, inclusive a antiga pendência31/32 e as respostas de defesa sobre aquele estado; não prevalecem sobre este relatório.

## Relatório consolidado vigente — terceira rodada, 15–16/11/2026

**Finalidade: versão consolidada para encaminhamento ao Prof. Rafael Rieder, não conformidade institucional definitiva.** A rodada parte do PDF de38 páginas (`ebf4e063…`) e das decisões PA01–PA18, sem reiniciar o trabalho. O protocolo autoral foi lido integralmente antes da atividade. As novas reformulações estão disponíveis para leitura e aprovação intelectual do pesquisador; a assistência substancial de IA permanece declarada.

### 1. Problemas tratados e alterações

| Problema | Intervenção / seções | Resultado |
|---|---|---|
| Voz de auditor externo | Introdução, métodos, resultados, conclusão e IA | Pesquisa narrada sob responsabilidade do pesquisador; removidas expressões de suspeita não sustentada e histórico de revisão |
| Contribuição diluída em inventário de funcionalidades | Introdução, desenvolvimento e discussão | Integração raster/vetor, responsabilidades, validade de estado, transferência servidor/navegador e contexto comum de exportação apresentados como contribuição própria |
| Ressalvas repetidas | Fundamentos, plataforma e discussão | Delimitação geral na introdução; condições do algoritmo no método; dois pontos/indisponibilidade nos resultados; limites gerais na discussão |
| Discussão descritiva | Discussão reestruturada | Compromissos transferência/memória, persistência local/sessão, testes/oráculos e síntese/saídas estruturadas interpretados com Parnas, Bender, Davis e Meroni |
| Questionário tratado como investigação da honestidade | Métodos e avaliação exploratória | Declaração autoral acolhida;31 registros rastreados na fonte pública e cálculos reproduzidos; interpretações limitadas ao recorte, autorrelato e amostragem |
| Diferença de tamanho da fonte | Metodologia e pendências |32 públicos versus31 analisados; adicional também elegível. Diferença explicitada sem exclusão por triagem inventada ou recálculo silencioso |
| Excesso de telas intermediárias | Apresentação da plataforma | Retirados quatro agrupamentos redundantes da paginação e integrado QR à figura móvel; capturas originais preservadas |
| Resultados de transferência na implementação | Desenvolvimento/resultados | Procedimento permanece na implementação; valores medidos movidos para subseção de resultados |
| Pendências bibliográficas | Parecer bibliográfico | PDFs de Davis/Braun obtidos e confrontados no escopo citado; limitações restantes delimitadas; nenhuma nova referência |
| Transparência de IA excessivamente burocrática | Declarações | Concisão sem omitir geração/reformulação substancial, análise, supervisão ou atos institucionais pendentes |

Não foram alterados código funcional, testes, respostas, carimbos, atribuições temáticas, parâmetros, gráficos numéricos, equações ou classe. Não houve commit, push, deploy ou novo experimento da aplicação. A releitura não atribui DSR, TDD uniforme, calibração ou motivações históricas não documentadas.

### 2. Comparação e evidências

- Antes:38 páginas,27 figuras,5 tabelas; PDF e fontes preservados em `/tmp/opencode/terceira-rodada/antes/`.
- Depois: **32 páginas, 22 figuras, cinco tabelas e 51 chaves citadas**, conforme `../evidencias/terceira_rodada/compilacao.json`. Redução de seis páginas (15,8%), sem reduzir fonte, margens ou espaçamentos institucionais.
- Diferenças integrais contra a cópia de trabalho anterior em `antes_depois.diff`; a comparação com HEAD inclui revisões prévias e não deve ser confundida com o escopo desta rodada.
- Os logs originais confirmam710 testes Python em11,73s,2.735 instruções/856 ramificações/100% no escopo medido e três verificações JavaScript aprovadas. Não são novos resultados desta rodada.
- Demonstração preservada: área≈4,36ha; duas aquisições; médias0,7070/0,2140/0,2380;61 registros climáticos;635,56mm;16,24°C; radiação indisponível; três páginasPDF/sete abasXLSX/seteCSV; consultaNDMI0,3228.
- A busca de séries extensas abrangeu `docs/validation`, manifestos, exports e capturas. Cenários por cultura são planejamento/script, não resultados executados comprovados. Capturas extensas não têm série/metadados completos que permitam avaliar o detector. Permanecem distintos testes controlados e demonstração real de dois pontos; nenhum novo experimento foi executado.
- Conferência pública:31 linhas idênticas incluindo datas,40 itens/191 categorias,13 temas/142 células; notas e quartis reproduzidos. Validação independente por Counter/statistics também passou. A recomputação temática usa as atribuições preservadas, não nova codificação.
- A planilha pública confirma disponibilidade/correspondência documental, não identidade dos participantes. A declaração de participantes reais e encerramento foi acolhida; não há evidência concreta apresentada de falsidade. O adicional elegível exige esclarecer o recorte, não imputar fraude.
- Os nove gráficos foram regenerados em cache a partir dos CSV conferidos: os pixels dos nove PNG coincidiram integralmente com os gráficos preservados. Não foram substituídos os arquivos publicados. Os seis cruzamentos, a distribuição da nota e os nove denominadores de conclusão também coincidiram.

### 2.1 Compilação e inspeção visual final

Tectonic concluiu a compilação sem erros, referências/citações indefinidas ou excessos `Overfull hbox/vbox`. Permanecem avisos de caixas pouco preenchidas, substituições de tamanho de fontes matemáticas da classe e compatibilidade do pacote epstopdf com o driver, sem corte observado. O aviso de bloco inicial `twocolumn too tall` foi eliminado por síntese equivalente do resumo/abstract, sem reduzir fonte. A classe e a configuração tipográfica institucional foram preservadas. Foram feitas somente quebras locais para evitar títulos órfãos, alinhamento dos painéis móveis e desvio de um conector no diagrama.

Todas as 32 páginas foram renderizadas a 1500 px de altura e examinadas individualmente pelo agente de IA. Após os ajustes visuais e a síntese final do resumo, as 32 foram renderizadas novamente: 21 diferem da primeira inspeção e foram reexaminadas; 11 permanecem pixel a pixel idênticas à leitura individual anterior. A última alteração afetou somente a página 1, novamente examinada. As duas páginas da declaração independente também foram examinadas. **Não houve aprovação visual humana.**

| Página(s) | Itens conferidos / observações |
|---|---|
| 1 | Título, autor, orientador, mês, endereço institucional, resumo/abstract equivalentes e palavras-chave; sem transbordamento |
| 2 | Problema, contribuição e oito objetivos; título da fundamentação deslocado para a página seguinte para evitar orfandade |
| 3 | Conceitos e NDVI, definição prévia de posição/aquisição e primeira equação |
| 4 | NDWI/NDMI, agregações e suas fontes, sem colisão das fórmulas |
| 5 | Séries, Engenharia de Software, clima, avaliação de uso e início dos relacionados |
| 6 | Quatro esquemas: bandas, raster/vetor, agregações e janela didática; sem curvas espectrais presumidas |
| 7 | Tabela documental e transição para métodos; título acompanhado do texto |
| 8 | Entradas, QA60, datas e agregações espaciais |
| 9 | Fluxo de processamento e equações da janela, dispersão e escore |
| 10 | Fluxo de anomalias, unidades e somas/médias climáticas |
| 11 | Recorte31/32, escalas, qualitativo, ética e início da implementação |
| 12 | Arquitetura e componentes; conector não atravessa a caixa de arquivos |
| 13 | Estado, armazenamento e orquestração; identificadores longos causam alguns espaços amplos, sem excesso de caixa |
| 14 | Diagramas de serviço/repositórios e fluxo de áreas |
| 15 | Consulta local, transformação de coordenadas, escala e exportação |
| 16 | Diagramas de lookup/exportação e fechamento da implementação; espaço residual mantido para não comprimir figuras |
| 17 | Fluxo de apresentação, referências às capturas e distinção da imagem de radiação |
| 18 | Telas inicial e polígono; detalhes pequenos dos originais continuam limitados em impressão |
| 19 | Três painéis de importação GeoJSON com confirmações e avisos legíveis |
| 20 | Mapa e painel/série; ausência do eixo temporal no original expressamente indicada |
| 21 | Clima e captura do PDF, sem alteração de valores; Figura18 não usada como prova da radiação |
| 22 | Duas capturas móveis e QR alinhados no topo, sem página exclusiva para QR |
| 23 | Resultados técnicos e demonstração de duas aquisições; título da avaliação com usuários deslocado para a página seguinte |
| 24 | Perfil e interpretação das tarefas com denominadores distintos |
| 25 | Gráfico de tarefas e tabela de utilidade; linhas e percentuais preservados |
| 26 | Gráfico ordinal de experiência, categorias e n válido, sem truncamento do eixo |
| 27 | Tabela temática e transição para discussão sem título órfão |
| 28 | Objetivos/evidências e discussão de contratos e autonomia |
| 29 | Limitações, conclusão e início da declaração deIA |
| 30–32 | Final da declaração e referências; URLs quebradas dentro das colunas, última página com continuação em uma coluna |
| Declaração1–2 | Quatro campos do anexo, prompts reais e área de assinatura em branco |

As capturas mantêm a resolução e o conteúdo originais. A leitura assistida de página não certifica conforto de leitura de todo detalhe em impressão nem acessibilidade do PDF. A imagem efetivamente embutida na página21 foi extraída com `pdfimages` e seus pixels conferem integralmente com o arquivo original.

### 3. Figuras e matemática

A representação de bandas/centros/resoluções é suficiente para explicar as combinações implementadas. Não foi inserida curva espectral sem fonte. Os demais esquemas identificam dados didáticos e não são apresentados como resultados empíricos.

Originais, homônimos, datas, hashes e inclusão LaTeX da captura de59,00 foram conferidos. Não apareceu arquivo substituto de conteúdo diferente: original e cópias têm SHA-256 `6d91cb54…`. Conforme a decisão expressa posterior de mantê-la, a imagem permanece **como ilustração da organização do relatório**, não como evidência de radiação correta. A verificação de unidades usa a resposta NASA e regressões/arquivos instrumentados, não a captura. Isso concilia a preservação autoral com a exclusão dessa imagem do conjunto probatório de correção científica. O novo diretório de compilação e a conferência da imagem embutida evitam atribuir o resultado a cache antigo.

As12 equações, três expressões de lookup e regressão foram examinadas; variáveis, unidades e condições permanecem explícitas. Janela3, z<−1 e inclinação±0,01 continuam heurísticos não calibrados. O relatório matemático delimita fontes e a pendência específica de precedente científico B8A/B11.

### 4. Síntese bibliográfica e originalidade

Nenhuma referência adicionada, removida ou substituída nesta rodada. Davis e Braun/Clarke passaram de acesso pendente a conteúdo primário conferido para as afirmações usadas. Gorelick teve resumo/autoria/veículo confirmados em fonte primária Google Research; texto integral, Amani e McFeeters permanecem parcialmente verificados. Não foram incorporadas candidatas sem leitura ou obras apenas para ampliar contagem.

A revisão de originalidade confrontou definições, sínteses e atribuições com as fontes disponíveis. Não foram encontradas novas passagens literais não atribuídas nesse confronto dirigido, sem alegar busca universal ou percentual. Não foram utilizados detectores ou enviados manuscrito/respostas a serviços de similaridade. Ver `AUDITORIA_REFERENCIAS.md` e `AUDITORIA_ORIGINALIDADE.md`.

### 5. Encaminhamento institucional e alternativa sem questionário

O questionário integra a versão para apreciação, como solicitado. Permanecem a decisão institucional sobre admissibilidade ética, a formalização do uso de IA/dados inéditos e a ciência à banca. Não houve assinatura simulada ou contato automático com autoridades.

Caso a UPF determine que os resultados do questionário não podem integrar o TCC, a alternativa preparada é:

1. Manter problema, OE1–OE8, fundamentos espectrais, arquitetura, métodos de processamento, testes, transferência controlada e demonstração real.
2. Retirar, **somente após essa decisão**, a subseção de avaliação com usuários dos métodos e a inclusão `final_4a_usuarios` nos resultados, preservando dados e histórico fora do artigo.
3. Retirar gráficos/tabelas e discussão de percepções, bem como números do questionário do resumo e da conclusão.
4. Manter na declaração de IA o tratamento e a análise efetivamente realizados, ainda que os resultados sejam retirados da apresentação científica.
5. Apresentar avaliação observacional com usuários como trabalho futuro condicionado a protocolo e apreciação institucional, sem prometer execução.

Essa alternativa é estrutural e está pronta para decisão do orientador; não foi ativada nem produzida uma exclusão definitiva nesta rodada.

### 6. Simulação crítica de banca

**Exercício assistido de preparação, não parecer de avaliadores reais nem previsão de aprovação.**

| Perspectiva | Pontos fortes e evidências | Fragilidade / questionamento provável | Gravidade e encaminhamento |
|---|---|---|---|
| Engenharia de Software | Responsabilidades modularizadas, repositórios intercambiáveis, snapshot e identidade de aquisição; `main.py`, `export_context.py`, pipeline, specs16/17;710 testes e Node | “Se os índices já existem, o que foi desenvolvido?” A resposta deve explicar integração, contratos e fronteiras, não reivindicar método espectral novo | Média: narrativa fortalecida; preparar demonstração dos contratos |
| Engenharia de Software | Gradefloat32/zlib/Base64 e consulta no navegador verificáveis | “Qual o custo em memória e qual o ganho de latência?” Há tamanhos controlados, não benchmark em produção; consultas por aquisição permanecem sequenciais | Alta para alegação de desempenho: não fazê-la; ensaios futuros |
| Engenharia de Software | Testes têm escopos separados e arquivos reais são preservados | “100% significa que está correto?” Serviços substituídos e expectativas podem não abranger semântica; entrypoint/JavaScript fora da cobertura Python | Alta: escopo explícito; nenhuma garantia de ausência de defeitos |
| Metodologia Científica | Questão e objetivos computacionais coerentes; rastreabilidade e métodos descritos | “Que método científico formal foi aplicado?” Construção e avaliação do artefato com consulta dirigida; não atribuir DSR retrospectivamente | Média: sustentar procedimento efetivo, não rótulo metodológico inventado |
| Metodologia Científica | Fonte pública contém integralmente o recorte e cálculos são reproduzíveis | “Por que31 se a fonte tem32 elegíveis?” Justificativa ainda não documentada; não responder que o adicional falhou na triagem | Alta: decisão/explicação do recorte necessária antes da entrega definitiva |
| Metodologia Científica | Consentimento informado e transparência de IA preservados | “Qual a aprovação ou dispensa ética e a autorização de IA?” Documentação formal não comprovada; declaração não substitui aprovação | Alta institucional: orientador/instância competente; alternativa estrutural acima |
| Metodologia Científica | Frequências, denominadores e codificação multirrótulo explícitos | “Questionário mede usabilidade validada?” Autorrelato por adesão, sem controle/psicometria/dupla codificação; não inferir causalidade ou população | Média: limites e prioridade de avaliação observacional |
| Sensoriamento/Geoespacial | Fórmulas e bandas explicitadas; ordem das agregações correta | “Por que NDWI e NDMI próximos?” Diferem emB8/B8A; não duas medições independentes de solo nem superioridade | Alta se interpretação errada: definições no texto e fonte técnica/científica delimitada |
| Sensoriamento/Geoespacial | QA60, escala nativa e ponderação descritas | “Nuvens/sombras e CRS não fixado afetam a comparação?” Sim, além de cobertura variável por aquisição; grade10m não cria detalhe em20m | Alta para equivalência numérica irrestrita: limitar alcance; avaliação futura de máscaras/grades |
| Sensoriamento/Geoespacial | Regra temporal reproduzível e exemplo didático explícito | “Qual sensibilidade/especificidade do detector?” Não medidas; janela não sazonal e demonstração com dois pontos não ativa regra | Alta para eficácia agronômica: não alegar; evidência atual é computacional |
| Sensoriamento/Geoespacial | Unidades normalizadas por metadados e saída ausente preservada | “A captura59,00 prova que a radiação está correta?” Não: ilustração da interface, excluída da verificação científica do valor | Alta de comunicação: distinção explícita e captura sem adulteração |

### 7. Perguntas de defesa e respostas fundamentadas

1. **Qual a contribuição própria?** A integração modular de serviços, geometrias, grades, estado e formatos, com consulta local e contratos verificáveis. Não são novos índices ou um modelo agronômico. Evidência: arquitetura, pipeline, snapshot e exportadores.
2. **Por que SDD?** O processo efetivamente utilizou especificações, critérios e tarefas para orientar implementação e testes. Não foi medido ganho sobre outros métodos e não se afirma uso do Spec Kit. Evidência: `docs/specs/index.md` e histórico.
3. **Por que transferir a grade?** Para consultar células no navegador após a análise, sem nova requisição de valor ao Earth Engine por evento. O compromisso é transferência/memória inicial; a latência em produção não foi medida. Evidência: `preload_index_values`, HTML e teste Node.
4. **O que os710 testes comprovam?** Aprovação dos comportamentos representados nos casos e cobertura de todos os caminhos medidos em `src/app`, no ambiente registrado. Não comprovam todos os usos, serviços externos ou correção de todas as expectativas. Evidência: log original e escopos dos testes.
5. **Como evitar exportar resultados de outra área?** A mudança de parâmetros invalida o snapshot; a geração verifica correspondência e usa contexto comum normalizado. Evidência: `invalidate_changed_analysis` e `build_export_context`.
6. **O mapa e a série deveriam ter a mesma média?** Não. O mapa é mediana por posição e depois média espacial; a série é média espacial por aquisição. A ordem das operações, máscaras e pesos muda o resultado. Evidência: equações e exemplo0,6/0,5.
7. **NDWI mede água superficial ou umidade do solo?** O identificador do sistema usaB8/B11, varianteNIR–SWIR; não é o verde–NIR de McFeeters e não mede diretamente umidade do solo. O chamadoNDMI usaB8A/B11. Evidência: código, catálogo e fontes delimitadas.
8. **Por que janela3 e−1?** São parâmetros heurísticos da implementação, sem calibração por cultura. A literatura oferece precedentes de padronização, não valida esses parâmetros locais. Não há justificativa histórica adicional comprovada. Evidência: código e auditoria matemática.
9. **A demonstração validou as anomalias?** Validou o encadeamento e os arquivos, não a aplicação do escore: duas aquisições são insuficientes. Os casos de regra foram verificados com dados controlados. Evidência: XLSX/CSV real, manifesto e testes.
10. **O que se conclui do questionário?** No recorte31 há média7,74, mediana8 e interesse declarado acompanhado de barreiras de autonomia; não uso continuado, representatividade ou eficácia agronômica. Evidência: distribuições e recomputação.
11. **Por que o registro32 não foi incluído?** A diferença entre fonte pública e arquivo analisado foi identificada e explicitada; sua razão ainda precisa ser esclarecida pelo responsável. Não há resposta documental que permita alegar inelegibilidade ou outra justificativa. Evidência: conferência pública.
12. **Houve aprovação ética e autorização formal de IA?** Não se apresenta aprovação ou dispensa ética, nem formalização de IA como comprovadas. O encaminhamento cabe ao orientador e àUPF. Há declarações transparentes e minuta sem assinatura, não regularização retrospectiva.
13. **A IA participou só da gramática?** Não. Houve especificação, geração/revisão de código e testes, análise quantitativa, codificação qualitativa, diagramas, pesquisa e reformulação substancial do artigo. Supervisão e responsabilidade são do pesquisador. Evidência: registro e declarações.
14. **Por que não comparar o sistema com plataformas comerciais em desempenho?** A comparação realizada é documental e por finalidade. Não houve benchmark; as plataformas podem ter recursos semelhantes, inclusive leitura por posição. Evidência: matriz e guias oficiais.
15. **Qual a próxima avaliação prioritária?** Para software, desempenho/compatibilidade e observação de tarefas; para interpretação agronômica, protocolo de campo e calibração temporal. São propostas de continuidade, não resultados obtidos.

### 8. Estado dos critérios e pendências

A consolidação editorial, a apresentação da contribuição e a recomputação do recorte foram realizadas. A verificação técnica/visual final é registrada nos manifestos desta rodada, sem alegar inspeção humana. Permanecem **parciais** a verificação primária integral de algumas referências e a justificativa31/32; permanecem **pendentes de decisão humana/institucional** a leitura substantiva final, a admissibilidade ética e os atos formais deIA. Portanto, o artigo pode ser encaminhado para apreciação do orientador, mas não se declara aceite integral de todos os critérios ou regularidade institucional definitiva.

Lista objetiva e classificação por responsabilidade em `PENDENCIAS_AUTOR.md`; alterações por arquivo em `CHANGELOG_ARTIGO.md`. As seções seguintes são histórico e não prevalecem sobre este parecer.

## Parecer histórico — rodada PA01–PA18

**15/11/2026, base `f31d0a5`: revisão implementada parcialmente; não concluída pelos critérios de aceite.** Todas as 18 decisões receberam encaminhamento em `PENDENCIAS_AUTOR.md`, mas autorização de execução não foi confundida com evidência ou aprovação institucional. A versão resultante é para revisão, não para entrega institucional definitiva.

### Alterações realizadas

- Orientador corrigido para Prof. Rafael Rieder; mês dezembro de 2026; classe institucional e endereço do repositório preservados.
- Escopo definitivo computacional; retirada da cobrança de estudos agronômicos por cultura como objetivos atuais. O histórico permanece no Git e neste registro.
- SDD descrito com especificações/tarefas/decisões/commits existentes e supervisão declarada pelo autor. Fontes técnicas de SDD distinguidas de publicações científicas.
- Formulação B8/B11 conferida na Tabela 1 do PDF de Izquierdo-Sanz e Moltó; NIST acrescentado à mediana e Meroni ao escore/limiar, sem atribuir validação à janela3.
- Fundamentos de responsabilidades de módulos, testes e limites da cobertura ampliados; sem atribuir um padrão arquitetural novo ao projeto.
- Trabalhos relacionados em seção própria, com comparação por finalidade e funcionalidades verificadas em fontes oficiais; arquitetura local não apresentada como exclusividade.
- Registro de aprovação qualitativa pelo autor e distinção entre estratégia, execução assistida e supervisão. Ausência de dupla codificação preservada.
- Declaração de IA no artigo e minuta independente conforme o anexo da IN oficial, incluindo geração/reformulação substancial e auditorias posteriores.
- Análise da planilha identificada como tal, sem consolidá-la como evidência empírica confirmada. Não houve alteração de respostas, carimbos ou categorias nesta rodada.
- Auditoria preliminar de atribuição/originalidade criada, sem percentual inventado.

### Integridade dos dados: resultado e impedimento

As duas planilhas foram localizadas: original preservado (`d61b9f...`) e versão anteriormente corrigida (`9adb66...`). A conferência independente passou para 31 registros, 40 itens e 191 categorias; as 49 colunas de respostas permanecem idênticas, e somente os sete carimbos da retificação histórica diferem. Não houve retificação nova.

O original recebido contém metadados openpyxl e sete carimbos posteriores à data de criação declarada. Isso **não prova fabricação**, mas impede usar metadados como autenticação de exportação original do Forms. As fixtures conhecidas em `tests/test_user_survey_analysis.py` e `avaliacao_usuarios/scripts/test_analise.py` são separadas da planilha; a ausência de seus textos não exclui toda possível origem sintética desconhecida.

O autor declara dados reais, fuso Brasília e encerramento; são informações registradas como declaração. Não foram localizados exportação independente original do serviço, registro administrativo de encerramento ou commit exato público. A consulta passiva do formulário mostrou a primeira etapa e o orientador antigo; **não foi enviada resposta nem acionada a etapa seguinte**. A página, sozinha, não confirma nem refuta recebimento de novas respostas. O artigo mantém números para inspeção, mas não os apresenta como resultados empíricos confirmados, e não consolida aceitação na conclusão/resumo.

### Ética, consentimento e IA

A primeira etapa pública informa finalidade acadêmica, ausência de solicitação de nome/e-mail e participação voluntária, com pergunta conjunta de idade/leitura/consentimento. Não foi obtido histórico imutável completo das páginas do formulário em todas as datas da coleta. Idade é autodeclarada. Ausência de identificador direto não certifica anonimato, sobretudo em perfis pequenos e excertos literais.

O autor informa não submissão ao CEP e ausência de orientação prévia sobre a necessidade. A Resolução CNS510/2016 foi obtida em fonte oficial: art.1º diferencia hipóteses e §1º não permite presumir que TCC seja simples atividade de ensino dispensada pelo incisoVIII. A hipótese de opinião pública do incisoI tampouco foi automaticamente aplicada a este instrumento. A investigação identificou também a necessidade de conferir o regime da Lei14.874/2024 e Decreto12.651/2025 e orientações de transição; não se concluiu parecer jurídico de enquadramento. Cabe à instância competente da UPF decidir o encaminhamento e a possibilidade de utilização dos resultados. O texto não regulariza retrospectivamente a pesquisa.

A IN03/2026/PROACAD de 28/10/2026, obtida por link oficial público da UPF, foi lida integralmente (5 páginas e anexo). Art.4º exige autorização e limites em documento por canais formais; art.6º exige descrição no trabalho e declaração específica; art.8º exige ciência à banca; art.3ºVI protege dados inéditos. Os arts.5º/10/11 não são atendidos apenas pela existência de um PDF assinado: uso efetivo, transparência e responsabilidade precisam corresponder à prática. Não há documento de autorização, limites, dados inéditos ou comunicação à banca localizado. A minuta não foi assinada.

### Impedimentos que permanecem

1. PA05/07/08: procedência e decisões institucionais acima.
2. PA11/12: validação bibliográfica integral e ampliação científica ainda parcial. Oito novas entradas estão individualmente delimitadas; fontes primárias bloqueadas não foram dadas como lidas.
3. PA14: reconstrução das três curvas com fonte/direitos específicos não concluída. O esquema anterior foi retirado do PDF, com histórico preservado no Git; não se aceita atribuição genérica a Weiss como origem das três curvas. As outras quatro figuras conceituais foram preservadas.
4. PA15: captura disponível é idêntica à excluída e ainda mostra radiação59,00 MJ/m²/dia. Não incorporada.
5. PA18: leitura e aprovação humana da nova versão e da minuta, além da revisão direta das fontes pelo pesquisador.

### Entrega e rastreabilidade

Fontes/PDF atualizados, bibliografia, pareceres, matriz, originalidade, registro de IA, minuta independente, diff antes/depois, hashes, relatório de compilação e inspeção assistida ficam ligados por `evidencias/revisao_final_pa/README.md`. Os manifestos anteriores não foram sobrescritos. Não houve alteração funcional, novo deploy, commit, push ou contato com autoridades acadêmicas.

## Registro histórico da auditoria anterior

**Data:** 15/11/2026. **Parecer:** revisão parcial com correções fundamentadas; **não declarar conclusão integral**. A entrega reúne fontes/PDF revistos e os seis registros solicitados, mas a validação semântica exaustiva de todas as afirmações, a normalização institucional e decisões substantivas continuam abertas.

## 1. Escopo, versão e método

- Entrada: `docs/artigo_final/Relatorio_Final.tex`, classe `CC-EC_TF-TC.cls`, inclusões `final_*.tex`, figuras e resultados gerados da avaliação com usuários. Não confundir arquivos antigos `Proposta.tex`/capítulos da proposta com o artigo final.
- Checkout: `dev`, HEAD `6edf8707dc047eae762365b71c5e892321eeaef6`, com alterações anteriores não commitadas. A linha de base é a cópia de trabalho pré-auditoria, não HEAD. Hashes em `INVENTARIO.json`; backup em `/tmp/opencode/auditoria-cientifica/artigo-antes-auditoria.tar.gz`.
- Protocolo autoral lido integralmente; artigo lido antes das alterações, em confronto com núcleo analítico, geoespacial, armazenamento, exportação, testes, manifestos e histórico. Código e resultados não foram alterados nesta auditoria.
- Pesquisa: consultas públicas oficiais/científicas com status, URL, tamanho e hash em `CONSULTAS_FONTES.json` e `CONSULTAS_COMPLEMENTARES.json`. Cache local `/tmp/opencode/auditoria-cientifica/fontes/`; sua retenção é local, não um repositório público de PDFs de terceiros.
- Metadados foram separados do conteúdo. Acesso bloqueado, desafio HTML com HTTP 200 e PDF efetivo têm tratamentos distintos. “Texto integral disponível” não significa leitura de todas as páginas; o parecer individual indica as seções examinadas.
- Foram feitas correções localizadas após conferir a fundamentação. As alterações substantivas são propostas para aprovação do autor, não uma substituição de sua contribuição.

## 2. Contagens e significado

| Item | Quantidade / situação |
|---|---|
| Entradas bibliográficas originais com parecer individual | 34 |
| Novas entradas | 18 |
| Entradas atuais no `.bib` | 52 |
| Substituídas / removidas | 0 / 0 |
| Fontes com escopo substantivo conferido | 36 de 52; não significa validação integral de todos os metadados e afirmações |
| Demais registros | 16 com acesso, metadados, suporte ou condições parcialmente confirmados/pendentes |
| Equações analíticas examinadas | 12 |
| Expressões de lookup adicionais | 3, em duas linhas numeradas |
| Ajuste linear | 1 método não numerado |
| Blocos na matriz | 197, inventário de triagem; não 197 afirmações integralmente validadas |
| Problemas agrupados abaixo | 24: 14 corrigidos no escopo indicado, 10 pendentes/parciais |

As contagens não somam citações repetidas nem resultados históricos como novas observações. Fontes candidatas não incorporadas estão separadas da bibliografia. Slaiffer 2023 e 2025 foram conservados como documentos distintos relacionados, não como duas confirmações independentes do mesmo resultado.

## 3. Registro de problemas e correções

Gravidade: crítica = pode mudar interpretação científica; alta = suporte/metodologia insuficientes; média = precisão, rastreabilidade ou normalização. “Corrigido” limita-se à lacuna descrita, não aprova todo o parágrafo.

| ID | Localização | Gravidade | Problema / fundamento | Correção recomendada e executada | Evidência / status |
|---|---|---|---|---|---|
| AC01 | Fundamentação, representação espacial | Média | Raster/vetor/legenda sem fonte específica. | Inseridas referências técnicas QGIS próximas às definições. | QGIS Vector/Raster/Map Production; Corrigido |
| AC02 | NDVI, Eq. 1 | Alta | Base histórica descrita somente pelo registro NASA; limites genericamente atribuídos a Weiss. | Conferida seção Spectral Analysis de Rouse; separada adaptação Sentinel-2; Gao sustenta saturação/solo e Weiss condições de aquisição. | PDFs Rouse/Gao/Weiss; Corrigido |
| AC03 | NDWI, Eq. 2 | Crítica | Omissão dos comprimentos de onda originais pode sugerir equivalência Gao/B11. | Explicitar 0,86/1,24 µm versus B11 ~1,61 µm; preservar identificador do software. | Gao 1996 e catálogo S2; Corrigido |
| AC04 | NDMI, Eq. 3 e resolução | Alta | USGS não sustenta sozinho adaptação B8A/B11; grade 10 m exige explicação de reamostragem. | Adicionado exemplo técnico Sentinel Hub com inconsistência interna explícita; descrito vizinho mais próximo padrão e ausência de ganho físico de resolução. | USGS/Sentinel Hub/EE Resample; Corrigido |
| AC05 | Médias espaciais, Eqs. 5–6 | Alta | Pesos gerais pouco explícitos, risco de supor produto máscara×fração. | Definidos mínimo, quantização de oito bits, limiar aproximado e denominador positivo. Mantidas fórmulas gerais. | Guia EE reduceRegion; Corrigido |
| AC06 | Média móvel, Eq. 7 | Alta | Conceito sem referência estatística; janela de três pode parecer calibrada. | Fundamentado conceito em Hyndman e explicitada janela retrospectiva heurística de observações. | Livro aberto e anomalies.py; Corrigido |
| AC07 | Desvio/escore, Eqs. 8–9 | Alta | Divisor e distinção de testes formais precisavam de suporte próximo. | Adicionados NumPy e NIST com distinção entre escore da janela e escore amostral/teste; limites e NaN preservados. | np.std/ddof e NIST; Corrigido |
| AC08 | Tendência | Alta | polyfit/limiares sem fundamentação e insuficiência n<2 pouco explícita. | Inserida função objetivo de mínimos quadrados; definidas inclinação/intercepto e natureza heurística; “estável” com n<2 não é evidência. | Hyndman/NumPy/código/histórico 32c462d; Corrigido |
| AC09 | NASA, fundamentação | Alta | Resoluções originais não explicitadas. | Inseridas grades principais 0,5°×0,625° e 1°×1°, distinguindo aliases de alta resolução. | NASA Methodology; Corrigido |
| AC10 | NASA, Eqs. 10–12 | Alta | Definições/unidades dos parâmetros sem dicionário específico. | Acrescentado catálogo diário AG, precipitação, temperatura a 2 m e energia solar diária; prevalência de metadados mantida. | JSON oficial; Corrigido |
| AC11 | Radiação, Eq. 12 | Alta | Conversão correta no código, sem derivação e fonte metrológica. | Mostrada identidade kWh→MJ pelas definições SI; nenhuma inferência por magnitude. | BIPM/climate.py/regressões; Corrigido |
| AC12 | Avaliação técnica | Alta | Escopos de testes/cobertura sem fonte específica de Engenharia de Software. | Adicionado capítulo de Bender sobre escopo/comportamento/cobertura; sem atribuir processos Google ao projeto. | Software Engineering at Google, cap. 11; Corrigido |
| AC13 | Avaliação por adesão | Alta | Amostragem/autoseleção sem fonte metodológica próxima. | Referência AAPOR adicionada; não acrescentada inferência populacional. | Relatório 2013, sumário/recomendações; Corrigido |
| AC14 | Estado da interface | Média | Reexecução e estado descritos sem documentação de arquitetura da biblioteca. | Inserida documentação oficial Session State e limitação de persistência. | Streamlit e código; Corrigido |
| AC15 | Citações a artigos/norma sem acesso integral | Alta | Amani/Gorelick/McFeeters/Davis/Braun/ISO não tiveram conteúdo integral confirmado nesta rodada. | Limites registrados individualmente; obter textos e conferir subafirmações antes da aprovação. Não foi declarado suporte integral. | Auditoria de referências, PA11; Pendente |
| AC16 | Metadados e registros não citados | Média | Rouse duplicado, TCCs registrados como mastersthesis, Phiri com nome divergente, Wazlawick e repositórios pendentes. | Preservados sem correção especulativa; resolver com exemplares/registros institucionais. | Pareceres individuais; Pendente |
| AC17 | Modelo institucional/cabeçalho | Alta | Classe local não confirma vigência institucional, mês vazio e campo/link do template. | Classe preservada; solicitar confirmação institucional e dados. Aviso overfull histórico continua. | Classe v1.1, PA09–10; Pendente |
| AC18 | Caracterização aplicada/tecnológica | Alta | Descrição condiz com artefato, mas fundamentação metodológica formal incompleta. | Não inserir DSR/TDD/revisão sistemática por retrospectiva; consultar obra metodológica efetiva com autor. | Código/histórico; PA12; Pendente |
| AC19 | Arquitetura/modularidade/interoperabilidade | Média | Correspondência técnica examinada, mas fundamentação conceitual ampla ainda insuficiente. | Estado e testes fundamentados; não atribuir microsserviços/REST. Completar fontes específicas sem referências decorativas. | Código/diagramas; PA12; Parcial |
| AC20 | Tabela de plataformas | Alta | Página comercial não comprova automaticamente cada célula/condição de plano; EO Browser bloqueado. | NI preservado sem inferência negativa. Necessária matriz célula→trecho/URL/data antes de validação integral. | EOSDA/OneSoil/consulta EO Browser; Parcial |
| AC21 | Figura espectral | Média | Desenho qualitativo identificado, mas Weiss não confirma origem exata de cada curva solo/água. | Preservado como esquema; solicitar fonte específica ou revisão conceitual aprovada. | PA14; Pendente |
| AC22 | Figuras/capturas e revisão visual | Média | Não concluir legibilidade integral pelo sucesso da compilação; captura de radiação inválida permanece excluída. | Originais preservados; inventário gráfico e inspeção final devem ser concluídos, sem reconstrução de evidências. | PA15/18; Parcial |
| AC23 | Análise temática/ética/IA | Alta | Categorização e interpretação ainda sem aprovação substantiva e documentação institucional. | Manter transparência sobre IA, ausência de dupla codificação e pendências; não alegar chancela ética. | PA06–08; Dependente do autor |
| AC24 | Proveniência temporal/versão de coleta e rastreabilidade exaustiva | Alta | Commit público/fuso/fechamento e sustentação fina de cada subafirmação ainda incompletos. | Preservados intervalo, respostas, resultados e distinção de versões; matriz explicita triagem, sem aprovação automática. | PA05, matriz; Parcial |

## 4. Achados preservados sem nova alteração funcional

- Problema e objetivo tratam integração/verificação de plataforma computacional, não diagnóstico agronômico. A contribuição não é criar índices ou mínimos quadrados.
- Equações e código correspondem nos contratos examinados; rótulos NIR–SWIR exigem bandas explícitas, não duas “medidas independentes” de água no solo.
- Mediana do índice por pixel é distinta do índice das medianas de bandas; médias espaciais e temporais não são intercambiáveis.
- Série ordenada por data, sem interpolação, sem composição diária, admite múltiplas aquisições por data; irregularidade influencia janela e inclinação.
- QA60: bits 10/11, sem máscara específica de sombras; indisponibilidade histórica descrita. A documentação tem uma fronteira temporal que não foi “resolvida” artificialmente. Filtro de nuvem do produto não equivale à nuvem no talhão.
- Datas UTC inclusivas na interface, próximo dia exclusivo no EE; NASA usa `time-standard=UTC`. Resposta histórica LST não foi rebatizada como nova consulta UTC.
- Não foram alteradas respostas, dados da planilha, números da avaliação, código da aplicação, imagens originais ou arquivos de execução histórica. Nenhum commit, push, merge ou deployment nesta auditoria.

## 5. Evidência computacional

### Execução histórica — preservada no artigo

Commit `28759bf`, 710 aprovados em 11,73 s, 2.735 instruções e 856 ramificações em `src/app`, cobertura medida 100%; três verificações JavaScript e demonstração instrumentada em navegador com serviços reais. Evidências em `evidencias/` e `evidencias/demonstracao_real/`.

### Nova execução — não substitui números históricos

Comando na raiz: `COVERAGE_CORE=ctrace .venv/bin/python -m pytest -q -p no:cacheprovider`.

Resultado: **710 aprovados em 12,29 s**, 2.735 instruções, 856 ramificações, zero perdas e caminhos parcialmente cobertos, **100%** no escopo configurado `--cov=src/app --cov-branch` em `pytest.ini`. Log `TESTES_PYTHON.txt`. Não inclui entrypoint externo `streamlit_app.py`, JavaScript, dependências, serviço remoto ou arquivos fora de `src/app`.

JavaScript: `node --test tests/browser/index_hover.test.cjs`; resultado em `TESTES_JAVASCRIPT.txt`. Esta rodada não executou nova demonstração manual em navegador nem avaliação de hospedagem. Cobertura não prova ausência de defeitos, correção científica, segurança, desempenho ou qualidade agronômica.

Versão avaliada nesta rodada: checkout indicado acima, com fontes documentais modificadas; código da aplicação não alterado pela auditoria. O manifesto de validação registra hashes e ambiente para não atribuir indevidamente testes a um commit inexistente.

## 6. Figuras, tabelas e resultados

| Item | Conferência / limite |
|---|---|
| Figura 1, espectro | Curvas qualitativas sem escala/medição; fonte específica de solo/água pendente, AC21. |
| Figura 2, bandas | Centros S2A/S2B e resoluções B4/B8/B8A/B11 conferidos no catálogo harmonizado; não generalizar valores para todo satélite da missão. |
| Figura 3, raster/vetor | Esquema autoral, não observações; polígonos/grade/legenda coerentes com representação. |
| Figura 4, agregações | Aritmética conferida: média das médias 0,6 versus média da mediana por pixel 0,5. Pesos iguais, sem máscaras. |
| Figura 5, janela | Exemplo didático: média 0,6; σ≈0,08165; z≈−4,899. Não demonstra eficácia agronômica. |
| Fluxos de análise/anomalias | Correspondência examinada com pipeline, séries e anomalies; primeiros registros/escore zero e ausência de diagnóstico preservados. |
| Arquitetura, serviço de áreas, fluxos de áreas/lookup/exportação | Fronteiras Python/navegador/EE e armazenamento local/sessão examinadas; não representam microsserviços. Rotação da grade não é implementada no lookup. |
| Capturas do autor | 16 de 17 imagens em 11 agrupamentos, originais preservados; não pressupor a mesma execução ou versão da demonstração instrumentada. Captura problemática de PDF excluída. |
| Gráficos/tabelas de usuários | Descritivos das 31 submissões elegíveis; não avaliação observacional ou psicométrica. Sem mudança de dados, denominadores ou resultados nesta rodada. Codificação/ética dependem do autor. |
| Tabela de plataformas | Documental; validação célula por célula não concluída, AC20. |
| Tabela de componentes | Conferida em relação aos módulos; abstrações não constituem aplicação integral de padrão arquitetural. |
| Objetivos/resultados/conclusão | Distinguem recurso implementado, teste e estudo agronômico não realizado. Aprovação da mudança de escopo e interpretações pendente. |

`COMPILACAO.json` confirma 33 páginas, 27 figuras, cinco tabelas, 45 chaves citadas, nenhuma referência indefinida, oito ambientes matemáticos preservados e classe institucional inalterada. Permanece o aviso de cabeçalho `Overfull hbox (54.64pt)`. `VALIDACAO_FINAL.json` complementa o registro de ambiente, integridade e hashes. PDF: SHA-256 `0fffb8827d34c75662a20bce87a5fa68f991de1ae226cca678790164b65c7f8d`.

As 33 páginas foram renderizadas e examinadas em seis folhas de contato para triagem do layout geral: não foram identificadas páginas vazias ou sobreposições grosseiras. Essa escala não permite certificar todos os detalhes de capturas, caracteres, referências e equações; a inspeção ampliada e a aprovação visual do autor permanecem pendentes. Páginas com figuras isoladas e espaços amplos são consequência dos floats existentes, não novas medições.

## 7. Critérios de aceite

| Critério | Estado |
|---|---|
| Leitura do artigo, confronto de código/testes/evidências | Executado no escopo registrado |
| Todas as referências originais inventariadas e com parecer | Atendido: 34 |
| Todas as referências integralmente confirmadas em conteúdo e metadados | Não atendido: limitações individuais |
| Novas fontes com origem verificável | Atendido no escopo de trechos consultados: 18 |
| Doze equações e regressão examinadas | Atendido, mais três expressões; calibração não demonstrada |
| Heurísticas e nomenclatura esclarecidas | Melhorado; decisão de nomenclatura depende do autor |
| Todas as afirmações relevantes sustentadas individualmente | Não atendido: matriz é triagem, revisão fina permanece |
| Métodos/resultados correspondentes às evidências | Confrontados nos contratos descritos; não valida todo uso possível |
| Respostas sintéticas não apresentadas como resultados | Preservado; nenhum dado novo gerado |
| Limitações explicitadas | Preservadas e ampliadas localmente |
| Compilação sem erros/citações indefinidas | Ver validação automatizada desta versão, não reutilizar hash anterior |
| Revisão visual integral e normalização institucional | Não concluídas |
| Seis documentos obrigatórios | Disponíveis neste diretório |
| Aprovação autoral/ética/IA | Pendente |

## 8. Parecer

A versão revista esclarece a diferença entre fórmula histórica, adaptação espectral, estatística elementar e heurística da aplicação. A fundamentação de agregação espacial, mínimos quadrados, unidades meteorológicas, amostragem e testes ficou mais específica. Isso melhora a defensabilidade do recorte computacional, **sem demonstrar validação agronômica**.

Ainda não é possível emitir parecer de revisão científica integral concluída. A existência dos seis documentos, a execução dos testes e a compilação são entregas verificáveis, mas não suprem textos inacessíveis, revisão de todas as subafirmações, validação visual, normalização institucional ou aprovação intelectual do autor/orientador. As pendências não devem ser convertidas em fatos por redação.
