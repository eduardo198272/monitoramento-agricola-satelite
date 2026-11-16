# Revisão didática do artigo

## Escopo e autorização

Revisão editorial aplicada após o autor aprovar, na conversa, o diagnóstico e os exemplos de [`REVISAO_DIDATICA_ESCRITA.md`](../../REVISAO_DIDATICA_ESCRITA.md). Referência anterior: commit `1862dd7`.

O perfil autoral foi lido integralmente antes da atividade. A revisão mantém a exposição acadêmica, mas apresenta a finalidade das operações antes dos termos, símbolos e detalhes de implementação. Não houve nova pesquisa agronômica ou bibliográfica. A assistência de IA não substitui a aprovação intelectual do autor nem resolve as pendências científicas e institucionais.

## Alterações

- Revisados os dez arquivos `final_*.tex`, do resumo à conclusão.
- Explicados pelo contexto termos como banda, composição temporal, redução espacial, janela de observações, contratos de dados, interoperabilidade, proveniência e estado da interface.
- Separadas explicações de funcionamento, detalhes de código e condições de interpretação.
- Organizada a exposição dos resultados sem alterar categorias, valores, denominadores ou comentários desfavoráveis.
- Retirada da apresentação de Slaiffer a descrição do processo de consulta do revisor; a comparação científica e as citações foram preservadas.
- Resumo e abstract revistos por último e alinhados entre si.
- Fluxograma de exportação antecipado dentro da mesma subseção, sem alteração de conteúdo, legenda ou rótulo, para evitar uma página isolada.
- Atualizado o índice documental em `../../README.md`; os registros de compilações anteriores permanecem históricos.

As ressalvas que limitam o significado das evidências foram preservadas. Não foram modificadas motivações do autor, critérios da aplicação ou conclusões para sugerir validação inexistente.

## Validação de preservação

`validar_revisao.py` compara as fontes com o commit anterior e gera `preservacao.json` e `alteracoes.diff`. Foram conferidos:

- oito ambientes matemáticos numerados, sem alteração literal das expressões;
- mesmas citações, rótulos e referências cruzadas em cada arquivo;
- mesmas macros que inserem os resultados da avaliação com usuários;
- tabelas e blocos de figuras intactos, admitindo apenas o reposicionamento do fluxograma;
- nenhum número anterior removido da prosa: apenas a explicação de `float32` como 32 bits e as repetições explicativas de 20 e 11,73 foram acrescentadas;
- aplicação, testes, bibliografia, classe institucional, figuras, capturas, gráficos, resultados gerados e evidências históricas sem alterações;
- planilha analisada com SHA-256 `9adb66b330103ca858c37d7dc6cdb5e4e954f09f749a0c122fa6e6b2f4f5de59`.

Essas verificações protegem elementos formais e quantitativos; não medem compreensão do leitor nem comprovam, sozinhas, equivalência semântica de toda frase. A comparação editorial antes/depois está disponível no diff.

## PDF atualizado

Resultado registrado em `compilacao.json`:

| Verificação | Resultado |
|---|---|
| Páginas | 35; versão anterior com 33 |
| Figuras / tabelas | 27 / 5, preservadas |
| Chaves bibliográficas citadas | 45, preservadas |
| Citações ou referências cruzadas indefinidas | Nenhuma |
| Classe institucional | Preservada |
| Novo excesso de caixa após ajuste do resumo | Nenhum registrado |
| Aviso remanescente | `Overfull hbox (54.64pt)` do cabeçalho, já existente |
| SHA-256 do PDF | `0f94a512abde41f78066f3b7f8ed79ae6fb90b9e84425732eb133e40ed9f6ca8` |

As 35 páginas foram renderizadas e examinadas em seis folhas de contato para conferir distribuição geral, presença de figuras e ausência de sobreposições grosseiras. Essa triagem não certifica a leitura de todos os detalhes em tamanho final. A leitura integral e a aprovação final pelo autor permanecem necessárias.

A compilação intermediária apresentou excesso vertical na primeira página; o resumo e o abstract foram condensados sem remover seus resultados e limites centrais. O aviso deixou de aparecer na compilação final. Uma página quase vazia com o fluxograma de exportação foi eliminada pelo reposicionamento do bloco.

Não foi necessário reexecutar os testes da aplicação, pois código, dependências e testes não foram modificados. Os números desses testes no artigo continuam identificados como resultados históricos, não como uma nova execução desta etapa.

## Reproduzir as verificações

Depois de compilar em um diretório separado, executar na raiz:

```bash
.venv/bin/python docs/artigo_final/avaliacao_usuarios/scripts/validar_artigo.py --build-dir /tmp/opencode/revisao-didatica/build --output docs/artigo_final/evidencias/revisao_didatica/compilacao.json
.venv/bin/python docs/artigo_final/evidencias/revisao_didatica/validar_revisao.py --build-dir /tmp/opencode/revisao-didatica/build
```

Os JSONs e o diff desta pasta correspondem à revisão didática. Os manifestos em `auditoria_cientifica/`, `evidencias/capturas_autor/` e `evidencias/revisao_redacao_usuarios/` não foram sobrescritos e não identificam o novo PDF.

Não houve commit, push, merge ou deployment nesta etapa.
