# Projeto Aplicado I

## Metodologia & Cronograma

**Professor:** Marcelo Trindade Rebonatto  
**Curso:** Ciência da Computação  
**Curso:** Engenharia de Computação  
**Instituição:** Universidade de Passo Fundo - UPF

---

## Slide 2 - Base do material

O material apresentado neste conjunto de slides foi baseado nos slides da disciplina de Metodologia da Pesquisa em Ciência da Computação, disponibilizados pela professora Maria Cristina Ferreira de Oliveira, do ICMC-USP.

O conteúdo foi construído com base no livro:

> WAZLAWICK, Raul Sidnei. *Metodologia de Pesquisa para Ciência da Computação*. 2. ed. Elsevier, 2014.

---

## Slide 3 - Sumário

### Metodologia de um projeto na área de Computação

- Materiais;
- métodos;
- validação;
- cronograma de ações;
- resultados esperados;
- limitações do estudo.

### Guia geral da proposta

---

## Slide 4 - Metodologia

- Descrição do método utilizado para chegar às conclusões;
  - procedimentos realizados durante a execução do projeto.
- O método é definido após a definição dos objetivos;
  - a revisão da literatura, em geral, não faz parte da metodologia;
  - ela é anterior à metodologia.
- Método: sequência de passos necessários para demonstrar que o objetivo proposto foi atingido.
  - Indicar se protótipos serão desenvolvidos;
    - informar se modelos teóricos serão construídos.
  - Informar quais experimentos serão realizados;
    - indicar se serão utilizados *benchmarks*.
  - Explicar como será realizada a validação.

---

## Slide 5 - Materiais e métodos

- Definir, mesmo que inicialmente como previsão, o conjunto de recursos e ferramentas que serão utilizados:
  - sistemas operacionais, linguagens e bancos de dados;
  - recursos de processamento e plataformas;
  - formas de comunicação, meios e tecnologias;
  - bibliotecas;
  - outros recursos necessários.
- Certificar-se de que tudo o que foi planejado está disponível.
  - Verificar os tipos de licença de cada software utilizado.
- Os materiais e métodos podem ser modificados durante a execução, porém:
  - essa mudança pode implicar retrabalho;
  - a alteração pode atrasar o desenvolvimento.

---

## Slide 6 - Protótipos

- Definir se, durante a execução do trabalho, serão criados protótipos.
- Informar:
  - quantos protótipos serão criados;
  - quais serão os objetivos de cada um;
  - como ocorrerá a avaliação dos protótipos.
- A avaliação dos protótipos é indispensável para o seguimento das ações.
- Protótipos podem ser usados como marcos de avanço:
  - metas intermediárias a serem alcançadas.
- São uma estratégia interessante para validar partes da evolução do trabalho.
- Não se deve gastar tempo excessivo em protótipos quando o trabalho ainda passará por uma versão definitiva.

---

## Slide 7 - Embasamento de metodologia

### Dados versus conceitos

- Uma pesquisa não consiste apenas em coletar dados.
- Os dados devem:
  - apoiar uma hipótese de trabalho;
  - contribuir para responder ao problema de pesquisa.

### Contribuição

- O elemento mais importante é a contribuição.
- O trabalho não deve se limitar a uma pesquisa de opinião dos participantes.

### Questionários

- Questionários podem e devem ser utilizados.
- É necessário saber:
  - qual informação se busca coletar;
  - quais comparações serão realizadas;
  - se haverá grupo de controle.
- Sempre que possível, devem ser usados questionários validados.

---

## Slide 8 - Exemplos de questionários

### Para avaliar a usabilidade de um sistema

- Sistemas web;
- sistemas móveis;
- outros tipos de interface.
- Instrumento sugerido:
  - **System Usability Scale - SUS**;
  - Brooke, 1996.

### Para avaliar a aceitação de tecnologia

- Questionários derivados do:
  - **Modelo de Aceitação da Tecnologia - TAM**.

### Para avaliar a qualidade de software e sistemas

- Modelo:
  - **SQuaRE**;
  - ISO/IEC 25010:2011.

---

## Slide 9 - Embasamento de metodologia: definições

### Definições constitutivas

- Definem um termo em função de seus constituintes.
- Exemplo:
  - uma gramática formal.
- São utilizadas em trabalhos formais.

### Definições operacionais

- São utilizadas em trabalhos que empregam termos não formais, como:
  - facilidade;
  - adequação;
  - flexibilidade.
- Esses termos exigem uma definição operacional.
- Uma definição operacional:
  - não define a natureza de um fenômeno;
  - especifica os meios para obter uma medição;
  - caracteriza o resultado da medição como representação do próprio fenômeno.

---

## Slide 10 - Definições operacionais

### Exemplos

- **Facilidade:** número de toques no teclado ou de cliques no mouse necessários para realizar uma determinada ação.
- **Flexibilidade:** tempo médio que um programador leva para introduzir um conjunto predefinido de características no objeto.

Esses são apenas exemplos. Eles não podem ser considerados definições operacionais gerais e universais para esses termos.

---

## Slide 11 - Embasamento de metodologia: variáveis

### Variáveis

- São fenômenos de interesse que podem ser medidos.
- Variam conforme a medição;
  - constantes não variam.
- Possuem um domínio:
  - conjunto de valores válidos.

### Domínio discreto

- Valores pertencentes a um conjunto de elementos.
- Os conjuntos podem:
  - ser ordenados;
  - ser finitos.

### Domínio contínuo

- Valores reais.
- Entre dois valores pode existir um terceiro valor.

---

## Slide 12 - Variáveis

### Variáveis discretas em conjuntos finitos

- Exemplo:
  - categorias;
  - conceitos de avaliação: A, B, C, E e F.

### Discretização

- Regras de conversão de valores contínuos para valores discretos.
- Atribuição de um valor discreto a intervalos de valores contínuos.

### Observação versus controle

- **Variáveis medidas:** aquilo que se deseja observar.
- **Variáveis manipuladas:** modificadas pelo pesquisador para realizar um experimento.
  - Também chamadas de variáveis experimentais.

---

## Slide 13 - Experimentos

- Por meio de experimentos, colocam-se à prova as variáveis de observação.
  - Elas são analisadas em relação à variação das variáveis de controle.

### Experimentos simulados

- Utilizam pessoas ou artefatos computacionais específicos.
- Geram entradas para a execução do projeto.
- Podem inicialmente buscar validar protótipos.
- Também podem ser utilizados em validações finais.

### Experimentos reais

- Utilizam dados ou sujeitos reais.
- Buscam validar o projeto como um todo.

---

## Slide 14 - Benchmarks

- *Benchmarks* são programas de computador que executam testes para avaliar o desempenho.
- O uso indiscriminado pode ser inadequado, pois alguns *benchmarks* podem ser tendenciosos.
- Em geral, *benchmarks* aceitos pela comunidade científica da área podem e devem ser utilizados.
- Deve-se especificar:
  - se serão utilizados;
  - quais serão utilizados;
  - quais elementos serão analisados.

---

## Slide 15 - Validação

- A validação definirá se a hipótese foi aceita ou refutada.
- Quando não houver hipótese:
  - deve-se verificar se aquilo que foi construído atende ou não aos objetivos.
- As avaliações podem utilizar:
  - experimentos;
    - formulários específicos;
  - simuladores;
  - *benchmarks*;
  - oráculos.

---

## Slide 16 - Validação e análise dos resultados

Na metodologia, deve-se especificar a forma como a validação será realizada.

Também é necessário especificar como os resultados serão analisados:

- **Estatísticas:** quando a pesquisa for quantitativa.
- **Outras formas de análise:** quando a pesquisa for qualitativa.

---

## Slide 17 - Exemplo de análise estatística

Objetivo: verificar se a média obtida nos resultados apresenta ou não diferença significativa em relação a outra média.

### Etapas possíveis

1. Realizar repetições das medições para obter uma média.
   - Utilizar amostras grandes, com mais de 32 execuções.
2. Verificar a normalidade das amostras.
   - Teste de Shapiro-Wilk.
3. Verificar a homogeneidade das variâncias.
   - Teste de Levene.
4. Verificar se há diferença significativa entre duas médias.
   - Teste t de Student para amostras independentes.

---

## Slide 18 - Cronograma

- A organização é essencial em qualquer trabalho.
  - Profissionalismo;
  - estética;
  - trabalho final;
  - disciplina.
- Um cronograma mal ajustado pode ser:
  - um carrasco;
  - um importante aliado.
- O cronograma deve servir como guia para:
  - cumprir as tarefas decorrentes dentro do tempo disponível;
  - evitar o acúmulo de tarefas.
- A ideia central é visualizar todo o trabalho necessário para implementar o projeto.

---

## Slide 19 - Elaborando um cronograma

- Reunir todas as tarefas que deverão ser realizadas até a entrega do trabalho final.
  - Destacar as tarefas mais importantes.
- Escalonar e distribuir as tarefas no período disponível.
  - Evitar colocar apenas meses, pois normalmente o período é curto.
  - Utilizar semanas, dias ou horas.
  - Considerar que um mês pode consumir aproximadamente 25% do tempo disponível.
- Tentar utilizar previsões tão realistas quanto possível.
  - Evitar mudanças frequentes relacionadas a atrasos ou pânico.
- Iniciar pelas tarefas independentes.

---

## Slide 20 - Elaborando um cronograma: cuidados

- Considerar as demais atividades pessoais e profissionais.
  - O Trabalho Final é importante, mas a vida continua.
- As atividades consideradas mais difíceis devem receber prazo e atenção maiores.
  - Cuidado para não reservar tempo em excesso.
  - Comprometer também as demais atividades.
- Programar algumas folgas entre as tarefas.
  - Imprevistos sempre acontecem.
- Incluir no cronograma as entregas parciais:
  - validações parciais;
  - provas de conceito;
  - protótipos;
  - outros marcos.
- As entregas parciais auxiliam na avaliação do progresso.

---

## Slide 21 - Formato do cronograma

- Em geral, não existe um formato único ou padrão.
- Uma opção comum é uma tabela:
  - atividades nas linhas;
  - períodos nas colunas;
  - ou a disposição inversa.
- Marcam-se as interseções para demonstrar:
  - quando cada tarefa será realizada;
  - por quanto tempo será realizada.
- Outras formas:
  - diagrama de Gantt;
  - software de controle de projetos.
- Cada ação deve ser detalhada.
  - Não se deve deixar apenas o termo genérico "tabela".

---

## Slide 22 - Exemplo de cronograma

O slide apresenta uma tabela de cronograma distribuída entre os anos de 2020 e 2021.

### Etapas exemplificadas

- Levantamento de tecnologias para comunicação de sensores em casas de cidades inteligentes;
- revisão bibliográfica sobre tecnologias elencadas;
- estudo sobre comunicação entre medidores residenciais e sistemas computacionais;
- definição de requisitos para a comunicação de casas em cidades inteligentes;
- escolha das tecnologias para implementação da prova de conceito;
- implementação de software e firmware para a prova de conceito;
- validação da prova de conceito com testes reais;
- participação em eventos científicos.

---

## Slide 23 - Exemplo de cronograma: detalhamento inicial

### a) Levantamento de tecnologias

Inicialmente, o bolsista realizará uma busca sobre tecnologias de rede para proporcionar comunicação de casas no ambiente de cidades inteligentes. Tecnologias como 6LoWPAN, LoRa e ZigBee serão utilizadas como ponto de partida.

### b) Revisão bibliográfica

A partir da relação de tecnologias possíveis, será realizada uma revisão bibliográfica acerca das tecnologias selecionadas. Questões como limites de distância, vazão, latência de conexão e custo financeiro serão alguns dos elementos investigados.

### c) Estudo sobre medidores residenciais

Após o conhecimento das tecnologias de comunicação, será realizado um estudo sobre medidores residenciais e formas de integração com sistemas computacionais. Inicialmente, o foco estará em medidores de energia elétrica, podendo posteriormente ser ampliado.

---

## Slide 24 - Exemplo de cronograma: detalhamento final

### d) Levantamento de requisitos

Será realizado um levantamento de requisitos para aplicações de casas em ambientes de cidades inteligentes. Os requisitos servirão como ponto de partida para a definição de uma Prova de Conceito - POC.

### e) Escolha das tecnologias

Serão escolhidas as tecnologias a serem empregadas no desenvolvimento da POC.

### f) Implementação

Será realizada a implementação de firmware e software para a criação da prova de conceito.

### g) Validação

A POC será validada e os resultados obtidos serão analisados.

### h) Revisão e divulgação científica

O bolsista deverá escrever textos sobre as revisões bibliográficas realizadas e também contribuir ativamente para a confecção de artigos para posterior submissão em congressos e revistas da área.

---

## Slide 25 - Elementos comuns em cronogramas de TCC

- Levantamento bibliográfico inicial;
  - revisão da literatura.
- Definição dos instrumentos de coleta de dados.
- Encaminhamento ao comitê de ética da universidade, quando necessário.
- Coleta de dados.
- Apuração e análise dos dados.
- Redação do relatório final.
- Revisão do trabalho.
- Entrega do Trabalho Final.

---

## Slide 26 - Adições comuns aos trabalhos de Computação

- Definição do modelo da solução projetada;
  - arquitetura.
- Definição da base de dados a ser utilizada;
  - modelagem.
- Definição de um protocolo de comunicação.
- Implementação:
  - protótipo;
  - prova de conceito;
  - solução para validar ideias.
- Implementação da solução proposta.
- Validação inicial.

---

## Slide 27 - Durante a execução do cronograma

- Manter atividades tediosas em conjunto com atividades agradáveis.
  - Todas precisarão ser realizadas.
- Manter disciplina para seguir o planejamento.
  - Caso seja necessário, alterar o cronograma o quanto antes.
  - Manter contato constante com o orientador.
- Sempre que possível, antecipar tarefas.
- Reservar tempo para revisão ortográfica e gramatical do texto.
  - Fazer uma primeira revisão pessoal;
  - realizar outra revisão em conjunto com o orientador.
- Manter cópias de segurança atualizadas dos arquivos.

---

## Slide 28 - Resultados esperados

- É interessante que os resultados esperados estejam presentes na proposta.
- Resultados esperados não são iguais aos objetivos.

### Objetivos

- São buscados durante a execução do projeto.
- Podem ou não ser alcançados.

### Resultados esperados

- Podem ocorrer após a conclusão do trabalho.
- Representam:
  - aquilo que possivelmente mudaria caso todos os objetivos fossem atingidos;
  - a expectativa do autor diante do alcance dos objetivos.

---

## Slide 29 - Exemplo de resultados esperados

Segundo Wazlawick (2014):

### Objetivo

Definição de um método de cálculo de esforço para desenvolvimento de software mais preciso do que os métodos então existentes.

- Um conjunto de experimentos e uma base teórica definirão se os objetivos foram ou não alcançados.

### Resultados esperados

- Adoção do método pela indústria;
- melhoria do desempenho das empresas produtoras de software que utilizarem esse método.

---

## Slide 30 - Limitações do trabalho

- É interessante que as limitações estejam presentes na proposta.
- As limitações evitam divagações em busca de aspectos que extrapolam os objetivos.
- Delimitam a abrangência do trabalho.
  - Informar até que ponto os resultados podem ou não ser generalizados.
  - Cortes nos objetivos ao longo da execução podem ser necessários.
- Limitar questões:
  - trabalhos extensos que não cabem no prazo disponível;
  - objetivos demasiadamente amplos.
- Evitar "síndromes" como:
  - querer mudar o mundo;
  - pretender alcançar um prêmio Nobel ou Turing Award.

---

## Slide 31 - Limitações do trabalho: condições de validação

- Em vez de validar um método ou uma implementação para todos os casos:
  - a validação pode ser feita sob determinadas condições.

### Exemplo baseado em Wazlawick (2014)

- Um método de estimativa de esforço é comprovadamente mais preciso:
  - para uma determinada classe de sistemas, como sistemas baseados na Web.
- O método não foi testado com outros tipos de sistemas.
  - Essa condição deve ser apresentada como limitação do trabalho.

---

## Slide 32 - Estrutura geral da proposta

1. Introdução;
   - justificativa;
   - objetivos.
2. Revisão da literatura.
3. Metodologia;
   - cronograma;
   - resultados esperados;
   - limitações.

---

## Slide 33 - Revisão de literatura

### Fundamentação

- Técnicas e teorias relevantes para o tratamento do problema.
- Pode incluir:
  - evolução da área;
  - contexto;
  - técnicas;
  - terminologia;
  - livros;
  - links;
  - *surveys*;
  - *reviews*.

### Trabalhos relacionados

- Artigos e outros referenciais relacionados ao trabalho.
- Devem evidenciar:
  - trabalhos clássicos;
  - contribuições recentes;
  - o estado atual da arte.
- A revisão pode ser obtida por meio de um processo sistemático.

---

## Slide 34 - Metodologia: síntese

### Materiais e métodos

- Como o trabalho será realizado;
- sequência de passos para atingir os objetivos.

### Recursos e ferramentas

- Conjunto de recursos e ferramentas que serão utilizados.

### Protótipos

- Informar se serão ou não construídos protótipos.

### Experimentos

- Quais experimentos serão realizados;
- se serão utilizados *benchmarks*;
- quais *benchmarks* serão utilizados;
- como ocorrerá a análise dos resultados obtidos nos experimentos.

### Validação

- Explicar como será realizada a validação.

---

## Slide 35 - Referências

- WAZLAWICK, R. S. *Metodologia de Pesquisa para Ciência da Computação*. 2. ed. Elsevier, 2014.
- WAINER, Jacques. Métodos de pesquisa quantitativa e qualitativa para a Ciência da Computação. In: Atualização em Informática 2007. Sociedade Brasileira de Computação; Editora PUC-Rio, 2007.
- OLIVEIRA, Maria Cristina Ferreira de. *Metodologia de Pesquisa para Ciência da Computação*. ICMC-USP.
- BROOKE, J. *SUS: A Quick and Dirty Usability Scale*. In: Usability Evaluation in Industry. Edited by P. W. Jordan, B. Thomas, B. A. Weerdmeester and I. L. McClelland. London: Taylor & Francis, 1989-1994.

---

## Slide 36 - Referências complementares

- PARREIRA, Pedro; PROENÇA, Sara; SOUSA, Liliana; MÓNICO, Lisete. Technology Assessment Model - TAM: modelos precursores e modelos evolutivos. 2018.
- INTERNATIONAL ORGANIZATION FOR STANDARDIZATION. ISO/IEC 25010:2011 - Systems and software engineering - Systems and software Quality Requirements and Evaluation - SQuaRE - System and software quality models. Geneva, Switzerland: ISO, 2011.
