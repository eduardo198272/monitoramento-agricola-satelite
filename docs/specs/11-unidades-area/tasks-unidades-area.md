# Tasks: Unidade de Área em Hectares e Acres

Referência: `docs/specs/11-unidades-area/spec-unidades-area.md`

| ID | Descrição | Critério de Aceitação | Esforço |
|---|---|---|---|
| SPEC-11-01 | Criar constantes e funções de conversão de m² para hectares e hectares para acres | Fórmulas e fator `2,47105` aplicados corretamente | 45min |
| SPEC-11-02 | Implementar validação de valores e unidades | Negativos, tipos inválidos, infinitos e unidades desconhecidas são rejeitados | 45min |
| SPEC-11-03 | Implementar `format_area()` com duas casas decimais | Valor possui símbolo e separador padronizados | 30min |
| SPEC-11-04 | Adicionar seletor `Unidade da área` na sidebar | Opções `Hectares (ha)` e `Acres (ac)` disponíveis | 30min |
| SPEC-11-05 | Definir hectares como padrão e persistir a escolha | Estado inicial é `ha` e seleção sobrevive ao rerun | 30min |
| SPEC-11-06 | Atualizar o card de área da análise | Card acompanha a unidade escolhida sem novo processamento | 45min |
| SPEC-11-07 | Aplicar unidade em tabelas, relatórios e exportações | Todos os pontos de exibição usam a mesma unidade | 1h |
| SPEC-11-08 | Corrigir textos para usar “acres” e os símbolos `ha`/`ac` | Não há ocorrência de “hacres” na UI | 30min |
| SPEC-11-09 | Criar testes unitários e funcionais | Conversões, validações, padrão e troca na UI cobertos | 1h30 |
