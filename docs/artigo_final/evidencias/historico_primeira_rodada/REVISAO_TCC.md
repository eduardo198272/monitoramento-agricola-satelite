# Relatório de evolução da redação científica

## 1. Identificação

Revisão de 15/11/2026, a partir de `b7c325c`, realizada exclusivamente em
documentação acadêmica. Orientador confirmado pelo autor nesta solicitação:
Prof. Carlos Amaral Holbig. Não houve commit, push, merge, refatoração ou mudança
funcional. O trabalho está na worktree `task/TCC-02-evolucao-redacao`.

## 2. Reposicionamento e organização

O relatório foi reposicionado como pesquisa aplicada e tecnológica em Ciência da
Computação, com plataforma computacional como resultado principal. A avaliação
considera implementação, contratos, testes e evidências disponíveis. Não exige
revalidar sensores ou produtos meteorológicos, nem infere validade agronômica.
Verificar equações, bandas, unidades e contratos de integração continua sendo
responsabilidade computacional da solução.

Mantiveram-se `Relatorio_Final.tex`, classe institucional `CC-EC_TF-TC.cls`,
configuração de autoria, modelo de duas colunas, bibliografia `dcu` e referências
cruzadas. Nenhuma classe institucional foi alterada. A proposta original e seus
capítulos permanecem preservados, inclusive o nome de orientador que constava
historicamente nela; a identificação atual é explicitada no relatório.

Estrutura final:
1. Introdução.
2. Fundamentação teórica.
3. Materiais e métodos.
4. Desenvolvimento e implementação (novo arquivo).
5. Apresentação da plataforma desenvolvida (novo arquivo).
6. Resultados da avaliação técnica.
7. Discussão.
8. Conclusão e trabalhos futuros.

Não foi acrescentado sumário de monografia a um modelo institucional de artigo
que não o possui. A divisão em oito seções preserva a separação já existente
entre resultados e discussão, sem forçar a numeração ilustrativa da solicitação.

## 3. Alterações por arquivo

| Arquivo | Alteração e justificativa |
|---|---|
| `Relatorio_Final.tex` | Inclui duas seções novas e macro de figuras; identifica orientador; controla encerramento de floats entre grandes seções |
| `final_0_resumo.tex` | Reescrita equivalente em português/inglês, com plataforma, avaliação real, contagem atual e limites |
| `final_1_introducao.tex` | Problema de integração computacional, justificativa sem alegações comerciais, objetivos OE1–OE8 e delimitação explícita |
| `final_2_fundamentacao.tex` | Amplia agricultura digital, índices, bandas, nomenclatura, agregações, mapas, séries e clima; diferencia serviços |
| `final_3_metodos.tex` | Pesquisa tecnológica, fontes de evidência, filtros, equações, parâmetros, estatística e avaliação |
| `final_3a_implementacao.tex` | Arquitetura, estados, persistência, consulta de grade, browser, cores e exportações em profundidade |
| `final_3b_plataforma.tex` | Apresentação técnica de todos os fluxos principais e 19 espaços de captura |
| `final_4_resultados.tex` | Resultado do artefato, suíte atual, limites dos testes e consulta pública de unidade NASA POWER |
| `final_5_discussao.tex` | Atendimento dos objetivos, evolução frente à proposta, defeitos/limitações e contribuição de engenharia |
| `final_6_conclusao.tex` | Síntese coerente com evidências; viabilidade condicionada, ausência de campo e prioridades futuras |
| `figuras_relatorio.tex` | Macro que mantém placeholder explícito e carrega automaticamente PNG real quando disponível |
| `fig/arquitetura_atual.tex`, `fig/fluxo_analise.tex` | Revisados para separar navegador, servidor e tipos de produto |
| `fig/fluxo_anomalias.tex`, `fluxo_areas.tex`, `fluxo_consulta_pixel.tex`, `fluxo_exportacao.tex` | Novos diagramas baseados no código |
| `fig/classes_localizacao.tex` | Preservado e reutilizado, sem alterar classes existentes |
| `referencias.bib` | Acrescenta fontes conferidas e corrige metadado de autor Amani/Crossref; preserva entradas históricas não confirmadas |
| `FIGURAS_PENDENTES.md` | Inventário CAP/DIA, contexto, arquivos, estados, dados, introdução e discussão por figura |
| `RASTREABILIDADE_TCC.md` | Objetivos originais/finais, requisitos iniciais/posteriores, funções, testes, figuras e status |
| `ANALISE_TECNICA_TCC.md` | Arquitetura, algoritmos, limitações e observações técnicas para futura tarefa funcional |
| `evidencias/nasa_power_unidades.json` | Resposta pública observada, formatada sem alterar valores; sem credenciais |
| `README.md` acadêmico | Atualiza estrutura, evidências e pendências desta redação |
| `auditoria-relatorio-final.md` | Acrescenta aviso de registro histórico e ponte para a revisão atual, sem reescrever evidências antigas |
| `Relatorio_Final.pdf` | Versão recompilada da redação atual; não é o relatório PDF exportado pela aplicação |

## 4. Conteúdos acrescentados

- Equações das três formulações, mediana por posição, reduções espaciais,
  janela móvel com desvio populacional, escore unilateral, agregações climáticas
  e localização de célula por transformação da grade.
- Diferença entre resolução nativa e escala nominal solicitada.
- `sampleRectangle`, NoData, UTM, float32, compressão, transferência e consulta
  local pelo cursor; dependências de browser e limites de volume.
- Estado da interface, snapshots e invalidação dos resultados/exportações.
- Centro da caixa delimitadora salvo versus centroide analítico do EE.
- Persistência SQLite, sessão e transferência atômica de locais.
- Estruturas efetivas de PDF/XLSX/CSV ZIP; quantidade depende dos índices.
- Limitações verificadas: unidade de radiação, legenda, resumo multiíndice,
  metadados de exportação individual, datas repetidas e parâmetros alterados.
- Rastreabilidade explícita da atividade original não realizada.

## 5. Conteúdos substituídos ou retirados da redação atual

- “Conclusão parcial” centrada em experimentos agrícolas a executar foi
  substituída por conclusão do artefato com evidências e limites. Não se retirou
  a ausência de avaliação ponta a ponta.
- Contagem de 677 foi substituída por 686 onde o texto descreve o estado atual.
  O registro anterior permanece identificado por versão e data.
- Promessa de estudos futuros por cultura como condição para existir resultado
  computacional foi substituída por delimitação transparente do escopo realizado.
- Métricas numéricas dos trabalhos relacionados, não reconferidas integralmente
  nesta sessão, foram retiradas do corpo e substituídas por comparação de escopo.
  Entradas bibliográficas e registros de auditorias anteriores foram preservados.
- Não se reutilizaram figuras antigas da proposta como se fossem capturas reais.
- Não se afirmam classes universais de vegetação saudável/seca, diagnóstico
  causal, validação dos sensores, baixo custo comprovado ou usabilidade demonstrada.

Nenhum arquivo da proposta ou fonte funcional foi removido. O BibTeX compartilhado
teve alteração pontual de autoria conferida e adições; as entradas da proposta
foram mantidas para não quebrar sua compilação.

## 6. Mudanças de escopo a apreciar pelo orientador

| Planejamento | Tratamento na redação final |
|---|---|
| Estudos em soja, milho e pastagem | Não realizados conforme autor; documentados explicitamente como mudança |
| Validação interpretativa com faixas esperadas | Não tratada como validação científica universal; script não prova cultura ou precisão |
| Ausência inicial de banco | SQLite local implementado e alternativa web de sessão |
| NDMI como trabalho futuro na proposta | Implementação adicional B8A/B11; diferença da menção ampla no V1.1 documentada |
| Interface e processamento essencial | Expansão para consulta local de grade, formatos de resultados e GeoJSON |
| Viabilidade/baixo custo | Evidência computacional condicionada; custo/latência/usabilidade sem avaliação própria |

O objetivo original não realizado não foi “compensado” pelas funcionalidades
adicionais. A matriz permite revisar cada item separadamente.

## 7. Revisão bibliográfica: fontes e grau de confirmação

“Verificado” abaixo não significa leitura integral do artigo, salvo indicação.
Datas de acesso antigas não foram reescritas por suposição. Documentação dinâmica
com ano 2026 já no BibTeX foi preservada; novas fontes sem data identificável
mantêm essa condição, em vez de inventar ano de publicação.

| Chave | Verificação nesta tarefa | Decisão/pendência |
|---|---|---|
| `ESA_SENTINEL2` | SentiWiki oficial consultada: instrumento, resoluções e revisita nominal | Mantida; não afirmar composição exclusivamente A/B em 2026 |
| `GOOGLE_S2_SR` | Catálogo consultado: bandas, escala, QA60, metadado de nuvens | Mantida; sustenta detalhes do produto |
| `GOOGLE_EE_ND` | Documentação consultada: fórmula, máscara de entrada negativa e propriedades | Mantida |
| `GOOGLE_EE_DATE` | Documentação consultada: início inclusivo/fim exclusivo | Mantida |
| `GOOGLE_EE_SERVICE_ACCOUNT` | Guia oficial consultado | Mantida; não equivale a login do usuário |
| `GOOGLE_EE_NONCOMMERCIAL` | Página oficial de tiers/cotas consultada | Mantida; condições de gratuidade delimitadas |
| `STREAMLIT_CLOUD_SECRETS` | Documentação oficial consultada | Mantida; não afirma deploy executado |
| `NASA_POWER_DAILY` | Documentação consultada e requisição pública curta | Mantida; parâmetros/unidades dependem de contrato real |
| `GAO1996` | DOI resolveu metadados de título, autor, periódico, volume/número/páginas | Mantida; não atribui validação B8/B11 ao original |
| `GORELICK2017` | Crossref confirmou título, seis autores, ano, volume e páginas | Mantida; não leitura integral nova |
| `WEISS2020` | Crossref confirmou título, autores em iniciais, ano, volume e número de artigo | Mantida; grafia expandida preexistente não foi inventada |
| `PATRICIO2018` | Crossref confirmou autores, título, periódico, volume/páginas | Mantida; menção limitada ao escopo de revisão |
| `AMANI2020` | Crossref confirmou metadados; nome de Mirmazloumi constava diferente | Corrigido para S. Mohammad Mirmazloumi, conforme registro; não inventar expansão |
| `PHIRI2020` | Tentativas de Crossref/página MDPI não concluídas nesta revisão | Entrada preservada, não citada no relatório atual; conferência integral pendente |
| `SLAIFFER2023` | Registro e resumo UFSM consultados; confirma TCC, autor e escopo | Mantida citação qualitativa; não afirmar leitura integral |
| `LOVATO2021` | Acesso UNESP expirou; auditoria anterior tem registro de consulta | Preservada, sem métrica nova; leitura/conferência integral pendente |
| `ARAUJO2025` | Acesso Zenodo expirou; auditoria anterior descreve consulta | Preservada, não citada como evidência quantitativa nesta redação |
| `CHAVES2019` | Acesso UFLA expirou; divergência 2018/2019 já registrada | Preservada, ano e texto integral pendentes |
| `ROUSE1973` | Registro NASA NTRS 19740022614 informa publicação em 1974, embora item existente use 1973 | Entrada histórica preservada; não usar metadado incerto como nova citação |
| `WAZLAWICK2014` | Edição e dados não reconferidos em fonte editorial nesta tarefa | Preservada; não citada na redação atual como protocolo executado |
| `WAZLAWICK2020` | Dados de edição/ano não reconferidos em fonte editorial nesta tarefa | Preservada para proposta; pendente |
| `MCFEETERS1996` (nova) | DOI confirmou autor, título, ano, periódico, 17(7), 1425–1432 | Incluída para distinguir água superficial; não é algoritmo implementado |
| `USGS_NDMI` (nova) | Página oficial descreve fórmula NIR–SWIR em Landsat | Incluída; não sustenta validação específica de B8A/B11 |
| `GOOGLE_EE_SAMPLE` (nova) | Documentação oficial consultada | Incluída; matrizes por banda/projeção |
| `GOOGLE_EE_MEDIAN` (nova) | Documentação oficial consultada | Incluída; mediana por pixel/banda |
| `GOOGLE_EE_REDUCE` (nova) | Documentação oficial consultada | Incluída; redução, escala e CRS |
| `NOMINATIM_POLICY` (nova) | Política OSMF consultada | Incluída; limites/atribuição/privacidade precisam ser observados |
| `ROUSE1974_NTRS` (nova) | Registro oficial NASA NTRS confirmou autores, título, tipo, volume/seção e publicação em 1974 | Incluída sem inventar paginação; entrada de 1973 permanece histórica, pendente de cotejo entre edições |

Registro NASA consultado:
<https://ntrs.nasa.gov/citations/19740022614>.
O ano do evento e o da publicação devem ser distinguidos antes de corrigir a
entrada histórica compartilhada. Não foram inventados DOI, páginas ou edições.

## 8. Verificações realizadas

### Software

- Suíte existente: 686 aprovados em 12,06 s; 100% de cobertura em `src/app`,
  2.669 instruções e 834 ramificações.
- Comando e ambiente completos: `ANALISE_TECNICA_TCC.md`, seção 12.
- Nenhum novo teste funcional foi criado e nenhuma validação de cultura foi
  executada. Além da consulta NASA POWER, houve reprodução local de seu campo de
  radiação com `summarize_climate_data`: média independente 21,315, resumo
  implementado 76,734, razão 3,6. Sem nova chamada de rede ou inicialização EE.
- Nenhuma alteração em `src/`, `tests/`, dependências, configuração de execução
  ou ponto de entrada web.

### Documentação

- Compilação com Tectonic 0.17.0 disponível em `/tmp/opencode/tectonic`,
  intermediários/logs fora do repositório.
- Verificação de citações existentes no BibTeX, rótulos/referências, arquivos
  incluídos e correspondência entre 19 espaços CAP e o inventário.
- `git diff --check` para espaços/conflitos.
- Revisão visual por rasterização do PDF; estado final e alertas editoriais
  registrados na seção de fechamento abaixo.

## 9. Pendências exclusivas do autor/orientador

1. Fornecer capturas reais CAP-01–19 e identificar área autorizada, parâmetros e
   revisão; confirmar eventual cultura apenas se houver evidência independente.
2. Aprovar delimitação tecnológica e alteração do objetivo de estudos por cultura.
3. Confirmar mês da defesa e papel Letter/A4 com a instituição; o modelo original
   foi preservado em Letter.
4. Conferir referências pendentes, especialmente Rouse, Chaves e edições de
   Wazlawick; aprofundar leitura integral de trabalhos relacionados.
5. Decidir autorização de tarefa funcional separada para inconsistências
   OBS-01–12; a redação não autoriza corrigi-las automaticamente.
6. Validar implantação e fluxos reais, se exigidos para a entrega. Não substituir
   essa evidência por widgets testados com mocks.
7. Confirmar o endereço de repositório exibido pela classe no cabeçalho: é
   configuração herdada do modelo, não URL de publicação deste trabalho comprovada.

Nenhuma dessas pendências autoriza inventar evidências ou remover ressalvas.

## 10. Fechamento da compilação e revisão

Comando executado em `docs/artigo_final`:

```sh
/tmp/opencode/tectonic --keep-logs --keep-intermediates \
  --outdir /tmp/opencode/tcc02-build Relatorio_Final.tex
```

Resultado: **compilação concluída, 25 páginas em Letter**, preservando a classe
institucional. O arquivo compilado foi copiado para `Relatorio_Final.pdf`.
Não se trata de versão pronta para entrega: há 19 placeholders explícitos de
captura, mês “A confirmar” e pendências bibliográficas/editoriais.

Checagens concluídas:
- 28 entradas BibTeX, 21 usadas por citações no relatório atual; todas resolvidas.
  Entradas não citadas foram preservadas para a proposta e revisão bibliográfica.
- 26 figuras numeradas (sete diagramas e 19 reservas de captura), três tabelas e
  equações numeradas; rótulos e referências cruzadas sem indefinição/duplicação
  no log final. Verificação documental também confirmou arquivos incluídos e
  correspondência dos 19 nomes de captura com o inventário.
- BibTeX sem erro ou warning; nenhum aviso final de citação/referência indefinida
  ou caractere ausente.
- PDF convertido em imagens; conferência panorâmica das 25 páginas e inspeção
  ampliada da identificação, diagramas, equações e exemplos de quadros/tabelas.
  Não se observaram cortes nos elementos examinados; revisão editorial final
  continua necessária após inserir as capturas.
- Persiste a caixa horizontal excedente de **54,64 pt no cabeçalho da primeira
  página**, já registrada na auditoria anterior e associada à classe preservada.
  Há avisos de fontes e caixas subpreenchidas; não foram escondidos alterando o
  modelo institucional. O resumo foi ajustado para eliminar o excedente vertical
  observado na primeira compilação.
- A última página contém continuação da bibliografia; a distribuição dos floats
  e a paginação devem ser revistas com as imagens definitivas, sem reduzir
  artificialmente o conteúdo para uma meta de páginas.
- Nenhuma diferença em código, testes, dependências, configurações de execução,
  proposta original ou classes. `git diff --check` sem problemas.

Logs/intermediários e rasterizações ficam em `/tmp/opencode/tcc02-build/`,
fora do repositório. A verificação não valida dados agronômicos, site publicado,
licenciamento de todas as dependências ou correções dos defeitos registrados.
