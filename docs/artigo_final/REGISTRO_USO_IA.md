# Registro de uso de inteligência artificial

## Quarta rodada — 16/11/2026

Assistência por GPT-6.1 Sol no OpenCode: conferência do snapshot público e original privado, reprocessamento quantitativo/qualitativo, geração de tabelas e gráficos, atualização pontual do artigo, pesquisa e confronto de três publicações primárias, revisão de declarações/documentos e validação de compilação/páginas. A assistência continua substantiva; não foi limitada à gramática.

Instrução literal: “Não presumir que a inclusão da resposta adicional manterá os resultados anteriores.” A fonte pública passou a conter33, e a opção escolhida pelo pesquisador na pergunta de esclarecimento foi “Snapshot de 32 respostas”. Foi recuperada e validada a exportação anterior32, sem reconstruir ou editar a planilha.

A atribuição temática adicional é vazia porque os cinco campos estão vazios; nenhuma resposta ou interpretação foi criada para preenchê-los. Categorias e atribuições anteriores foram preservadas; não se presumiu leitura/aprovação humana da nova redação. A declaração específica e as menções metodológicas necessárias foram mantidas; repetições foram removidas dos resumos e das legendas.

Não foram executados novos experimentos da aplicação nem recebidas evidências complementares do detector. Houve somente validação documental e do código de análise estatística. Sem commit, push, deploy ou assinatura.

## Terceira rodada — 15–16/11/2026

Continuidade por GPT-6.1 Sol no OpenCode: leitura integral do protocolo, documentos e artigo; confronto de código e evidências; consulta dirigida de fontes pendentes; recomputação do recorte público; **reformulação substancial de parágrafos e da discussão**, síntese de ressalvas, seleção editorial de figuras, tradução do resumo, atualização de declarações/auditorias e preparação assistida de banca/defesa. Compilação e inspeção de páginas são assistidas, não aprovação visual humana.

Instrução literal da solicitação atual:

> O artigo deve comunicar a pesquisa realizada, e não narrar o processo de revisão científica pelo qual passou.

Diretriz autoral prioritária da mesma mensagem:

> O artigo não é uma avaliação externa do pesquisador. É a apresentação científica da pesquisa realizada pelo próprio pesquisador, sob sua responsabilidade intelectual e acadêmica.

Esses excertos provêm desta conversa, não foram reconstruídos como prompts históricos. A mensagem integral permanece no histórico do projeto; não se inventou identificador de mensagem não consultado. A autorização editorial atual não comprova formalização institucional deIA. A aprovação qualitativa anterior foi preservada e não convertida em aprovação antecipada da nova redação.

Não houve novo experimento com a aplicação, commit, push ou deploy. Recalcular estatísticas já disponíveis e compilar documentos não foi descrito como nova execução de teste da aplicação. Não se geraram respostas, dados de campo, figuras espectrais medidas ou assinaturas. As pendências institucionais e de identificação histórica de “Luna” permanecem abaixo.

Atualização: 15/11/2026. **Registro retrospectivo baseado em evidências existentes e declaração do autor; não é um diário contemporâneo completo.** A revisão atual ainda exige leitura e aprovação humana. A assinatura não foi simulada.

## Ferramentas e identificadores

Foi consultada a API local do OpenCode (`GET /api/session`, filtrada pelo diretório deste projeto), usando a documentação oficial de API. A instalação responde `opencode v2.3.0`; isso não determina versões históricas.

| Evidência | Identificador registrado | Alcance |
|---|---|---|
| `ses_e34528856ffe6NfqlLR6yl60oo` | `openai/gpt-6.1-terra` | Sessão do projeto: verificação de material para artigo |
| `ses_e2e01a217ffekAm1RXafBH8cb0` | `openai/gpt-6.1-terra` | Sessão do projeto: organização de pastas |
| `ses_e2a5885b7ffelMbnE0RLzCNHJD` | `openai/gpt-6.1-sol` | Sessão do projeto: aplicação |
| `ses_e20ba7f84ffeHY9BMnCHj89NXj` | `openai/gpt-6.1-sol` | Sessão com revisão do artigo e execução atual |
| Declaração do autor nesta rodada | “ChatGPT 6 - Luna” | Não localizado vínculo do modelo com sessão deste projeto no recorte consultado |

Os metadados de sessão não provam que somente o modelo atual da sessão foi utilizado em todo seu histórico. Não certificam o nome comercial do fornecedor. Os registros completos permanecem locais para preservar dados e instruções privadas.

## Finalidades e resultados

| Etapa | Assistência efetivamente registrada | Supervisão / evidência |
|---|---|---|
| Requisitos e SDD | Especificações, critérios, planos e decomposição de tarefas | `docs/specs/index.md`, `spec-*.md`, `tasks-*.md`; commit `733e402` introduz estrutura SDD; `0c676d9` registra especificações de exportação e áreas salvas |
| Implementação | Geração/revisão de código, testes e documentação | Histórico Git, PRs de integração, `docs/validation/`; autor confirma decisões técnicas e arquiteturais |
| Verificação | Execução assistida de suíte, regressões, serviços reais e navegador | Evidências históricas distinguem simulações e demonstração real; não foram criados novos resultados de execução da aplicação nesta rodada |
| Questionário | Scripts quantitativos, leitura e codificação multirrótulo, agrupamento, tabelas e gráficos | `avaliacao_usuarios/scripts/`, `codificacao.json`; 142 células / 13 temas; aprovação qualitativa declarada pelo autor nesta rodada |
| Artigo | Geração e reformulação substancial, organização, revisão gramatical/didática e tradução do resumo | Diffs Git `1862dd7`, `f31d0a5`; não se reduz o uso a correção ortográfica |
| Auditoria | Pesquisa bibliográfica, conferência assistida de fontes/equações, originalidade preliminar, registro de lacunas | `auditoria_cientifica/`; os acessos de IA não certificam leitura direta de todas as fontes pelo pesquisador |
| Figuras e PDF | Diagramas, preparação de capturas, compilação e triagem visual | Fontes TikZ, scripts e manifestos; capturas fornecidas pelo autor não são imagens sintéticas |

## Prompts recuperados

Fonte: mensagens `type=user` da sessão do projeto. Excertos literais, com identificador para recuperação; não reconstruídos a partir de respostas da IA:

1. `msg_1e0f1bee5001QnNu3YHb8uvtC7`:
   > Antes de consolidar os resultados, verifique a procedência dos registros e eventuais correspondências com bases sintéticas existentes no projeto. Separe registros comprovadamente reais, sintéticos e de procedência não confirmada.
2. Mesma mensagem:
   > Diferenciar execução autodeclarada de uma avaliação observacional conduzida em ambiente controlado.
3. `msg_1e1f9356f001lL77wG8k7hQ4Rx`, PA03:
   > Não atribuir esses limiares a de Jong et al.
4. Mesma mensagem, restrições:
   > Não converter automaticamente os nomes informados pelo autor em nomes comerciais oficiais sem evidências.

A mensagem sobre avaliação já solicita análise quantitativa e qualitativa, critérios e limites; não comprova que as treze categorias específicas tenham sido fixadas antes da leitura do corpus. A metodologia histórica registra agrupamentos definidos a partir dele. O autor confirma planejamento prévio da **estratégia**, não se converte isso em pré-registro das categorias. Não se encontrou protocolo datado que certificasse pré-registro.

## Normativa e encaminhamentos

Íntegra da IN nº 03/2026/PROACAD e anexo obtidos no portal oficial da UPF. URL e hash constam da evidência da rodada; cópia de consulta em `/tmp/opencode/revisao-final-pa/IN_03_2026_PROACAD.pdf`. A minuta `DECLARACAO_USO_IA.tex` usa os quatro campos do anexo e os dois parágrafos finais de declaração, sem assinatura.

| Artigos | Ação / evidência | Ainda necessário |
|---|---|---|
| 3º | Registro de ferramentas, limites e responsabilidade; nenhuma nova resposta gerada | Consulta direta e revisão crítica pelo autor; comprovação de autorização para dados inéditos e avaliação de privacidade |
| 4º | Autor relata ciência do orientador e orientações institucionais | Documento formal estabelecendo autorização, finalidades, limites e condições |
| 5º e 10 | Declaração explicita geração/reformulação substancial e análise; não apresenta como redação humana sem assistência | Conferência de completude pelo autor e orientador |
| 6º | Declaração no artigo e minuta independente conforme anexo | Revisar, completar e assinar após aprovação real |
| 7º | Responsabilidade do autor preservada | Acompanhamento e validação institucional do orientador |
| 8º | Preparada informação a ser entregue | Comprovante de comunicação à banca |
| 11 | Sem afirmação de regularidade automática | Eventual apreciação cabe à UPF, não ao agente |

Não houve contato com orientador, CEP, ProAcad ou banca por esta ferramenta. Nenhum manuscrito ou resposta individual foi enviado a ferramentas antiplágio. As consultas bibliográficas usaram temas, títulos, DOIs e URLs públicos, não o manuscrito inédito completo.
