# Decisões de Arquitetura - MVP

## Decisão 1: Localização da Criação do Mapa

### Contexto

A especificação SPEC-09 define que o pipeline deve:
1. Criar mapa base
2. Adicionar camada do índice
3. Adicionar legenda

### Decisão Tomada

**Manter a criação do mapa na camada de UI (`main.py`), não no `pipeline.py`**

### Justificativa

1. **Separação de Responsabilidades**
   - `pipeline.py` → Lógica de negócio (processamento de dados)
   - `main.py` → Apresentação (UI do Streamlit)

2. **Testabilidade**
   - `pipeline.py` pode ser testado com mocks sem dependência de `geemap`
   - UI pode ser testada separadamente

3. **Flexibilidade**
   - O mesmo `pipeline.py` pode ser usado por diferentes interfaces
   - API, CLI, ou diferentes UIs podem consumir o pipeline

4. **Simplicidade**
   - `run_analysis()` retorna dados serializáveis
   - UI fica responsável por renderizar visualizações

### Fluxo de Dados

```
Usuário seleciona área/datas → main.py → run_analysis() → pipeline.py
                                                            ↓
                                                      { index_map,
                                                        time_series,
                                                        anomalies,
                                                        climate_data,
                                                        mean_value,
                                                        area_ha }
                                                            ↓
main.py ← { map (criado via maps.py),
            summary (criado localmente) }
```

### Alternativas Consideradas

| Opção | Prós | Contras |
|-------|------|---------|
| **A: Manter no UI (escolhida)** | Separação clara, testável | - |
| B: Mover para pipeline | Tudo em um lugar | UI acoplada, testes difíceis |

### Conclusão

A decisão mantém o MVP modular e testável, permitindo evoluções futuras sem refatorações complexas.
