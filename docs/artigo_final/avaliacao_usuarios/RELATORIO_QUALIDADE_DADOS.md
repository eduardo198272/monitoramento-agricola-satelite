# Qualidade, procedência e retificação dos dados

## Fonte preservada e autorização

Planilha recebida: `docs/Respostas – Avaliação da plataforma agrícola – TCC UPF.xlsx`.
O autor confirmou nesta atividade que todos os registros devem ser considerados
reais e, depois, solicitou corrigir os dias 16 e 17 para 15/11/2026.
A instrução de preservar o original foi atendida mediante cópia byte a byte
**antes** da retificação expressamente autorizada.

| Versão | SHA-256 |
|---|---|
| Recebida, backup privado imutável | `d61b9f11514f8d42f276abdb3e4e173782955c468fb50d774680032d342ce48a` |
| Corrigida e usada na análise | `9adb66b330103ca858c37d7dc6cdb5e4e954f09f749a0c122fa6e6b2f4f5de59` |

Backup: `dados_originais/respostas_recebidas.xlsx`; auditoria por célula:
`privado/retificacao_datas.json`. Pastas ignoradas por Git. Sete células da
primeira coluna foram alteradas; horários e as outras 49 colunas foram
comparados e preservados. Não houve reordenação de linhas. A análise posterior
não regrava a planilha.

Os metadados do XLSX recebido identificavam openpyxl e criação em 15/11/2026,
enquanto sete carimbos apontavam 16/17. Isso motivou a pendência inicial;
o autor atribuiu a diferença a erro de digitação e autorizou a retificação.
Metadados de edição não certificam nem refutam autenticidade das respostas.
Não há mais datas posteriores ao dia 15 no recorte corrigido. Fuso e data
formal de encerramento não foram informados.

## Inventário e triagem

| Verificação | Resultado |
|---|---:|
| Abas | 2 |
| Aba de respostas | 31 registros, 50 colunas |
| Aba `Página1` | Vazia |
| Consentimento/maioridade/leitura conjuntos: Sim | 31 |
| Exploração de pelo menos um recurso: Sim | 31 |
| Duplicatas exatas | 0 |
| Correspondências integrais sem carimbo | 0 |
| Excluídos por triagem | 0 |
| Submissões elegíveis para análise descritiva | 31 |
| Campos discursivos preenchidos | 142 |
| Comentários opcionais ausentes | 13 |
| Campo de impedimento de acesso vazio | 31 |

Não há campos fechados vazios neste recorte, mas há impossibilidade de
avaliação, que não é ausência nem neutralidade. A utilidade de gerenciamento
de áreas e consulta por pixel tem oito `Não consegui avaliar` cada. A partição
por coluna, incluindo todas as ausências, está em `resultados/qualidade.json`.

Não se prova que as 31 submissões correspondam a 31 pessoas diferentes.
Não se tentaram inferir identidades a partir dos horários ou das respostas.
Apenas inexistência de duplicatas não comprova independência.

## Classificação de procedência

| Categoria operacional | Registros | Fundamento |
|---|---:|---|
| Reais por declaração do autor | 31 | Confirmação expressa para a planilha fornecida |
| Sintéticos identificados entre os recebidos | 0 | Sem correspondência com fixtures de pesquisa locais |
| Sem confirmação na classificação operacional | 0 | A declaração abrange todos os registros desta fonte |

**Não confundir a classificação com verificação externa.** Não houve acesso
ao painel de respostas do Forms, logs de submissão ou lista autenticada de
respondentes. A procedência foi declarada, não certificada independentemente.

A busca no repositório identificou os exemplos de
`tests/test_user_survey_analysis.py`: cabeçalhos mínimos `consent`/`score` e
`ok`/`tools`/`comment`/`profile`, sem o instrumento de 50 colunas. O único texto
discursivo distintivo, `Comentário sintético`, não aparece na planilha.
Nenhuma dessas fixtures foi importada na análise. Matrizes de compressão e
snapshots sintéticos dos testes da plataforma não são bases de participantes.
O alcance é o material disponível no repositório, não fontes externas desconhecidas.

## Consistência interpretativa

- O item de conhecimento é agricultura de precisão, não teste de sensoriamento remoto.
- Séries/anomalias e relatório/dados aparecem agrupados nas tarefas; não foram
  criadas taxas artificiais para subfunções.
- Avaliar facilidade ou utilidade não exige, neste instrumento, comprovação
  observada de sucesso na tarefa. Existem não tentativas e avaliações em outros
  itens; isso é mantido e tratado como limite do autorrelato, não fraude.
- Algumas respostas mencionam comparação lado a lado, alertas por cores e
  estação meteorológica, que não são confirmados na implementação inspecionada.
  Podem expressar expectativas, interpretação ou confusão; não são provas de
  implementação e não foram motivo de exclusão discricionária.
- Não foram investigadas culturas, produtividade, doenças ou condições de
  propriedades dos respondentes. Alegações agronômicas nos comentários são
  opiniões, não resultados de campo.

## Validação executada

`scripts/validar_resultados.py` confronta 40 itens fechados e 191 categorias
com a planilha por Counter/statistics, independentemente das funções de análise
pandas/NumPy. Conferiu notas, quartis, frequências, percentuais, retificação e
28 hashes dos módulos funcionais da demonstração. O resultado detalhado está
em `resultados/validacao.json`. Oito testes sintéticos isolados verificam
ausência, impossibilidade, tentativas, triagem, duplicatas, extremos, novos
textos e supressão de grupos pequenos. Não são participantes adicionais.

## Pendências

- Aprovação pelo autor da codificação temática e da interpretação.
- Identificador da revisão pública e documentação do período efetivo de coleta.
- Confirmação institucional de ética, citações e declaração de assistência de IA.
- Validação externa da independência, se o autor dispuser de evidência adequada,
  sem coletar/publicar identificadores desnecessários retrospectivamente.
- Apreciação de privacidade antes de qualquer publicação da planilha completa.
