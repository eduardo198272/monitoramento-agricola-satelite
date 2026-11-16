# Auditoria científica — versão de trabalho

**Data:** 15/11/2026. **Parecer:** revisão parcial com correções fundamentadas; **não declarar conclusão integral**. A entrega reúne fontes/PDF revistos e os seis registros solicitados, mas a validação semântica exaustiva de todas as afirmações, a normalização institucional e decisões substantivas continuam abertas.

## 1. Escopo, versão e método

- Entrada: `docs/artigo_final/Relatorio_Final.tex`, classe `CC-EC_TF-TC.cls`, inclusões `final_*.tex`, figuras e resultados gerados da avaliação com usuários. Não confundir arquivos antigos `Proposta.tex`/capítulos da proposta com o artigo final.
- Checkout: `dev`, HEAD `6edf8707dc047eae762365b71c5e892321eeaef6`, com alterações anteriores não commitadas. A linha de base é a cópia de trabalho pré-auditoria, não HEAD. Hashes em `INVENTARIO.json`; backup em `/tmp/opencode/auditoria-cientifica/artigo-antes-auditoria.tar.gz`.
- Protocolo autoral lido integralmente; artigo lido antes das alterações, em confronto com núcleo analítico, geoespacial, armazenamento, exportação, testes, manifestos e histórico. Código e resultados não foram alterados nesta auditoria.
- Pesquisa: consultas públicas oficiais/científicas com status, URL, tamanho e hash em `CONSULTAS_FONTES.json` e `CONSULTAS_COMPLEMENTARES.json`. Cache local `/tmp/opencode/auditoria-cientifica/fontes/`; sua retenção é local, não um repositório público de PDFs de terceiros.
- Metadados foram separados do conteúdo. Acesso bloqueado, desafio HTML com HTTP 200 e PDF efetivo têm tratamentos distintos. “Texto integral disponível” não significa leitura de todas as páginas; o parecer individual indica as seções examinadas.
- Foram feitas correções localizadas após conferir a fundamentação. As alterações substantivas são propostas para aprovação do autor, não uma substituição de sua contribuição.

## 2. Contagens e significado

| Item | Quantidade / situação |
|---|---|
| Entradas bibliográficas originais com parecer individual | 34 |
| Novas entradas | 18 |
| Entradas atuais no `.bib` | 52 |
| Substituídas / removidas | 0 / 0 |
| Fontes com escopo substantivo conferido | 36 de 52; não significa validação integral de todos os metadados e afirmações |
| Demais registros | 16 com acesso, metadados, suporte ou condições parcialmente confirmados/pendentes |
| Equações analíticas examinadas | 12 |
| Expressões de lookup adicionais | 3, em duas linhas numeradas |
| Ajuste linear | 1 método não numerado |
| Blocos na matriz | 197, inventário de triagem; não 197 afirmações integralmente validadas |
| Problemas agrupados abaixo | 24: 14 corrigidos no escopo indicado, 10 pendentes/parciais |

As contagens não somam citações repetidas nem resultados históricos como novas observações. Fontes candidatas não incorporadas estão separadas da bibliografia. Slaiffer 2023 e 2025 foram conservados como documentos distintos relacionados, não como duas confirmações independentes do mesmo resultado.

## 3. Registro de problemas e correções

Gravidade: crítica = pode mudar interpretação científica; alta = suporte/metodologia insuficientes; média = precisão, rastreabilidade ou normalização. “Corrigido” limita-se à lacuna descrita, não aprova todo o parágrafo.

| ID | Localização | Gravidade | Problema / fundamento | Correção recomendada e executada | Evidência / status |
|---|---|---|---|---|---|
| AC01 | Fundamentação, representação espacial | Média | Raster/vetor/legenda sem fonte específica. | Inseridas referências técnicas QGIS próximas às definições. | QGIS Vector/Raster/Map Production; Corrigido |
| AC02 | NDVI, Eq. 1 | Alta | Base histórica descrita somente pelo registro NASA; limites genericamente atribuídos a Weiss. | Conferida seção Spectral Analysis de Rouse; separada adaptação Sentinel-2; Gao sustenta saturação/solo e Weiss condições de aquisição. | PDFs Rouse/Gao/Weiss; Corrigido |
| AC03 | NDWI, Eq. 2 | Crítica | Omissão dos comprimentos de onda originais pode sugerir equivalência Gao/B11. | Explicitar 0,86/1,24 µm versus B11 ~1,61 µm; preservar identificador do software. | Gao 1996 e catálogo S2; Corrigido |
| AC04 | NDMI, Eq. 3 e resolução | Alta | USGS não sustenta sozinho adaptação B8A/B11; grade 10 m exige explicação de reamostragem. | Adicionado exemplo técnico Sentinel Hub com inconsistência interna explícita; descrito vizinho mais próximo padrão e ausência de ganho físico de resolução. | USGS/Sentinel Hub/EE Resample; Corrigido |
| AC05 | Médias espaciais, Eqs. 5–6 | Alta | Pesos gerais pouco explícitos, risco de supor produto máscara×fração. | Definidos mínimo, quantização de oito bits, limiar aproximado e denominador positivo. Mantidas fórmulas gerais. | Guia EE reduceRegion; Corrigido |
| AC06 | Média móvel, Eq. 7 | Alta | Conceito sem referência estatística; janela de três pode parecer calibrada. | Fundamentado conceito em Hyndman e explicitada janela retrospectiva heurística de observações. | Livro aberto e anomalies.py; Corrigido |
| AC07 | Desvio/escore, Eqs. 8–9 | Alta | Divisor e distinção de testes formais precisavam de suporte próximo. | Adicionados NumPy e NIST com distinção entre escore da janela e escore amostral/teste; limites e NaN preservados. | np.std/ddof e NIST; Corrigido |
| AC08 | Tendência | Alta | polyfit/limiares sem fundamentação e insuficiência n<2 pouco explícita. | Inserida função objetivo de mínimos quadrados; definidas inclinação/intercepto e natureza heurística; “estável” com n<2 não é evidência. | Hyndman/NumPy/código/histórico 32c462d; Corrigido |
| AC09 | NASA, fundamentação | Alta | Resoluções originais não explicitadas. | Inseridas grades principais 0,5°×0,625° e 1°×1°, distinguindo aliases de alta resolução. | NASA Methodology; Corrigido |
| AC10 | NASA, Eqs. 10–12 | Alta | Definições/unidades dos parâmetros sem dicionário específico. | Acrescentado catálogo diário AG, precipitação, temperatura a 2 m e energia solar diária; prevalência de metadados mantida. | JSON oficial; Corrigido |
| AC11 | Radiação, Eq. 12 | Alta | Conversão correta no código, sem derivação e fonte metrológica. | Mostrada identidade kWh→MJ pelas definições SI; nenhuma inferência por magnitude. | BIPM/climate.py/regressões; Corrigido |
| AC12 | Avaliação técnica | Alta | Escopos de testes/cobertura sem fonte específica de Engenharia de Software. | Adicionado capítulo de Bender sobre escopo/comportamento/cobertura; sem atribuir processos Google ao projeto. | Software Engineering at Google, cap. 11; Corrigido |
| AC13 | Avaliação por adesão | Alta | Amostragem/autoseleção sem fonte metodológica próxima. | Referência AAPOR adicionada; não acrescentada inferência populacional. | Relatório 2013, sumário/recomendações; Corrigido |
| AC14 | Estado da interface | Média | Reexecução e estado descritos sem documentação de arquitetura da biblioteca. | Inserida documentação oficial Session State e limitação de persistência. | Streamlit e código; Corrigido |
| AC15 | Citações a artigos/norma sem acesso integral | Alta | Amani/Gorelick/McFeeters/Davis/Braun/ISO não tiveram conteúdo integral confirmado nesta rodada. | Limites registrados individualmente; obter textos e conferir subafirmações antes da aprovação. Não foi declarado suporte integral. | Auditoria de referências, PA11; Pendente |
| AC16 | Metadados e registros não citados | Média | Rouse duplicado, TCCs registrados como mastersthesis, Phiri com nome divergente, Wazlawick e repositórios pendentes. | Preservados sem correção especulativa; resolver com exemplares/registros institucionais. | Pareceres individuais; Pendente |
| AC17 | Modelo institucional/cabeçalho | Alta | Classe local não confirma vigência institucional, mês vazio e campo/link do template. | Classe preservada; solicitar confirmação institucional e dados. Aviso overfull histórico continua. | Classe v1.1, PA09–10; Pendente |
| AC18 | Caracterização aplicada/tecnológica | Alta | Descrição condiz com artefato, mas fundamentação metodológica formal incompleta. | Não inserir DSR/TDD/revisão sistemática por retrospectiva; consultar obra metodológica efetiva com autor. | Código/histórico; PA12; Pendente |
| AC19 | Arquitetura/modularidade/interoperabilidade | Média | Correspondência técnica examinada, mas fundamentação conceitual ampla ainda insuficiente. | Estado e testes fundamentados; não atribuir microsserviços/REST. Completar fontes específicas sem referências decorativas. | Código/diagramas; PA12; Parcial |
| AC20 | Tabela de plataformas | Alta | Página comercial não comprova automaticamente cada célula/condição de plano; EO Browser bloqueado. | NI preservado sem inferência negativa. Necessária matriz célula→trecho/URL/data antes de validação integral. | EOSDA/OneSoil/consulta EO Browser; Parcial |
| AC21 | Figura espectral | Média | Desenho qualitativo identificado, mas Weiss não confirma origem exata de cada curva solo/água. | Preservado como esquema; solicitar fonte específica ou revisão conceitual aprovada. | PA14; Pendente |
| AC22 | Figuras/capturas e revisão visual | Média | Não concluir legibilidade integral pelo sucesso da compilação; captura de radiação inválida permanece excluída. | Originais preservados; inventário gráfico e inspeção final devem ser concluídos, sem reconstrução de evidências. | PA15/18; Parcial |
| AC23 | Análise temática/ética/IA | Alta | Categorização e interpretação ainda sem aprovação substantiva e documentação institucional. | Manter transparência sobre IA, ausência de dupla codificação e pendências; não alegar chancela ética. | PA06–08; Dependente do autor |
| AC24 | Proveniência temporal/versão de coleta e rastreabilidade exaustiva | Alta | Commit público/fuso/fechamento e sustentação fina de cada subafirmação ainda incompletos. | Preservados intervalo, respostas, resultados e distinção de versões; matriz explicita triagem, sem aprovação automática. | PA05, matriz; Parcial |

## 4. Achados preservados sem nova alteração funcional

- Problema e objetivo tratam integração/verificação de plataforma computacional, não diagnóstico agronômico. A contribuição não é criar índices ou mínimos quadrados.
- Equações e código correspondem nos contratos examinados; rótulos NIR–SWIR exigem bandas explícitas, não duas “medidas independentes” de água no solo.
- Mediana do índice por pixel é distinta do índice das medianas de bandas; médias espaciais e temporais não são intercambiáveis.
- Série ordenada por data, sem interpolação, sem composição diária, admite múltiplas aquisições por data; irregularidade influencia janela e inclinação.
- QA60: bits 10/11, sem máscara específica de sombras; indisponibilidade histórica descrita. A documentação tem uma fronteira temporal que não foi “resolvida” artificialmente. Filtro de nuvem do produto não equivale à nuvem no talhão.
- Datas UTC inclusivas na interface, próximo dia exclusivo no EE; NASA usa `time-standard=UTC`. Resposta histórica LST não foi rebatizada como nova consulta UTC.
- Não foram alteradas respostas, dados da planilha, números da avaliação, código da aplicação, imagens originais ou arquivos de execução histórica. Nenhum commit, push, merge ou deployment nesta auditoria.

## 5. Evidência computacional

### Execução histórica — preservada no artigo

Commit `28759bf`, 710 aprovados em 11,73 s, 2.735 instruções e 856 ramificações em `src/app`, cobertura medida 100%; três verificações JavaScript e demonstração instrumentada em navegador com serviços reais. Evidências em `evidencias/` e `evidencias/demonstracao_real/`.

### Nova execução — não substitui números históricos

Comando na raiz: `COVERAGE_CORE=ctrace .venv/bin/python -m pytest -q -p no:cacheprovider`.

Resultado: **710 aprovados em 12,29 s**, 2.735 instruções, 856 ramificações, zero perdas e caminhos parcialmente cobertos, **100%** no escopo configurado `--cov=src/app --cov-branch` em `pytest.ini`. Log `TESTES_PYTHON.txt`. Não inclui entrypoint externo `streamlit_app.py`, JavaScript, dependências, serviço remoto ou arquivos fora de `src/app`.

JavaScript: `node --test tests/browser/index_hover.test.cjs`; resultado em `TESTES_JAVASCRIPT.txt`. Esta rodada não executou nova demonstração manual em navegador nem avaliação de hospedagem. Cobertura não prova ausência de defeitos, correção científica, segurança, desempenho ou qualidade agronômica.

Versão avaliada nesta rodada: checkout indicado acima, com fontes documentais modificadas; código da aplicação não alterado pela auditoria. O manifesto de validação registra hashes e ambiente para não atribuir indevidamente testes a um commit inexistente.

## 6. Figuras, tabelas e resultados

| Item | Conferência / limite |
|---|---|
| Figura 1, espectro | Curvas qualitativas sem escala/medição; fonte específica de solo/água pendente, AC21. |
| Figura 2, bandas | Centros S2A/S2B e resoluções B4/B8/B8A/B11 conferidos no catálogo harmonizado; não generalizar valores para todo satélite da missão. |
| Figura 3, raster/vetor | Esquema autoral, não observações; polígonos/grade/legenda coerentes com representação. |
| Figura 4, agregações | Aritmética conferida: média das médias 0,6 versus média da mediana por pixel 0,5. Pesos iguais, sem máscaras. |
| Figura 5, janela | Exemplo didático: média 0,6; σ≈0,08165; z≈−4,899. Não demonstra eficácia agronômica. |
| Fluxos de análise/anomalias | Correspondência examinada com pipeline, séries e anomalies; primeiros registros/escore zero e ausência de diagnóstico preservados. |
| Arquitetura, serviço de áreas, fluxos de áreas/lookup/exportação | Fronteiras Python/navegador/EE e armazenamento local/sessão examinadas; não representam microsserviços. Rotação da grade não é implementada no lookup. |
| Capturas do autor | 16 de 17 imagens em 11 agrupamentos, originais preservados; não pressupor a mesma execução ou versão da demonstração instrumentada. Captura problemática de PDF excluída. |
| Gráficos/tabelas de usuários | Descritivos das 31 submissões elegíveis; não avaliação observacional ou psicométrica. Sem mudança de dados, denominadores ou resultados nesta rodada. Codificação/ética dependem do autor. |
| Tabela de plataformas | Documental; validação célula por célula não concluída, AC20. |
| Tabela de componentes | Conferida em relação aos módulos; abstrações não constituem aplicação integral de padrão arquitetural. |
| Objetivos/resultados/conclusão | Distinguem recurso implementado, teste e estudo agronômico não realizado. Aprovação da mudança de escopo e interpretações pendente. |

`COMPILACAO.json` confirma 33 páginas, 27 figuras, cinco tabelas, 45 chaves citadas, nenhuma referência indefinida, oito ambientes matemáticos preservados e classe institucional inalterada. Permanece o aviso de cabeçalho `Overfull hbox (54.64pt)`. `VALIDACAO_FINAL.json` complementa o registro de ambiente, integridade e hashes. PDF: SHA-256 `0fffb8827d34c75662a20bce87a5fa68f991de1ae226cca678790164b65c7f8d`.

As 33 páginas foram renderizadas e examinadas em seis folhas de contato para triagem do layout geral: não foram identificadas páginas vazias ou sobreposições grosseiras. Essa escala não permite certificar todos os detalhes de capturas, caracteres, referências e equações; a inspeção ampliada e a aprovação visual do autor permanecem pendentes. Páginas com figuras isoladas e espaços amplos são consequência dos floats existentes, não novas medições.

## 7. Critérios de aceite

| Critério | Estado |
|---|---|
| Leitura do artigo, confronto de código/testes/evidências | Executado no escopo registrado |
| Todas as referências originais inventariadas e com parecer | Atendido: 34 |
| Todas as referências integralmente confirmadas em conteúdo e metadados | Não atendido: limitações individuais |
| Novas fontes com origem verificável | Atendido no escopo de trechos consultados: 18 |
| Doze equações e regressão examinadas | Atendido, mais três expressões; calibração não demonstrada |
| Heurísticas e nomenclatura esclarecidas | Melhorado; decisão de nomenclatura depende do autor |
| Todas as afirmações relevantes sustentadas individualmente | Não atendido: matriz é triagem, revisão fina permanece |
| Métodos/resultados correspondentes às evidências | Confrontados nos contratos descritos; não valida todo uso possível |
| Respostas sintéticas não apresentadas como resultados | Preservado; nenhum dado novo gerado |
| Limitações explicitadas | Preservadas e ampliadas localmente |
| Compilação sem erros/citações indefinidas | Ver validação automatizada desta versão, não reutilizar hash anterior |
| Revisão visual integral e normalização institucional | Não concluídas |
| Seis documentos obrigatórios | Disponíveis neste diretório |
| Aprovação autoral/ética/IA | Pendente |

## 8. Parecer

A versão revista esclarece a diferença entre fórmula histórica, adaptação espectral, estatística elementar e heurística da aplicação. A fundamentação de agregação espacial, mínimos quadrados, unidades meteorológicas, amostragem e testes ficou mais específica. Isso melhora a defensabilidade do recorte computacional, **sem demonstrar validação agronômica**.

Ainda não é possível emitir parecer de revisão científica integral concluída. A existência dos seis documentos, a execução dos testes e a compilação são entregas verificáveis, mas não suprem textos inacessíveis, revisão de todas as subafirmações, validação visual, normalização institucional ou aprovação intelectual do autor/orientador. As pendências não devem ser convertidas em fatos por redação.
