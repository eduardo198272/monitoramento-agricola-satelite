# Auditoria bibliográfica final

**Data:** 16/11/2026. **Trabalho:** Sistema de Monitoramento Agrícola por Imagens de Satélite.
**Responsável intelectual:** Eduardo Steffens Hoppen. Pesquisa, conferência e
implementação assistidas por IA; esta auditoria não substitui a conferência do
pesquisador nem a aprovação do orientador.

## 1. Escopo, método e resultado

Foram inventariadas individualmente **63 entradas**, das quais **54 citadas**
e nove conservadas sem uso no artigo. Os registros estruturados incluem os
campos bibliográficos, autoria ordenada, locais das citações, consultas HTTP,
redirecionamentos, tipo de conteúdo e hashes das respostas. Os artigos com
DOI foram confrontados com registros Crossref; DOI Zenodo não foi considerado
inexistente por não pertencer ao Crossref. Documentações foram consultadas nos
domínios oficiais. A correspondência textual foi examinada nos arquivos
efetivamente incluídos, não em versões antigas do manuscrito.

**Resultado:** oito entradas corrigidas; nenhuma referência adicionada ou
excluída. Nenhum arquivo de seção científica foi alterado. Compilação limpa
com Tectonic 0.17.0/XeTeX e BibTeX/dcu; PDF com 32 páginas, 54 referências,
22 figuras, cinco tabelas e 14 expressões numeradas. Sem citações indefinidas,
duplicações na lista publicada ou extrapolações `Overfull`. Permanecem avisos
de caixas `Underfull`, substituições de tamanhos de fontes e aviso `epstopdf`
compatíveis com a configuração anterior; não foram suprimidos por alterações
de margens, fontes ou estilo.

**Não se certifica validação integral de todos os metadados ou leitura integral
de todas as publicações.** A existência de registros bibliográficos foi
distinguida da obtenção do texto primário. As limitações individuais abaixo
integram o resultado da auditoria, não são confirmações tácitas.

Evidências: [`evidencias/revisao_bibliografica_final/`](evidencias/revisao_bibliografica_final/).
O inventário `referencias.json` contém os campos completos e as ocorrências
de citação; `consultas.json` contém as respostas de acesso e metadados
selecionados. O conteúdo bruto de PDFs externos permanece em cache privado:
não foi republicado, especialmente o PDF da UPF com identificador pessoal
de assinatura. Trechos probatórios foram selecionados sem esse identificador.

## 2. Correções confirmadas

### EOSDA

- URL específica adotada: <https://eos.com/user-guide/crop-monitoring/>.
- HTTP 200 e guia real obtido. O endereço antigo também funciona por dois
  redirecionamentos 301 até o mesmo guia; portanto, não era um endereço morto.
- O breadcrumb identifica **EOSDA Crop Monitoring User Guide**; o cabeçalho
  usa **EOSDA Crop Monitoring Guide** e o título HTML acrescenta
  **Learn How To Use Our Software**. A designação bibliográfica anterior
  corresponde ao breadcrumb e foi preservada.
- Conferidos *Add field* (desenho e upload), *Monitoring* (índices, gráficos),
  *Weather* (histórico/previsão), *Work With Crop Map / Split view*
  (valores por posição e download) e *Account And Pricing* (planos e
  complementos). As células EOSDA da tabela e o parágrafo correspondente
  permanecem sustentados em nível documental, não experimental.
- Continua sendo **documentação comercial**, sem comprovação independente
  de produtividade, precisão agronômica ou retorno financeiro.

### UPF

- PDF direto solicitado: HTTP 200, assinatura de arquivo PDF e cinco páginas.
- Documento: **INSTRUÇÃO NORMATIVA Nº 03/2026/PROACAD**.
- Ementa: **Dispõe sobre o uso de Inteligência Artificial (IA) nas atividades
  acadêmicas na Universidade de Passo Fundo (UPF) e dá outras providências.**
- Órgão emissor: **Pró-Reitoria Acadêmica da Universidade de Passo Fundo**.
  Data expressa: **Passo Fundo, 28 de outubro de 2026**.
- Corrigidos URL e título; registrado órgão emissor e data estruturada.
  A data de 28 out. 2026 já era recuperada pelo adaptador do registro histórico.
- Arts. 3º, II–VIII, 4º e §§, 6º–8º e anexo sustentam responsabilidade,
  autorização/limites, transparência, declaração e comunicação à banca.
  Não comprovam que o autor obteve autorização, consentimento ou aprovação.
  A declaração existente conserva explicitamente essas pendências e não
  foi modificada.
- Percentuais codificados da URL são escapados **somente na projeção para
  TeX**, pois `\harvardurl` lê seu argumento antes de `\url`. A base conserva
  o endereço literal; os links extraídos do PDF coincidem com esse endereço,
  sem barras de escape. A primeira tentativa de compilação identificou
  esse problema; o log de falha foi conservado junto ao log final.

### NASA POWER

- Endpoint original consultado por GET: **HTTP 200**, JSON sintaticamente
  válido, objeto com os três parâmetros. Não é uma página HTML defeituosa.
- Acrescentada à **mesma entrada**, sem nova citação, a documentação
  [Manager API](https://power.larc.nasa.gov/docs/services/api/system/manager/).
  Ela informa que o serviço sincroniza parâmetros e retorna JSON.

| Parâmetro | Definição oficial conferida | Unidade no dicionário AG/DAILY | Metadados da resposta pontual consultada |
|---|---|---|---|
| `PRECTOTCORR` | Precipitação total média à superfície, corrigida de viés MERRA-2 | `mm/day` | `mm/day` |
| `T2M` | Temperatura média do ar, bulbo seco, a 2 m da superfície | `C` | `C` |
| `ALLSKY_SFC_SW_DWN` | Irradiância solar total direta + difusa incidente num plano horizontal à superfície, sob todas as condições de céu | `MJ/m^2/day` | `MJ/m^2/day` |

A consulta pontual foi uma **sondagem documental**, não novo resultado do
TCC: −52,4°, −28,2°, 01–02/01/2025, comunidade AG, padrão LST. Não foi
usada para substituir a evidência histórica nem o comportamento UTC da
aplicação. O catálogo e uma resposta atual não fixam unidades de todas as
respostas possíveis. Continua correta a precedência dos metadados e a
conversão condicional por 3,6; equações, constantes e código não mudaram.

### BIPM

A [página oficial](https://www.bipm.org/en/si-brochure-9) declara:

> Bureau International des Poids et Mesures. (2026). Le Système international
> d'unités/The International System of Units [Brochure]. 9th edition.
> https://doi.org/10.59161/AUEZ1291

Por essa **recomendação explícita**, o ano foi atualizado de 2019 para 2026.
Mantidos título da versão inglesa, 9ª edição, versão **4.01, junho de 2026**,
DOI e PDF oficial. A edição original continua sendo de maio de 2019;
o PDF mantém 2019 na folha de rosto. O registro Crossref também apresenta
2019: neste caso prevaleceu a recomendação bibliográfica da própria
instituição para a versão revisada, não uma inferência pelo acesso.
A citação no corpo foi atualizada automaticamente pelo BibTeX.

### QGIS

O roadmap oficial e o comunicado do PSC de 03/10/2026 identificam a linha
**3.44 como LTR**, com versões 4.x mais recentes e transição de LTR
planejada. Os painéis de download/roadmap divergem quanto ao ponto de
atualização; não se certifica aqui um número de patch como o mais recente.

As três páginas 3.44 foram obtidas com HTTP 200 e comparadas às páginas 3.40.
Permanecem equivalentes os trechos usados: §3.1/3.4, geometria vetorial e
polígonos; §6.1/6.2, matriz de células com valores; §9.1/9.4, legenda e
interpretação dos símbolos. Adotada **3.44 LTR**, não uma versão de teste
nem a suposição de que a versão numericamente maior é obrigatória.
O rodapé informa atualização da documentação em 30/10/2026; isso não
certifica a data de redação original de cada conceito. Ano 2026 mantido.

### Rouse

O registro NASA NTRS e o PDF oficial de nove páginas confirmam autoria,
publicação em 1974 e páginas impressas **309–317**, agora preenchidas.
O ano do evento, 1973, não substitui o ano da publicação citada. A entrada
histórica `ROUSE1973`, não citada, continua preservada e identificada como
representação potencialmente duplicada do mesmo trabalho.

## 3. Legenda dos estados de acesso

- **Funcional:** conteúdo identificável obtido, não apenas HTTP 200.
- **Redirecionamento válido:** cadeia HTTP até destino pertinente. Quando o
  destino contém só JavaScript ou uma página de encaminhamento, isso é
  explicitado; não significa obtenção do artigo.
- **Assinatura/autenticação:** acesso ao texto/exemplar depende de acesso
  autorizado. Diferente de bloqueio automatizado.
- **Bloqueio automatizado:** desafio JavaScript, antirobô ou 403 com proteção.
  Não torna o DOI inválido e não prova assinatura.
- **Indisponível nesta consulta:** timeout, 404 ou resposta vazia, sem
  concluir inexistência da publicação.
- **Existência não confirmada:** evidência primária insuficiente para
  certificar a entrada, independentemente do status de rede.

As datas das consultas constam dos recibos. Somente oito entradas alteradas
receberam nova data de acesso; as demais preservam os acessos históricos.
Anos com `c` são copyright; `[20--?]` permanece indicação aproximada
preexistente, não ano editorial confirmado. Datas do rodapé de geração,
copyright e acesso não foram confundidas com publicação original.

## 4. Tabela individual — 54 referências utilizadas

Os DOI/URLs completos e todos os campos constam também de `referencias.json`.
“Crossref” abaixo significa conferência de metadados, não leitura do artigo.
Variações de caixa, travessão e abreviações não foram tratadas como obras
diferentes. Na ausência de evidência corretiva, os metadados foram mantidos.

| Referência | DOI/URL | Status de acesso | Validação bibliográfica | Qualidade da fonte | Alteração realizada |
|---|---|---|---|---|---|
| `ESA_SENTINEL2` | [SentiWiki](https://sentiwiki.copernicus.eu/web/s2-mission) | Funcional, 200 | Missão MSI, 13 bandas, resoluções e revisita; página institucional. Ano da publicação original da página não certificado. | Documentação oficial; não ensaio de desempenho | Nenhuma |
| `GOOGLE_S2_SR` | [Catálogo](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED) | Funcional, 200 | Coleção, título, bandas, escala e harmonização; autoria institucional. Ano é da documentação dinâmica, não do início da missão. | Documentação oficial do produto | Nenhuma |
| `GOOGLE_EE_ND` | [API](https://developers.google.com/earth-engine/apidocs/ee-image-normalizeddifference) | Funcional, 200 | Função, razão normalizada e máscara; atualização exibida em 2026. | Contrato técnico oficial | Nenhuma |
| `GOOGLE_EE_DATE` | [API](https://developers.google.com/earth-engine/apidocs/ee-filter-date) | Funcional, 200 | Função e início inclusivo/fim exclusivo; não confundido com inclusão aplicada pelo código. | Contrato técnico oficial | Nenhuma |
| `GOOGLE_EE_SERVICE_ACCOUNT` | [Guia](https://developers.google.com/earth-engine/guides/service_account) | Funcional, 200 | Título e autenticação por conta de serviço; não prova credenciais/configuração do projeto. | Documentação oficial | Nenhuma |
| `GOOGLE_EE_NONCOMMERCIAL` | [Guia](https://developers.google.com/earth-engine/guides/noncommercial_tiers) | Funcional, 200 | Modalidades não comerciais; não prova elegibilidade individual ou gratuidade irrestrita. | Política oficial do serviço | Nenhuma |
| `STREAMLIT_CLOUD_SECRETS` | [Documentação](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management) | Funcional, 200 | Título e autoria institucional; `c2026` não é data editorial comprovada. | Documentação técnica oficial | Nenhuma |
| `SLAIFFER2023` | [UFSM](https://repositorio.ufsm.br/handle/1/29995) | Funcional, 200 | Registro confirma Henrique Slaiffer, título, UFSM, TCC Engenharia Agrícola, 17/07/2023; resumo compatível. Não é dissertação, apesar do tipo técnico BibTeX. | TCC institucional; não revisão por pares presumida | Nenhuma; tipo descritivo já explícito |
| `NASA_POWER_DAILY` | [Daily API](https://power.larc.nasa.gov/docs/services/api/temporal/daily/) | Funcional, 200 | Serviço diário, argumentos e convenções temporais; ano original da página não certificado. | Documentação oficial NASA | Nenhuma |
| `GAO1996` | [10.1016/S0034-4257(96)00067-3](https://doi.org/10.1016/S0034-4257(96)00067-3) | DOI redireciona, 200; destino só encaminhamento | Crossref confirma autor, título, 1996, RSE 58(3), 257–266. Acesso primário histórico registrado na auditoria anterior; não obtido novamente por este DOI. | Artigo científico clássico; não valida diretamente B8/B11 | Nenhuma |
| `PATRICIO2018` | [10.1016/j.compag.2018.08.001](https://doi.org/10.1016/j.compag.2018.08.001) | DOI redireciona, 200; destino só encaminhamento | Crossref confirma Patrício e Rieder, ordem, título, 2018, CEA 153, 69–81. Leitura histórica identificada, sem nova leitura integral. | Revisão científica; contexto, não certificação do artefato | Nenhuma |
| `GORELICK2017` | [10.1016/j.rse.2017.06.031](https://doi.org/10.1016/j.rse.2017.06.031) | DOI redireciona para encaminhamento; Google Research funcional | Crossref e Google Research confirmam seis autores, título, 2017, RSE 202, 18–27. Texto integral não reconferido. | Artigo científico sobre infraestrutura | Nenhuma |
| `AMANI2020` | [10.1109/JSTARS.2020.3021052](https://doi.org/10.1109/JSTARS.2020.3021052) | Redireciona para IEEE, 202 sem conteúdo | Crossref confirma 12 autores ordenados, título, 2020, JSTARS 13, 5326–5350; acesso integral continua limitado. | Revisão científica; referência temática delimitada | Nenhuma |
| `WEISS2020` | [10.1016/j.rse.2019.111402](https://doi.org/10.1016/j.rse.2019.111402) | DOI redireciona, 200; destino só encaminhamento | Crossref confirma iniciais M. Weiss, F. Jacob, G. Duveiller, título, 2020, RSE 236, 111402. Prenomes completos não certificados pelo Crossref. | Meta-revisão científica; limitações da interpretação espectral | Nenhuma |
| `MCFEETERS1996` | [10.1080/01431169608948714](https://doi.org/10.1080/01431169608948714) | Bloqueio automatizado, 403 | Crossref confirma autor, título, 1996, IJRS 17(7), 1425–1432. Texto integral não obtido nesta rodada. | Artigo científico clássico; água superficial, não variante NIR–SWIR | Nenhuma |
| `USGS_NDMI` | [USGS](https://www.usgs.gov/landsat-missions/normalized-difference-moisture-index) | Funcional, 200; timeout anterior superado | Título e NIR–SWIR para Landsat confirmados. Data editorial específica não identificada. | Documentação oficial; não validação Sentinel-2 B8A/B11 | Nenhuma; data incerta preservada |
| `GOOGLE_EE_SAMPLE` | [API](https://developers.google.com/earth-engine/apidocs/ee-image-samplerectangle) | Funcional, 200 | Nome da função, matriz por banda e projeção; uso técnico compatível. | Contrato oficial | Nenhuma |
| `GOOGLE_EE_MEDIAN` | [API](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-median) | Funcional, 200 | Mediana por pixel/bandas correspondentes; uso compatível. | Contrato oficial | Nenhuma |
| `GOOGLE_EE_REDUCE` | [API](https://developers.google.com/earth-engine/apidocs/ee-image-reduceregion) | Funcional, 200 | Nome, parâmetros e redução regional; uso compatível. | Contrato oficial | Nenhuma |
| `NOMINATIM_POLICY` | [OSMF](https://operations.osmfoundation.org/policies/nominatim/) | Funcional, 200 | Política e autoria institucional; data 11/05/2026 refere-se ao arquivo-fonte, conforme evidência anterior, não publicação original. | Política técnica oficial | Nenhuma |
| `ROUSE1974_NTRS` | [NASA NTRS](https://ntrs.nasa.gov/citations/19740022614) | Página, API e PDF funcionais, 200 | Quatro autores, ordem, título, veículo NASA, 1974 e páginas impressas confirmados. | Anais científicos históricos; não usa Sentinel-2 | Páginas 309–317 e acesso |
| `ISO9241_2018` | [ISO](https://www.iso.org/standard/63500.html) | Bloqueio automatizado, 403; norma integral comercial | Identificação/título e resumo oficial já conferidos na auditoria anterior; texto pago não examinado. Não se infere assinatura a partir do 403. | Norma institucional, quadro conceitual; não certificação do TCC | Nenhuma |
| `DAVIS1989` | [10.2307/249008](https://doi.org/10.2307/249008) | Bloqueio automatizado, 403 | Crossref confirma Fred D. Davis, título, 1989, MISQ 13(3), 319–340; PDF histórico registrado na terceira rodada, não novamente baixado. | Artigo científico clássico; questionário local não é TAM validado | Nenhuma |
| `SULLIVAN2013` | [10.4300/JGME-5-4-18](https://doi.org/10.4300/JGME-5-4-18) | Redirecionamento válido, 200; aplicação exige JavaScript | Crossref confirma dois autores, título, 2013, JGME 5(4), 541–542; sufixo Jr. preservado da fonte anterior, não certificado pelo registro abreviado. | Artigo metodológico; não valida psicometria do instrumento | Nenhuma |
| `BRAUN2006` | [10.1191/1478088706qp063oa](https://doi.org/10.1191/1478088706qp063oa) | Bloqueio automatizado, 403 | Crossref confirma Braun e Clarke, título, 2006, QRP 3(2), 77–101; PDF UWE documentado na terceira rodada. | Artigo metodológico; não comprova execução integral das seis fases | Nenhuma |
| `QGIS_VECTOR` | [3.44, Vector Data](https://docs.qgis.org/3.44/en/docs/gentle_gis_introduction/vector_data.html) | Funcional, 200 | Título e §§3.1/3.4 equivalentes; versão LTR oficial, atualização documental 2026. | Documentação conceitual oficial | 3.40 → 3.44, URL e acesso |
| `QGIS_RASTER` | [3.44, Raster Data](https://docs.qgis.org/3.44/en/docs/gentle_gis_introduction/raster_data.html) | Funcional, 200 | Título e §§6.1/6.2 equivalentes; matriz de células/valores. | Documentação conceitual oficial | 3.40 → 3.44, URL e acesso |
| `QGIS_MAP` | [3.44, Map Production](https://docs.qgis.org/3.44/en/docs/gentle_gis_introduction/map_production.html) | Funcional, 200 | Título e §§9.1/9.4 equivalentes; legenda e interpretação. | Documentação conceitual oficial | 3.40 → 3.44, URL e acesso |
| `GOOGLE_EE_RESAMPLE` | [Guia](https://developers.google.com/earth-engine/guides/resample) | Funcional, 200 | Reamostragem e distinção entre grade e resolução; padrão não equivale a interpolação explícita. | Documentação oficial | Nenhuma |
| `GOOGLE_EE_REGION` | [Guia](https://developers.google.com/earth-engine/guides/reducers_reduce_region) | Funcional, 200 | Título, redução e pesos; não transformado em evidência agronômica. | Documentação oficial | Nenhuma |
| `SENTINELHUB_NDMI` | [Custom Scripts](https://custom-scripts.sentinel-hub.com/custom-scripts/sentinel-2/ndmi/) | Funcional, 200 | Código B8A/B11 e texto B08/B11 reconferidos. Data é atualização do arquivo-fonte já documentada. | Exemplo técnico de fornecedor; inconsistência explícita | Nenhuma |
| `HYNDMAN2021` | [OTexts](https://otexts.com/fpp3/) | Funcional, 200 | Título, autores e 3ª edição confirmados; página hoje atualizada em 14/11/2026. Não se mudou o ano da edição para o da atualização. Detalhes editoriais de 2021 não integralmente reconferidos. | Livro acadêmico aberto; não justifica janela/limiares particulares | Nenhuma |
| `NIST_OUTLIERS` | [§1.3.5.17](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35h.htm) | Funcional, 200 | Seção, escore Z e cautela com pequenas amostras conferidos; data editorial específica ausente. | Manual técnico estatístico oficial | Nenhuma |
| `NUMPY_STD` | [API](https://numpy.org/doc/stable/reference/generated/numpy.std.html) | Funcional, 200 | Nome, divisor N−ddof e padrão 0; stable aponta manual 2.5. Copyright não é ano original. | Documentação técnica oficial, não validação do limiar | Nenhuma |
| `NUMPY_POLYFIT` | [API](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html) | Funcional, 200 | Ajuste por mínimos quadrados; versão stable dinâmica, não prova versão instalada. | Documentação técnica oficial | Nenhuma |
| `BIPM_SI` | [10.59161/AUEZ1291](https://doi.org/10.59161/AUEZ1291) | PDF funcional, 200; DOI redireciona à página oficial | 9ª edição 2019, revisão 4.01/2026; recomendação oficial cita 2026, apesar do registro Crossref 2019. | Fonte metrológica primária | Ano 2026 e acesso |
| `BENDER2020` | [Capítulo 11](https://abseil.io/resources/swe-book/html/ch11.html) | Funcional, 200 | Autoria Adam Bender expressa no capítulo; livro e editores preservados. Não se atribui a ele todo o livro. | Capítulo técnico especializado; não estudo experimental do TCC | Nenhuma |
| `AAPOR2013` | [Relatório](https://aapor.org/wp-content/uploads/2022/11/NPS_TF_Report_Final_7_revised_FNL_6_22_13.pdf) | PDF funcional, 200 | Relatório da Task Force, junho de 2013; capa também nomeia oito membros. Entrada institucional mantida; não se inventou autoria pessoal nova. | Relatório metodológico de associação científica | Nenhuma |
| `SLAIFFER2025` | [10.31413/nat.v13i3.18592](https://doi.org/10.31413/nat.v13i3.18592) | Redirecionamento válido, página funcional, 200 | Crossref e página confirmam quatro autores, ordem, título, 2025, Nativa 13(3), 495–502. | Artigo científico; relação índices/produtividade, não eficácia do sistema local | Nenhuma |
| `IZQUIERDO2026` | [10.3390/agronomy16050541](https://doi.org/10.3390/agronomy16050541) | DOI redireciona, 200; conteúdo automatizado não legível | Crossref confirma dois autores, título, 2026, Agronomy 16(5), 541; PDF primário foi examinado na auditoria anterior. | Artigo científico; modelagem com campo, distinta deste artefato | Nenhuma |
| `NASA_POWER_METHOD` | [Metodologia](https://power.larc.nasa.gov/docs/methodology/) | Funcional, 200 | Título institucional; página agregadora remete às metodologias. Resoluções específicas têm rastreabilidade histórica; data editorial ausente. | Documentação oficial NASA | Nenhuma |
| `NASA_POWER_PARAMETERS` | [JSON AG/DAILY](https://power.larc.nasa.gov/api/system/manager/parameters?community=AG&temporal=DAILY) | Funcional, HTTP 200, JSON válido | Definições/unidades dos três parâmetros e resposta pontual conferidas; título descritivo de recurso, sem data editorial identificada. | Dicionário técnico oficial | Nota com Manager API e acesso |
| `STREAMLIT_STATE` | [Session State](https://docs.streamlit.io/develop/concepts/architecture/session-state) | Funcional, 200 | Estado entre reruns e escopo da sessão; `c2026` não certifica publicação original. | Documentação técnica oficial | Nenhuma |
| `MERONI2019` | [10.1016/j.rse.2018.11.041](https://doi.org/10.1016/j.rse.2018.11.041), [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6360378/) | PMC funcional, 200; DOI até encaminhamento | Crossref e artigo PMC confirmam cinco autores, ordem, título, 2019, RSE 221, 508–521. | Artigo científico; histórico sazonal não equivale à janela local | Nenhuma |
| `PARNAS1972` | [10.1145/361598.361623](https://doi.org/10.1145/361598.361623), [PDF TU/e](https://wstomv.win.tue.nl/edu/2ip30/references/criteria_for_modularization.pdf) | PDF funcional, 200; DOI com bloqueio 403 | Crossref/PDF confirmam autor, título, 1972, CACM 15(12), 1053–1058. | Artigo científico clássico; não mede manutenibilidade do TCC | Nenhuma |
| `NIST_LOCATION` | [§1.3.5.1](https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm) | Funcional, 200 | Média/mediana par e ímpar, sensibilidade e exemplo Cauchy; data da seção não identificada. | Manual técnico estatístico oficial | Nenhuma |
| `GITHUB_SDD` | [Spec Kit](https://github.com/github/spec-kit/blob/main/spec-driven.md) | Funcional, 200 | Título e fluxo SDD; data de atualização do arquivo já rastreada, não criação do método. | Documentação técnica de ferramenta; não ensaio científico | Nenhuma |
| `BOECKELER2025` | [Artigo técnico](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) | Funcional, 200 | Birgitta Böckeler, título e 15/10/2025 confirmados. | Análise técnica/blog especializado; não revisão por pares | Nenhuma |
| `UPF_IA2026` | [PDF oficial](https://www.upf.br//_uploads/Conteudo/IN%20n%C2%BA%2003_2026%20Uso%20de%20Intelig%C3%AAncia%20Artificial%20%28IA%29%20nas%20atividades%20acad%C3%AAmicas%20da%20UPF_docx%281%29.pdf) | PDF funcional, 200 | Número, ementa, ProAcad/UPF e 28/10/2026 conferidos no documento. | Ato normativo primário; não comprova autorização individual | URL, título, órgão, data estruturada e acesso |
| `EOSDA_GUIDE` | [Guia específico](https://eos.com/user-guide/crop-monitoring/) | Funcional, 200; URL antiga redireciona validamente | Nome do guia e recursos da comparação conferidos; sem data editorial identificada. | Documentação comercial, não validação independente | URL e acesso |
| `ONESOIL_PLATFORM_DETAIL` | [OneSoil](https://onesoil.ai/en/platform) | Funcional, 200 | Produto, Mobile/Pro, clima, comparação e exportação documentados; não se assumem métricas promocionais como resultados. Data editorial ausente. | Página comercial; disponibilidade depende de modalidade | Nenhuma |
| `GOTEL1994` | [10.1109/ICRE.1994.292398](https://doi.org/10.1109/ICRE.1994.292398), [UCL](https://discovery.ucl.ac.uk/749/) | UCL e PDF funcionais, 200; DOI → IEEE 202 vazio | UCL/PDF confirmam Gotel e Finkelstein, 1994, evento e 94–101. Crossref abrevia Finkelstein como C.W.; não substituiu Anthony C.W. confirmado no PDF. | Artigo científico de conferência | Nenhuma |
| `BJARNASON2015` | [10.1007/978-3-319-18612-2_3](https://doi.org/10.1007/978-3-319-18612-2_3), [arXiv](https://arxiv.org/abs/2308.06509) | arXiv funcional, 200; Springer Client Challenge | Crossref confirma quatro autores, título, obra e 27–39; arXiv indica XP 2015 e DOI relacionado. Depósito 2023 não é ano da publicação. | Artigo científico de conferência; versão aberta de autor | Nenhuma |
| `VAITHILINGAM2022` | [10.1145/3491101.3519665](https://doi.org/10.1145/3491101.3519665), [PDF dos autores](https://tianyi-zhang.github.io/files/chi2022-lbw-copilot.pdf) | PDF funcional, 200; DOI com bloqueio 403 | Crossref/PDF confirmam três autores, título, CHI Extended Abstracts 2022, 1–7. | Artigo curto científico; não prova ganhos deste TCC | Nenhuma |

## 5. Nove entradas não citadas — preservadas

Estas entradas não integram as 54 referências impressas. As limitações não
foram “resolvidas” removendo registros ou acrescentando citações decorativas.

| Referência | DOI/URL | Status de acesso | Validação bibliográfica | Qualidade da fonte | Alteração realizada |
|---|---|---|---|---|---|
| `LOVATO2021` | [UNESP](https://repositorio.unesp.br/entities/publication/b9caa0ff-8be4-44b6-ba3d-e40bbfa7e275) | Página funcional, 200 | Registro institucional localizado; título/autor/ano compatíveis, grau e edição do texto não integralmente conferidos. | TCC institucional, sem revisão por pares presumida | Nenhuma |
| `ARAUJO2025` | [10.5281/zenodo.15871939](https://doi.org/10.5281/zenodo.15871939) | DOI redireciona ao Zenodo, 200; Crossref 404 | Existência do depósito confirmada; título inglês na página. Autores e dados da versão publicada em BOCA não integralmente conferidos nesta rodada. Registrador distinto explica 404 Crossref. | Depósito de artigo; publicação editorial não certificada só pelo depósito | Nenhuma |
| `CHAVES2019` | [UFLA](https://repositorio.ufla.br/items/62ad79ab-a7b3-400b-ad28-5779e424f3d3) | Indisponível nesta consulta: timeout | Existência e metadados não confirmados diretamente; entrada provisória preservada. | Tese indicada na base, sem validação primária atual | Nenhuma |
| `ROUSE1973` | Sem DOI/URL nesta entrada; confronto com NTRS acima | Entrada sem endereço próprio | Possível duplicata de ROUSE1974_NTRS, com ano do evento em lugar do ano de publicação; não conta como segunda fonte independente. | Registro histórico de anais | Nenhuma; mantido fora da lista citada |
| `PHIRI2020` | [10.3390/rs12142291](https://doi.org/10.3390/rs12142291) | DOI redireciona, 200; conteúdo não legível automaticamente | Crossref confirma título/veículo/2020/12(14)/2291; diverge o prenome Salekin: Serajis versus Sharif. Sem PDF primário não se corrigiu por suposição. | Revisão científica, não utilizada | Nenhuma; divergência preservada como pendência |
| `WAZLAWICK2014` | Sem DOI/URL na base | Sem consulta a exemplar | Livro/edição/ano não integralmente confirmados; não tratado como fonte consultada. | Livro acadêmico indicado, sem certificação da edição | Nenhuma |
| `WAZLAWICK2020` | [Biblioteca](https://integrada.minhabiblioteca.com.br/books/9788595157712) | Redireciona, 200; Bookshelf exige aplicação/autenticação | Não foi obtido exemplar nem confirmação integral de edição/ano; acesso anterior não certificado retroativamente. | Livro acadêmico em biblioteca licenciada | Nenhuma |
| `EOSDA_PLATFORM` | [Produto](https://eos.com/products/crop-monitoring/) | Funcional, 200 | Produto existe; página promocional, sem data editorial específica certificada. Não duplica a entrada do guia como publicação independente equivalente. | Comercial, não utilizada | Nenhuma |
| `ONESOIL_PLATFORM` | [OneSoil](https://onesoil.ai/en/platform) | Funcional, 200 | Mesmo recurso de ONESOIL_PLATFORM_DETAIL, com ano distinto; duplicata potencial na base, não na bibliografia impressa. | Comercial, não utilizada | Nenhuma |

## 6. Limitações e decisões conservadoras

1. As sete datas antes incertas permanecem sem comprovação editorial:
   `USGS_NDMI`, `NIST_OUTLIERS`, `NIST_LOCATION`, `NASA_POWER_METHOD`,
   `NASA_POWER_PARAMETERS`, `EOSDA_GUIDE`, `ONESOIL_PLATFORM_DETAIL`.
   Anos de páginas dinâmicas e copyrights também não certificam suas
   publicações originais. Nenhum ano foi criado para eliminar a lacuna.
2. Não foi repetida a leitura integral de todos os artigos. Auditorias
   anteriores são usadas como **evidência histórica identificada**, não
   como downloads novos; os recibos atuais delimitam o que foi obtido agora.
   Crossref sustenta existência/metadados, não todas as afirmações científicas.
3. Prenomes completos de Weiss/Jacob/Duveiller não são certificados pelo
   registro abreviado; foram mantidos. O prenome de Salekin na entrada não
   citada PHIRI2020 continua divergente, sem correção não comprovada.
4. Busca complementar de acesso aberto para Weiss retornou uma página HAL
   sobre bebidas e nutrição, sem relação com o artigo: **rejeitada**, não
   usada como evidência. Uma tentativa de página de citação do OTexts
   retornou 404: também não valida edição/ano. Ambas estão nos recibos.
5. Não se concluiu que DOI com 403/202/Client Challenge seja inválido.
   Também não se chamou de texto integral uma página de encaminhamento,
   aplicação JavaScript ou HTML vazio com HTTP 200.
6. Documentação NASA/Google/NumPy/Streamlit justifica contratos técnicos,
   não eficácia agronômica. Sentinel Hub é exemplo de fornecedor.
   EOSDA/OneSoil não são ensaios independentes; suas promessas de ROI e
   precisão não foram incorporadas ao artigo. Spec Kit/Böckeler são fontes
   técnicas de terminologia, complementadas pelos trabalhos científicos
   de requisitos, rastreabilidade e supervisão já existentes.
7. A tabela de plataformas continua comparação documental por finalidade.
   A página atual da OneSoil sustenta monitoramento, clima, exportação,
   Mobile/Pro e comparação entre safras; pormenores de desenho/upload,
   limites e assinaturas conservam a rastreabilidade histórica anterior,
   sem alegar que todos os planos foram testados nesta rodada.
8. Preservadas as fontes clássicas. Slaiffer 2023/2025 são trabalhos
   relacionados, não duplicatas indevidas. Não há DOI repetido entre as
   54 entradas impressas. Duplicatas potenciais **não citadas** não foram
   apagadas para não descartar histórico fora da necessidade editorial.

## 7. Validação, comparação e reprodução

- A base bibliográfica canônica é `referencias_normalizadas.bib`.
  `scripts/preparar_bib_dcu.py` gera `referencias_institucionais.bib`.
  Não houve edição manual de `.bbl` ou do estilo `dcu`.
- Os únicos arquivos preexistentes modificados nesta tarefa são a base,
  o adaptador, sua projeção, o PDF e os dois registros de auditoria
  complementados. O manifesto anterior inclui alterações locais já
  existentes: não se usou `git diff HEAD` para atribuí-las a esta revisão.
- Todos os `.tex` científicos, classe, configuração autoral condicional,
  Abstract/Resumo, macros, imagens, dados, resultados e aplicação mantêm
  os hashes anteriores. As citações e eventuais sufixos são gerados pelo
  estilo institucional; “and” foi preservado.
- Comparação textual, visual e de links está em `validacao.json` e
  `INSPECAO_VISUAL.md`. A mudança automática de 2019 para 2026 na citação
  BIPM não é reescrita da seção. As referências podem redistribuir-se
  dentro das páginas finais devido ao título/URL normativos completos.
- Páginas de referências 30–32 renderizadas e inspecionadas por IA:
  sem sobreposição, corte de URL ou invasão da coluna adjacente.
  Isso não substitui revisão humana nem prova física de impressão.
- O snapshot em **`docs/envio_professor/` não foi sincronizado**: continua
  sendo a entrega anterior independente. Seu ZIP/PDF não deve ser confundido
  com a versão bibliograficamente atualizada de `docs/artigo_final/`.

Reprodução, com Python contendo `pybtex` e Tectonic disponível:

```sh
python3 docs/artigo_final/scripts/preparar_bib_dcu.py
```

Em cópia isolada das dependências, sem arquivos auxiliares prévios:

```sh
tectonic -X compile Relatorio_Final.tex --outdir DIRETORIO_LIMPO --keep-logs --keep-intermediates
```

O arquivo `validacao.json` registra hashes, contagens e resultados verificáveis.
Scripts auxiliares de coleta/validação estão nas evidências para rastreabilidade;
as dependências foram instaladas apenas em ambiente temporário, sem alterar
as dependências da aplicação. **Sem commit ou push.**
