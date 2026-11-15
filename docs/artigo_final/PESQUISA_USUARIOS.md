# Pesquisa de experiência de uso

## Atualização com a planilha recebida

A avaliação foi executada sobre 31 submissões elegíveis, declaradas reais pelo
autor, da planilha `docs/Respostas – Avaliação da plataforma agrícola – TCC UPF.xlsx`.
O autor autorizou retificar sete carimbos de 16/17 para 15/11/2026; a cópia
recebida e as respostas foram preservadas. A unidade é submissão, não pessoa
independentemente autenticada. A análise refere-se à versão pública anterior
às correções, sem deploy. Documentação e comandos atuais:
[avaliação com usuários](avaliacao_usuarios/README.md).

Os procedimentos genéricos abaixo são o protocolo de preparação da rodada
anterior; os scripts XLSX, escalas mapeadas e resultados atuais estão na pasta
acima. Não usar o exemplo CSV como instrumento desta coleta.

## Instrumento e alcance

- Formulário: https://forms.gle/VXqtdCgH9us774VE6
- Plataforma: https://eduardo198272-monitoramento-agricola-satel-streamlit-app-q0mow9.streamlit.app/
- Objetivo: experiência, clareza, usabilidade e utilidade percebida; não validação agronômica.
- Público: agrônomos, produtores, técnicos, pesquisadores, estudantes e profissionais de tecnologia/agronegócio.
- Divulgação informada: WhatsApp e LinkedIn; amostragem não probabilística por adesão.
- Primeira página verificada em 15/11/2026, somente por leitura: participação voluntária,
  maiores de 18 anos e concordância; não solicita nome/e-mail; orienta não inserir
  dados pessoais, explorar a plataforma antes e reservar 5–8 minutos para responder.
- Nenhuma resposta foi enviada e nenhuma resposta existente foi modificada.
- As perguntas posteriores à triagem não foram percorridas por envio do formulário.
  Seus cabeçalhos e categorias foram posteriormente mapeados na planilha recebida;
  regras de navegação/obrigatoriedade não foram autenticadas no editor Forms.

## Dados necessários e ética

Receber CSV real exportado pelo responsável, período de coleta, forma de divulgação,
instrumento completo, opções/escalas exatas e decisão de encerramento da coleta.
Conferir com orientador os procedimentos éticos institucionais aplicáveis. Não há
documento que permita atribuir aprovação CEP, protocolo ou dispensa formal.
Não armazenar respostas identificáveis no repositório público.

## Procedimento reproduzível

1. Preservar o CSV original em local privado, imutável; produzir cópia de trabalho.
2. Preencher `experimentos/pesquisa_config_exemplo.json` com cabeçalhos reais,
   coluna/valor de consentimento e definição de cada questão.
3. Tipos admitidos: `categorical`, `multiple` (com separador explícito), `ordinal`
   (dicionário rótulo→valor ordenado) e `open`. Não presumir escala 1–5.
4. Mapear perfil, conhecimento prévio, experiência similar, funcionalidades,
   facilidade, clareza, organização, desempenho, utilidade, relevância, intenção
   e avaliação geral **somente quando constarem efetivamente no instrumento**.
5. Executar:

```bash
python docs/artigo_final/experimentos/analisar_pesquisa.py \
  --input /caminho-privado/respostas.csv \
  --config /caminho-privado/mapeamento.json \
  --output /caminho-privado/analise --natureza reais
```

6. Conferir totais e denominadores do JSON contra a planilha antes de publicar.
   Revisar manualmente duplicações ou respostas incompatíveis; registrar critérios,
   sem exclusões discricionárias para favorecer resultados.
7. Produzir tabelas e gráficos de barras/Likert a partir das distribuições conferidas.
   O script atual prepara estatísticas, não gera gráficos finais automaticamente.

## Tratamento quantitativo

Separar recebidas, elegíveis e excluídas pela triagem. Para cada questão: número válido,
ausências, inválidas, “Não se aplica” e “Não consegui avaliar”. Frequências relativas
usam denominador válido da questão; seleção múltipla pode exceder 100% e repetições
da mesma opção por participante não são contadas duas vezes. Ordinais recebem
mediana, quartis e IQR com percentis NumPy; explicitar essa convenção no relatório.
Não calcular índices psicométricos ou chamar o instrumento de SUS/TAM/UTAUT.
Não fazer inferência populacional com esta amostra de adesão.

## Tratamento qualitativo

Ler integralmente; retirar identificadores pessoais; criar códigos a partir das
respostas; registrar definições/exemplos em livro de códigos; agrupar temas e
reexaminar casos divergentes. Incluir dificuldades e avaliações negativas.
O arquivo `abertas_PARA_ANONIMIZAR.json` é material **privado** de trabalho:
P001 etc. são pseudônimos, não garantia de anonimato do texto livre.
Revisar toda citação e risco de reidentificação antes de inserir no artigo.

## Integridade e pendências

Na rodada anterior não havia dataset fornecido. Agora há análise quantitativa,
codificação discursiva e gráficos da planilha, com procedência declarada pelo
autor e limites explícitos. Os dois testes antigos continuam sintéticos,
separados dos oito testes sintéticos da nova rotina XLSX e dos resultados
das 31 submissões. Permanecem pendentes a aprovação da codificação, o commit
público, encerramento/fuso da coleta e os procedimentos éticos institucionais.
