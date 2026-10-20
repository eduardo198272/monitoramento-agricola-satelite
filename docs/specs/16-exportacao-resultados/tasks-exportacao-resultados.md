# Tasks: Exportação de Resultados (PDF, Excel e CSV)

Referência: `spec-exportacao-resultados.md`.

| ID | Descrição | Critério de aceite | Dependências | Esforço | Status |
|---|---|---|---|---:|---|
| SPEC-16-01 | Fechar contrato do snapshot exportável e validar pré-condições multiíndice | Contexto normalizado contém período, área/geometria, três índices, clima, séries e anomalias disponíveis; análise single/incompleta é rejeitada sem serviço remoto | SPEC-15-08, critérios desta spec | 2h | Concluída |
| SPEC-16-02 | Definir/adicionar dependências de renderização e serialização | Bibliotecas para PDF, imagens estáticas e XLSX são justificadas, fixadas em `requirements.txt` e importáveis no ambiente de teste | SPEC-16-01 | 1h | Concluída |
| SPEC-16-03 | Implementar preparação de dados compartilhada para exportação | Normalização pura preserva tipos, ISO dates, nulos, unidades, GeoJSON e dados comuns sem mutar resultados | SPEC-16-01 | 2h | Concluída |
| SPEC-16-04 | Gerar mapa temático estático sobre imagem de satélite para cada índice | Cada índice produz imagem raster com base satélite, overlay temático, contorno da área e legenda; falhas retornam estado explícito e são mockáveis | SPEC-15-02/03, SPEC-16-02/03 | 4h | Concluída |
| SPEC-16-05 | Implementar layout de relatório PDF com exatamente três páginas | Render NDVI/NDWI/NDMI em ordem fixa; conteúdo e contexto comuns cabem sem página de capa/apêndice e mantêm legibilidade | SPEC-16-03/04 | 4h | Concluída |
| SPEC-16-06 | Implementar builder XLSX com abas, colunas, tipos e unidades estáveis | Workbook abre com `Resumo`, abas NDVI/NDWI/NDMI, `Clima`, `Anomalias`, `Geografia`; vazios/nulos e GeoJSON são representados conforme spec | SPEC-16-03 | 3h | Concluída |
| SPEC-16-07 | Implementar pacote CSV ZIP equivalente ao XLSX | ZIP contém os sete CSVs definidos, UTF-8, cabeçalhos presentes mesmo sem linhas e sem caminhos/arquivos indevidos | SPEC-16-03/06 | 2h | Concluída |
| SPEC-16-08 | Integrar ações e downloads Streamlit ao ciclo de análise | PDF/XLSX/CSV ficam disponíveis após sucesso multiíndice; estado inválido e exceções recebem mensagem sem rerun remoto | SPEC-16-05/06/07 | 2h | Concluída |
| SPEC-16-09 | Cobrir validação, erros, dados ausentes e ausência de chamadas externas | Testes inspecionam páginas/conteúdo PDF, abas/células XLSX, membros/dados CSV, estado single-index e contagem zero de requests externos | SPEC-16-04 a SPEC-16-08 | 3h | Concluída |
| SPEC-16-10 | Validar artefatos visualmente e documentar limitações/atribuições | PDF revisado em viewer com três páginas/mapas legíveis; fontes e limitações do mapa estático registradas; suíte relevante passa | SPEC-16-09 | 1h30 | Não iniciado |

## Ordem de execução

1. Fechar o contrato e validar a pré-condição de análise completa
   (SPEC-16-01).
2. Escolher dependências e implementar os dados compartilhados
   (SPEC-16-02/03).
3. Implementar a captura/renderização dos mapas estáticos
   (SPEC-16-04).
4. Construir os geradores PDF, XLSX e CSV ZIP (SPEC-16-05/06/07).
5. Integrar os botões à UI e testar gating/erros (SPEC-16-08/09).
6. Revisar visualmente o PDF e registrar atribuições/limitações (SPEC-16-10).

## Regras de execução

- Seguir SDD/TDD: validar os contratos com testes antes de conectar a UI.
- Mockar Earth Engine, NASA POWER, downloads de tiles e qualquer request nos
  testes automatizados; geração de export não pode chamar o pipeline novamente.
- Usar fixtures reais sintéticas somente nos testes, nunca como fallback de
  produção.
- Conferir equivalência semântica entre XLSX e os CSVs do ZIP.
- Remover artefatos temporários em sucesso e falha; não versionar relatórios nem
  dados analisados.
- Seguir branch/worktree e PR definidos em `.agent-context/development-rules.md`.
