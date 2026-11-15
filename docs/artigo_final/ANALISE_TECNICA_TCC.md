# Análise técnica — estado vigente

15/11/2026; base `b7c325c` com correções locais, sem versionamento/publicação
automática. O relatório anterior permanece como evidência histórica em
`evidencias/historico_primeira_rodada/ANALISE_TECNICA_TCC.md`.

## Arquitetura

Monólito modular Python/Streamlit, não microsserviços. Earth Engine processa
coleções; NASA POWER fornece contexto pontual; Nominatim faz busca explícita;
Esri fornece mapa-base. Componente Leaflet/Proj4 consulta grade float32 local,
após zlib/Base64. SQLite atende execução local e repositório em memória atende
sessão web. GeoJSON é transferência, não persistência remota permanente.
Snapshots vinculam dados e exportações à geometria/período/índices.

## Contratos corrigidos

Normalização de radiação baseada em metadados, escalas coerentes, propagação do
clima multiíndice, datas inclusivas UTC, invalidação de resultados, harmonização
de contagem/tendência e IDs de aquisição. Causas, regressões e limites estão em
`CORRECOES_TECNICAS.md`. QA60 não foi substituída.

## Verificação

710 testes Python aprovados em 11,73 s; 100% das linhas/ramificações medidas,
2.735 instruções e 856 ramificações. Node: 3 testes aprovados, separado da cobertura.
Os testes remotos simulados não demonstram precisão agronômica. Chrome real
executou o fluxo até PDF/XLSX/ZIP e GeoJSON, importou o GeoJSON em nova sessão
e consultou a mesma célula por cursor/toque (NDMI 0,3228). Manifesto e arquivos
estão em `evidencias/demonstracao_real/`. A interface pública foi
carregada com HTTP 200; não houve deploy das correções.

## Evidência de engenharia

Histórico contém especificações, branches de tarefa e merges de pull requests
com testes de exportação/localizações/regressão (por exemplo, #23 e #31).
Não foi encontrado histórico/configuração `.github` de integração contínua.
Houve reprodução antes da correção nesta rodada, sem atribuir TDD universal
ao histórico. Dependências da aplicação não foram ampliadas pelas ferramentas
de captura/QR, instaladas exclusivamente em diretório temporário.

## Segurança e limites

Secrets foram utilizados pelo processo autorizado via caminho de configuração,
sem copiar seus valores para documentação. Não houve exposição, commits, push,
merge, submissão ao formulário nem alteração de respostas.
Dados por sessão não são autorização por propriedade. GeoJSON pode conter
coordenadas sensíveis. Nominatim não tem limitador global implementado; cotas,
atribuição e política devem ser reavaliadas antes de ampliar o público.
Não há autenticação de visitantes, histórico permanente de análises, exclusão
de localizações na UI, raster GeoTIFF, teste de carga ou validação de campo.
As capturas revelam contraste insuficiente em alguns rótulos/valores quando o CSS
escuro encontra o tema de widgets do ambiente. Não foi modificada a identidade
visual; recomenda-se revisão de acessibilidade e contraste como pendência de UI.
