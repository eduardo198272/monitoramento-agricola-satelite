# Revisão da complexidade da escrita e da progressão didática

## 1. Escopo e estado

Diagnóstico editorial da versão do artigo registrada no commit `1862dd7`, com leitura dos dez arquivos `final_*.tex`, incluindo resumo, introdução, fundamentação, métodos, implementação, apresentação da plataforma, resultados, avaliação com usuários, discussão e conclusão.

Referência obrigatória lida integralmente: [`../PERFIL_AUTORAL_E_PROTOCOLO_REVISAO.md`](../PERFIL_AUTORAL_E_PROTOCOLO_REVISAO.md), especialmente perfil autoral, amostras de escrita e fluxo de aprovação por seção.

**Estado: direção editorial e exemplos aprovados pelo autor na conversa; revisão aplicada aos dez arquivos do artigo.** A aprovação do tom não substitui a leitura e a aprovação final das seções revisadas. A revisão foi assistida por IA. Os exemplos abaixo registram a proposta que orientou as alterações; não acrescentam experimentos, justificativas de desenvolvimento ou resultados. Evidências da aplicação e da compilação: [`evidencias/revisao_didatica/README.md`](evidencias/revisao_didatica/README.md).

Esta é uma análise qualitativa de leitura, não uma medição validada de legibilidade. Não foram atribuídos escores de dificuldade, níveis de escolaridade ou percentuais artificiais de melhoria. Também não é uma nova validação das fontes: continuam valendo as pendências da auditoria científica.

## 2. Parecer

A percepção de excesso de tecnicidade é compatível com os trechos examinados. O principal problema não é a presença de conteúdo técnico, necessário ao TCC, mas a ordem e a concentração em que ele aparece.

O texto frequentemente reúne, no mesmo parágrafo:

1. a operação realizada;
2. sua formulação ou nome técnico;
3. nomes de funções e parâmetros;
4. condições de execução;
5. exceções e limites de interpretação.

O leitor precisa compreender todas essas camadas simultaneamente. Em alguns pontos, o texto assume a forma de documentação de implementação ou de relatório de auditoria, quando deveria primeiro explicar a pesquisa.

A direção recomendada é **explicar antes de especificar**: apresentar o problema ou a tarefa, explicar o funcionamento, introduzir o termo necessário e então detalhar condições e limites. Não é uma sequência obrigatória para todo parágrafo.

### Relação com a escrita do autor

As amostras do perfil autoral desenvolvem ideias por contexto, exemplos e consequências. Na amostra sobre programação e desenvolvimento de software, por exemplo, os requisitos e as decisões de arquitetura aparecem relacionados a situações de uso. Isso é diferente de apresentar uma lista de propriedades técnicas sem mostrar primeiro o problema que elas resolvem.

Para aproximar o artigo desse estilo, convém recuperar essas relações explicativas. Não se recomenda copiar expressões das amostras, imitar erros, acrescentar experiências pessoais ou tornar todo período curto. Um período mais longo pode ser claro quando desenvolve uma única relação de raciocínio.

## 3. Pontos que dificultam a leitura

| Ponto | Localização representativa | Efeito na leitura | Tratamento recomendado |
|---|---|---|---|
| Conceitos abstratos antes da situação concreta | Introdução, segundo parágrafo: “contratos de dados”, “convenções temporais” | O leitor identifica o vocabulário, mas pode não compreender o problema prático. | Mostrar o que precisa permanecer coerente entre área, período, mapa e arquivo; depois nomear o contrato. |
| Conceitos novos apresentados em sequência | Fundamentação, sensoriamento remoto: produto, reflectância, harmonização, fator de escala | Exige conhecimento prévio de sensoriamento remoto. | Explicar a finalidade do produto e introduzir os termos em etapas, sem alterar suas definições. |
| Definição quase circular | Fundamentação: “cada posição recebe a mediana de suas observações válidas” | Explica a operação por outro conceito que talvez ainda não tenha sido compreendido. | Explicar mediana e o que é combinado: valores de uma mesma posição em imagens diferentes. |
| Detalhe de API antes da finalidade | Métodos e implementação: `reduceRegion`, `sampleRectangle`, parâmetros e identificadores | Aproxima o artigo de um manual de código. | Apresentar primeiro a transformação dos dados; manter a chamada técnica como especificação posterior. |
| Muitas operações em um único bloco | Implementação, pré-carregamento e transferência da grade | Mistura processamento geográfico, representação numérica, compressão e consulta. | Separar obtenção, transferência e leitura dos valores, explicando o vínculo entre as etapas. |
| Ressalvas sucessivas | Introdução, métodos, apresentação, discussão e conclusão | A leitura fica defensiva e fragmentada. | Preservar limites, mas reunir os gerais na discussão e manter junto ao método os que mudam sua interpretação. |
| Vocabulário de auditoria no corpo do artigo | Trabalhos relacionados: “conferida em texto completo nas seções de métodos” | Interrompe a apresentação do estudo para narrar o trabalho do revisor. | Deixar o estado de acesso no relatório da auditoria; no artigo, apresentar o método e a comparação sustentados pela fonte. |
| Listas extensas de números na prosa | Resultados com usuários | Dificulta reconhecer o resultado principal e seus denominadores. | Destacar achados centrais no texto e remeter às distribuições completas já existentes, sem esconder avaliações negativas. |
| Termos técnicos usados como substitutos automáticos de palavras comuns | “artefato”, “geometria”, “produtos derivados”, “proveniência”, “cliente” | Aumenta a abstração mesmo quando uma expressão concreta bastaria. | Escolher pelo contexto; não banir termos necessários. “Geometria” continua adequado em uma definição matemática. |

## 4. Prioridades por seção

Os níveis indicam prioridade editorial, não erro científico.

| Seção | Prioridade | Intervenção principal |
|---|---|---|
| Resumo e abstract | Alta | Apresentar o que a plataforma permite fazer antes de acumular tecnologias e produtos. Revisar os dois idiomas em conjunto, depois do corpo do artigo. |
| Introdução | Alta | Tornar o problema concreto; explicar “contratos de dados” e reduzir enumerações abstratas. Preservar pergunta e contribuição. |
| Fundamentação | Alta | Ensinar banda, pixel, índice, composição e série em uma progressão; separar explicação conceitual de controvérsia de nomenclatura. |
| Materiais e métodos | Alta | Introduzir o sentido das operações antes das equações e parâmetros. Explicar a leitura dos símbolos sem substituir o formalismo. |
| Implementação | Alta | Relacionar cada decisão observável a uma necessidade do fluxo; separar explicação de funcionamento e especificação de código. |
| Apresentação da plataforma | Média | Organizar pelo percurso de uso e evitar repetir a auditoria técnica de cada captura. Manter a distinção entre versões e tipos de evidência. |
| Resultados técnicos | Média | Apresentar primeiro o que foi verificado e observado; organizar ambiente e métricas sem perder a identificação da execução. |
| Resultados com usuários | Média | Dar hierarquia aos achados e manter claros os denominadores; não alterar categorias, valores ou distinção entre tentativas e não tentativas. |
| Discussão | Média | Aproveitar explicações concretas já existentes; conectar achados e consequências em vez de repetir listas técnicas. |
| Conclusão | Média | Responder ao problema com termos diretos e organizar trabalhos futuros por finalidade, não apenas por tecnologia. |

Uma passagem que já oferece um bom modelo é a discussão do erro de radiação em `final_5_discussao.tex`: ela mostra que executar o código não basta se a unidade de entrada foi interpretada incorretamente. Há problema, mecanismo e consequência. Esse modo de explicar deve ser ampliado.

## 5. Exemplos de tom proposto

Os exemplos são propostas editoriais, não alterações já consolidadas. As referências são identificadas pelas chaves do artigo para permanecerem ligadas às afirmações correspondentes.

### 5.1. Introdução: tornar concreto o problema de integração

**Local:** `final_1_introducao.tex`, segundo parágrafo.

**Trecho atual representativo:**

> Uma série espectral pode conter aquisições em datas irregulares, enquanto os dados meteorológicos são diários e seguem convenções temporais próprias. Por isso, a integração depende de regras explícitas sobre geometrias, datas, unidades e valores ausentes. Essas regras constituem os contratos de dados entre os componentes e situam o problema também no campo da Engenharia de Software.

**Proposta para o parágrafo:**

> Para explorar esses dados em uma aplicação, não basta calcular um índice. O mapa, o gráfico e os arquivos exportados precisam corresponder à área e ao período escolhidos pelo usuário. Essa integração exige cuidado porque as imagens de satélite podem estar disponíveis em datas irregulares, enquanto as informações meteorológicas são organizadas por dia. É necessário, portanto, definir como cada parte do sistema trata a área selecionada, as datas, as unidades de medida e os dados ausentes. Essas regras de troca e interpretação das informações, chamadas aqui de contratos de dados, também fazem parte do problema de Engenharia de Software.

**O que muda:** a situação de uso antecede o termo abstrato. Preserva o problema, sem acrescentar justificativa histórica ou resultado.

### 5.2. Fundamentação: explicar a composição temporal

**Local:** `final_2_fundamentacao.tex`, agregação espacial e temporal.

**Trecho atual:**

> Para representar um período em um único mapa, é necessário combinar as imagens disponíveis. Na composição por mediana, cada posição recebe a mediana de suas observações válidas.

**Proposta para o parágrafo:**

> Para apresentar um período em um único mapa, o sistema combina valores de imagens obtidas em diferentes datas. Em cada posição do mapa, reúne os valores válidos do índice e calcula sua mediana, uma medida central obtida a partir dos valores ordenados. Esse procedimento forma a composição temporal por mediana (`GOOGLE_EE_MEDIAN`). Como os filtros podem excluir uma posição em determinada imagem, nem todas as posições contam com a mesma quantidade de observações. Por isso, o mapa representa uma combinação do período e não necessariamente uma imagem de uma data específica.

**O que muda:** explica o que é combinado antes de nomear a operação. A explicação introdutória da mediana não substitui sua definição formal ou o tratamento de conjuntos pares e vazios, quando necessário.

### 5.3. Métodos: apresentar a regra de anomalias antes dos símbolos

**Local:** `final_3_metodos.tex`, abertura de “Regra de detecção e tendência”.

**Trecho atual:**

> Seja $x_i$ o valor da série na posição $i$, com indexação iniciada em zero. Para $i\geq3$, a janela contém os três registros anteriores:

**Proposta de abertura, mantendo as equações seguintes:**

> Para sinalizar quedas na série, o sistema compara cada valor com os três registros imediatamente anteriores. Primeiro, calcula a média e o desvio padrão desses registros; depois, verifica quanto o valor atual se afasta dessa referência. Esse afastamento é expresso pelo escore $z_i$. A janela considera três observações, não três dias, pois o intervalo entre imagens pode variar. Nas equações seguintes, $x_i$ representa o valor na posição $i$ da série, com contagem iniciada em zero. O cálculo pode ser aplicado a partir da quarta observação, quando $i\geq3$.

**O que muda:** o leitor entende a comparação antes da notação. Preservar depois das equações o limiar estrito, os casos sem cálculo e a classificação dos parâmetros como heurísticos não calibrados. A abertura não pode ser apresentada isoladamente como descrição completa ou validação da regra.

### 5.4. Implementação: explicar a função dos módulos

**Local:** `final_3a_implementacao.tex`, abertura da arquitetura.

**Trecho atual representativo:**

> Para isso, a aplicação organiza apresentação, orquestração e acesso a dados em módulos de um mesmo processo Python.

**Proposta para o parágrafo:**

> A plataforma precisa receber as escolhas do usuário, consultar os serviços externos e apresentar os resultados. Essas tarefas são divididas entre módulos executados no mesmo processo Python. A parte de apresentação reúne os controles e exibe as informações; a de coordenação organiza a sequência de consultas e cálculos; e a de acesso a dados realiza a comunicação necessária com as fontes externas. O Streamlit apresenta a interface e mantém informações durante a sessão, enquanto um componente JavaScript consulta os valores da grade no navegador. Essa divisão de responsabilidades não corresponde a microsserviços nem a um servidor independente com API REST.

**O que muda:** descreve responsabilidades por ações. Não atribui ao projeto uma nova arquitetura nem motivos de escolha não documentados.

### 5.5. Discussão: traduzir “invalidação de estado”

**Local:** `final_5_discussao.tex`, consistência das integrações.

**Trecho atual representativo:**

> A invalidação de estado complementa esse cuidado ao impedir apresentação de resultados sob parâmetros analíticos diferentes.

**Proposta para a frase:**

> Quando o usuário altera a área, o período ou o conjunto de índices solicitado, os resultados anteriores deixam de ser apresentados como válidos para a nova configuração. Esse controle evita, por exemplo, que o mapa de uma análise anterior permaneça associado a outra área selecionada.

**O que muda:** torna visível a consequência do controle. O exemplo descreve um comportamento já documentado, não um novo teste ou episódio observado.

## 6. Critérios para aplicar a revisão

- Explicar o que uma operação faz antes de apresentar seu nome quando o leitor ainda não tiver essa base.
- Manter uma questão central identificável por parágrafo; separar detalhes que respondem a questões diferentes.
- Definir siglas e termos no contexto de uso, sem transformar o artigo em glossário.
- Usar exemplos do próprio processamento já documentado. Identificar claramente qualquer exemplo apenas didático.
- Não simplificar “média espacial da composição mediana” para “média do período”: são conceitos diferentes.
- Não trocar “escolha heurística não calibrada” por “método confiável” ou “alerta de problema na lavoura”.
- Não confundir amostragem por adesão com representatividade, nem submissões elegíveis com indivíduos verificados.
- Preservar referências próximas das afirmações, equações, unidades, dados e distinção entre versões.
- Manter no método as limitações indispensáveis à interpretação. Consolidar repetições gerais somente após conferir que não se perde informação.
- Não enviar detalhes a apêndices ou remover conteúdo técnico apenas para tornar o texto mais curto; mudanças de estrutura exigem aprovação.
- Não estabelecer metas artificiais de tamanho de frase, porcentagem de simplificação ou substituição de palavras.

### Perguntas de verificação por parágrafo

1. O leitor sabe qual problema ou operação está sendo discutido?
2. Os termos necessários foram explicados antes de serem usados como base para outros conceitos?
3. Está claro o que o sistema recebe, faz e produz?
4. A ligação entre a explicação e a equação ou figura está explícita?
5. Há detalhes de implementação interrompendo a explicação principal?
6. A ressalva acrescenta uma distinção necessária ou apenas repete outra passagem?
7. A revisão manteve a precisão e o alcance das evidências?
8. O autor reconhece sua forma de desenvolver a ideia e consegue explicá-la oralmente?

## 7. Aprovação e sequência proposta

**Direção adotada após aprovação dos exemplos:** explicar os conceitos para um leitor com formação geral em Computação, sem pressupor especialização simultânea em sensoriamento remoto, geoprocessamento e estatística.

**Aprovação recebida:** o autor confirmou que o nível de explicação dos exemplos corresponde ao desejado. A leitura final de cada seção revisada permanece necessária.

Sequência de aplicação:

1. Revisar introdução e fundamentação para construir o vocabulário necessário.
2. Revisar métodos e implementação com explicação progressiva e formalismo preservado.
3. Revisar apresentação, resultados, discussão e conclusão, reduzindo repetições sem esconder limites.
4. Revisar resumo e abstract por último.
5. Comparar antes/depois, conferir citações, equações, valores e referências cruzadas; recompilar e inspecionar o PDF.

Não executar automaticamente commit ou push por continuidade da solicitação anterior: esta é uma nova atividade editorial.

## 8. Alterações aplicadas

| Arquivo | Alterações de exposição |
|---|---|
| `final_1_introducao.tex` | Situação de uso antes de contratos de dados; contribuição explicada pelo percurso da área ao resultado. |
| `final_2_fundamentacao.tex` | Bandas, polígonos, grades e legendas apresentados por sua função; mediana e redução espacial explicadas antes da distinção formal; retirado comentário sobre o processo de auditoria de Slaiffer. |
| `final_3_metodos.tex` | Finalidade dos filtros e agregações antes de chamadas de API; comparação das três observações antes das equações; explicação dos limites e dos denominadores da avaliação. |
| `final_3a_implementacao.tex` | Responsabilidades por ações; separação entre preparação, transferência e consulta da grade; explicação dos termos e variáveis do lookup e do controle de resultados. |
| `final_3b_plataforma.tex` | Percurso de uso mais direto: buscar, desenhar, salvar, analisar, consultar e exportar; distinções de versão preservadas. |
| `final_4_resultados.tex` | Resultado dos testes antes dos detalhes de execução; separação de escopos e explicação concreta das verificações de integração. |
| `final_4a_usuarios.tex` | Separação de achados em parágrafos; explicação da diferença entre concluir a tarefa e concluí-la sem ajuda; valores e categorias preservados. |
| `final_5_discussao.tex` | Consequências de cada escolha explicadas; termos de interoperabilidade, proveniência e invalidação ligados a situações do sistema. |
| `final_6_conclusao.tex` | Retomada direta do problema e organização da continuidade por avaliação, processamento e utilização. |
| `final_0_resumo.tex` | Resumo e abstract revistos por último e alinhados: o que o usuário faz precede o conjunto de tecnologias e resultados. |

O diff integral antes/depois está em `evidencias/revisao_didatica/alteracoes.diff`. Não foram removidas citações, alteradas equações numeradas ou modificados dados para melhorar a fluidez. As ressalvas que mudam a interpretação dos resultados permanecem. As pendências científicas e institucionais da auditoria anterior não foram resolvidas por esta revisão editorial.
