# Relatório final do TCC

O padrão para o relatório final é o modelo institucional `CC-EC_TF-TC.cls`,
com entrada em `Relatorio_Final.tex`. Os arquivos `final_*.tex` contêm o texto,
`referencias.bib` contém a bibliografia e `logoColorHorizontalComplemento.png`
é necessário para o cabeçalho. A redação foi ampliada em 15/11/2026 a partir da
revisão `b7c325c`, caracterizando pesquisa aplicada e tecnológica centrada na
plataforma. As seções de implementação e apresentação estão em
`final_3a_implementacao.tex` e `final_3b_plataforma.tex`.
A execução final aprovou 710 testes em 11,73 s, com 100% de cobertura em `src/app`;
três verificações Node foram aprovadas separadamente.
O teste mínimo anterior com Earth Engine permanece identificado como histórico no
[registro de verificação](../validation/streamlit-cloud-readiness.md).
O fluxo real com serviços e downloads foi executado em Chrome na versão local.
O acesso público foi verificado, mas as correções não foram publicadas.
Os diagramas editáveis ficam em `fig/` como arquivos LaTeX/TikZ e descrevem a
implementação observada, não uma validação operacional dos fluxos.

## Documentos da revisão

- [Análise técnica e observações do software](ANALISE_TECNICA_TCC.md)
- [Matriz de rastreabilidade](RASTREABILIDADE_TCC.md)
- [Inventário de capturas, sete diagramas e cinco esquemas científicos](FIGURAS_PENDENTES.md)
- [Relatório de alterações, referências e pendências](REVISAO_TCC.md)

- [Correções técnicas e testes de regressão](CORRECOES_TECNICAS.md)
- [Pesquisa com usuários e incorporação de respostas reais](PESQUISA_USUARIOS.md)
- [Checklist de entrega](CHECKLIST_ENTREGA.md)

As capturas existentes são reais; imagens ausentes não geram placeholders.
CAP-18/19 continuam planejadas para visualizador de planilha/ZIP.
A consulta pública registrada em `evidencias/nasa_power_unidades.json` identificou
uma conversão de radiação incompatível com a unidade AG retornada. A aplicação
foi corrigida pelos metadados de origem, com regressões multiformato.
Arquivos reais e manifesto estão em `evidencias/demonstracao_real/`.

## Gerar o PDF

Com o [Tectonic](https://tectonic-typesetting.github.io/) instalado, execute
na raiz do repositório:

```sh
cd docs/artigo_final
tectonic Relatorio_Final.tex
```

O comando gera `Relatorio_Final.pdf` no modelo atual, substituindo o PDF de
mesmo nome. O Tectonic executa o BibTeX automaticamente e pode precisar de
acesso à internet para baixar dependências na primeira compilação.

Confira a paginação, as referências e os avisos de diagramação após gerar o
PDF. A classe fornecida usa papel Letter, embora o exemplo mencione A4; confirme
essa diferença com o orientador antes da entrega.

## Arquivos anteriores

`Proposta.tex`, os capítulos associados e `upf-ccc.cls` pertencem à proposta
original, não são o padrão para o relatório final e foram preservados. A pasta
`docs/modelo_latex` também contém o modelo anterior. O arquivo
`Relatorio_Final-modelo-anterior.pdf`, quando presente localmente, é apenas um
backup histórico, não a versão atual nem parte desta atualização versionada.

## Pendências acadêmicas

- Confirmar mês da defesa, formato de papel e endereço institucional do cabeçalho.
  O orientador informado pelo autor é Prof. Carlos Amaral Holbig.
- Conferir integralmente trabalhos relacionados e a referência específica de NDMI.
- Revisar com o orientador a mudança de escopo: estudos de soja, milho e pastagem
  e experimentos de campo não foram realizados; não são resultados do artigo.
- Concluir capturas de Excel/ZIP em visualizador e avaliação em aparelhos físicos.
- Receber instrumento completo e respostas reais da pesquisa; conferir ética com orientador.
- Revisar a adequação histórica da QA60 e compatibilidade de navegadores.
- Autorizar/publicar correções somente em atividade posterior, fora desta execução.
- Não remover essas ressalvas apenas porque os testes de software passaram.
