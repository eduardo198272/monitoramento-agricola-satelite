# Auditoria e atualização do relatório final

> **Registro histórico.** A revisão acadêmica posterior está documentada em
> [REVISAO_TCC.md](REVISAO_TCC.md) e
> [ANALISE_TECNICA_TCC.md](ANALISE_TECNICA_TCC.md). Estado vigente: base `b7c325c`
> com correções locais, 710 testes e demonstração real com downloads.
> O autor confirmou Carlos Amaral Holbig como orientador e informou que os estudos
> por cultura não foram realizados. As descrições abaixo preservam as condições
> e pendências da auditoria anterior, sem substituir o estado da nova redação.

> Revisão de 15/11/2026: texto e diagramas alinhados ao software `a9a9677`.
> A classe atual é `CC-EC_TF-TC.cls`; `upf-ccc.cls` e `Proposta.tex` são históricos.
> As alterações atuais não encerram a redação acadêmica ou a avaliação agronômica.

Escopo atual: inspeção de código e documentos, execução da suíte automatizada e
verificação mínima do Earth Engine com conta de serviço. O ponto de entrada do
relatório é `Relatorio_Final.tex`, usando `CC-EC_TF-TC.cls` e `referencias.bib`.
A proposta original permanece separada. Não foi verificada publicação no
Streamlit Cloud nem execução agrícola ponta a ponta.

## Classificação por evidência

“Verificada” indica somente o aspecto e o limite documentados. Na revisão
`a9a9677`, o comando `COVERAGE_CORE=ctrace .venv/bin/python -m pytest -q`
aprovou 677 testes, com 100% de cobertura de linhas e ramificações em `src/app`.
O teste remoto confirmou inicialização, `1 + 1 = 2` e leitura do tamanho de uma
coleção Sentinel-2 limitada a uma imagem. Comandos, ambiente e limites estão em
`docs/validation/streamlit-cloud-readiness.md`; credenciais não foram versionadas.

A ausência de `pandas` registrada na auditoria inicial foi um bloqueio daquele
ambiente, superado pelo uso da `.venv`. As contagens de 307 e 309 testes nos
registros anteriores permanecem históricas, não representam a suíte atual.

| Funcionalidade | Classificação | Evidência e limite |
|---|---|---|
| Anomalias por janela e tendência | Implementada e verificada em testes locais | `src/app/anomalies.py`, `tests/test_anomalies.py`: casos sintéticos e desvio zero; sem validação de eficácia agronômica. |
| Seleção das bandas para índices e máscara | Implementada e verificada parcialmente | `src/app/earth_engine.py`, `tests/test_earth_engine.py`: testes conferem chamadas simuladas; não verificam resultados numéricos remotos. |
| Composição visual do PDF | Implementada e verificada parcialmente | `docs/validation/export-pdf-visual-review.md`: revisão de 20/10/2026 com dados sintéticos e serviços simulados; não comprova mapas reais. |
| Conta de serviço e catálogo Sentinel-2 | Acesso básico verificado com serviço real | Inicialização, cálculo simples e consulta limitada descritos no registro atual; não validam processamento espectral ou mapas. |
| Consulta Earth Engine, máscaras, índices e séries com imagens reais | Implementada, mas verificação operacional e numérica independente pendente | `earth_engine.py`, `pipeline.py`, `time_series.py`; não foi localizada evidência estruturada de execução atual dos casos agrícolas. |
| Integração NASA POWER e interpretação conjunta | Implementada, mas verificação operacional atual pendente | `climate.py`, `pipeline.py`, `tests/test_climate.py`; chamada real e unidades da resposta ainda devem ser registradas. |
| Interface, desenho e mapas com serviços externos | Implementada, mas verificação operacional atual pendente | `main.py`, `maps.py`, `map_interaction.py`; testes isolados não comprovam integração atual com provedores. |
| Exportação CSV ZIP/XLSX/PDF | Implementada e verificada com dependências simuladas | `export_*.py` e testes correspondentes; verificação ponta a ponta com dados reais e disponibilidade dos mapas permanece pendente. |
| Localizações SQLite, sessões e GeoJSON | Implementada e verificada em testes | Ida e volta, validação, conflitos sem importação parcial e isolamento, incluindo widgets reais com a fronteira EE substituída; não há login de visitantes ou persistência automática na web. |
| Streamlit Community Cloud | Código preparado; publicação não verificada | `streamlit_app.py`, `.streamlit/config.toml` e `docs/deploy-streamlit.md`; resolução de dependências não substitui instalação e execução no Cloud. |
| Validação por soja, milho e pastagem | Planejada; execução real documentada não localizada | `docs/validation/scenarios.md` e `validate_scenarios.py` descrevem protocolo; sem JSON de resultados no diretório verificado. Confirmar culturas e geometrias. |
| Dados de campo, diagnóstico causal, comparação com sistemas e estudo de usabilidade | Não demonstrados; possíveis avaliações futuras, não entregas reivindicadas | Nenhuma evidência suficiente identificada nesta auditoria. |

## Divergências e riscos

- Orientador: `Proposta.tex` informa Rafael Rieder; `docs/report-andamento-tcc.md` informa Carlos Amaral Holbig. `Relatorio_Final.tex` não fixa um orientador e mantém confirmação pendente; nenhum dos nomes foi validado nesta revisão.
- A proposta classifica NDMI como futuro e exclui banco; o código possui NDMI B8A/B11 e SQLite local. Na web, usa memória por sessão e transferência GeoJSON, sem banco externo, login ou armazenamento de análises. A proposta não foi reescrita como se descrevesse o estado atual.
- O diagrama anterior incluía exclusão de localizações como ação de interface. Essa operação existe no serviço, mas não aparece na interface atual; o diagrama foi corrigido e inclui importação/exportação GeoJSON.
- O site ainda não foi publicado nesta verificação. A conta de serviço autentica o servidor perante o Earth Engine; não é login Google para visitantes. As cotas do projeto são compartilhadas.
- NDWI implementado é B8/B11 e NDMI é B8A/B11; ambos usam NIR–SWIR. A terminologia específica NDMI requer fonte adicional. Gao não é apresentado como validação direta da substituição de bandas Sentinel-2.
- O filtro de data final do Earth Engine é exclusivo; revisar a correspondência temporal com NASA POWER em experimentos. O limite de nuvem padrão usa comparação estrita e metadado do produto, não percentual local.
- QA60 tem mudanças de disponibilidade entre 2022 e 2024, conforme o catálogo oficial; o código não aplica uma máscara específica de sombras. Confirmar efeitos por período e área.
- A redução é solicitada a 10 m apesar da resolução nativa de 20 m de B8A e B11; registrar projeção, reamostragem e efeitos ao reproduzir resultados.
- O protocolo de cenários descreve quadrados de 1,0/0,7/0,5 km, mas também áreas sugeridas maiores; não tratar essas descrições como equivalentes. A cultura nas coordenadas não foi confirmada. Critérios esperados não são observações.
- A documentação existente e as legendas de figuras da proposta não são evidência automática de origem de dados ou de experimentos; figuras da proposta não foram reutilizadas no relatório final sem rastreamento adicional.

## Referências e pendências

A auditoria inicial registra consulta ao catálogo Sentinel-2, às documentações
`ee.Image.normalizedDifference`, `ee.Filter.date` e NASA POWER Daily, e
conferência no Crossref de Gao (1996), Gorelick et al. (2017) e Weiss et al. (2020).
Esses registros foram preservados, sem atribuir nova conferência integral a esta
revisão. A bibliografia inclui os trabalhos relacionados acrescentados na
redação local e as fontes oficiais de conta de serviço, uso não comercial e
Secrets do Streamlit consultadas durante a preparação do deploy. Datas antigas
de acesso não foram atualizadas por suposição.

A referência Rouse (1973) já está no `.bib`, mas a consulta independente dos seus metadados não foi concluída; não foi citada na nova redação. A referência específica para NDMI/B8A-B11 ainda precisa ser localizada e verificada. Hevner et al. não foi inserido nem se declarou adoção formal de DSR: a adequação metodológica e o protocolo ainda não foram estabelecidos.

Na integração de `Estrutura_Artigo_TCC_Monitoramento_Agricola.md`, foram conferidos os registros e resumos institucionais de Slaiffer, Lovato e Chaves e a página do periódico e o registro Zenodo de Araujo et al. A redação limita-se ao que esses resumos e registros sustentam; a leitura integral das obras permanece necessária para aprofundar a comparação. O registro da UFLA apresenta data de 2019, mas sua seção de citação contém 2018; utilizou-se provisoriamente 2019, pendente de conferência na tese. Os resultados numéricos citados pertencem aos estudos referenciados, não a este sistema. A comparação funcional detalhada com outras plataformas permanece pendente.

Em 15/11/2026, as páginas institucionais de Slaiffer e Lovato e o registro Zenodo
de Araujo et al. foram novamente consultados: os resumos sustentam os recortes e
os números citados no texto. A página da UFLA não respondeu dentro do tempo
limite desta revisão; a ressalva anterior sobre o ano de Chaves permanece.
Não se declarou leitura integral dessas obras ou nova confirmação do ano da tese.

## Evidências necessárias

1. Manter a execução dos testes e o registro de revisão, ambiente, comando e cobertura atualizados quando o software mudar; o registro atual identifica os testes simulados e o teste remoto mínimo.
2. Conferir por cálculo independente os três índices e casos de máscara/dados ausentes; documentar o comportamento com imagens ou entradas controladas no Earth Engine.
3. Executar fluxo autenticado com AOIs e culturas confirmadas; preservar geometria, período, versões, coleção, filtros, datas de aquisição, resultados, gráficos, clima e erros.
4. Verificar efeitos da máscara, das resoluções, da escala e das datas e justificar critérios de comparação; não inferir causalidade ou validação de campo de coerência visual.
5. Confirmar modelo final, orientador, referências específicas e quais avaliações complementares são viáveis; redigir resultados e conclusões depois das evidências.

## Compilação

Na auditoria original não havia compilador no PATH. Na revisão de 15/11/2026,
o Tectonic 0.17.0 foi obtido da distribuição oficial em diretório temporário,
sem alterar a classe institucional. O comando, executado em `docs/artigo_final`,
foi:

```sh
/tmp/opencode/tectonic --keep-logs --outdir /tmp/opencode/article-build Relatorio_Final.tex
```

O PDF foi regenerado com sucesso, com nove páginas em papel Letter. Não foram
encontrados avisos de citações ou referências indefinidas, rótulos duplicados
ou caracteres ausentes no log final. A inspeção visual preliminar das páginas
e dos diagramas não substitui revisão editorial com o orientador.

Persistem avisos de carregamento de fontes e caixas subpreenchidas, além de uma
caixa de cabeçalho excedendo a largura interna em 54,64 pt, associada à classe
institucional na primeira página; essa classe foi preservada. O endereço longo
do cabeçalho e a opção Letter devem ser revisados na preparação da entrega.
O PDF do modelo anterior permanece somente como backup histórico local e não
integra este versionamento.
