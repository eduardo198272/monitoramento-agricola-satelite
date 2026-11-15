# Relatório final do TCC

O padrão para o relatório final é o modelo institucional `CC-EC_TF-TC.cls`,
com entrada em `Relatorio_Final.tex`. Os arquivos `final_*.tex` contêm o texto,
`referencias.bib` contém a bibliografia e `logoColorHorizontalComplemento.png`
é necessário para o cabeçalho. O conteúdo ainda está em elaboração.
Os métodos, diagramas e resultados de software foram alinhados à revisão
`a9a9677` em 15/11/2026: SQLite local, sessões isoladas no ponto de entrada web,
transferência GeoJSON e autenticação por conta de serviço. A suíte de 677 testes
e o teste mínimo com Earth Engine estão descritos no
[registro de verificação](../validation/streamlit-cloud-readiness.md).
Isso não demonstra publicação do site ou validação agronômica concluídas.
Os diagramas editáveis ficam em `fig/` como arquivos LaTeX/TikZ e descrevem a
implementação observada, não uma validação operacional dos fluxos.

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

- Confirmar orientador, mês da defesa e formato de papel com o orientador.
- Conferir integralmente trabalhos relacionados e a referência específica de NDMI.
- Executar e registrar cenários agrícolas, conferência independente dos índices,
  máscara, escala e unidades climáticas.
- Validar o deploy e revisar visualmente o PDF para a entrega.
- Não remover essas ressalvas apenas porque os testes de software passaram.
