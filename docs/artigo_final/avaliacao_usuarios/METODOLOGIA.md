# Metodologia da avaliação de usuários

## Estado vigente — terceira rodada

O procedimento abaixo continua aplicado ao recorte preservado de31 respostas, sem mudanças de triagem, escalas, quartis, atribuições qualitativas ou valores. O pesquisador confirmou participantes reais, coleta06–15/11/2026 emBrasíliaUTC−3, encerramento e estabilidade da versão pública. As categorias e interpretações qualitativas já foram aprovadas.

A [planilha pública](https://docs.google.com/spreadsheets/d/1wQJfoqnhpUMK8nJkZCLo9wp2YA34BsBons0T_NRZNFw/edit?usp=sharing) foi acessada e as31 linhas foram recuperadas por igualdade integral, independentemente da ordem. A recomputação do recorte reproduziu resultados quantitativos e contagens temáticas. Há32 registros públicos; o adicional também atende à triagem, portanto a diferença não foi justificada por inelegibilidade. O esclarecimento do recorte permanece necessário e está expresso no artigo.

Disponibilidade e correspondência documental não constituem autenticação individual, mas sua ausência não foi utilizada como indício especulativo de falsidade. Não houve geração ou incorporação de dados sintéticos. Aprovação ética/dispensa e identificação do commit público continuam sem documentação; sua apreciação cabe ao orientador/instância competente.

Davis e Braun/Clarke foram obtidos em PDF primário e confrontados no escopo conceitual utilizado, conforme a auditoria bibliográfica atualizada. A fonte e os cálculos não foram substituídos. Os estados de aprovação/fuso/acesso indicados no registro abaixo são **históricos**, superados apenas onde esta seção informa nova evidência.

## Atualização PA01–PA18 — 15/11/2026

O autor informa coleta de06 a15/11/2026, Brasília UTC−3, encerrada e com versão pública estável; aprova as13 categorias, a correspondência com as142 células e as interpretações anteriores. Essa aprovação substitui a pendência de apreciação pessoal, mas não certifica procedência independente. A exportação original independente do Forms, a prova administrativa de encerramento e o commit público exato não foram localizados. A análise descreve a planilha recebida, sem confirmação empírica definitiva.

A estratégia qualitativa foi previamente definida, segundo o autor; as categorias foram organizadas a partir do corpus, conforme registro abaixo. Não se transforma planejamento da estratégia em pré-registro de categorias. IA executou codificação/agrupamento sob supervisão; não houve segundo avaliador independente. Ética e autorização institucional de IA continuam pendentes. O restante desta página descreve o procedimento histórico; afirmações de aprovação/fuso pendentes abaixo estão superadas por esta atualização apenas no nível da declaração autoral.

## Delineamento e versão

Avaliação exploratória e descritiva do artefato, quantitativa e qualitativa, por
questionário autoadministrado após exploração da plataforma. Divulgação por
WhatsApp e LinkedIn informada pelo autor, com adesão voluntária e sem quadro
amostral. Não é experimento controlado, amostra probabilística ou validação de
eficácia agronômica. Não se conhece o número de convidados ou visitantes:
portanto, não se calcula taxa de resposta.

O público-alvo abrange agronomia, produção rural, pesquisa, estudantes e tecnologia.
O perfil efetivo é descrito pelos itens existentes, sem inferir escolaridade,
vínculo específico ou domínio de sensoriamento remoto a partir da pergunta
mais ampla sobre agricultura de precisão.

| Evidência | Versão / alcance |
|---|---|
| Questionário | Versão pública Streamlit anterior às correções; commit e logs individuais não fornecidos |
| Testes e demonstração existentes | Código consolidado em `28759bf`, base `b7c325c` com correções |
| Redação e análise atuais | Mesmos arquivos funcionais; somente documentação, análise e retificação autorizada dos carimbos |

Conforme decisão expressa do autor, a versão pública foi preservada durante a
coleta. Não atribuir aos respondentes avaliação posterior de normalização da
radiação, legenda, clima multiíndice, datas inclusivas, invalidação ou IDs.
Nenhum deploy foi executado.

## Fonte e elegibilidade

A aba `Respostas ao formulário 1` contém 31 registros × 50 colunas; `Página1`
está vazia. A contagem de colunas inclui itens de matrizes, triagem e carimbo.
O mapeamento integral consta de `instrumento.json`.

Incluir submissões com `Sim` no consentimento conjunto (maioridade, leitura e
participação voluntária) e na pergunta de exploração de ao menos um recurso.
Isso é autodeclaração, não aferição documental de idade. Todos os 31 atenderam.
Duplicatas integralmente idênticas seriam retidas uma vez e contadas na auditoria;
nenhuma ocorreu. Também não houve equivalência integral sem o carimbo.
Eventuais correspondências requerem revisão antes de qualquer exclusão.
A unidade descritiva é a submissão elegível ao questionário; não foram
coletados identificadores individuais. A planilha de respostas constitui a
fonte da análise, separada das entradas utilizadas nos testes dos scripts.

Sete carimbos foram corrigidos de 16/17 para 15/11/2026 mediante autorização
expressa. A cópia original e os horários foram preservados. O período de 06 a
15/11/2026 é o intervalo dos carimbos corrigidos do recorte, não uma certificação
independente do início/fim efetivos da coleta. Fuso e encerramento formal pendentes.

## Instrumento e escalas

- Perfil: três perguntas categóricas — área, conhecimento em agricultura de
  precisão e uso prévio de monitoramento por satélite com frequência no próprio item.
- Execução: nove atividades, quatro categorias exatas. Séries/anomalias e
  relatório/dados são agrupados no instrumento; não foram separados na análise.
- Experiência de uso: nove afirmações de concordância, de 1 a 5.
- Utilidade: onze recursos, de 1 nada útil a 5 muito útil; 3 é moderadamente útil.
- Aplicabilidade: oito afirmações de concordância, incluindo intenção e recomendação.
- Discursivas: cinco perguntas; a última é opcional. Há ainda um campo de
  impedimento de acesso vazio em todo o recorte, compatível com a triagem.
- Nota geral: inteiro de 0 a 10, não pergunta NPS.

Concordância: 1 discordo totalmente; 2 discordo parcialmente; 3 neutro;
4 concordo parcialmente; 5 concordo totalmente. Utilidade: 1 nada útil;
2 pouco útil; 3 moderadamente útil; 4 útil; 5 muito útil.
Não se somam itens num escore SUS/TAM/UTAUT ou outro indicador psicométrico.

## Tratamento e estatística

Apenas normalização Unicode NFC e espaços em torno/dentro das categorias, sem
trocar o conteúdo. `Outra\n` torna-se `Outra`. Ausências não são preenchidas.
Categorias inesperadas são contabilizadas como inválidas, nunca convertidas
para avaliação positiva, negativa ou neutra. `Não consegui avaliar`,
`Não se aplica` e ausências são separados.

Por item, o denominador das frequências é o número válido da pergunta; cada
saída contém os componentes da partição das 31 submissões. A impossibilidade
de avaliar não integra a distribuição ordinal. Na execução, `Não tentei`
compõe a distribuição das quatro categorias, mas não o denominador da conclusão:

```text
conclusão entre tentativas =
(conseguiu sem ajuda + conseguiu com ajuda) /
(conseguiu sem ajuda + conseguiu com ajuda + tentou sem conseguir)
```

Calcular frequências absolutas e relativas completas, mediana, Q1, Q3 e IIQ
(Q3−Q1). Percentis com interpolação linear, equivalentes a
`statistics.quantiles(..., method="inclusive")`. Códigos ordinais 4–5,
3 e 1–2 são também agrupados para leitura, sem ocultar a distribuição.
A categoria 3 só é denominada neutra em concordância, não em utilidade.

Média e DP amostral (`ddof=1`) são complementares nos códigos ordinais; não se
pressupõem distâncias psicologicamente iguais entre âncoras nem são calculados
testes paramétricos a partir dessa codificação. Para a nota, apresentar também
moda(s), extremos e histograma com todas as notas de 0 a 10. Sem imputação,
intervalos de confiança populacionais, p-valores ou causalidade.

Seis cruzamentos exploratórios: experiência/compreensão; área/utilidade dos
índices; conhecimento/autonomia; experiência/nota; compreensão/intenção;
utilidade dos mapas/nota. Um único agrupamento amplo por vez, sem tabelas
multidimensionais identificadoras. Grupos com menos de cinco respostas válidas
são suprimidos. Esse limiar reduz exposição, mas não garante anonimato.

## Codificação qualitativa

Foram lidas integralmente as 142 células discursivas não vazias. Unidades de
significado receberam códigos semânticos, agrupados em treze categorias
definidas a partir do corpus. A leitura incluiu elogios, barreiras, sugestões,
aplicações e casos que negam dificuldade. Não foi usada classificação de
sentimento como substituto da interpretação.

O vínculo é pelo SHA-256 dos cinco textos normalizados, não pelo perfil, nota,
data ou posição atual da linha. Categorias são multirrótulo: uma resposta pode
receber mais de um código; a frequência temática principal conta cada registro
uma vez, independentemente de repetições entre perguntas. As colunas por
pergunta preservam a origem das menções. Contagens podem somar mais de 31 ou
100%, pois os temas não são exclusivos.

Livro de códigos, exemplos e atribuições estão em `codificacao.json`, e a
tabela completa em `resultados/categorias_qualitativas.csv`/`RESULTADOS.md`.
Os trechos publicados são literais e curtos, sem profissão, nota, horário,
localização ou pseudônimo associado. Não são apresentados relatos completos.

A categorização foi assistida por GPT-6.1 Sol, no OpenCode, após leitura do
protocolo autoral. É uma proposta de análise para validação substantiva do autor.
Não houve segundo codificador independente, medida de concordância, saturação
teórica ou validação pelos respondentes. Textos novos ficam pendentes, sem
classificação automática por palavras-chave.

## Referências e alcance da consulta

- ISO 9241-11:2018: resumo/metadados oficiais lidos
  (<https://www.iso.org/standard/63500.html>); não houve acesso integral pago.
- Davis (1989), DOI <https://doi.org/10.2307/249008>: metadados conferidos; acesso
  JSTOR não forneceu o texto integral. Não se afirma adoção validada do TAM.
- Sullivan e Artino (2013), DOI <https://doi.org/10.4300/JGME-5-4-18>: texto integral
  lido em <https://pmc.ncbi.nlm.nih.gov/articles/PMC3886444/>, com debate sobre
  natureza ordinal, distribuição, médias e interpretação.
- Braun e Clarke (2006), DOI <https://doi.org/10.1191/1478088706qp063oa>: autores,
  ano, título, periódico, volume e páginas conferidos via Crossref. O acesso
  integral na editora e no repositório UWE retornou 403. A referência é
  metodológica; não se atribui leitura integral renovada ou aplicação certificada
  de todas as recomendações. Conferência integral permanece pendente.

## Ética, privacidade e limites

Não há documento que autorize declarar aprovação CEP ou dispensa formal.
O autor/orientador devem verificar enquadramento institucional, consentimento,
uso de citações e declaração de assistência de IA. O n representa submissões
elegíveis ao questionário. Há autoseleção, possível viés de desejabilidade,
predomínio de agrônomos, ausência de controle de ambiente/dispositivo e
interpretações de funcionalidades não confirmadas.

Usabilidade percebida, intenção de uso, uso efetivo e eficácia agronômica são
dimensões distintas. Relatos sobre produtividade, doenças, compactação, estações
meteorológicas ou comparações entre safras são percepções/propostas, não provas
de funcionalidades ou diagnóstico. Não se excluíram relatos por discordar da
implementação ou por avaliar negativamente a plataforma.
