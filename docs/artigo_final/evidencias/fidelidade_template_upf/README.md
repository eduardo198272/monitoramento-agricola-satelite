# Revisão de fidelidade ao template da Ciência da Computação / UPF

Estado vigente da apresentação do artigo. O conteúdo científico não foi
revisado nesta etapa. A comparação detalhada e a limitação de acesso aos
três trabalhos institucionais estão em `../../AUDITORIA_ABNT.md`.

## Entrega e configuração

- PDF principal: `../../Relatorio_Final.pdf`, 32 páginas, autoria individual
  enquanto a coautoria de Rafael Rieder não for explicitamente confirmada.
- `../../autoria.tex`: opção `TCCIncluirRafaelComoCoautor=0`.
  Somente depois da confirmação, alterar para 1. Isso inclui Rafael,
  usa uma filiação institucional comum e atualiza cabeçalho/metadados.
- Classe `CC-EC_TF-TC.cls` e estilo `dcu.bst` sem alterações.
- Entrada volta a chamar BibTeX com `\bibliography{referencias_institucionais}`.
- `referencias_normalizadas.bib` é a base de metadados preservada da quinta
  rodada; `referencias_institucionais.bib` é a projeção para os campos do dcu.
- `scripts/preparar_bib_dcu.py` não gera autores formatados, rótulos de
  citações ou `bibitem`: apenas acrescenta a `note` os campos que o dcu não
  exibe nativamente. Também protege a caixa de siglas/nomes próprios com
  chaves BibTeX, sem alterar os caracteres do título. Os demais campos e
  as 63 chaves são preservados.
- O antigo `scripts/gerar_referencias_normalizadas.py` e o produto
  `referencias_normalizadas.tex` não participam da compilação vigente.

## Reproduzir

Compilação normal, sem dependência do gerador bibliográfico personalizado:

```sh
tectonic -X compile Relatorio_Final.tex --keep-logs --keep-intermediates
```

Executar em `docs/artigo_final`. Se os metadados da base estruturada forem
alterados, atualizar a projeção antes de compilar:

```sh
python docs/artigo_final/scripts/preparar_bib_dcu.py
```

Esse adaptador requer o ambiente editorial com pybtex, não as dependências
da aplicação. Na execução atual foi utilizado o pacote isolado em
`/tmp/opencode/quinta-rodada/python`.

## Evidências

- `comparacao.json`: configurações verificadas e origens comparadas.
- `consultas_repositorio.json`: respostas dos links externos; HTML antirobô,
  não PDFs obtidos.
- `compilacao.json`, `Relatorio_Final.log`, `Relatorio_Final.bbl` e
  `Relatorio_Final.blg`: compilação e saída efetiva do BibTeX/dcu.
- `preservacao.json`: metadados, texto científico, dados, imagens, equações
  e declarações preservados.
- `inspecao_visual.md` e `renderizacao.json`: inspeção individual das páginas,
  além das duas páginas iniciais da prévia isolada de coautoria.
- `antes_depois.diff`: diferenças em relação ao início desta revisão.

Backups privados de referência:

- `/tmp/opencode/quinta-rodada/antes/`: estado anterior à quinta rodada.
- `/tmp/opencode/ajuste-pretextual-upf/antes/`: estado ao iniciar a correção
  pontual de ordem dos resumos.
- `/tmp/opencode/fidelidade-upf/antes/`: estado ao ampliar a revisão para a
  fidelidade integral ao modelo local.

As comparações não usam HEAD como substituto desses estados: HEAD antecede
alterações científicas que já estavam aprovadas. Os registros históricos
da quarta e quinta rodadas não foram sobrescritos.

## Limites

A fidelidade foi verificada contra a classe local e sua origem Git, não
contra uma cópia independente do pacote oficial baixada nesta revisão.
Os três links fornecidos do repositório e os endpoints canônicos da API
retornaram verificação Anubis. Não foi possível conferir visualmente esses
artigos nem declarar recorrências institucionais a partir deles.

Sem assinatura, aprovação institucional, ativação definitiva de coautoria,
novo experimento, nova coleta, commit ou push.
