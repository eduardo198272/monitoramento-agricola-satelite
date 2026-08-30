# Cenários de Validação - MVP

## Visão Geral

Este documento define 3 cenários de validação para o sistema de monitoramento agrícola, representando as principais culturas-alvo do projeto.

---

## Cenário 1: Soja

### Características

| Atributo | Valor |
|-----------|-------|
| **Cultura** | Soja (Glycine max) |
| **Ciclo** | ~120 dias |
| **Período de Plantio** | Outono (Outubro-Novembro) |
| **Período de Colheita** | Verão (Fevereiro-Março) |

### Localização

**Coordenadas Centrais:** -50.5°, -15.5°
**Região:** Brasil Central (MT/GO)
**Área Sugerida:** ~1000 hectares (polígono de 5x2 km)

### NDVI Esperado

```
Ciclo da Soja:
     0.9 |                    *****
         |               ****     ****
     0.5 |          ****             ****
         |       ***                      ***
     0.3 |-----                          -----
         | 0.2                              0.3
         +----------------------------------------
           Out    Nov    Dez    Jan    Fev    Mar

Fases:
- Plantio (Out): NDVI ~0.2 (solo exposto)
- Desenvolvimento (Nov-Dez): NDVI sobe para 0.9
- Maturação (Jan-Fev): NDVI começa a cair
- Colheita (Mar): NDVI ~0.3
```

### Validações

| Checkpoint | Critério |
|------------|----------|
| NDVI máximo | Entre 0.8 e 0.95 |
| NDVI mínimo (início/fim) | Entre 0.15 e 0.35 |
| Tendência | Crescente → Estável → Decrescente |
| Duração do ciclo | ~120 dias |

---

## Cenário 2: Milho

### Características

| Atributo | Valor |
|-----------|-------|
| **Cultura** | Milho (Zea mays) |
| **Ciclo** | ~150 dias |
| **Período de Plantio** | Primavera (Setembro-Outubro) |
| **Período de Colheita** | Outono (Fevereiro-Março) |

### Localização

**Coordenadas Centrais:** -52.0°, -25.0°
**Região:** Paraná
**Área Sugerida:** ~500 hectares (polígono de 2.5x2 km)

### NDVI Esperado

```
Ciclo do Milho:
     0.9 |               ********
         |           ****         ****
     0.5 |        **                 **
         |      **                     **
     0.4 |----                         ----
         | 0.2                              0.4
         +----------------------------------------
           Set    Nov    Dez    Jan    Fev    Mar

Fases:
- Plantio (Set): NDVI ~0.2 (solo exposto)
- Desenvolvimento (Out-Nov): NDVI sobe para 0.9
- Maturação (Dez-Jan): NDVI permanece alto
- Colheita (Fev-Mar): NDVI cai para ~0.4 (mais gradual que soja)
```

### Validações

| Checkpoint | Critério |
|------------|----------|
| NDVI máximo | Entre 0.75 e 0.95 |
| NDVI mínimo (início/fim) | Entre 0.15 e 0.45 |
| Tendência | Crescente → Estável → Decrescente (mais gradual) |
| Duração do ciclo | ~150 dias |

---

## Cenário 3: Pastagem

### Características

| Atributo | Valor |
|-----------|-------|
| **Cultura** | Pastagem (Brachiaria/Panicum) |
| **Ciclo** | Perene (ano todo) |
| **Variabilidade** | Estável com variações sazonais |

### Localização

**Coordenadas Centrais:** -50.0°, -16.5°
**Região:** Goiás
**Área Sugerida:** ~200 hectares (polígono de 1x2 km)

### NDVI Esperado

```
Ciclo da Pastagem (ano):
     0.8 |    ****            ****
         |   **  **          **  **
     0.6 |  **    **        **    **
         | **      **      **      **
     0.4 |**        ****          **
         +----------------------------------------
           Jan    Mar    Mai    Jul    Set    Nov

Sazonalidade:
- Verões (Jan-Fev): NDVI ~0.7-0.8 (chuvoso)
- Invermos (Jul-Ago): NDVI ~0.4-0.5 (seco)
- Variação anual: < 0.3 de amplitude
```

### Validações

| Checkpoint | Critério |
|------------|----------|
| NDVI médio anual | Entre 0.5 e 0.7 |
| NDVI máximo | Entre 0.65 e 0.85 |
| NDVI mínimo | Entre 0.35 e 0.55 |
| Amplitude anual | < 0.35 |
| Estabilidade | Desvio padrão < 0.15 |

---

## Resumo dos Cenários

| Cultura | Coordenadas | Área | Ciclo | NDVI Mín | NDVI Máx | Tendência |
|---------|------------|------|-------|-----------|-----------|-----------|
| Soja | -50.5°, -15.5° | ~1000ha | 120 dias | 0.2 | 0.9 | Cresce → Cai |
| Milho | -52.0°, -25.0° | ~500ha | 150 dias | 0.2 | 0.9 | Cresce → Estável → Cai |
| Pastagem | -50.0°, -16.5° | ~200ha | Perene | 0.4 | 0.7 | Estável com variação |

---

## Uso para Validação

Estes cenários devem ser usados para:

1. **Teste de Integração**
   - Executar `run_analysis()` com cada geometria/período
   - Verificar se valores de NDVI estão dentro dos ranges esperados

2. **Documentação do TCC**
   - Ilustrar comportamento típico dos índices para cada cultura
   - Validar que o sistema detecta corretamente as características

3. **Verificação de Requisitos**
   - RF04: Cálculo NDVI → Validação Soja/Milho
   - RF05: Cálculo NDWI/NDMI → Validação umidade
   - RF08: Detecção de Anomalias → Validação com variações de NDVI
