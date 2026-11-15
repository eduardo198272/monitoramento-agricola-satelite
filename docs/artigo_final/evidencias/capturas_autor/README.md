# Substituição das capturas da plataforma

Revisão de 15/11/2026, sobre `dev` em `d4bc63d`, a pedido do autor.
Protocolo autoral lido integralmente antes da atividade.

## Resultado editorial

As capturas anteriores da apresentação foram substituídas por **16 das 17
imagens fornecidas pelo autor em `Imagens Artigo/`**, distribuídas em onze
figuras (13–22 e 24). O QR permanece como figura 23. Não foi necessário
acrescentar apêndice. O PDF continua com **33 páginas**, agora com 27 figuras
e cinco tabelas no total. Os diagramas, equações, resultados quantitativos e
gráficos da avaliação de usuários foram preservados.

As figuras ocupam a largura das duas colunas. Busca, salvamento, importação e
celular foram agrupados em painéis; as três barras GeoJSON foram recortadas
sem redesenhar controles ou modificar informações. Não foi feita interpolação
para alegar resolução adicional, troca de cores ou correção de valores nas imagens.
Os detalhes pequenos de telas desktop continuam dependentes da resolução de
origem e da ampliação do PDF; a série original não enquadra o eixo temporal.

| Arquivo da pasta do autor | Destino editorial |
|---|---|
| Imagem1 — Página Inicial | Figura 13 |
| Imagem1.2 — Barra de configuração | Figura 14 |
| Imagem1.3 — Barra de pesquisa | Figura 15(a) |
| Imagem1.4 — Resultado da busca | Figura 15(b) |
| Imagem4.4 — Desenho no mapa | Figura 16 |
| Imagem4.5 — Salvamento | Figura 17(a) |
| Imagem4.6 — Localização salva | Figura 17(b) |
| Imagem4.7 — Restauração | Figura 18 |
| Imagem4.1 — Upload GeoJSON | Figura 19(a), recorte da barra |
| Imagem4.2 — Arquivo GeoJSON selecionado | Figura 19(b), recorte da barra |
| imagem4.3 — Confirmação da importação | Figura 19(c), recorte da barra |
| Imagem2.1 — Mapa do índice e consulta pontual | Figura 20 |
| Imagem2.2 — Painel e série | Figura 21 |
| Imagem2.3 — Anomalias e clima | Figura 22 |
| Imagem5.1 — Mapa no celular | Figura 24(a) |
| Imagem5.2 — Painel no celular | Figura 24(b) |
| Imagem3.1 — Relatório PDF | **Não incluída: aguarda nova captura** |

## Relatório pendente

`relatorio_pdf_pendente.png` é cópia byte a byte da imagem recebida, mantida
somente nesta pasta de evidências. Não é referenciada pelo LaTeX. A captura
exibe radiação média de **59,00 MJ/m²/dia**; a correspondência com as unidades
de origem e a versão corrigida não foi validada. Não se afirma que o número
está correto, nem se altera o texto da captura para aparentar correção.

Após o autor atualizar a produção, obter nova captura e conferir os dados:

1. Identificar versão publicada, período, unidade de origem e relatório gerado.
2. Conferir a radiação contra os dados retornados, não apenas sua plausibilidade.
3. Guardar a nova evidência separadamente da captura histórica.
4. Inserir a figura do PDF e substituir a nota de pendência na seção de
   relatórios, recompilando e verificando paginação e referências.

O script de preparação **não aprova automaticamente** um novo arquivo: a
exclusão do relatório é explícita e deve ser revista somente após conferência.

## Proveniência e limites

- Originais em `Imagens Artigo/` intocados; cópias para compilação em
  `fig/capturas_autor/`, com nomes estáveis e hashes no `manifesto.json`.
- Capturas antigas e arquivos da demonstração anterior foram preservados.
- As imagens foram declaradas reais pelo autor. Data de captura, commit
  desktop, modelo do celular e versão do navegador não foram fornecidos.
- Desktop, mobile e a demonstração instrumentada anterior mostram exemplos
  distintos. Seus valores não foram combinados ou tratados como uma única execução.
- As imagens novas não comprovam as correções ainda não publicadas; o texto
  distingue as regras da implementação corrigida da interface ilustrada.
- Os screenshots móveis documentam a apresentação da tela, não uma matriz de
  compatibilidade, acessibilidade ou sucesso em tarefas.
- Os nomes locais “Teste1”/“Teste2” não são identificação de respondentes da
  pesquisa; não se inferiu proprietário, cultura ou diagnóstico para os polígonos.
- A revisão foi assistida por IA (GPT-6.1 Sol, OpenCode), com aprovação
  substantiva de texto e apresentação ainda sob responsabilidade do autor.

## Validação

- Compilação Tectonic concluída; 27 chaves citadas e referências cruzadas
  resolvidas. Classe institucional e oito ambientes de equações inalterados.
- `compilacao.json` registra esta versão. Os manifests de compilação e hashes
  anteriores em `avaliacao_usuarios/` são históricos, não o hash do PDF atual.
- SHA-256 do PDF atual:
  `1c2bc294904a5438204358c3a68cc32b3e53ec54d4f60af78eee8456d8f33447`.
- Renderização das 33 páginas em
  `/tmp/opencode/capturas-autor-visual/final-contato-1.png` a
  `final-contato-3.png`, com inspeção das páginas alteradas e detalhes de
  importação, salvamento e celular.
- Sem novos excessos horizontais ou verticais; persiste o excesso de 54,64 pt
  do cabeçalho herdado e avisos de fonte, `headheight` e espaçamento.
- A funcionalidade da aplicação e a análise dos questionários não foram
  reexecutadas para substituir imagens. Não são reivindicados novos ensaios.
- Nenhum deploy, commit ou push foi executado nesta revisão.

## Reproduzir

Na raiz do repositório, com Pillow instalado e a pasta original disponível:

```sh
.venv/bin/python docs/artigo_final/experimentos/preparar_capturas_autor.py
```

Na pasta `docs/artigo_final`, com o diretório de saída existente:

```sh
/tmp/opencode/tectonic --keep-logs --keep-intermediates \
  --outdir /tmp/opencode/capturas-autor-build Relatorio_Final.tex
```

Na raiz, sem sobrescrever o registro histórico da integração da pesquisa:

```sh
.venv/bin/python docs/artigo_final/avaliacao_usuarios/scripts/validar_artigo.py \
  --build-dir /tmp/opencode/capturas-autor-build \
  --output docs/artigo_final/evidencias/capturas_autor/compilacao.json
```

O validador passou a conferir os rótulos **expandidos no AUX** para suportar
figuras declaradas por macro e aceita caminho de saída separado. A regra
anterior procurava somente rótulos literais na fonte. Os caminhos temporários
e do Tectonic pertencem a esta sessão e podem ser adaptados.
