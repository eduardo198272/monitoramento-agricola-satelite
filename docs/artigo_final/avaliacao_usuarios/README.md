# Avaliação da plataforma com usuários

**Quarta rodada:** conjunto definitivo de **32 respostas**, com coleta concluída. Fonte: snapshot público SHA-256 `c9c267230e803a8aa09073c438ff6264de3a597a3e7478aacfd979026c245a34`, escolhido expressamente pelo pesquisador após comunicação de que a fonte dinâmica já continha 33 registros. Os 40 itens, 191 categorias, seis cruzamentos e nove gráficos foram reprocessados. Média 7,72, mediana 8, DP amostral 1,78. A resposta incluída não preencheu os campos abertos: 142 células e 13 temas mantidos após conferência, percentuais por 32 submissões. Ver `../evidencias/quarta_rodada/` e [pendências vigentes](../auditoria_cientifica/PENDENCIAS_AUTOR.md).

Análise de **32 submissões elegíveis ao questionário de avaliação com usuários**,
preservadas em `privado/snapshot_publico_32.xlsx` (arquivo privado ignorado pelo Git).
A versão pública avaliada antecede as correções locais. Os dados são
apresentados de forma agregada, sem identificação individual.

- [Metodologia](METODOLOGIA.md)
- [Qualidade, procedência e retificação autorizada](RELATORIO_QUALIDADE_DADOS.md)
- [Resultados quantitativos e qualitativos](RESULTADOS.md)
- [Validação final, PDF e pendências de aprovação](VALIDACAO_FINAL.md)
- [Instrumento mapeado](instrumento.json): todas as 50 colunas, categorias
  observadas e âncoras das escalas; não confundir colunas com perguntas independentes.
- [Codificação discursiva](codificacao.json): definições, trechos selecionados e
  vínculo por hash dos cinco textos normalizados, sem perfis, notas ou carimbos.
- `resultados/`: tabelas CSV, frequências completas, cruzamentos, indicadores e
  tabelas LaTeX. Nenhuma linha de respostas individuais é exportada.
- `figuras/`: nove gráficos em PDF e SVG vetoriais e PNG a 300 dpi. O artigo
  seleciona perfil, tarefas e usabilidade; os demais são complementares.

## Executar na raiz do repositório

Usar o ambiente do projeto com pandas, NumPy, openpyxl e Matplotlib:

```sh
.venv/bin/python docs/artigo_final/avaliacao_usuarios/scripts/analisar_respostas.py \
  --input "docs/artigo_final/avaliacao_usuarios/privado/snapshot_publico_32.xlsx"
.venv/bin/python docs/artigo_final/avaliacao_usuarios/scripts/gerar_tabelas.py
.venv/bin/python docs/artigo_final/avaliacao_usuarios/scripts/gerar_graficos.py
.venv/bin/python docs/artigo_final/avaliacao_usuarios/scripts/validar_resultados.py
.venv/bin/python -m pytest -q -o addopts='' -p no:cacheprovider \
  docs/artigo_final/avaliacao_usuarios/scripts/test_analise.py
```

Os scripts de análise não alteram a planilha. As estatísticas, os gráficos,
as tabelas e `RESULTADOS.md` são regenerados. Os indicadores LaTeX são lidos
pelo artigo. A narrativa interpretativa precisa ser revista após atualizações:
não há publicação automática de conclusões ou novas respostas.

Para novas submissões, conferir novamente procedência e duplicidades. Textos
novos não recebem códigos por aproximação: ficam pendentes até leitura e
atualização explícita de `codificacao.json`. Mudança de cabeçalhos interrompe
a análise para revisão do mapeamento. O validador da retificação refere-se ao
recorte recebido nesta atividade; uma base ampliada exige atualizar a auditoria,
não remover as verificações.

Um hash de fonte diferente do recorte confirmado interrompe a análise antes de
sobrescrever resultados. Para uma fonte atualizada, usar
`--confirmar-procedencia` **somente após nova confirmação do responsável**.
Esse parâmetro controla a atualização da fonte utilizada na análise. O snapshot32 está preservado privadamente; uma nova exportação da fonte dinâmica pode conter mais respostas e não deve substituí-lo automaticamente.

## Retificação já executada — não repetir

O autor confirmou erro de digitação nos dias 16 e 17/11/2026 e autorizou ambos
para 15/11/2026. `scripts/corrigir_datas.py` alterou somente sete células de
carimbo, preservando horários e respostas. A cópia byte a byte recebida está em
`dados_originais/respostas_recebidas.xlsx`, e os detalhes por célula em
`privado/retificacao_datas.json`. Ambos os diretórios são ignorados por Git.
O script se recusa a sobrescrever o backup e não é parte da rotina de análise.

A antiga cópia de trabalho corrigida foi excluída por autorização do autor após
a terceira rodada; o original privado permanece. Não publicar planilhas ou auditorias individuais sem
revisão específica de privacidade; ausência de nome/e-mail não garante anonimato.

## Limites

O delineamento é descritivo, com adesão voluntária e respostas autodeclaradas.
Não se atribuem SUS/TAM/UTAUT/NPS ao
instrumento, eficácia agronômica, redução de custos ou desempenho cronometrado.
A codificação e a interpretação assistidas por IA dependem de aprovação
substantiva do autor e das orientações institucionais.
