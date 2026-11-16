# Relatório de revisão autoral

**Data:** 15/11/2026. **Base:** `af120d5d25bbde5446541917ea0e9fe3c50c4425` (`dev`).
**Referência obrigatória:** [`../PERFIL_AUTORAL_E_PROTOCOLO_REVISAO.md`](../PERFIL_AUTORAL_E_PROTOCOLO_REVISAO.md), lida integralmente antes do diagnóstico.
**Situação:** revisão textual executada e disponível para aprovação substantiva do autor; validação técnica descrita abaixo. Sem commit ou push.

## 1. Diagnóstico inicial — fase 1

A leitura integral abrangeu `Relatorio_Final.tex`, os nove arquivos `final_*.tex`,
`referencias.bib`, `figuras_relatorio.tex` e os arquivos TikZ de `fig/`.
O diagrama `casos_uso.tex` existe, mas não integra a árvore de inclusão atual.
A proposta e seus capítulos são históricos: não serão reescritos.

O artigo apresenta contribuição de integração computacional, não novos índices
ou validação agronômica. A estrutura e as equações estão coerentes com esse
recorte. Já existem ressalvas importantes sobre QA60, bandas de 20 m,
denominadores válidos, serviços externos, cobertura de testes e pesquisa sem
respostas. Essas ressalvas devem ser preservadas, não tratadas como falhas de estilo.

As principais divergências em relação ao perfil qualitativo são:

- Parágrafos enumerativos que apresentam componentes antes do problema que resolvem.
- Termos de engenharia sem explicação inicial, como contratos, snapshot e lookup.
- Transições curtas entre fundamentos e aplicação, sobretudo em agregação e arquitetura.
- Repetição de delimitações entre apresentação, resultados e discussão.
- Construções próprias de relatório de auditoria no corpo do artigo.
- Siglas científicas e técnicas sem definição na primeira ocorrência.

Pontos científicos/editoriais a tratar:

- Os 710 testes e tempos são resultados históricos documentados, não uma execução nova desta revisão.
- A resposta NASA usada para demonstrar o erro de unidade é LST; o fluxo corrigido consulta UTC.
- O gráfico une observações por segmentos, mas não calcula observações diárias intermediárias.
- A coluna `classification` pertence à exportação de anomalias, sem classe agronômica produzida pelo detector.
- O instrumento completo da pesquisa não foi disponibilizado; não atribuir perguntas e escalas verificadas apenas a partir da apresentação.
- As fontes bibliográficas precisam distinguir verificação de metadados, leitura da documentação e leitura integral de artigos.

## 2. Plano por seção — fase 2

P1: integridade e consistência científica; P2: raciocínio, clareza e continuidade;
P3: padronização e apresentação. Não significa que todo parágrafo precise mudar.

| Seção / arquivo | Prioridade e intervenção | Confirmação ou limite |
|---|---|---|
| Introdução / `final_1_introducao.tex` | P2: explicar o problema de integração e os contratos por exemplos; preservar pergunta e OE1–OE8 | P1: aprovação do orientador para o escopo executado |
| Fundamentação / `final_2_fundamentacao.tex` | P1/P2: definir siglas, relacionar bandas, agregações e aplicação; preservar fórmulas e citações | Fonte específica da variante B8A/B11; leitura integral bibliográfica |
| Métodos / `final_3_metodos.tex` | P1/P2: distinguir procedimentos executados e previstos; explicar dependências e regras sem inventar motivações | Instrumento, ética e justificativas pessoais não documentadas |
| Implementação / `final_3a_implementacao.tex` | P2: problema → mecanismo → consequência; explicar termos de engenharia | Sem alterações funcionais ou reconstituição de decisões pessoais |
| Plataforma / `final_3b_plataforma.tex` | P1/P2: esclarecer séries, exportações e caráter das capturas; revisar legendas | CAP-18/19 e dispositivos físicos permanecem pendentes |
| Resultados / `final_4_resultados.tex` | P1: contextualizar evidências históricas, LST e dois pontos por série | Sem novo experimento ou resultados de usuários |
| Discussão / `final_5_discussao.tex` | P2: interpretar compromissos de engenharia e limites, reduzir repetições | Preservar ressalvas operacionais e mudança de escopo |
| Conclusão / `final_6_conclusao.tex` | P2: responder ao problema a partir das evidências; priorizar continuidade | Sem generalizar eficácia agronômica ou usabilidade |
| Resumo/abstract / `final_0_resumo.tex` | P1/P2: revisar por último, com equivalência e escopo dos resultados | Não ampliar evidências ou omitir avaliação pendente |
| Figuras, tabelas e bibliografia | P1/P3: conferir inclusão, legendas, termos, chaves e metadados | Manter classe institucional e fontes históricas |

## 3. Preservação e rastreabilidade

- Cópia anterior de 22 arquivos (fontes, diagramas e PDF):
  `/tmp/opencode/revisao-autoral-original.tar.gz`.
- SHA-256 do backup:
  `2e7185c96a31dae2fe88f1402111974111c68ca453c5249ed1fce3d1434b33c8`.
- A base Git permite comparar cada trecho rastreado por `git diff`.
- Preservados os arquivos preexistentes não rastreados: `AGENTS.md`,
  `docs/PERFIL_AUTORAL_E_PROTOCOLO_REVISAO.md`, `Imagens Artigo/` e
  `Relatorio_Final-modelo-anterior.pdf`. O protocolo não será reescrito.
- A revisão não modifica código, testes, dados da demonstração ou relatórios históricos.

## 4. Registro da assistência de IA

Revisão assistida por GPT-6.1 Sol (OpenAI), no OpenCode, sob solicitação do autor.
A assistência compreende diagnóstico, edição textual, inspeção de código e
evidências, conferência bibliográfica e validação do LaTeX. Não representa
certificação de autoria, aprovação institucional ou leitura integral de fontes
indisponíveis. Não foram utilizados detectores, humanizadores ou serviços de
classificação; o manuscrito não foi enviado a serviços externos de revisão.
O autor deve aprovar substantivamente a argumentação e confirmar com o orientador
como declarar a assistência segundo as regras da UPF.

## 5. Alterações executadas — fase 3

| Arquivo / seção | Alteração e justificativa |
|---|---|
| `final_1_introducao.tex` | A integração foi explicada pela necessidade de manter área, imagens e saídas correspondentes. O termo “contratos” ganhou exemplos de datas, unidades e ausências. A contribuição passou de inventário de recursos a fluxo de uso; retirou-se a ambiguidade de que experiência de uso já teria sido avaliada. Pergunta, objetivo geral e OE1–OE8 preservados. |
| `final_2_fundamentacao.tex` | Polígono, raster, legenda, bandas e agregações foram relacionados à aplicação. MSI, NIR, SWIR, NDVI, NDWI, NDMI, USGS, ERTS-1 e API foram explicitados. Preservaram-se a distinção Gao/McFeeters, os limites da fonte Landsat para NDMI e a resolução nativa de 20 m. O fechamento dos esquemas foi integrado ao raciocínio, sem repetir toda a fundamentação. |
| `final_3_metodos.tex` | O método foi organizado em função da construção e verificação do artefato. Explicaram-se TDD, UTC, CRS, UTM, LST e SUS e a diferença entre fórmula populacional do desvio e população agronômica. A resposta histórica LST foi distinguida da requisição atual UTC. A descrição das perguntas não recebidas foi convertida em previsão a conferir, não fato sobre o instrumento completo. |
| `final_3a_implementacao.tex` | Estado, armazenamento, orquestração, grade, legenda e exportação passaram a explicitar problema, mecanismo e consequência. Snapshot, tiles e lookup foram explicados em contexto. A versão avaliada foi identificada pelo commit que efetivamente consolidou as correções, sem alterar a data ou os resultados dos ensaios. |
| `final_3b_plataforma.tex` | O fluxo parte da definição da área. A consulta por célula foi distinguida de precisão agronômica; esclareceu-se que segmentos no gráfico não são observações diárias calculadas. Pendências visuais de XLSX/ZIP foram explicitadas, e a legenda móvel informa 390 × 844 pixels. |
| `final_4_resultados.tex` | O artefato foi apresentado como resposta ao fluxo proposto. O tempo de 11,73 s foi situado como execução registrada, não desempenho do sistema. A evidência LST e a origem do erro MJ/kWh ficaram explícitas. Com dois pontos, a regra de anomalias nem chega a ser aplicável; isso foi separado de eficácia. |
| `final_5_discussao.tex` | Foram desenvolvidas as consequências das fronteiras entre representações e do pré-carregamento. Reduziu-se repetição sobre o escopo original, preservando integralmente a ausência de estudos de culturas/campo. A divergência de unidade foi interpretada como limite da cobertura, não falha de sintaxe. SCL foi explicitada. |
| `final_6_conclusao.tex` | A conclusão responde ao problema por integração e coerência entre entradas e saídas, vinculando testes e demonstração aos limites do que comprovam. A continuidade foi priorizada pela consolidação da avaliação; possibilidades de expansão já existentes permanecem futuras, não foram atribuídas ao autor novas decisões executadas. |
| `final_0_resumo.tex` | Resumo e abstract foram revisados por último e conferidos quanto a método, recursos, 710 testes, escopo de cobertura, três testes JavaScript e limites. As siglas dos índices foram definidas e a síntese ajustada ao espaço da primeira página sem reduzir fonte nem alterar a classe. |
| `fig/fluxo_consulta_pixel.tex` | O evento passou de apenas `mousemove` para movimento ou toque, conforme os handlers `mousemove` e `click` implementados. A nota distingue consulta numérica e carregamento de tiles. |
| Figuras e tabelas restantes | Conferidas integralmente; mantidas quando já adequadas. Os cinco esquemas permanecem didáticos e as capturas continuam reais. Não foram criados gráficos, screenshots ou dados experimentais. |
| `referencias.bib` | Protegida a capitalização de Google Earth Engine, EOSDA Crop Monitoring e OneSoil em títulos. Eliminada a impressão duplicada de URL em duas entradas, mantendo os endereços e datas nas notas. Autores, anos, DOI/URL e chaves preservados; nenhuma referência removida ou introduzida. |

Não foi imposta uma sequência fixa de conectivos ou frases. Os trechos já
adequados permaneceram, inclusive descrições técnicas detalhadas necessárias à
reprodução. As ressalvas que cumprem funções diferentes em método, resultados
e discussão não foram eliminadas apenas por mencionar o mesmo limite.

## 6. Auditoria de consistência — fase 4

O conjunto revisado foi relido e confrontado com:

- `earth_engine.py`, `pipeline.py`, `time_series.py` e `anomalies.py`: bandas,
  datas inclusivas, máscara, mediana, médias, IDs, janela, limiar e tendência.
- `climate.py`: consulta ao centroide, UTC, parâmetros, unidades declaradas,
  números finitos, ausências e agregações.
- `main.py`, `maps.py`, `map_interaction.py` e HTML/JavaScript: seleção,
  restauração, invalidação, grade UTM, limites, legenda e consulta por toque.
- Serviço de localizações, importador GeoJSON e contratos de exportação:
  alternativas local/sessão, nomes, limites, snapshot, campos e formatos.
- `evidencias/pytest_segunda_rodada.txt`, `node_segunda_rodada.txt`,
  `nasa_power_unidades.json` e `demonstracao_real/`: resultados e sua procedência.
- Proposta histórica e `CORRECOES_TECNICAS.md`: planejamento não foi convertido
  retrospectivamente em experimento executado.

Os 28 arquivos de código enumerados no manifesto da demonstração têm SHA-256
idêntico ao código atual. A suíte Python não foi reexecutada nesta atividade
editorial; os 710 testes em 11,73 s e 100% de cobertura continuam sendo os
resultados históricos preservados. Não houve nova consulta agrícola, novo
ensaio em navegador, submissão ao Forms ou implantação.

Permanecem coerentes entre as seções: NDWI B8/B11 e NDMI B8A/B11; resumo da
composição distinto da série por aquisição; clima como contexto sem causalidade;
heurística sem diagnóstico; demonstração sem identidade de cultura; avaliação
de usuários apenas prevista. Os oito ambientes de equações foram preservados
literalmente, assim como os oito objetivos específicos, títulos de seções,
rótulos e conjunto de chaves citadas.

## 7. Conferência bibliográfica

Consulta de fontes públicas em 15/11/2026, sem envio do manuscrito.
**Documentação lida** não equivale a validação independente do produto;
**metadados conferidos** não equivalem à leitura integral de um artigo.

| Chave(s) citada(s) | Verificação e limite |
|---|---|
| `ESA_SENTINEL2` | Página oficial SentiWiki acessível: resoluções e revisita nominal, com ressalva sobre a configuração operacional. A figura de bandas informa explicitamente S2A/S2B, não todos os instrumentos futuros. |
| `GOOGLE_S2_SR` | Catálogo oficial lido: doze bandas L2A, ausência de B10, escala, resoluções, centros espectrais, metadado de nuvens e restrição histórica de QA60. |
| `GOOGLE_EE_ND`, `GOOGLE_EE_DATE` | Documentação acessível e conferida: fórmula, máscara para entradas negativas e limite final exclusivo. |
| `GOOGLE_EE_SAMPLE`, `GOOGLE_EE_MEDIAN`, `GOOGLE_EE_REDUCE` | Páginas oficiais lidas: amostragem na projeção de entrada, mediana por posição/banda, escala e projeção da redução. A página `reduceRegion` não detalha por si só toda a ponderação: a semântica de pesos permanece item de conferência numérica, sem alterar a equação geral preexistente. |
| `NASA_POWER_DAILY` | Documentação diária lida: resolução de origem, LST padrão e seleção explícita UTC. A unidade concreta foi confrontada com a resposta JSON preservada, não inferida apenas da página. |
| `USGS_NDMI` | Página oficial lida: fórmula NIR–SWIR e bandas Landsat. Não sustenta, isoladamente, validação específica de B8A/B11 Sentinel-2. |
| `ROUSE1974_NTRS` | Registro NASA NTRS 19740022614 lido: autores, título, publicação em 1974 e resumo sobre bandas ERTS-1. Texto integral do artigo não foi relido; a afirmação no TCC está limitada ao registro. |
| `SLAIFFER2023` | Registro e resumo institucional UFSM lidos: autor, data, colhedora, produtividade e Crop Monitoring. Não foram incorporadas correlações ou métricas novas a partir do resumo. Leitura integral pendente antes de ampliar a discussão. |
| `GAO1996`, `MCFEETERS1996`, `GORELICK2017`, `WEISS2020` | DOI e metadados Crossref acessíveis: títulos, autoria registrada, ano, periódico, volume e páginas/número de artigo compatíveis. Para Weiss, a consulta identifica iniciais dos autores; nomes completos preexistentes não foram reconfirmados por esse registro. Leitura integral e verificação de todas as atribuições conceituais permanecem pendentes. |
| `PATRICIO2018`, `AMANI2020` | Crossref retornou 429 na primeira consulta; resolução dos DOI forneceu depois metadados bibliográficos compatíveis. Isso não constitui acesso ou leitura dos textos integrais. |
| `EOSDA_PLATFORM`, `ONESOIL_PLATFORM` | Páginas oficiais acessíveis e conteúdo sobre áreas, índices, clima e saídas examinado. Comparação continua documental, condicionada a modalidade/plano; sem ensaio funcional de terceiros ou inferência de superioridade. |
| `GOOGLE_EE_SERVICE_ACCOUNT`, `GOOGLE_EE_NONCOMMERCIAL`, `STREAMLIT_CLOUD_SECRETS` | Documentação oficial acessível e compatível com conta de serviço, condições/cotas e Secrets. Não foram inspecionadas credenciais nem atribuídas garantias de gratuidade comercial. |
| `NOMINATIM_POLICY` | Política oficial lida: máximo agregado de uma requisição por segundo, identificação, atribuição e proibição de autocomplete. Limites e ausência de controle global no código continuam explicitados. |

URLs/DOI estão preservados em `referencias.bib`. As 23 chaves citadas constam da
bibliografia compilada. Os resultados HTTP e metadados da consulta automatizada
inicial estão em `evidencias/consulta_bibliografica_revisao_autoral.json`; os dois
retornos 429 foram complementados por consultas DOI nesta sessão, não apagados.

### Pendências bibliográficas explícitas

- `[FONTE NECESSÁRIA]` Fundamentação específica da variante Sentinel-2 B8A/B11,
  caso se pretenda atribuir validação espectral além da descrição da implementação.
- `[FONTE NECESSÁRIA]` Leitura integral dos artigos citados e correspondência
  de cada afirmação conceitual/figura com páginas ou trechos das fontes originais.
  Nenhuma ampliação de resultado científico foi feita a partir de metadados.
- `[VALIDAR COM AUTOR]` Os anos 2026 de algumas páginas web preexistentes não
  foram certificados como datas de publicação. Conferir data/“sem data” segundo
  o padrão institucional; não foi inventada nem alterada uma data de publicação.
- `[VALIDAR COM AUTOR]` `SLAIFFER2023` e `LOVATO2021` usam tipo BibTeX
  `mastersthesis`, mas o campo `type` identifica TCC de graduação. Conferir a
  convenção bibliográfica institucional antes de mudar o tipo; não chamá-los de
  dissertações em razão do identificador interno.
- Preservadas sete entradas não citadas na versão final: `ARAUJO2025`,
  `CHAVES2019`, `LOVATO2021`, `PHIRI2020`, `ROUSE1973`, `WAZLAWICK2014` e
  `WAZLAWICK2020`. Pertencem ao acervo compartilhado com a proposta, não foram
  removidas nem inseridas artificialmente no artigo. Sua verificação integral
  permanece pendente caso sejam utilizadas. Em particular, não confundir
  `ROUSE1973` com a data de publicação do registro NTRS citado.
- EO Browser permanece com verificação funcional pendente. O bloqueio HTTP 403
  é um registro da rodada anterior, não uma nova consulta nem evidência de
  inexistência de funcionalidades.

## 8. Confirmações do autor e limites científicos remanescentes

1. `[VALIDAR COM AUTOR]` Aprovar a redação de cada seção e a prioridade proposta
   para trabalhos futuros. A revisão não certifica identidade linguística.
2. `[VALIDAR COM AUTOR]` Apreciar com o orientador a diferença entre os estudos
   de soja, milho e pastagem planejados e a avaliação computacional executada.
3. `[EVIDÊNCIA NECESSÁRIA]` Disponibilizar instrumento completo e respostas coletadas
   da pesquisa; confirmar divulgação, período efetivo de coleta e procedimentos
   éticos. Não há estatísticas nem depoimentos de participantes nesta revisão.
4. `[VALIDAR COM AUTOR]` Confirmar mês da defesa, identificador/link institucional,
   papel Letter e campos administrativos herdados; a classe não foi modificada.
5. `[EVIDÊNCIA NECESSÁRIA]` Conferência entre grades, cobertura útil por aquisição,
   efeito histórico da QA60 e avaliação de sombras, sem presumir que substituir
   a máscara já resolva o problema.
6. `[EVIDÊNCIA NECESSÁRIA]` Avaliações de acessibilidade, aparelhos físicos,
   carga, latência e custos; a demonstração não comprova esses atributos.
7. `[VALIDAR COM AUTOR]` Confirmar declaração e regras institucionais de uso de IA.

As pendências não são novos resultados nem foram inseridas no artigo como fatos
consolidados. Permanecem registradas para que o autor possa decidir e defender
o conteúdo com base nas evidências reais.

## 9. Validação final — fase 5

A conferência automatizada reproduzível está em
`experimentos/verificar_revisao_autoral.py`. Ela compara a estrutura com a base
Git, confere chaves e rótulos, identifica capturas opcionais ausentes, verifica
os hashes do código demonstrado e examina os arquivos de compilação. Não mede
estilo autoral, correção científica completa ou qualidade visual.

```sh
cd docs/artigo_final
/tmp/opencode/tectonic --keep-logs --keep-intermediates \
  --outdir /tmp/opencode/revisao-autoral-build Relatorio_Final.tex
```

Na raiz do repositório:

```sh
python3 docs/artigo_final/experimentos/verificar_revisao_autoral.py \
  --build-dir /tmp/opencode/revisao-autoral-build \
  --output docs/artigo_final/evidencias/validacao_revisao_autoral.json
git diff --check
```

O executável e o diretório de compilação são caminhos desta sessão; em outro
ambiente, instalar Tectonic e criar/ajustar o diretório de saída.

### Checklist de entrega para aprovação

- [x] Leitura integral do protocolo antes das alterações.
- [x] Leitura e revisão de todas as seções atuais, legendas e tabelas.
- [x] Adequação orientada por contextualização, causa/consequência e aplicações,
  sem quotas de conectivos ou simulação de experiências do autor.
- [x] Objetivos, estrutura, equações e resultados preservados.
- [x] Redundâncias localizadas e ambiguidades corrigidas sem remover ressalvas necessárias.
- [x] Siglas e terminologia principal conferidas.
- [x] Referências citadas verificadas no nível disponível ou sinalizadas para conferência.
- [x] Coerência com código e evidências examinada; código da demonstração inalterado.
- [x] Nenhum dado, citação ou resultado experimental fictício introduzido.
- [x] Relatório com diagnóstico, plano, alterações e assistência de IA produzido.
- [x] Compilação, inspeção visual e resultado final de validação registrados abaixo.
- [ ] Aprovação substantiva final do autor e apreciação das pendências pelo orientador.

### Resultado efetivamente obtido

- Tectonic 0.17.0: compilação concluída, com BibTeX automático e sem erros.
- **28 páginas**, papel Letter, metadados de título e autor preservados.
- **23 chaves citadas**, todas na bibliografia gerada; nenhuma citação ou
  referência cruzada indefinida, nenhuma chave ou rótulo duplicado.
- **31 figuras e três tabelas** na compilação; os oito ambientes de equações
  mantêm o conteúdo literal da base. Não foram adicionadas seções.
- **28 hashes de código coincidentes** com o manifesto da demonstração.
- `git diff --check`: sem problemas de espaços em branco.
- Resultado automatizado: `passed: true` em
  `evidencias/validacao_revisao_autoral.json`. Isso significa aprovação dos
  critérios estruturais do script, não aprovação acadêmica automática.
- PDF atualizado em `Relatorio_Final.pdf`, SHA-256
  `61aa0540ef16f4a9a0e4e94c3ba6d06c603636e979f2785ed31bf69802449c07`.
- Todas as páginas foram renderizadas e inspecionadas em duas folhas de contato,
  com detalhes da primeira página, tabela comparativa, diagramas de consulta/
  exportação e referências. Imagens de inspeção ficam em
  `/tmp/opencode/revisao-autoral-visual/`; não são novas evidências da aplicação.
- O ajuste de concisão do resumo/abstract eliminou o excesso vertical observado
  nas compilações intermediárias, sem alterar fonte ou classe.
- Persistem o excesso horizontal herdado de **54,64 pt** no cabeçalho,
  `headheight` insuficiente, avisos de fonte e espaçamentos `underfull`.
  Não foram ocultados nem classificados como erros de compilação.
- A primeira página ainda contém mês vazio e URL institucional herdado,
  pendentes de confirmação; capturas de contexto têm texto pequeno/contraste
  limitado. A inspeção visual não substitui avaliação formal de acessibilidade.
- CAP-18 e CAP-19 continuam ausentes e são omitidas condicionalmente, como antes.
- Log completo em `/tmp/opencode/revisao-autoral-build/Relatorio_Final.log`;
  saída do compilador em `/tmp/opencode/revisao-autoral-compilacao.txt`.

As cinco fases foram executadas. A versão resultante é uma **proposta revisada
nos arquivos**, disponível para aprovação do autor, não uma declaração de
encerramento das pendências científicas, bibliográficas ou institucionais.

## Atualização posterior: integração da pesquisa com usuários

O PDF e o diagnóstico acima registram a rodada autoral anterior à entrega da
planilha. A atividade posterior incorporou a avaliação descritiva das respostas;
seus arquivos, hashes, paginação e validações estão em
`avaliacao_usuarios/VALIDACAO_FINAL.md`. Os resultados anteriores foram
preservados como histórico, não devem ser usados para conferir o hash do PDF
depois dessa integração. A planilha teve somente a retificação de datas
expressamente autorizada pelo autor, com backup byte a byte preservado.
