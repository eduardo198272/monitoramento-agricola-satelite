# Auditoria matemática

## Terceira rodada — conferência final

As 12 expressões analíticas, as três expressões de consulta à grade e o objetivo de mínimos quadrados foram reconferidos frente a `earth_engine.py`, `pipeline.py`, `time_series.py`, `anomalies.py`, `climate.py` e ao componente de consulta. Os oito ambientes `equation`/`align` permanecem literalmente iguais à base de 38 páginas, assim como o ajuste não numerado; o manifesto registra a comparação. A numeração inclui duas linhas adicionais da consulta à grade, não duas novas equações agronômicas.

- Acrescentada a definição de `p` (posição) e `t` (aquisição) antes das fórmulas espectrais. Bandas são reflectâncias escaladas; fator comum cancela na razão, não offsets.
- Mediana do índice precede a média espacial; o denominador dos pesos deve ser positivo. Pesos padrão e CRS não explícito foram preservados, sem atribuir resolução física de10 m às bandas de20 m.
- Janela retrospectiva3, divisorN (`ddof=0`), limiar estrito `<−1`, dispersão zero e três primeiras observações mantidos. A regressão usa ordem sequencial e limiares estritos ±0,01, não taxa diária.
- Somas/médias climáticas usam dias válidos; a soma de registros diários integra implicitamente intervalos de um dia. Temperatura em°C e energia diária emMJ/m²/dia; `f(u)` permanece1 ou3,6 segundo metadados, com indisponibilidade para unidade não reconhecida.
- NIST, Hyndman, NumPy, NASA, BIPM e fontes espectrais mantêm os escopos já registrados. Meroni é precedente de padronização histórica sazonal, não calibração da janela local.
- O exemplo didático de agregação continua0,6 versus0,5. Para a janela[0,6;0,7;0,5], μ=0,6, σ≈0,08165 e z para0,2≈−4,899. Não são resultados agrícolas.

**Parecer:** nenhuma alteração matemática ou funcional necessária nos contratos examinados. Fundamentação matemática e fidelidade operacional não significam calibração científica dos parâmetros ou validação agronômica; a pendência de fonte científica específica B8A/B11 permanece delimitada na auditoria bibliográfica.

## Atualização PA01–PA18

15/11/2026. As 12 equações analíticas, as três expressões de lookup e o ajuste linear foram preservados; a comparação automática desta rodada é contra `f31d0a5`. A confirmação do autor autoriza manter os parâmetros particulares, não converte heurísticas em calibração. Complementos:

- **Eq. 2:** Tabela 1, p.5, de Izquierdo-Sanz e Moltó (2026), DOI `10.3390/agronomy16050541`, consultada em PDF integral do repositório IVIA, utiliza `(B8−B11)/(B8+B11)` sob o nome NDMI. É precedente exato de bandas, não validação de toda a aplicação.
- **Eq. 3:** exemplo técnico Sentinel Hub B8A/B11 mantido com inconsistência entre prosa/código. Pohjankukka não foi utilizado, pois não se obteve texto integral verificável. Não se declara completa a busca científica dessa variante.
- **Eq. 4:** NIST, *Measures of Location*, §1.3.5.1, fundamenta definição par/ímpar e menor sensibilidade da mediana a extremos. Earth Engine fundamenta a operação por pixel/banda e observações não mascaradas. “Pode reduzir interferências extremas” não significa eliminar nuvens ou sombras. Griffiths e Flood não foram confundidos com mediana convencional nem inseridos sem leitura.
- **Eq. 5–6:** guia oficial `reducers_reduce_region`, subseção *Pixels in the region*, reconferido: peso mínimo entre máscara e fração aproximada, quantização em 8 bits, escala e projeção. Não há nova área física observada a 10 m em bandas nativas de 20 m.
- **Eq. 7–8:** permanecem média retrospectiva de 3 observações e `np.std(..., ddof=0)`, com divisor N. Não foi alterado o conjunto de referência para alegar coincidência com literatura.
- **Eq. 9:** Meroni et al. (2019), Eq.1/§3.1, padroniza NDVI pela média/desvio históricos do mesmo decêndio; §3.2.3 examina limiar −1 SD. São 14 anos de referência (2003–2016), dados MODIS e consolidação/sazonalidade. Tabela 2 inclui fronteira `≤−1`, enquanto o código deste TCC usa estritamente `<−1`. Não se afirma equivalência operacional, normalidade ou probabilidade de 15,9% na janela de três observações. Peters/Rembold continuam candidatos, não fontes primárias lidas nesta rodada.
- **Regressão:** mínimos quadrados e NumPy mantidos. A consulta a de Jong não forneceu texto integral; nenhum limiar ±0,01 foi atribuído ao estudo.
- **Eq. 10–12:** preservadas somas/médias sobre dias válidos e fator 3,6 baseado em unidades; fonte NASA e resposta histórica continuam delimitadas. Não se executou nova consulta meteorológica nem reprocessamento remoto nesta rodada.

Os pareceres abaixo são o registro anterior, complementado e não substituído por uma alegação de validação integral.

Data: 15/11/2026. Escopo: 12 equações analíticas, três expressões de lookup e ajuste linear não numerado. A numeração deve ser conferida no PDF compilado; os rótulos e arquivos são os localizadores estáveis. Fórmulas elementares não recebem autoria artificial.

## Convenções comuns

`p`: posição na grade de processamento; `t`: aquisição, não necessariamente data única; `k`: índice. Bandas representam respostas de reflectância escaladas do produto harmonizado. Os três índices, sua média, mediana, dispersão e escore são adimensionais. `scale=10` é escala nominal de processamento em metros, não resolução física nova. Fontes e limites de acesso: `AUDITORIA_REFERENCIAS.md`.

| Nº | Formulação e origem | Implementação / condições | Parecer e correção |
|---|---|---|---|
| 1 | NDVI=(B8−B4)/(B8+B4). Base histórica: Rouse et al., publicação NASA de 1974, seção Spectral Analysis, p. 312–313: diferença de bandas 5/7 dividida pela soma; também apresenta TVI. | `earth_engine.calculate_ndvi`, bandas Sentinel-2 B8/B4; a adaptação para este sensor não pertence ao artigo ERTS. | Correspondente ao código. Texto passou a distinguir fonte histórica e adaptação, sem declarar que o original utilizava Sentinel-2. Limitações complementadas por Gao e Weiss. |
| 2 | NDWI_sistema=(B8−B11)/(B8+B11). Razão NIR–SWIR, identificador particular do software. | `calculate_ndwi`; B8 ~0,835 µm e B11 ~1,614 µm no S2A. | Correção crítica: Gao usa ~0,86/1,24 µm, não B8/B11. McFeeters trata verde–NIR/água superficial: metadados confirmados, texto integral não obtido nesta rodada. Atribuição específica a Gao não é válida. Manter rótulo com definição; recomendar NDMI_B8 separadamente. Não há determinação bibliométrica da nomenclatura predominante. |
| 3 | NDMI_sistema=(B8A−B11)/(B8A+B11). Família NIR–SWIR documentada pelo USGS para Landsat. | `calculate_ndmi`; ambas as bandas nativamente a 20 m. B8A é NIR estreito ~0,865 µm, diferente de B8 amplo a 10 m. | Sentinel Hub tem exemplo executável B8A/B11, mas prosa B8/B11: inconsistência registrada, não escondida. Não foi localizado estudo de campo que valide a superioridade de oferecer ambas como índices distintos. Não são duas medições independentes de umidade do solo. |
| 4 | C_k(p)=mediana_{t∈T_p} I_k(p,t). Estatística elementar aplicada à composição temporal. | `pipeline.py`: calcula índice antes de `ImageCollection.median`; `T_p` varia com máscaras. | API confirma mediana por banda/pixel. Se não há observações válidas, não há mediana numérica válida. Não equivale à aquisição mais recente. Não se inventa motivo histórico da escolha. |
| 5 | M_k=Σw_p,C C_k(p)/Σw_p,C. Média espacial ponderada da composição. | `Reducer.mean`, `scale=10`, sem CRS explícito, `maxPixels=1e9`. Denominador positivo. | Pesos padrão: mínimo da máscara e fração aproximada coberta, não produto; fração quantizada em oito bits e limiar ~1/256. Explicitação inserida; a expressão anterior já era geral e não foi alterada. |
| 6 | S_k(t)=Σw_p,t I_k(p,t)/Σw_p,t. Média espacial por aquisição. | `time_series.compute_time_series`; mesmas condições do redutor; resultados nulos omitidos. | Não confundir média das médias com média da composição mediana. Figura 4: (0,5+0,5+0,8)/3=0,6, enquanto (0,2+0,8)/2=0,5. Correta sob pesos iguais/sem máscaras. |
| 7 | μ_i=(1/3)Σ_{j=i−3}^{i−1}x_j. Média aritmética retrospectiva móvel. | `anomalies.detect_anomalies`, janela padrão 3; exclui valor atual; i≥3, indexação zero. | Hyndman/Athanasopoulos fundamentam médias móveis; sua apresentação de suavização não é validação desta regra unilateral. Janela de observações, não dias; parâmetro heurístico não calibrado. |
| 8 | σ_i=√[(1/3)Σ(x_j−μ_i)²]. Desvio com divisor N. | `np.std(..., ddof=0)`; divisor N−ddof. | NumPy confirma. N−1 seria fórmula amostral; com três pontos a dispersão é instável. “Populacional” descreve a fórmula, não representatividade agrícola. |
| 9 | z_i=(x_i−μ_i)/σ_i, σ_i>0. Padronização em relação à janela anterior. | Sinaliza estritamente z<−1. Primeiros três/σ=0: `anomaly=False`, `z_score=0`. | Zero armazenado nesses casos não é z calculado. NIST trata advertências de escores amostrais/testes, não valida esta regra com divisor N. Sem sazonalidade, calibração, remoção de anomalias anteriores ou tratamento próprio de NaN. Não é p-valor/teste formal/diagnóstico. |
| 10 | P_total=Σ_{d∈D_P}P_d. Soma elementar. | `climate.summarize_climate_data`; PRECTOTCORR diário, mm/dia; integração de dias de duração unitária produz mm. | Datas UTC inclusivas; dias ausentes não contribuem: soma parcial não significa precipitação total conhecida de todo o intervalo. Nenhum valor válido: indisponível. |
| 11 | T̄=ΣT_d/|D_T|. Média elementar. | T2M: média diária do ar a 2 m em °C, somente valores válidos. | Não é média de máximas/mínimas, nem temperatura pontual medida no talhão. D_T vazio: indisponível; lacunas mudam suporte temporal. |
| 12 | R̄=Σf(u)R_d/|D_R|. Média de energia diária normalizada. | `radiation_to_mj`: MJ/m²/dia→1; kWh/m²/dia→3,6; demais→indisponível. | 1 kWh=1000 J/s×3600 s=3,6 MJ. Fonte BIPM para unidades/prefixos, álgebra elementar. Não inferir unidade pela magnitude. Sentinela/booleano/não finito são descartados. Mesmo valor normalizado em resumo/exports; testes de regressão conferidos. |

### Condições dos índices

Para A,B≥0 e A+B>0, |A−B|≤A+B, logo a razão está em [−1,1]. Com negativos, essa propriedade não é garantida; A+B=0 torna a divisão indefinida. A API `normalizedDifference` mascara entrada negativa. O artigo não deve prometer resultado válido para denominador zero. Um fator multiplicativo comum cancela; deslocamentos aditivos não cancelam, o que torna relevante o produto harmonizado. Não foi executado experimento remoto novo de casos-limite aritméticos.

### Regressão linear

`compute_trend`: `np.polyfit(np.arange(n), values, 1)`, mínimos quadrados de Σ[x_i−(ai+b)]². Fonte matemática: Hyndman/Athanasopoulos, seção Least squares estimation; fonte operacional: NumPy `polyfit`. `a`: índice por incremento da ordem; `b`: índice no intercepto. Não há tempo transcorrido na variável explicativa, ajuste sazonal, inferência, intervalo de confiança ou taxa diária.

Limiares estritos ±0,01 constam do código e do commit histórico `32c462d`; não foi encontrada calibração experimental. Séries com n<2 retornam “estável” por convenção de saída, não por evidência científica. Correções no artigo: explicitar objetivo de mínimos quadrados, variáveis, heurística e insuficiência de pontos. Nenhuma mudança no software.

## Expressões adicionais: consulta à grade

| Expressão | Variáveis, unidade e contrato | Limitação |
|---|---|---|
| c=floor((x−x₀)/s_x)−c₀ | x/x₀ em metros UTM; s_x em metros por célula; c₀ origem inteira de coluna. | s_x≠0, grade alinhada; nenhuma inversão afim geral com rotação. |
| r=floor((y−y₀)/s_y)−r₀ | y/y₀ em metros UTM; s_y pode ser negativo; r₀ origem inteira de linha. | Piso, não arredondamento ao inteiro mais próximo. Conferir limites após subtrair origem. |
| q=r n_c+c | Índice linear sem unidade, armazenamento por linhas; n_c número de colunas. | 0≤r<n_r e 0≤c<n_c, finitude/NoData/pertencimento ao polígono antes de apresentar valor. |

Origem: indexação matricial e transformação afim elementares, aplicação do autor em `src/app/index_hover/index.html` e `maps.py`. Conferidas com os contratos de pré-carregamento; não requerem atribuição a Gao, Rouse ou método agronômico. As duas linhas do ambiente `align` contêm três expressões, resultando em 14 números de equação para 15 expressões ao todo.

## Evidência e limites do parecer

Fórmulas dos ambientes `equation` e `align` foram preservadas literalmente. Foram alteradas explicações e acrescentada a função objetivo não numerada. A aprovação da nomenclatura e das escolhas heurísticas continua sendo uma decisão do autor; fidelidade ao código não implica validação agronômica.
