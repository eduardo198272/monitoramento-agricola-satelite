# Pesquisa de experiência de uso

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
  Solicitar ao autor uma cópia do instrumento completo e dos cabeçalhos exportados.

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

Não há dataset real fornecido nem estatísticas oficiais calculadas. Os dois testes
em `tests/test_user_survey_analysis.py` usam somente dados sintéticos embutidos,
sem participantes reais. O script exige natureza explícita e impede saída sintética
sob `artigo_final`. Ainda cabe ao responsável conferir a origem de qualquer CSV.
Permanecem pendentes: instrumento completo, dados reais, análise temática,
gráficos, limitações observadas e revisão com orientador.
