# Spec P0 - Proposta de TCC em LaTeX ABNT2

## Prioridade

P0 - entrega obrigatoria para hoje.

## Objetivo

Construir a proposta de Trabalho de Conclusao de Curso do projeto "Sistema de Monitoramento Agricola por Imagens de Satelite", seguindo o modelo LaTeX da UPF, as normas ABNT2 suportadas pelo template e as orientacoes metodologicas presentes em `docs/documentação_artigo`.

O resultado final deve ser uma proposta academica completa, coesa, revisada em lingua portuguesa e pronta para compilacao em LaTeX, sem modificar nenhum arquivo da pasta `docs/modelo_latex`.

## Fontes obrigatorias

### Orientacoes de escrita e estrutura

- `docs/documentação_artigo/Técnicas para construção de artigo.md`
- `docs/documentação_artigo/Slides_Dicas_revisao_literatura.md`
- `docs/documentação_artigo/Slides_Revisao_Bibliografica.md`
- `docs/documentação_artigo/slides_motivação_e_Objetivos.md`
- `docs/documentação_artigo/slides_metodologia.md`

### Conteudo do trabalho

- `docs/documentação_artigo/motivacao_objetivos_tcc.md`
- `docs/documentação_artigo/metodologia_cronograma_eduardo_198272.md`
- `docs/documentação_artigo/sistema_monitoramento_agricola_imagens_satelite_v1_1.md`
- Specs existentes em `docs/specs`, quando ajudarem a detalhar funcionalidades do sistema.

### Modelo e LaTeX

- `docs/modelo_latex/Proposta.tex`
- `docs/modelo_latex/1_Resumo.tex`
- `docs/modelo_latex/2_Motivacao_e_objetivos.tex`
- `docs/modelo_latex/3_Revisão_Literatura.tex`
- `docs/modelo_latex/4_Materiais_Métodos.tex`
- `docs/modelo_latex/referencias.bib`
- `docs/modelo_latex/upf-ccc.cls`
- `docs/latex_documentation/Latex_Documentation_INDEX.md`
- Arquivos especificos de `docs/latex_documentation` somente quando forem necessarios para resolver uso de figuras, tabelas, citacoes, capitulos, bibliografia ou formatacao.

## Restricoes

- Nao editar, sobrescrever ou mover arquivos de `docs/modelo_latex`.
- Criar todo o artigo dentro de `docs/artigo_final`.
- Copiar para `docs/artigo_final` apenas os arquivos necessarios do modelo, preservando o original intacto.
- Manter a estrutura do template UPF: arquivo principal `.tex`, capitulos separados, pasta `fig` e arquivo `.bib`.
- Usar a classe `upf-ccc` e o estilo de citacao/bibliografia previsto no modelo.
- Nao inventar referencias academicas. Usar apenas referencias existentes nos documentos ou referencias verificadas posteriormente.
- Diagramas e imagens podem ser criados, mas devem servir a uma funcao textual clara: arquitetura, fluxo metodologico, indices espectrais, cronograma ou validacao.
- Toda figura, tabela e equacao inserida deve ser citada no texto e possuir `\label`.
- A proposta deve ser escrita em portugues formal, com concordancia, coesao e padrao academico.

## Estrutura obrigatoria da proposta

### Arquivo principal

O arquivo principal deve configurar:

- autor: Eduardo Steffens Hoppen;
- titulo em portugues;
- titulo em ingles;
- tipo de trabalho: monografia;
- orientador: Prof. Carlos Amaral Holbig;
- idioma: `brazilian`;
- inclusao dos capitulos obrigatorios;
- bibliografia.

### Resumo

Deve ser um unico paragrafo, sem quebras internas, contendo:

- contexto e motivacao do monitoramento agricola por satelite;
- problema abordado;
- objetivo geral;
- abordagem metodologica;
- tecnologias principais;
- resultados esperados;
- contribuicao academica do prototipo.

### Motivacao e objetivos

Deve conter:

- contextualizacao da agricultura moderna e do uso de sensoriamento remoto;
- problema ou necessidade real;
- justificativa tecnica, academica e social;
- delimitacao do tema;
- objetivo geral em verbo no infinitivo;
- objetivos especificos verificaveis;
- hipoteses, se forem adotadas, ou declaracao de que a validacao sera orientada por atendimento aos objetivos.

### Revisao de literatura

Deve ser uma sintese critica, nao uma lista de autores. Deve conter:

- protocolo ou estrategia de busca, ainda que narrativa;
- criterios de selecao e triagem das fontes;
- fundamentacao sobre sensoriamento remoto;
- imagens Sentinel-2;
- indices espectrais, especialmente NDVI e NDWI ou NDMI;
- Google Earth Engine;
- ferramentas de monitoramento agricola e lacunas de acesso/custo/reprodutibilidade;
- trabalhos relacionados ou referencias comparativas;
- fechamento conectando a lacuna encontrada ao sistema proposto.

### Materiais e metodos

Deve conter:

- ferramentas e recursos previstos;
- arquitetura do sistema;
- fluxo de dados;
- etapas de desenvolvimento;
- selecao de areas de estudo;
- coleta e filtragem de imagens;
- calculo de indices espectrais;
- integracao com dados climaticos;
- desenvolvimento da interface;
- validacao funcional;
- validacao dos indices por comparacao com faixas esperadas e literatura;
- metricas, estatisticas e criterio de anomalias;
- cronograma com semanas por mes;
- resultados esperados;
- limitacoes do estudo.

## Estrutura recomendada dos arquivos em `docs/artigo_final`

```text
docs/artigo_final/
  spec-proposta-tcc-p0.md
  tasks-proposta-tcc-p0.md
  Proposta.tex
  1_Resumo.tex
  2_Motivacao_e_objetivos.tex
  3_Revisao_Literatura.tex
  4_Materiais_Metodos.tex
  referencias.bib
  fig/
    arquitetura_sistema.pdf ou .png
    fluxo_metodologico.pdf ou .png
    indices_espectrais.pdf ou .png
```

## Regras de escrita

- Priorizar narrativa logica sobre ordem cronologica.
- Fazer o titulo, resumo e conclusoes parciais comunicarem claramente a contribuicao.
- Evitar detalhes que nao respondam aos objetivos ou perguntas de pesquisa.
- Explicar termos tecnicos antes de usa-los extensivamente.
- Usar paragrafos com progressao clara: contexto, problema, lacuna, proposta, validacao.
- Evitar afirmacoes absolutas quando o trabalho for um prototipo academico.
- Separar objetivo de resultado esperado.
- Apresentar limitacoes para delimitar o escopo.
- Garantir consistencia nos termos: NDVI, NDWI/NDMI, Sentinel-2, Google Earth Engine, Streamlit, NASA POWER.

## Regras de LaTeX e ABNT2

- Usar `\chapter`, `\section` e `\subsection` conforme o modelo.
- Usar `\cite`, `\citet` ou `\citep` conforme exemplos do template.
- Usar referencias BibTeX completas e consistentes.
- Para DOI e URL, seguir o padrao do modelo usando `note = {\url{...}}`.
- Legendas de tabelas devem ficar acima da tabela.
- Legendas de figuras devem ficar abaixo da figura.
- Tabelas e figuras devem possuir `\caption` e `\label`.
- Referenciar figuras, tabelas, secoes e equacoes com `\cref` quando possivel.
- Evitar comandos ou pacotes novos se o modelo ja oferecer suporte.

## Criterios de aceitacao

- Dado o diretorio `docs/artigo_final`, quando a etapa de redacao for concluida, entao ele deve conter uma copia independente e compilavel do artigo em LaTeX.
- Dado o modelo original em `docs/modelo_latex`, quando o artigo for criado, entao nenhum arquivo do modelo deve ter sido alterado.
- Dado o documento final, quando for lido do resumo aos materiais e metodos, entao a motivacao, objetivos, metodologia, validacao, cronograma, resultados esperados e limitacoes devem estar presentes e coerentes entre si.
- Dado o capitulo de revisao de literatura, quando for avaliado, entao ele deve apresentar sintese critica e nao apenas sequencia de citacoes.
- Dado o capitulo de metodologia, quando for avaliado, entao deve explicar como o sistema sera desenvolvido e como sera validado.
- Dado o cronograma, quando for avaliado, entao deve apresentar atividades futuras da execucao do TCC, com distribuicao semanal por mes.
- Dado o arquivo `.bib`, quando houver citacoes no texto, entao todas as chaves citadas devem existir na bibliografia.
- Dado o texto em portugues, quando a revisao final for realizada, entao devem ser corrigidos problemas de concordancia, ortografia, repeticao excessiva e fluidez.
- Dado o projeto LaTeX, quando houver ferramenta de compilacao disponivel, entao o PDF deve ser gerado sem erros impeditivos.

## Entregaveis

- Especificacao P0: `docs/artigo_final/spec-proposta-tcc-p0.md`.
- Checklist de execucao P0: `docs/artigo_final/tasks-proposta-tcc-p0.md`.
- Rascunho textual em Markdown consolidado.
- Projeto LaTeX final dentro de `docs/artigo_final`.
- Figuras e diagramas necessarios dentro de `docs/artigo_final/fig`.
- PDF compilado, se houver ambiente LaTeX disponivel.

## Riscos

- Referencias insuficientes para revisao de literatura com rigor academico.
- Falta de compilador LaTeX instalado no ambiente local.
- Necessidade de confirmar regras especificas do professor/orientador que nao estejam nos documentos.
- Inconsistencia entre NDWI e NDMI; deve-se padronizar a nomenclatura ou explicar a diferenca.
- Cronograma com atividades ja realizadas; o modelo orienta que o cronograma contenha apenas atividades futuras da execucao do trabalho final.

## Decisoes iniciais

- O artigo sera tratado como proposta de TCC, nao como artigo cientifico completo com resultados finais.
- A pesquisa sera descrita como desenvolvimento de prototipo funcional com validacao empirica e estudo de caso em areas agricolas.
- A revisao de literatura sera narrativa organizada, com estrategia de busca documentada, salvo se novas fontes exigirem formalizacao sistematica.
- A validacao sera baseada em testes funcionais, comparacao com faixas esperadas de indices espectrais, analise temporal e confronto com dados climaticos.
