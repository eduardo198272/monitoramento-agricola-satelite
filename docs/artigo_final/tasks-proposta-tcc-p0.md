# Tasks P0 - Proposta de TCC

## Status geral

Prioridade: P0  
Objetivo: construir a proposta de TCC completa em Markdown e LaTeX dentro de `docs/artigo_final`, sem alterar `docs/modelo_latex`.

## Checklist de execucao

### P0-01 - Consolidar orientacoes obrigatorias

- [x] Ler os markdowns de slides sobre motivacao, objetivos, revisao bibliografica e metodologia.
- [x] Ler `Técnicas para construção de artigo.md`.
- [x] Extrair a estrutura obrigatoria da proposta: resumo, motivacao, objetivos, revisao, materiais e metodos, validacao, cronograma, resultados esperados e limitacoes.
- [x] Registrar as regras de escrita e criterios de aceitacao na spec P0.

### P0-02 - Criar ambiente de trabalho do artigo

- [x] Criar a pasta `docs/artigo_final`.
- [x] Criar `spec-proposta-tcc-p0.md`.
- [x] Criar `tasks-proposta-tcc-p0.md`.
- [x] Copiar os arquivos necessarios de `docs/modelo_latex` para `docs/artigo_final`.
- [x] Criar subpasta `docs/artigo_final/fig`.
- [x] Garantir que o modelo original permaneca intacto.

### P0-03 - Produzir rascunho textual em Markdown

- [x] Analisar `motivacao_objetivos_tcc.md`.
- [x] Analisar `metodologia_cronograma_eduardo_198272.md`.
- [x] Analisar `sistema_monitoramento_agricola_imagens_satelite_v1_1.md`.
- [x] Consultar specs existentes do sistema quando ajudarem a detalhar requisitos, arquitetura ou validacao.
- [x] Criar `docs/artigo_final/rascunho-proposta.md`.
- [x] Redigir resumo em paragrafo unico.
- [x] Redigir motivacao e justificativa.
- [x] Redigir objetivo geral e objetivos especificos.
- [x] Redigir revisao de literatura em formato de sintese critica.
- [x] Redigir materiais e metodos.
- [x] Redigir validacao.
- [x] Redigir cronograma e descricao das atividades.
- [x] Redigir resultados esperados.
- [x] Redigir limitacoes e trabalhos futuros, se couber.

### P0-04 - Planejar e criar elementos visuais

- [x] Definir quais figuras realmente ajudam o texto.
- [x] Criar diagrama da arquitetura do sistema.
- [x] Criar diagrama do fluxo metodologico.
- [x] Criar figura explicativa dos indices espectrais, se necessario.
- [x] Usar diagramas inline no LaTeX, sem dependencia de arquivos externos em `fig`.
- [x] Inserir legendas academicas e referenciar cada figura no texto.

### P0-05 - Montar projeto LaTeX

- [x] Criar `Proposta.tex` em `docs/artigo_final` com dados do aluno, titulo, orientador e includes.
- [x] Criar `1_Resumo.tex`.
- [x] Criar `2_Motivacao_e_objetivos.tex`.
- [x] Criar `3_Revisao_Literatura.tex`.
- [x] Criar `4_Materiais_Metodos.tex`.
- [x] Criar ou adaptar `referencias.bib` com apenas referencias usadas.
- [x] Ajustar caminhos de figuras para `fig/...`.
- [x] Conferir acentos, caracteres especiais e comandos LaTeX.

### P0-06 - Revisar referencias

- [x] Garantir que toda citacao no texto possua entrada no `.bib`.
- [x] Remover entradas bibliograficas nao usadas, se isso nao prejudicar a compilacao.
- [x] Conferir autores, titulos, anos, paginas, DOI, URL e datas de acesso.
- [x] Padronizar referencias conforme o modelo.
- [x] Nao manter referencias ficticias do template no artigo final.

### P0-07 - Revisao academica e de portugues

- [x] Revisar concordancia nominal e verbal.
- [x] Revisar coesao entre capitulos.
- [x] Remover repeticoes e frases vagas.
- [x] Garantir que objetivos, metodologia, validacao e resultados esperados estejam alinhados.
- [x] Conferir se o texto nao promete produto comercial completo.
- [x] Conferir se as limitacoes delimitam o escopo.
- [x] Conferir se a revisao de literatura e critica, nao apenas descritiva.

### P0-08 - Validar LaTeX

- [x] Verificar se existe compilador LaTeX disponivel no ambiente.
- [x] Compilar o projeto, se possivel.
- [x] Corrigir erros de compilacao.
- [x] Corrigir referencias cruzadas ausentes.
- [x] Gerar PDF final, se o ambiente permitir.
- [x] Registrar qualquer limitacao caso a compilacao nao possa ser feita localmente.

## Observacoes de compilacao

- PDF gerado em `docs/artigo_final/Proposta.pdf`.
- A compilacao exigiu copiar `hyperref-compat.sty` do modelo para a pasta local do artigo.
- Restaram apenas avisos visuais de `underfull` e um `overfull` pequeno; nao ha erro fatal nem citacao indefinida no log final.
- O MiKTeX exibiu aviso local sobre atualizacoes nao verificadas, sem impedir a geracao do PDF.

## Ordem de execucao recomendada

1. Finalizar leitura dos documentos de conteudo.
2. Criar rascunho Markdown consolidado.
3. Revisar o rascunho quanto a estrutura academica.
4. Montar o LaTeX a partir do rascunho aprovado.
5. Criar ou inserir figuras.
6. Revisar referencias.
7. Revisar portugues.
8. Compilar e corrigir o PDF.

## Definicao de pronto

A tarefa P0 estara pronta quando `docs/artigo_final` contiver a proposta completa em LaTeX, com bibliografia, figuras necessarias, texto revisado e, se possivel, PDF compilado. O modelo em `docs/modelo_latex` deve permanecer sem alteracoes.
