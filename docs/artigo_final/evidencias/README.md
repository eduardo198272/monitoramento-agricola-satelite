# Evidência da consulta pública NASA POWER

## Origem

- Consulta executada em 15/11/2026 por ferramenta HTTP de leitura, sem autenticação.
- Resposta salva como `nasa_power_unidades.json`, reformatada para legibilidade,
  preservando os campos/valores recebidos.
- Endpoint e parâmetros:

```text
https://power.larc.nasa.gov/api/temporal/daily/point?parameters=PRECTOTCORR,T2M,ALLSKY_SFC_SW_DWN&community=ag&longitude=-52&latitude=-28&start=20250101&end=20250102&format=JSON
```

## Finalidade e observação

Verificar unidades e limites de datas do contrato consumido pelo software.
API v2.10.3; fontes MERRA2 e SYN1DEG; LST. Retornou duas datas, com radiação em
MJ/m²/dia. A coordenada foi escolhida para consulta técnica, sem atribuição de
propriedade ou cultura.

A conferência local leu os dois valores, construiu um DataFrame e chamou
`src.app.climate.summarize_climate_data`. Resultado observado: 76,734 para média
independente 21,315, razão 3,6. O código assume kWh/m²/dia; a resposta já traz
MJ/m²/dia. Não houve modificação funcional, nova rede nessa conferência local,
autenticação Earth Engine ou geração de resultados agrícolas.

Este arquivo não constitui estudo agronômico, verdade de campo, teste de precisão
do provedor ou demonstração integral do pipeline. A API pode revisar produtos;
repetir a consulta no futuro pode não retornar bytes idênticos.
