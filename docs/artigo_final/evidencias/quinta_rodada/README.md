# Quinta rodada — normalização

Comparação contra a versão local da **quarta rodada**, não contra HEAD.
O backup exato está em `/tmp/opencode/quinta-rodada/antes/`; o inventário
inicial, em `/tmp/opencode/quinta-rodada/baseline.json`.

## Entregas

- `../../Relatorio_Final.pdf`: versão compilada após a normalização.
- `../../AUDITORIA_ABNT.md`: achados ABNT-01–22, limitações e pendências.
- `referencias.json`: inventário individual das 63 entradas, antes/depois,
  tipo, situação de citação, notas anteriores e lacunas.
- `links.json`: consultas HTTP desta rodada, incluindo falhas de acesso.
- `datas.json`: evidências e critérios das datas, sem confundir acesso e edição.
- `compilacao.json` e `Relatorio_Final.log`: resultado da compilação.
- `inspecao_visual.md` e `renderizacao.json`: inspeção das páginas.
- `preservacao.json` e `antes_depois.diff`: preservação e comparação da rodada.

## Geração bibliográfica

O arquivo de origem `../../referencias.bib` foi preservado. O gerador
`../../scripts/gerar_referencias_normalizadas.py` produz os arquivos
`referencias_normalizadas.bib` e `referencias_normalizadas.tex`. O artigo
inclui o segundo, formado por `\bibitem` compatíveis com **natbib**.
Não há coexistência de biblatex e natbib nem edição manual de `.bbl`.

O gerador é uma solução editorial **específica deste artigo**, não um
pacote universal ou certificação automática das normas de 2023/2025.
O inventário de links é uma entrada de evidência para datas de acesso
efetivamente realizadas, não uma verificação de conteúdo científico.
O comando LaTeX não precisa de Python: os produtos gerados estão incluídos.
Após mudanças no `.bib` ou nas citações, regenerar antes de compilar:

```sh
# Em ambiente editorial separado, instalar requirements-normalizacao.txt.
python docs/artigo_final/scripts/gerar_referencias_normalizadas.py
```

A dependência foi instalada somente em
`/tmp/opencode/quinta-rodada/python`, sem mudar as dependências da aplicação.
Neste ambiente, a execução usou `PYTHONPATH` apontando para esse diretório.

## Limite de entrega

Há correções materiais aplicadas e validações técnicas, mas **não se declara
conformidade integral ou aceite institucional**. Não foi obtida uma cópia
oficial independente do modelo final; a conferência de todas as emendas e
versões corrigidas também não foi encerrada. Datas aproximadas e metadados
ausentes estão discriminados, não tratados como fatos confirmados.
Não houve commit, push, assinatura, novo experimento ou nova coleta.
