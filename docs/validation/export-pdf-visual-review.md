# Revisão Visual da Exportação PDF

## Execução

- Data: 2026-10-20
- Artefato: PDF temporário gerado pelo `render_analysis_pdf` e inspecionado no leitor de PDF integrado.
- Escopo: três páginas na ordem NDVI, NDWI e NDMI; layout, séries, mapas estáticos, legendas, atribuição e rodapé.
- Dados: snapshot sintético usado exclusivamente para esta revisão; respostas de tiles e thumbnail foram simuladas. Nenhum dado ou relatório foi adicionado ao repositório.
- Earth Engine: não inicializado neste ambiente; a revisão não valida uma imagem satelital real nem o acesso remoto ao serviço.

## Resultado Visual

- O PDF contém exatamente três páginas, uma para cada índice, na ordem esperada.
- Títulos, período, data de geração, área, métricas, contexto climático e anomalias estão visíveis.
- Gráficos temporais e mapas cabem na página sem cortes ou sobreposição aparente; os elementos principais permanecem legíveis na visualização da página inteira.
- Os mapas gerados pelo renderizador estático mostram a imagem-base de teste, camada temática colorida, contorno da geometria e legenda com intervalo `-1.0` a `+1.0`.
- A atribuição cartográfica está visível no mapa e abaixo dele.

## Fonte, Atribuição e Limitações

- A imagem-base é solicitada ao serviço Esri World Imagery, pelo endpoint definido em `src/app/maps.py` (`ESRI_WORLD_IMAGERY_URL`).
- O texto de atribuição configurado em `ESRI_WORLD_IMAGERY_ATTRIBUTION` é: `Tiles © Esri — Source: Esri, Maxar, Earthstar Geographics, and the GIS User Community`.
- A camada do índice é obtida como thumbnail do Earth Engine; sua disponibilidade depende do serviço e de uma sessão autenticada. Falhas de serviço ou de tiles podem deixar o mapa indisponível, estado que o PDF deve sinalizar sem remover as outras páginas.
- A composição é uma imagem estática e não oferece zoom, inspeção de pixels ou interação do mapa Streamlit. Resolução, enquadramento e aparência da imagem-base dependem da geometria, do nível de zoom e da disponibilidade do serviço de tiles.
- A revisão usou respostas simuladas e valida o layout/composição, não a fidelidade de uma análise agrícola real, a cobertura dos tiles em uma área específica ou os termos de uso aplicáveis fora da atribuição exibida. A fonte deve ser usada conforme os termos atuais do provedor.

## Verificações

- Artefato temporário gravado fora do repositório em `C:\Users\Eduardo Hoppen\AppData\Local\Temp\opencode\spec16_10_visual_review.pdf`.
- Abertura e inspeção das três páginas pelo leitor integrado; nenhuma chamada de rede foi feita durante a geração.
- Suíte completa de testes de exportação e regressão: `py -m pytest -q`.
