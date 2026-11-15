# Validação final da integração da avaliação de usuários

> Registro histórico da integração da pesquisa, anterior à substituição das
> capturas da plataforma. Para o PDF e as figuras atuais, consultar
> [`../evidencias/capturas_autor/README.md`](../evidencias/capturas_autor/README.md).
> Os cálculos e dados da pesquisa não foram alterados nessa troca visual.

**Data:** 15/11/2026. **Base Git:** `af120d5`, preservadas as alterações locais
da revisão autoral anterior. **Situação:** arquivos e PDF atualizados para
aprovação substantiva do autor; sem commit, push, merge ou deploy.

## Entregas

| Entrega | Arquivos / resultado |
|---|---|
| Artigo LaTeX | `final_0_resumo.tex`, `final_1_introducao.tex`, `final_2_fundamentacao.tex`, `final_3_metodos.tex`, `final_4_resultados.tex`, `final_4a_usuarios.tex`, `final_5_discussao.tex`, `final_6_conclusao.tex` |
| Entrada/bibliografia | `Relatorio_Final.tex` lê indicadores gerados; quatro referências metodológicas adicionadas e conferidas no nível descrito em `METODOLOGIA.md` |
| PDF | `../Relatorio_Final.pdf`, 33 páginas |
| Rotina reproduzível | `scripts/analisar_respostas.py`, `gerar_tabelas.py`, `gerar_graficos.py` |
| Auditoria/retificação | `scripts/corrigir_datas.py`, backup e auditoria privados; sete células autorizadas |
| Conferência | `scripts/validar_resultados.py`, `validar_artigo.py`, `test_analise.py` |
| Estatística | 40 itens fechados e nota geral, 191 categorias; CSV em `resultados/` |
| Gráficos | Nove conjuntos PDF/SVG/PNG, 27 arquivos em `figuras/` |
| Qualitativa | 142 células, treze temas multirrótulo, livro de códigos e tabela de trechos |
| Documentação | `README.md`, `METODOLOGIA.md`, `RESULTADOS.md`, `RELATORIO_QUALIDADE_DADOS.md` |
| Rastreabilidade | `../RASTREABILIDADE_TCC.md`, `../CHECKLIST_ENTREGA.md` e `../PESQUISA_USUARIOS.md` atualizados |

## Conferência dos dados e cálculos

- 31 submissões, todas com consentimento e exploração autodeclarados.
- Zero duplicatas exatas e zero equivalências integrais sem o carimbo.
- Procedência real declarada pelo autor, sem correspondência com exemplos
  sintéticos de pesquisa conhecidos; não se autenticaram identidades no Forms.
- Sete carimbos 16/17→15/11/2026, com horários e demais respostas preservados.
- Fonte recebida SHA-256:
  `d61b9f11514f8d42f276abdb3e4e173782955c468fb50d774680032d342ce48a`.
- Fonte corrigida SHA-256:
  `9adb66b330103ca858c37d7dc6cdb5e4e954f09f749a0c122fa6e6b2f4f5de59`.
- Conferência independente por Counter/statistics dos resultados pandas/NumPy:
  frequências, denominadores, percentuais, quartis, medianas, médias e desvios
  padrão amostrais, além da nota geral. Resultado `passed: true` em
  `resultados/validacao.json`.
- Oito testes sintéticos isolados: **8 aprovados em 0,40 s** na execução final
  registrada. Casos de ausência, impossibilidade, triagem, duplicidade, tentativas,
  nota inválida, novos textos sem código e grupos pequenos; não são novas
  participações nem foram usados para preencher dados.
- Os testes da aplicação de 710 casos e três Node continuam resultados históricos;
  não foram reexecutados nem somados aos testes estatísticos.

### Síntese conferida

- Nota: n=31; média 7,74; mediana 8; moda 9; DP amostral 1,81; Q1=7; Q3=9;
  mínimo 3 e máximo 10.
- Execução: busca sem ajuda 31/31; demarcação sem ajuda 18/31; séries/anomalias
  com cinco tentativas sem sucesso e conclusão 23/28.
- Experiência: compreensão 24/30 concordâncias; satisfação com tempo de resposta
  21/31; todas as distribuições incluem discordâncias e neutralidade.
- Utilidade: pixel 20/23 avaliações 4–5, mas oito impossibilidades de avaliação;
  análise espectral com cinco avaliações 1–2 entre 30 válidas.
- Intenção de uso: 24/30 concordâncias; não equivale a utilização efetiva.
- Qualitativa: treze menções a navegação/desenho/orientação nas dificuldades,
  oito aos critérios dos alertas e três a latência/conectividade.

## Compilação e inspeção

Tectonic 0.17.0, com BibTeX automático, concluiu a compilação sem erros.
O resultado automatizado está em `resultados/compilacao.json`:

- **33 páginas**, papel Letter conforme a classe institucional preservada.
- **27 chaves citadas**, nenhuma citação ou referência cruzada indefinida.
- **34 figuras e cinco tabelas** compiladas.
- Oito ambientes de equações preservados literalmente em relação à base.
- Metadados de título/autor preservados; 23 arquivos de inclusão examinados.
- SHA-256 do PDF:
  `3df58aa1904d7c1cb5e93ea81c68544e4d44e7ac195d7782eee3fb8cb6e4436b`.
- Todas as 33 páginas foram renderizadas e inspecionadas em folhas de contato;
  detalhes da primeira página, gráficos/tabelas de usuários e referências
  também foram examinados. Os nove gráficos foram conferidos em visão
  complementar; os arquivos vetoriais mantêm legibilidade ao ampliar.
- Imagens de inspeção em `/tmp/opencode/usuarios-visual/`, folhas
  `contato-final-1.png` a `contato-final-3.png`. Não são novas capturas da aplicação.
- Ajustes de concisão eliminaram o excesso vertical intermediário da primeira
  página. Não houve redução de fonte ou alteração de margens/classe para ocultar avisos.
- Persistem avisos herdados: excesso horizontal do cabeçalho de 54,64 pt,
  `headheight`, fontes e espaçamentos `underfull`. Mês da defesa e endereço
  institucional herdado continuam pendentes. Capturas antigas de contexto têm
  texto pequeno/contraste limitado; CAP-18/19 permanecem ausentes.
- `git diff --check`: sem problemas. Os 28 arquivos funcionais do manifesto
  coincidem com os hashes da demonstração e não há diff em `src`, entrada
  Streamlit, testes da plataforma ou dependências.

Backup da documentação anterior à integração:
`/tmp/opencode/avaliacao-usuarios-pre-integracao.tar.gz`, SHA-256
`184825eaf5b76055f41a463875491cfc85386e20770a189531273327b924306b`.
O backup recebido da planilha permanece separado e ignorado por Git.

## Reproduzir a validação do LaTeX

Na pasta `docs/artigo_final`, com diretório de saída já criado:

```sh
/tmp/opencode/tectonic --keep-logs --keep-intermediates \
  --outdir /tmp/opencode/usuarios-build Relatorio_Final.tex
```

Na raiz do repositório:

```sh
.venv/bin/python docs/artigo_final/avaliacao_usuarios/scripts/validar_artigo.py \
  --build-dir /tmp/opencode/usuarios-build
git diff --check
```

Os caminhos Tectonic/temporários são desta sessão; adaptar em outro ambiente.
Logs completos: `/tmp/opencode/usuarios-build/Relatorio_Final.log` e
`/tmp/opencode/usuarios-compilacao.txt`. Metadados de PDF podem variar entre
compilações, mesmo quando as estatísticas se reproduzem.

## Checklist

- [x] Protocolo autoral consultado integralmente antes da redação.
- [x] Planilha, abas, itens, escalas, consentimento e ausências inspecionados.
- [x] Procedência declarada e comparação com sintéticos locais documentadas.
- [x] Datas retificadas somente após autorização, com backup e auditoria.
- [x] Unidade de análise e ausência de autenticação individual explicitadas.
- [x] Estatísticas, gráficos, tabelas e narrativa confrontados.
- [x] Categorias de não tentativa/impossibilidade separadas de neutralidade.
- [x] Resultados desfavoráveis e limitações mantidos.
- [x] Análise qualitativa executada, sem depoimentos fabricados ou alegação de dupla codificação.
- [x] Versão pública anterior às correções distinguida da versão de desenvolvimento.
- [x] Resumo, abstract, método, resultados, discussão e conclusão atualizados.
- [x] Rastreabilidade e checklist do TCC atualizados.
- [x] Compilação, referências cruzadas e inspeção das páginas concluídas.
- [x] Código funcional, classe UPF e evidências históricas preservados.
- [x] Nenhum envio ao Forms, deploy ou operação de publicação Git.
- [ ] Aprovação substantiva do autor da codificação, trechos e interpretação.
- [ ] Confirmação de ética e regras institucionais de declaração da assistência.
- [ ] Commit público, fuso e encerramento formal da coleta documentados.
- [ ] Leitura integral complementar das referências cujo acesso foi limitado.

## Assistência de IA

Atividade executada com GPT-6.1 Sol (OpenAI), no OpenCode, sob solicitação do
autor: inspeção, scripts, cálculos, gráficos, codificação semântica proposta,
redação e validação. Não houve segundo pesquisador independente ou autenticação
do painel Forms. Os dados e o manuscrito não foram enviados às fontes
bibliográficas consultadas. A assistência não substitui responsabilidade
intelectual, aprovação do autor ou apreciação do orientador.
