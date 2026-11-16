# Auditoria das referências

## Terceira rodada — 15–16/11/2026

A retomada concentrou-se nas pendências citadas, sem expansão bibliográfica: **nenhuma entrada adicionada, removida ou substituída; 60 entradas preservadas**. As novas verificações abaixo sucedem os pareceres históricos de acesso, não alteram retrospectivamente o que foi lido antes.

| Referência | Acesso efetivo e localizador | Correspondência com a redação atual |
|---|---|---|
| Davis (1989), DOI 10.2307/249008 | PDF de 23 páginas, incluindo capa JSTOR, disponibilizado pela Universität Potsdam: `https://openup.uni-potsdam.de/pluginfile.php/210025/mod_folder/content/0/Davis1989.pdf?forcedownload=1`. Autoria, *MIS Quarterly* 13(3),319–340 e título conferidos. Lidos resumo, definições p.320 e discussão/limitações p.333–334. SHA-256 `c3d1633543e23cda23cd577fd80f6796742853ab3b3c9b0c2f08bab1dfc444e7` | Resolvida a pendência de acesso para o escopo utilizado: utilidade percebida ≠ facilidade percebida; intenção/autorrelato ≠ uso observado. O questionário não foi convertido em TAM validado e não reproduz as escalas de seis itens do estudo. |
| Braun e Clarke (2006), DOI 10.1191/1478088706qp063oa | PDF integral de 25 páginas em domínio UWE: `https://www2.uwe.ac.uk/services/Marketing/students/Newstudents/HAS/Using%20thematic%20analysis%20in%20psychology.pdf`. Autoras, periódico 3,77–101 e DOI conferidos. Lidos definição p.79, prevalência pp.82–83, indução/semântica pp.83–84 e Tabela1/p.87. SHA-256 `722a8f1350d575169fc4d3bf4835a8ca290afbf0471f61469da4b521092e3b48` | Resolvida a pendência de acesso para a referência conceitual. O artigo descreve codificação semântica assistida, categorias do corpus e contagem por submissão. Não alega execução integral das seis fases, saturação ou dupla codificação. Frequência não foi equiparada a importância analítica. |
| Gorelick et al. (2017), DOI 10.1016/j.rse.2017.06.031 | Página Google Research efetivamente lida: `https://research.google/pubs/google-earth-engine-planetary-scale-geospatial-analysis-for-everyone/`, com seis autores, *RSE*202,18–27 e resumo. Manuscrito aberto da editora retornou403 | Confirmação primária do escopo geral da infraestrutura em nuvem; leitura integral continua pendente. Sem importação de alegações de desempenho. Contratos operacionais são sustentados pela documentação oficial já examinada. |
| Amani et al. (2020), DOI 10.1109/JSTARS.2020.3021052 | Retomada da busca e tentativa IEEE sem obtenção de texto verificável; o endpoint consultado não constitui validação do identificador do documento | Mantido parecer parcial. A menção foi limitada ao tema da revisão, sem resultados quantitativos ou características não conferidas atribuídas a ela. |
| McFeeters (1996), DOI 10.1080/01431169608948714 | Novo acesso à página DOI da editora retornou403; buscas recuperaram registro/resumo, não texto primário integral | Parecer parcial preservado. A distinção de finalidade água superficial permanece; a formulação NIR–SWIR da plataforma não é atribuída ao estudo. Conferência direta da fórmula verde–NIR no original ainda necessária. |
| ISO 9241-11:2018 | Mantido escopo já verificado no resumo oficial, sem nova alegação de leitura do texto pago | Quadro conceitual, não certificação normativa de usabilidade ou método obrigatório. |

Os PDFs científicos permaneceram em cache privado, sem republicação. O registro de consultas desta rodada está em `../evidencias/terceira_rodada/consultas_fontes.json`. Não foram inseridas Peters, Griffiths, Flood, Rembold, de Jong ou Pohjankukka como se tivessem sido lidas ou validassem os parâmetros. O precedente científico específico B8A/B11 continua pendente; o exemplo técnico e a definição operacional são explicitados.

O histórico sobre indisponibilidade bibliográfica e exclusão do EO Browser foi retirado do artigo e mantido aqui. A representação atual de centros de bandas dispensa reconstruir curvas de alvos sem fonte específica. O conjunto citado é coerente no escopo delimitado; **não se declara validação primária integral de todas as referências**.

## Atualização PA01–PA18 — novas consultas e alterações

15/11/2026. Base `f31d0a5`, com 52 entradas; **oito entradas adicionadas, nenhuma removida ou substituída**. As entradas sem uso não foram apresentadas como fontes validadas por tema semelhante. Os pareceres individuais R01–R52 abaixo permanecem, com suas restrições; este complemento não os converte em leitura integral.

| Chave / identificação | Acesso e localização efetiva | Afirmação inserida / limites |
|---|---|---|
| `MERONI2019` — Meroni, Fasbender, Rembold, Atzberger e Klisch; *Remote Sensing of Environment* 221, 508–521 (2019); DOI 10.1016/j.rse.2018.11.041 | Texto integral público PMC6360378, CC BY; §2, Eq.1/§3.1, Tabela2, §3.2.3 | Padronização de NDVI e limiar −1; referência histórica sazonal e estágios de consolidação diferem de janela3. Não valida heurística implementada. |
| `PARNAS1972` — D. L. Parnas; *Communications of the ACM* 15(12), 1053–1058 (1972); DOI 10.1145/361598.361623 | PDF público em domínio universitário TU/e; p.1054, *What Is Modularization?*, e discussão das duas decomposições; resumo/critério de ocultação de decisões | Responsabilidades e fronteiras de módulos; não demonstra ganho de manutenibilidade medido no TCC. |
| `NIST_LOCATION` — NIST, *Measures of Location*, e-Handbook; sem ano editorial identificado; sem DOI específico declarado | Página oficial integral §1.3.5.1, definições de média/mediana e exemplo Cauchy | Mediana par/ímpar e sensibilidade a extremos. Fonte técnica estatística, não estudo Sentinel-2. |
| `GITHUB_SDD` — GitHub, *Specification-Driven Development*, documentação Spec Kit; sem ano editorial identificado; sem DOI | Markdown integral oficial, *The SDD Workflow in Practice* e *Core Principles* | Especificações como artefatos orientadores; fonte técnica, não validação experimental ou prova de uso do toolkit neste projeto. |
| `BOECKELER2025` — Birgitta Böckeler, *Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl*, 15/10/2025; sem DOI | Artigo técnico integral no site de Martin Fowler; *Definition*, *What is a spec?*, *Observations and questions* | Diferentes níveis e riscos de SDD; não é artigo revisado por pares ou evidência de superioridade. |
| `UPF_IA2026` — Universidade de Passo Fundo, IN nº03/2026/PROACAD, 28/10/2026; sem DOI | PDF oficial, 5 páginas, íntegra e anexo, obtido por link público da UPF | Arts.3–8/10–11; declaração e exigência de autorização/limites formais. Não comprova que o projeto recebeu essa autorização. |
| `EOSDA_GUIDE` — EOS Data Analytics, *Crop Monitoring User Guide*, sem data editorial identificada/DOI | Guia oficial integral; seções *Add field*, *Work With Crop Map*, *Monitoring*, *Weather* e página *Account And Pricing* | Matriz por funcionalidade; origem/comercialidade documentada. Leitura por cursor existe no produto; arquitetura local não estabelecida. Promessas agronômicas comerciais não adotadas como resultados. |
| `ONESOIL_PLATFORM_DETAIL` — OneSoil, *Platform*, sem data editorial identificada/DOI | Página detalhada integral; funcionalidades e FAQ de produtos, assinaturas, exportações e campos | Matriz de produto final, plataformas web/móvel, limites e assinaturas; não certifica desempenho nem equivalência das saídas. |
| `IZQUIERDO2026` — entrada existente, DOI10.3390/agronomy16050541 | PDF integral público IVIA `2026_Izquierdo-Sanz_Hybrid.pdf`, p.5/Tabela1 e §§2.3–2.4 | Confirmada fórmula exata B8/B11 chamada NDMI; suporte específico ampliado, sem nova entrada duplicada. |
| `ISO9241_2018` — entrada existente | Resumo oficial reconferido: quadro conceitual, usabilidade como resultado e ausência de método obrigatório; **não** texto integral pago | Afirmação atual restringe-se a esse conteúdo diretamente acessado; nenhuma definição normativa adicional foi atribuída. |

URLs públicas estão nas entradas BibTeX e no registro de acessos da rodada. Hashes dos conteúdos obtidos são evidência de identidade do arquivo consultado, não prova isolada de leitura. PDFs científicos ficam em cache local, sem republicação automática.

### Candidatas não incorporadas

| Candidata | Consulta / decisão |
|---|---|
| Pohjankukka et al. (2025), *Geoderma*455,117216, DOI10.1016/j.geoderma.2025.117216 | Título e registro localizados: *Digital mapping of peat thickness and extent in Finland using remote sensing and machine learning*. Jukuri e Helda devolveram desafios anti-bot; editora não forneceu texto. Não confirmada fórmula B8A/B11; não inserida. Link legítimo: https://helda.helsinki.fi/items/1665caeb-2541-4f9e-88ba-f0752cf39e2d |
| Peters et al. (2002), *Drought Monitoring with NDVI-Based Standardized Vegetation Index* | Registro e referências secundárias localizados, 68(1),71–75; URL tentada no ASPRS retornou404. Texto integral não lido; não transposto de Meroni como leitura primária. |
| Griffiths et al. (2013), *A Pixel-Based Landsat Compositing Algorithm for Large Area Land Cover Mapping* | Registro encontrado, sem leitura primária suficiente; composição por critérios/ponderação não equiparada à mediana simples. |
| Flood (2013), *Seasonal Composite Landsat TM/ETM+ Images Using the Medoid (a Multi-Dimensional Median)* | MDPI403; título e distinção medoid/mediana identificados, mas sem leitura primária nova. Não inserido como fundamento exato da Eq.4. |
| Rembold et al. (2019), DOI10.1016/j.agsy.2018.07.002 | Resumo e autoria no JRC109950; não se obteve texto integral. A descrição acadêmica de ASAP no artigo usa Meroni, texto lido, sem atribuir equivalência ao algoritmo local. |
| de Jong et al. (2011), DOI10.1016/j.rse.2010.10.011 | Registro ZORA encontrado; acesso apresentou Anubis, não texto. Não utilizado para ±0,01. |
| Amani, Gorelick, McFeeters, Davis, Braun/Clarke | Continuam com as restrições primárias registradas anteriormente. A autorização para manter não é certificação de leitura integral. |
| Chaves, Araujo, Phiri, Wazlawick, Lovato | Não citadas substantivamente no texto atual; registros mantidos sem substituição fictícia. Pendências de metadados/acesso não foram apagadas. |

**Resultado: auditoria individual com pareceres disponível, mas validação bibliográfica integral ainda não concluída.**

Data: 15/11/2026. Inventário de todas as 34 entradas originais e das novas. **Auditada não significa validada integralmente.** Os pareceres delimitam acesso, leitura e suporte; HTTP 200, DOI e snippets não comprovam conteúdo.

Os blocos BibTeX preservam autoria/ordem, título, ano, veículo, volume/número/páginas e URL tal como registrados. Campos não confirmados não são corrigidos por suposição. Acesso integral disponível significa documento obtido, não leitura de todas as páginas.

## Normalização

Classe local CC-EC_TF-TC v1.1, opção alpha-refs, natbib/dcu; mantida sem substituir por ABNT. Datas de acesso novas são 15/11/2026. Datas anteriores foram preservadas como histórico, não certificadas retroativamente. Ano de acesso não deve ser presumido como ano de publicação de página dinâmica. Entradas institucionais sem ano conservam nota explícita; padronização de s.d. depende do modelo. Tipos mastersthesis de TCCs e duplicação Rouse ainda requerem normalização. Nomes estendidos de Weiss não foram certificados somente a partir das iniciais do PDF.

## R01 — ESA_SENTINEL2

- Origem: original; tipo BibTeX: `misc`.
- Localização: final_2_fundamentacao.tex.
- Evidência: `bib_ESA_SENTINEL2`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Missão MSI, 13 bandas, resoluções e revisita nominal; documentação oficial.
- Decisão: Manter; não confundir revisita com pontos válidos.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{ESA_SENTINEL2,
author = {{European Space Agency} and {Copernicus}},
  title = {{Sentinel-2 Mission}},
  year = {2026},
  note = {Disponível em \url{https://sentiwiki.copernicus.eu/web/s2-mission}. Acessado em 24 jun 2026}
}
```

## R02 — GOOGLE_S2_SR

- Origem: original; tipo BibTeX: `misc`.
- Localização: final_2_fundamentacao.tex, final_3_metodos.tex, fig/conceitos.tex.
- Evidência: `ee_s2`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Catálogo completo: bandas/centros/resoluções, escala 0,0001, ausência B10, harmonização e intervalo QA60.
- Decisão: Manter; fronteira documental QA60 preservada sem inventar resolução da inconsistência de datas.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{GOOGLE_S2_SR,
author = {{Google}},
  title = {{Harmonized Sentinel-2 MSI: MultiSpectral Instrument, Level-2A (SR)}},
  year = {2026},
  note = {Disponível em \url{https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED}. Acesso em 15 nov. 2026}
}
```

## R03 — GOOGLE_EE_ND

- Origem: original; tipo BibTeX: `misc`.
- Localização: final_2_fundamentacao.tex.
- Evidência: `bib_GOOGLE_EE_ND`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Contrato normalizedDifference, razão e máscara de entradas negativas.
- Decisão: Manter; não extrapolar para validação agronômica ou casos-limite remotos não executados.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{GOOGLE_EE_ND,
author = {{Google}},
  title = {{ee.Image.normalizedDifference}},
  year = {2026},
  note = {Disponível em \url{https://developers.google.com/earth-engine/apidocs/ee-image-normalizeddifference}. Acessado em 24 jun 2026}
}
```

## R04 — GOOGLE_EE_DATE

- Origem: original; tipo BibTeX: `misc`.
- Localização: final_3_metodos.tex.
- Evidência: `bib_GOOGLE_EE_DATE`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Contrato de início inclusivo e término exclusivo.
- Decisão: Manter; aplicação acrescenta um dia ao término.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{GOOGLE_EE_DATE,
author = {{Google}},
  title = {{ee.Filter.date}},
  year = {2026},
  note = {Disponível em \url{https://developers.google.com/earth-engine/apidocs/ee-filter-date}. Acessado em 11 nov 2026}
}
```

## R05 — GOOGLE_EE_SERVICE_ACCOUNT

- Origem: original; tipo BibTeX: `misc`.
- Localização: final_3a_implementacao.tex.
- Evidência: `bib_GOOGLE_EE_SERVICE_ACCOUNT`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Documentação oficial de autenticação por conta de serviço.
- Decisão: Manter; conta autentica aplicação, não visitante.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{GOOGLE_EE_SERVICE_ACCOUNT,
author = {{Google}},
  title = {Service Accounts: {Google Earth Engine}},
  year = {2026},
  note = {Disponível em \url{https://developers.google.com/earth-engine/guides/service_account}. Acesso em 15 nov. 2026}
}
```

## R06 — GOOGLE_EE_NONCOMMERCIAL

- Origem: original; tipo BibTeX: `misc`.
- Localização: final_5_discussao.tex.
- Evidência: `bib_GOOGLE_EE_NONCOMMERCIAL`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Página oficial de modalidades não comerciais; não comprova elegibilidade individual do projeto.
- Decisão: Manter como contexto; não prometer gratuidade irrestrita.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{GOOGLE_EE_NONCOMMERCIAL,
author = {{Google}},
  title = {Noncommercial tiers: {Google Earth Engine}},
  year = {2026},
  note = {Disponível em \url{https://developers.google.com/earth-engine/guides/noncommercial_tiers}. Acesso em 15 nov. 2026}
}
```

## R07 — STREAMLIT_CLOUD_SECRETS

- Origem: original; tipo BibTeX: `misc`.
- Localização: final_3a_implementacao.tex.
- Evidência: `bib_STREAMLIT_CLOUD_SECRETS`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Página oficial de Secrets do Community Cloud.
- Decisão: Manter; confirmar configuração efetiva via código sem divulgar segredos.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{STREAMLIT_CLOUD_SECRETS,
author = {{Streamlit}},
  title = {Secrets management for your Community Cloud app},
  year = {2026},
  note = {Disponível em \url{https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management}. Acesso em 15 nov. 2026}
}
```

## R08 — SLAIFFER2023

- Origem: original; tipo BibTeX: `mastersthesis`.
- Localização: final_2_fundamentacao.tex.
- Evidência: `slaiffer2023`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Registro/resumo institucional: índices e produtividade de soja irrigada/sequeiro.
- Decisão: Complementar com artigo de 2025 lido em métodos; não presumir equivalência integral entre TCC e publicação.
- Status: Parcialmente validado / pendente de comprovação.

```bibtex
@mastersthesis{SLAIFFER2023,
author = {Slaiffer, Henrique},
  title = {Índices de vegetação e sua correlação com a produtividade da cultura da soja em área irrigada e de sequeiro},
  school = {Universidade Federal de Santa Maria},
  type = {Trabalho de Conclusão de Curso em Engenharia Agrícola},
  year = {2023},
  note = {Disponível em \url{https://repositorio.ufsm.br/handle/1/29995}. Acesso em 11 nov. 2026}
}
```

## R09 — LOVATO2021

- Origem: original; tipo BibTeX: `mastersthesis`.
- Localização: não citada no manuscrito atual.
- Evidência: `bib_LOVATO2021`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Consulta ao repositório UNESP expirou; texto e metadados integrais não conferidos.
- Decisão: Manter registro não citado, pendente de comprovação; não usar como apoio substantivo.
- Status: Parcialmente validado / pendente de comprovação.

```bibtex
@mastersthesis{LOVATO2021,
author = {Lovato, João Guilherme Lopes},
  title = {Identificação de áreas de renovação da cultura da cana-de-açúcar por meio de índice de vegetação e técnicas de sensoriamento remoto},
  school = {Universidade Estadual Paulista},
  type = {Trabalho de Conclusão de Curso em Engenharia Agronômica},
  year = {2021},
  address = {Jaboticabal},
  note = {Disponível em \url{https://repositorio.unesp.br/entities/publication/b9caa0ff-8be4-44b6-ba3d-e40bbfa7e275}. Acesso em 11 nov. 2026}
}
```

## R10 — ARAUJO2025

- Origem: original; tipo BibTeX: `article`.
- Localização: não citada no manuscrito atual.
- Evidência: `consulta/metadados descritos no parecer`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Crossref retornou 404 para DOI Zenodo, que usa outro registrador; isso não prova inexistência.
- Decisão: Não citado; existência, autores e suporte ainda pendentes. Não remover por 404.
- Status: Parcialmente validado / pendente de comprovação.

```bibtex
@article{ARAUJO2025,
author = {Araujo, Ralph Wendel Oliveira de and Cruz, Samir Herick Menezes da and Sousa, Deivson Nacim Teixeira and Cardoso, Ariston de Lima and Ribeiro, Ossival Lolato},
  title = {Utilização de imageamento multiespectral por satélite para monitoramento de ciclo fenológico da cultura da soja},
  journal = {Boletim de Conjuntura (BOCA)},
  volume = {23},
  number = {67},
  pages = {197--224},
  year = {2025},
  note = {\url{https://doi.org/10.5281/zenodo.15871939}}
}
```

## R11 — CHAVES2019

- Origem: original; tipo BibTeX: `phdthesis`.
- Localização: não citada no manuscrito atual.
- Evidência: `bib_CHAVES2019`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Consulta ao repositório UFLA expirou; conteúdo não conferido.
- Decisão: Não citado; manter registro provisório sem alegar validação.
- Status: Parcialmente validado / pendente de comprovação.

```bibtex
@phdthesis{CHAVES2019,
author = {Chaves, Michel Eustáquio Dantas},
  title = {Uso das séries temporais de índices de vegetação para o monitoramento agrícola no Estado de Mato Grosso},
  school = {Universidade Federal de Lavras},
  year = {2019},
  address = {Lavras},
  note = {Disponível em \url{https://repositorio.ufla.br/items/62ad79ab-a7b3-400b-ad28-5779e424f3d3}. Acesso em 11 nov. 2026}
}
```

## R12 — NASA_POWER_DAILY

- Origem: original; tipo BibTeX: `misc`.
- Localização: final_1_introducao.tex, final_2_fundamentacao.tex, final_3_metodos.tex.
- Evidência: `power_daily`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Documentação do serviço diário: UTC/LST, datas, parâmetros e limites.
- Decisão: Manter e complementar com metodologia/dicionário de parâmetros.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{NASA_POWER_DAILY,
author = {{NASA}},
  title = {{{NASA POWER}: Daily API}},
  year = {2026},
  note = {Disponível em \url{https://power.larc.nasa.gov/docs/services/api/temporal/daily/}. Acesso em 15 nov. 2026}
}
```

## R13 — ROUSE1973

- Origem: original; tipo BibTeX: `inproceedings`.
- Localização: não citada no manuscrito atual.
- Evidência: `rouse_pdf`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Possível duplicação de ROUSE1974_NTRS: evento 1973/publicação NASA 1974, p. 309–317.
- Decisão: Não citado; conservar até normalização pelo autor. Não contar como nova fonte independente.
- Status: Parcialmente validado / pendente de comprovação.

```bibtex
@inproceedings{ROUSE1973,
author = {Rouse, J. W. and Haas, R. H. and Schell, J. A. and Deering, D. W.},
  title = {Monitoring Vegetation Systems in the Great Plains with {ERTS}},
  booktitle = {Third Earth Resources Technology Satellite Symposium},
  year = {1973},
  pages = {309--317},
  publisher = {NASA},
  address = {Washington, DC}
}
```

## R14 — GAO1996

- Origem: original; tipo BibTeX: `article`.
- Localização: final_2_fundamentacao.tex.
- Evidência: `gao_pdf`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: PDF, resumo/introdução/formulação: 0,86/1,24 µm, saturação NDVI e efeito de solo residual.
- Decisão: Manter; título/autoria/ano/58(3):257–266/DOI conferidos. Não atribuir B8/B11 diretamente.
- Status: Validado no escopo delimitado acima.

```bibtex
@article{GAO1996,
author = {Gao, Bo-Cai},
  title = {{NDWI}: A Normalized Difference Water Index for Remote Sensing of Vegetation Liquid Water from Space},
  journal = {Remote Sensing of Environment},
  volume = {58},
  number = {3},
  pages = {257--266},
  year = {1996},
  note = {\url{https://doi.org/10.1016/S0034-4257(96)00067-3}}
}
```

## R15 — PATRICIO2018

- Origem: original; tipo BibTeX: `article`.
- Localização: final_2_fundamentacao.tex.
- Evidência: `patricio_pdf`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: PDF Embrapa, identificação e seções iniciais de revisão: visão computacional/IA em culturas de grãos.
- Decisão: Manter para contexto computacional agrícola; não sustenta qualquer decisão desta plataforma.
- Status: Validado no escopo delimitado acima.

```bibtex
@article{PATRICIO2018,
author = {Patrício, Diego Inácio and Rieder, Rafael},
  title = {Computer Vision and Artificial Intelligence in Precision Agriculture for Grain Crops: A Systematic Review},
  journal = {Computers and Electronics in Agriculture},
  volume = {153},
  pages = {69--81},
  year = {2018},
  publisher = {Elsevier},
  note = {\url{https://doi.org/10.1016/j.compag.2018.08.001}}
}
```

## R16 — GORELICK2017

- Origem: original; tipo BibTeX: `article`.
- Localização: final_1_introducao.tex, final_2_fundamentacao.tex.
- Evidência: `gorelick`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Metadados DOI conferidos; página do editor bloqueada, texto integral não lido.
- Decisão: Manter com validação parcial; características técnicas devem apoiar-se também na documentação oficial.
- Status: Parcialmente validado / pendente de comprovação.

```bibtex
@article{GORELICK2017,
author = {Gorelick, Noel and Hancher, Matt and Dixon, Mike and Ilyushchenko, Simon and Thau, David and Moore, Rebecca},
  title = {{Google Earth Engine}: Planetary-scale geospatial analysis for everyone},
  journal = {Remote Sensing of Environment},
  volume = {202},
  pages = {18--27},
  year = {2017},
  publisher = {Elsevier},
  note = {\url{https://doi.org/10.1016/j.rse.2017.06.031}}
}
```

## R17 — AMANI2020

- Origem: original; tipo BibTeX: `article`.
- Localização: final_2_fundamentacao.tex.
- Evidência: `amani_pdf`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Metadados DOI conferidos; resposta 200 não é PDF, acesso bloqueado.
- Decisão: Manter com validação parcial; não afirmar exame integral da revisão.
- Status: Parcialmente validado / pendente de comprovação.

```bibtex
@article{AMANI2020,
author = {Amani, Meisam and Ghorbanian, Arsalan and Ahmadi, Seyed Ali and Kakooei, Mohammad and Moghimi, Armin and Mirmazloumi, S. Mohammad and Moghaddam, Sayyed Hamed Alizadeh and Mahdavi, Sahel and Ghahremanloo, Masoud and Parsian, Saeid and Wu, Qiusheng and Brisco, Brian},
  title = {{Google Earth Engine} Cloud Computing Platform for Remote Sensing Big Data Applications: A Comprehensive Review},
  journal = {IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing},
  volume = {13},
  pages = {5326--5350},
  year = {2020},
  publisher = {IEEE},
  note = {\url{https://doi.org/10.1109/JSTARS.2020.3021052}}
}
```

## R18 — WEISS2020

- Origem: original; tipo BibTeX: `article`.
- Localização: final_1_introducao.tex, final_2_fundamentacao.tex, fig/conceitos.tex.
- Evidência: `weiss_pdf`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Postprint HAL/INRAE; introdução e seção 2.2.1: calibração empírica e condições de aquisição/cultura.
- Decisão: Manter. Não confirma origem exata das curvas qualitativas da figura; fonte primária adicional seria preferível para esse desenho.
- Status: Validado no escopo delimitado acima.

```bibtex
@article{WEISS2020,
author = {Weiss, Marie and Jacob, Frédéric and Duveiller, Gregory},
  title = {Remote sensing for agricultural applications: A meta-review},
  journal = {Remote Sensing of Environment},
  volume = {236},
  pages = {111402},
  year = {2020},
  publisher = {Elsevier},
  note = {\url{https://doi.org/10.1016/j.rse.2019.111402}}
}
```

## R19 — PHIRI2020

- Origem: original; tipo BibTeX: `article`.
- Localização: não citada no manuscrito atual.
- Evidência: `consulta/metadados descritos no parecer`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: DOI confirma publicação; divergência Salekin: BibTeX Sharif versus Crossref Serajis.
- Decisão: Não citado; conferir PDF/editor antes de corrigir autoria. Texto integral não verificado.
- Status: Parcialmente validado / pendente de comprovação.

```bibtex
@article{PHIRI2020,
author = {Phiri, Darius and Simwanda, Matamyo and Salekin, Sharif and Nyirenda, Vincent R. and Murayama, Yuji and Ranagalage, Manjula},
  title = {Sentinel-2 Data for Land Cover/Use Mapping: A Review},
  journal = {Remote Sensing},
  volume = {12},
  number = {14},
  pages = {2291},
  year = {2020},
  publisher = {MDPI},
  note = {\url{https://doi.org/10.3390/rs12142291}}
}
```

## R20 — WAZLAWICK2014

- Origem: original; tipo BibTeX: `book`.
- Localização: não citada no manuscrito atual.
- Evidência: `consulta/metadados descritos no parecer`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Livro sem URL no registro; edição/ano e conteúdo não verificados em exemplar.
- Decisão: Não citado; não usar para classificar metodologia sem consultar edição efetiva.
- Status: Parcialmente validado / pendente de comprovação.

```bibtex
@book{WAZLAWICK2014,
author = {Wazlawick, Raul Sidnei},
  title = {Metodologia de Pesquisa para Ciência da Computação},
  publisher = {Elsevier},
  year = {2014},
  edition = {2},
  address = {Rio de Janeiro}
}
```

## R21 — WAZLAWICK2020

- Origem: original; tipo BibTeX: `misc`.
- Localização: não citada no manuscrito atual.
- Evidência: `bib_WAZLAWICK2020`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: URL retorna aplicação/biblioteca, não exemplar legível.
- Decisão: Não citado; edição/ano e conteúdo pendentes, possível atualização/substituição da edição de 2014 a decidir.
- Status: Parcialmente validado / pendente de comprovação.

```bibtex
@misc{WAZLAWICK2020,
author = {Wazlawick, Raul Sidnei},
  title = {Metodologia de Pesquisa para Ciência da Computação},
  year = {2020},
  publisher = {Grupo GEN},
  edition = {3},
  note = {Disponível em \url{https://integrada.minhabiblioteca.com.br/books/9788595157712}. Acessado em 31 mar 2025}
}
```

## R22 — MCFEETERS1996

- Origem: original; tipo BibTeX: `article`.
- Localização: final_2_fundamentacao.tex.
- Evidência: `mcfeeters`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Metadados DOI conferidos; texto do editor bloqueado.
- Decisão: Manter com validação parcial. Distinção verde–NIR precisa de confirmação primária integral; não alegar leitura.
- Status: Parcialmente validado / pendente de comprovação.

```bibtex
@article{MCFEETERS1996,
author = {McFeeters, S. K.},
  title = {The use of the Normalized Difference Water Index ({NDWI}) in the delineation of open water features},
  journal = {International Journal of Remote Sensing},
  year = {1996},
  volume = {17},
  number = {7},
  pages = {1425--1432},
  note = {\url{https://doi.org/10.1080/01431169608948714}}
}
```

## R23 — USGS_NDMI

- Origem: original; tipo BibTeX: `misc`.
- Localização: final_2_fundamentacao.tex.
- Evidência: `bib_USGS_NDMI`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Página oficial: NDMI NIR–SWIR para Landsat, bandas por geração.
- Decisão: Manter; não é validação de B8A/B11 Sentinel-2.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{USGS_NDMI,
author = {{U.S. Geological Survey}},
  title = {Normalized Difference Moisture Index},
  note = {Disponível em \url{https://www.usgs.gov/landsat-missions/normalized-difference-moisture-index}. Acesso em 15 nov. 2026. Sem data de publicação identificada}
}
```

## R24 — GOOGLE_EE_SAMPLE

- Origem: original; tipo BibTeX: `misc`.
- Localização: final_3a_implementacao.tex.
- Evidência: `bib_GOOGLE_EE_SAMPLE`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Contrato sampleRectangle: matriz por banda/projeção e valores padrão.
- Decisão: Manter para método de extração; origem da grade vem do código.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{GOOGLE_EE_SAMPLE,
author = {{Google}},
  title = {{ee.Image.sampleRectangle}},
  note = {Disponível em \url{https://developers.google.com/earth-engine/apidocs/ee-image-samplerectangle}. Acesso em 15 nov. 2026. Sem data de publicação identificada}
}
```

## R25 — GOOGLE_EE_MEDIAN

- Origem: original; tipo BibTeX: `misc`.
- Localização: final_2_fundamentacao.tex.
- Evidência: `bib_GOOGLE_EE_MEDIAN`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Contrato ImageCollection.median: mediana por pixel entre bandas correspondentes.
- Decisão: Manter; não inventar justificativa histórica da escolha.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{GOOGLE_EE_MEDIAN,
author = {{Google}},
  title = {{ee.ImageCollection.median}},
  note = {Disponível em \url{https://developers.google.com/earth-engine/apidocs/ee-imagecollection-median}. Acesso em 15 nov. 2026. Sem data de publicação identificada}
}
```

## R26 — GOOGLE_EE_REDUCE

- Origem: original; tipo BibTeX: `misc`.
- Localização: final_2_fundamentacao.tex, final_3_metodos.tex.
- Evidência: `bib_GOOGLE_EE_REDUCE`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Contrato reduceRegion: escala, projeção e maxPixels.
- Decisão: Complementar com guia Statistics of an Image Region para pesos exatos.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{GOOGLE_EE_REDUCE,
author = {{Google}},
  title = {{ee.Image.reduceRegion}},
  note = {Disponível em \url{https://developers.google.com/earth-engine/apidocs/ee-image-reduceregion}. Acesso em 15 nov. 2026. Sem data de publicação identificada}
}
```

## R27 — NOMINATIM_POLICY

- Origem: original; tipo BibTeX: `misc`.
- Localização: final_5_discussao.tex.
- Evidência: `bib_NOMINATIM_POLICY`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Política oficial de uso do endpoint público.
- Decisão: Manter; código fornece User-Agent, mas atendimento integral da política requer exame operacional separado.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{NOMINATIM_POLICY,
author = {{OpenStreetMap Foundation}},
  title = {Nominatim Usage Policy},
  note = {Disponível em \url{https://operations.osmfoundation.org/policies/nominatim/}. Acesso em 15 nov. 2026. Sem data de publicação identificada}
}
```

## R28 — ROUSE1974_NTRS

- Origem: original; tipo BibTeX: `inproceedings`.
- Localização: final_2_fundamentacao.tex.
- Evidência: `rouse_pdf`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: PDF NASA, p. 309–313, especialmente Spectral Analysis: BRP e TVI; lista dos quatro autores.
- Decisão: Manter e esclarecer base histórica, não adaptação Sentinel-2; campo páginas pode ser complementado.
- Status: Validado no escopo delimitado acima.

```bibtex
@inproceedings{ROUSE1974_NTRS,
author = {Rouse, Jr., J. W. and Haas, R. H. and Schell, J. A. and Deering, D. W.},
  title = {Monitoring vegetation systems in the Great Plains with {ERTS}},
  booktitle = {Third Earth Resources Technology Satellite-1 Symposium, Volume 1, Section A},
  publisher = {NASA},
  year = {1974},
  note = {Registro NASA NTRS 19740022614. Disponível em \url{https://ntrs.nasa.gov/citations/19740022614}. Acesso em 15 nov. 2026}
}
```

## R29 — EOSDA_PLATFORM

- Origem: original; tipo BibTeX: `misc`.
- Localização: final_2_fundamentacao.tex.
- Evidência: `eosda`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Página comercial oficial: áreas, mapas/índices e funcionalidades anunciadas.
- Decisão: Manter como documentação comercial, não evidência científica; cada célula/plano da tabela ainda exige comprovação individual.
- Status: Parcialmente validado / pendente de comprovação.

```bibtex
@misc{EOSDA_PLATFORM,
author = {{EOS Data Analytics}},
  title = {{EOSDA Crop Monitoring}},
 year = {2026},
 note = {Disponível em \url{https://eos.com/products/crop-monitoring/}. Acesso em: 15 nov. 2026}
}
```

## R30 — ONESOIL_PLATFORM

- Origem: original; tipo BibTeX: `misc`.
- Localização: final_2_fundamentacao.tex.
- Evidência: `onesoil`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Página comercial oficial consultada; funcionalidades e produtos não equivalem a ensaio comparativo.
- Decisão: Manter com tabela parcialmente validada, sem deduzir ausência pelo silêncio da página.
- Status: Parcialmente validado / pendente de comprovação.

```bibtex
@misc{ONESOIL_PLATFORM,
author = {{OneSoil}},
  title = {{OneSoil} Platform},
 year = {2026},
 note = {Disponível em \url{https://onesoil.ai/en/platform}. Acesso em: 15 nov. 2026}
}
```

## R31 — ISO9241_2018

- Origem: original; tipo BibTeX: `misc`.
- Localização: final_2_fundamentacao.tex.
- Evidência: `iso`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Título e identificação normativa presentes na referência; conteúdo integral não disponível, página bloqueada nesta rodada.
- Decisão: Validação parcial; não reproduzir exigências normativas como auditadas.
- Status: Parcialmente validado / pendente de comprovação.

```bibtex
@misc{ISO9241_2018,
author = {{International Organization for Standardization}},
  title = {{ISO 9241-11:2018}: Ergonomics of human-system interaction --- Part 11: Usability: Definitions and concepts},
  year = {2018},
  note = {Resumo e metadados disponíveis em \url{https://www.iso.org/standard/63500.html}. Acesso em 15 nov. 2026}
}
```

## R32 — DAVIS1989

- Origem: original; tipo BibTeX: `article`.
- Localização: final_2_fundamentacao.tex, final_5_discussao.tex.
- Evidência: `davis`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Metadados DOI conferidos; HTML 200 é desafio, não artigo.
- Decisão: Manter com acesso integral pendente; não declarar questionário TAM validado.
- Status: Parcialmente validado / pendente de comprovação.

```bibtex
@article{DAVIS1989,
author = {Davis, Fred D.},
  title = {Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology},
  journal = {MIS Quarterly},
  volume = {13},
  number = {3},
  pages = {319--340},
  year = {1989},
  note = {\url{https://doi.org/10.2307/249008}}
}
```

## R33 — SULLIVAN2013

- Origem: original; tipo BibTeX: `article`.
- Localização: final_3_metodos.tex.
- Evidência: `sullivan`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Texto aberto sobre itens Likert, ordinalidade, distribuições e cautela na análise.
- Decisão: Manter; não confere validação psicométrica ao instrumento local.
- Status: Validado no escopo delimitado acima.

```bibtex
@article{SULLIVAN2013,
author = {Sullivan, Gail M. and Artino, Jr., Anthony R.},
  title = {Analyzing and Interpreting Data From {Likert}-Type Scales},
  journal = {Journal of Graduate Medical Education},
  volume = {5},
  number = {4},
  pages = {541--542},
  year = {2013},
  note = {\url{https://doi.org/10.4300/JGME-5-4-18}}
}
```

## R34 — BRAUN2006

- Origem: original; tipo BibTeX: `article`.
- Localização: final_3_metodos.tex.
- Evidência: `braun`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Metadados DOI conferidos; repositório bloqueado.
- Decisão: Manter com acesso pendente e aprovação da codificação; não certificar protocolo completo de análise temática.
- Status: Parcialmente validado / pendente de comprovação.

```bibtex
@article{BRAUN2006,
author = {Braun, Virginia and Clarke, Victoria},
  title = {Using thematic analysis in psychology},
  journal = {Qualitative Research in Psychology},
  volume = {3},
  number = {2},
  pages = {77--101},
  year = {2006},
  note = {\url{https://doi.org/10.1191/1478088706qp063oa}}
}
```

## R35 — QGIS_VECTOR

- Origem: adicionada; tipo BibTeX: `misc`.
- Localização: final_2_fundamentacao.tex.
- Evidência: `qgis_vector`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Documentação 3.40: entidades vetoriais e polígonos.
- Decisão: Adicionar para representação espacial; documentação técnica, não estudo agronômico.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{QGIS_VECTOR,
author = {{QGIS Project}},
 title = {A Gentle Introduction to GIS: Vector Data},
 note = {Documentação 3.40. \url{https://docs.qgis.org/3.40/en/docs/gentle_gis_introduction/vector_data.html}. Acesso em 15 nov. 2026}
}
```

## R36 — QGIS_RASTER

- Origem: adicionada; tipo BibTeX: `misc`.
- Localização: final_2_fundamentacao.tex.
- Evidência: `qgis_raster`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Documentação 3.40: células, grades, resolução e dados raster.
- Decisão: Adicionar; versão fixada, hoje indicada como versão encerrada pelo site.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{QGIS_RASTER,
author = {{QGIS Project}},
 title = {A Gentle Introduction to GIS: Raster Data},
 note = {Documentação 3.40. \url{https://docs.qgis.org/3.40/en/docs/gentle_gis_introduction/raster_data.html}. Acesso em 15 nov. 2026}
}
```

## R37 — QGIS_MAP

- Origem: adicionada; tipo BibTeX: `misc`.
- Localização: final_2_fundamentacao.tex.
- Evidência: `qgis_map`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Seções Overview e Map Legend: elementos e comunicação cartográfica.
- Decisão: Adicionar para legenda; não fundamenta avaliação perceptiva das paletas particulares.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{QGIS_MAP,
author = {{QGIS Project}},
 title = {A Gentle Introduction to GIS: Map Production},
 note = {Documentação 3.40. \url{https://docs.qgis.org/3.40/en/docs/gentle_gis_introduction/map_production.html}. Acesso em 15 nov. 2026}
}
```

## R38 — GOOGLE_EE_RESAMPLE

- Origem: adicionada; tipo BibTeX: `misc`.
- Localização: final_2_fundamentacao.tex.
- Evidência: `ee_resample`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Guia oficial: vizinho mais próximo padrão, bilinear/bicúbica explícitos.
- Decisão: Adicionar para distinguir grade de processamento e resolução física.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{GOOGLE_EE_RESAMPLE,
author = {{Google}},
 title = {Resampling and Reducing Resolution},
 note = {\url{https://developers.google.com/earth-engine/guides/resample}. Acesso em 15 nov. 2026}
}
```

## R39 — GOOGLE_EE_REGION

- Origem: adicionada; tipo BibTeX: `misc`.
- Localização: final_3_metodos.tex.
- Evidência: `ee_weight`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Guia reduceRegion: pesos, interseção, máscara e quantização de frações.
- Decisão: Adicionar; mínimo entre máscara/fração, não produto.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{GOOGLE_EE_REGION,
author = {{Google}},
 title = {Statistics of an Image Region},
 note = {\url{https://developers.google.com/earth-engine/guides/reducers_reduce_region}. Acesso em 15 nov. 2026}
}
```

## R40 — SENTINELHUB_NDMI

- Origem: adicionada; tipo BibTeX: `misc`.
- Localização: final_2_fundamentacao.tex.
- Evidência: `sentinel_ndmi`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Código B8A/B11 e texto B8/B11 na mesma página.
- Decisão: Adicionar com inconsistência explícita. Uso técnico, não prova de nomenclatura predominante ou calibração.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{SENTINELHUB_NDMI,
author = {{Sentinel Hub}},
 title = {Normalized Difference Moisture Index (NDMI)},
 note = {Custom Scripts. Texto e exemplos diferem na banda NIR. \url{https://custom-scripts.sentinel-hub.com/custom-scripts/sentinel-2/ndmi/}. Acesso em 15 nov. 2026}
}
```

## R41 — HYNDMAN2021

- Origem: adicionada; tipo BibTeX: `book`.
- Localização: final_2_fundamentacao.tex, final_3_metodos.tex.
- Evidência: `fpp_regression`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Livro aberto, seções Moving averages e Least squares estimation consultadas.
- Decisão: Adicionar para conceitos matemáticos; janela 3 e limiares não vêm do livro.
- Status: Validado no escopo delimitado acima.

```bibtex
@book{HYNDMAN2021,
author = {Hyndman, Rob J. and Athanasopoulos, George},
 title = {Forecasting: Principles and Practice},
 edition = {3},
 publisher = {OTexts},
 address = {Melbourne},
 year = {2021},
 note = {Versão on-line, seções Moving averages e Least squares estimation. \url{https://otexts.com/fpp3/}. Acesso em 15 nov. 2026}
}
```

## R42 — NIST_OUTLIERS

- Origem: adicionada; tipo BibTeX: `misc`.
- Localização: final_2_fundamentacao.tex.
- Evidência: `nist_outliers`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Seção 1.3.5.17: sinalização versus testes, padronização e advertência sobre amostras pequenas.
- Decisão: Adicionar com ressalva: aplicação usa janela anterior e divisor N, não teste NIST.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{NIST_OUTLIERS,
author = {{NIST/SEMATECH}},
 title = {e-Handbook of Statistical Methods: Detection of Outliers},
 note = {Seção 1.3.5.17. \url{https://www.itl.nist.gov/div898/handbook/eda/section3/eda35h.htm}. Acesso em 15 nov. 2026}
}
```

## R43 — NUMPY_STD

- Origem: adicionada; tipo BibTeX: `misc`.
- Localização: final_3_metodos.tex.
- Evidência: `numpy_std`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: API/documentação e notas: divisor N−ddof, ddof=0 e ddof=1.
- Decisão: Adicionar para implementação; documentação stable pode mudar em relação à versão instalada.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{NUMPY_STD,
author = {{NumPy Developers}},
 title = {numpy.std},
 note = {\url{https://numpy.org/doc/stable/reference/generated/numpy.std.html}. Acesso em 15 nov. 2026}
}
```

## R44 — NUMPY_POLYFIT

- Origem: adicionada; tipo BibTeX: `misc`.
- Localização: final_3_metodos.tex.
- Evidência: `numpy_polyfit`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: API: ajuste polinomial por mínimos quadrados, grau 1.
- Decisão: Adicionar para implementação, não validação dos limiares.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{NUMPY_POLYFIT,
author = {{NumPy Developers}},
 title = {numpy.polyfit},
 note = {\url{https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html}. Acesso em 15 nov. 2026}
}
```

## R45 — BIPM_SI

- Origem: adicionada; tipo BibTeX: `misc`.
- Localização: final_3_metodos.tex.
- Evidência: `si`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Brochura SI disponível, definições de unidades derivadas e prefixos.
- Decisão: Adicionar; identidade kWh→MJ é dedução elementar, não método agronômico.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{BIPM_SI,
author = {{Bureau International des Poids et Mesures}},
 title = {The International System of Units (SI)},
 note = {9. ed., versão on-line consultada. \url{https://www.bipm.org/documents/20126/41483022/SI-Brochure-9.pdf}. Acesso em 15 nov. 2026}
}
```

## R46 — BENDER2020

- Origem: adicionada; tipo BibTeX: `incollection`.
- Localização: final_3_metodos.tex.
- Evidência: `google_testing`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Capítulo 11 completo disponível; escopos, testes e seção A Note on Code Coverage lidos.
- Decisão: Adicionar como capítulo atribuído a Adam Bender, editores do livro separados; não imputar processos Google ao projeto.
- Status: Validado no escopo delimitado acima.

```bibtex
@incollection{BENDER2020,
author = {Bender, Adam},
 title = {Testing Overview},
 booktitle = {Software Engineering at Google: Lessons Learned from Programming Over Time},
 editor = {Winters, Titus and Manshreck, Tom and Wright, Hyrum},
 publisher = {O'Reilly Media},
 year = {2020},
 note = {Cap. 11, versão on-line. \url{https://abseil.io/resources/swe-book/html/ch11.html}. Acesso em 15 nov. 2026}
}
```

## R47 — AAPOR2013

- Origem: adicionada; tipo BibTeX: `techreport`.
- Localização: final_3_metodos.tex.
- Evidência: `aapor`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Relatório completo disponível; Executive Summary e recomendações iniciais lidos.
- Decisão: Adicionar para não probabilidade/transparência/limites inferenciais; não atribuir representatividade.
- Status: Validado no escopo delimitado acima.

```bibtex
@techreport{AAPOR2013,
author = {{American Association for Public Opinion Research}},
 title = {Report of the AAPOR Task Force on Non-Probability Sampling},
 institution = {AAPOR},
 year = {2013},
 note = {\url{https://aapor.org/wp-content/uploads/2022/11/NPS_TF_Report_Final_7_revised_FNL_6_22_13.pdf}. Acesso em 15 nov. 2026}
}
```

## R48 — SLAIFFER2025

- Origem: adicionada; tipo BibTeX: `article`.
- Localização: final_2_fundamentacao.tex.
- Evidência: `slaiffer2025_pdf`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: PDF p. 495–497, resumo e métodos: índices Crop Monitoring e produtividade da colhedora, análise espacial.
- Decisão: Adicionar como publicação posterior e comparação de desenho de evidência; não importar afirmações universais de classes agronômicas do artigo.
- Status: Validado no escopo delimitado acima.

```bibtex
@article{SLAIFFER2025,
author = {Slaiffer, Henrique and Bottega, Eduardo Leonel and Oliveira, Zanandra Boff de and Saretta, Ezequiel},
 title = {Índices de vegetação e sua correlação com a produtividade da cultura da soja em área irrigada e de sequeiro},
 journal = {Nativa},
 volume = {13},
 number = {3},
 pages = {495--502},
 year = {2025},
 note = {\url{https://doi.org/10.31413/nat.v13i3.18592}}
}
```

## R49 — IZQUIERDO2026

- Origem: adicionada; tipo BibTeX: `article`.
- Localização: final_2_fundamentacao.tex.
- Evidência: `izquierdo2026_pdf`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: PDF p. 1–5: autoria, desenho multissensor, dados FDR e proposta de validação interanual.
- Decisão: Adicionar para distinguir modelagem de umidade da plataforma. Metadados 16(5):541 conferidos; PDF diz publicação 28/02/2026, não inferir mês pelo número 5.
- Status: Validado no escopo delimitado acima.

```bibtex
@article{IZQUIERDO2026,
author = {Izquierdo-Sanz, Héctor and Moltó, Enrique},
 title = {Hybrid Physical--Machine Learning Soil Moisture Modeling at Orchard Scale in Irrigated Citrus Orchards Using Sentinel 1 and 2 and Agroclimatic Data},
 journal = {Agronomy},
 volume = {16},
 number = {5},
 pages = {541},
 year = {2026},
 note = {\url{https://doi.org/10.3390/agronomy16050541}}
}
```

## R50 — NASA_POWER_METHOD

- Origem: adicionada; tipo BibTeX: `misc`.
- Localização: final_2_fundamentacao.tex.
- Evidência: `power_sources`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Metodologia: grades de origem do arquivo principal e aliases de alta resolução.
- Decisão: Adicionar sem tratar consulta ao centroide como medida local.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{NASA_POWER_METHOD,
author = {{NASA}},
 title = {POWER Data Methodology},
 note = {\url{https://power.larc.nasa.gov/docs/methodology/}. Acesso em 15 nov. 2026}
}
```

## R51 — NASA_POWER_PARAMETERS

- Origem: adicionada; tipo BibTeX: `misc`.
- Localização: final_3_metodos.tex.
- Evidência: `power_parameters`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Dicionário JSON AG/DAILY: PRECTOTCORR, T2M, ALLSKY_SFC_SW_DWN.
- Decisão: Adicionar para definições/unidades; metadados da resposta efetiva continuam prevalecendo.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{NASA_POWER_PARAMETERS,
author = {{NASA}},
 title = {POWER Parameter Dictionary: Agricultural Community, Daily},
 note = {\url{https://power.larc.nasa.gov/api/system/manager/parameters?community=AG&temporal=DAILY}. Acesso em 15 nov. 2026}
}
```

## R52 — STREAMLIT_STATE

- Origem: adicionada; tipo BibTeX: `misc`.
- Localização: final_3a_implementacao.tex.
- Evidência: `streamlit_state`; URLs/status/hashes em CONSULTAS_FONTES.json ou CONSULTAS_COMPLEMENTARES.json.
- Conteúdo e verificação: Documentação oficial Session State lida: valores entre reruns, escopo e perda de sessão.
- Decisão: Adicionar para estado/limites de persistência; consulta adicional registrada em CONSULTAS_COMPLEMENTARES.json.
- Status: Validado no escopo delimitado acima.

```bibtex
@misc{STREAMLIT_STATE,
author = {{Streamlit}},
 title = {Add Statefulness to Apps: Session State},
 note = {\url{https://docs.streamlit.io/develop/concepts/architecture/session-state}. Acesso em 15 nov. 2026}
}
```

## Candidatas não incorporadas e pesquisa complementar

- **Pohjankukka et al. (2025)**: Jonne Pohjankukka, Timo A. Räsänen, Timo P. Pitkänen, Arttu Kivimäki, Ville Mäkinen, Tapio Väänänen, Jouni Lerssi, Aura Salmivaara e Maarit Middleton. *Digital mapping of peat thickness and extent in Finland using remote sensing and machine learning*. Geoderma 455, 117216. DOI https://doi.org/10.1016/j.geoderma.2025.117216. Registro Jukuri e metadados conferidos; download retornou HTML, não PDF. Mapeamento de turfa na Finlândia, não plataforma agrícola diretamente comparável. Não incorporada por pertinência insuficiente ao recorte, sem desqualificar o estudo.

- **SWEBOK v4.0 / v4.0a**: página oficial IEEE consultada, edição de Hironori Washizaki e atualização verificadas, mas capítulos integrais não lidos. Não incorporado como suporte de conteúdo não consultado.

- **Sommerville**: URL /web/intro/ retornou 404; não valida edição nem conteúdo. Pressman/Maxim, Myers, Robert C. Martin e Gonzalez/Woods não tiveram exemplares examinados. Ausência de incorporação evita referências decorativas; investigação desses livros permanece incompleta.

- **Parnas (1972)**: DOI 10.1145/361598.361623 e metadados obtidos; PDF UMD bloqueado. Não incorporado sem leitura substantiva. **Fowler, Repository**: página disponível, escopo específico não basta para fundamentar toda a arquitetura. **Kuefler, Unit Testing**: capítulo aberto lido, mas Bender foi suficiente para a afirmação localizada; não acrescentado redundantemente.

- **Frascati/OECD (2015)**: consultas oficiais bloqueadas; não atribuir classificação formal por critérios que não foram conferidos. **EO Browser**: documentação inacessível nesta rodada, não é prova de ausência funcional.
