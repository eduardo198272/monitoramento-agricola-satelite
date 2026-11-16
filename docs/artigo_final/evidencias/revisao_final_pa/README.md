# Rodada PA01–PA18 — revisão científica e institucional

Data:15/11/2026. Base fixa:`f31d0a5`. **Execução parcial, não certificação de conclusão científica ou conformidade institucional.** A aprovação do autor refere-se às decisões e à versão anterior, não à leitura humana da revisão produzida agora.

## Entregáveis e evidências

- [Relatório vigente](../../auditoria_cientifica/AUDITORIA_CIENTIFICA.md)
- [Encaminhamento das18 pendências](../../auditoria_cientifica/PENDENCIAS_AUTOR.md)
- [Matriz de afirmações alteradas](../../auditoria_cientifica/MATRIZ_RASTREABILIDADE_CIENTIFICA.md)
- [Pareceres bibliográficos](../../auditoria_cientifica/AUDITORIA_REFERENCIAS.md): oito adições, nenhuma substituição/remoção; leituras incompletas explicitadas
- [Equações e regressão](../../auditoria_cientifica/AUDITORIA_EQUACOES.md)
- [Originalidade preliminar](../../auditoria_cientifica/AUDITORIA_ORIGINALIDADE.md), sem ferramenta/percentual de similaridade inventados
- [Registro de uso de IA](../../REGISTRO_USO_IA.md)
- [Minuta independente](../../DECLARACAO_USO_IA.tex), conforme os campos do anexo oficial, sem assinatura
- [PDF do artigo](../../Relatorio_Final.pdf)
- `compilacao.json`: citações, rótulos, classe e ambientes matemáticos, contagens e hash do novo PDF
- `validacao.json`: arquivos protegidos, dados, fórmulas, captura, bibliografia, fontes em cache e limites do parecer
- `conferencia-planilha.json`:31 registros,40 itens e191 categorias reconferidos; não autentica origem empírica
- `comparacao.diff`: alterações e arquivos textuais novos contra a base fixa
- [Inspeção visual e compilação](INSPECAO_VISUAL.md):37 páginas do artigo e2 da minuta, inspeção assistida sem aprovação humana
- `renderizacao.json`: hashes das37 imagens finais; somente a página32 mudou após ajuste da legenda e foi novamente inspecionada
- `declaracao.json`: hash, paginação e condição de minuta não assinada
- `Relatorio_Final.log` / `DECLARACAO_USO_IA.log`: logs finais separados dos históricos

PDF final do artigo:37 páginas,26 figuras,5 tabelas,51 chaves citadas; sem referências indefinidas ou excessos de caixa. SHA-256:`74eaf2fb3f9f3683e16f3a740361b9357b7b011f22f8a409e79a54467f1fa994`.

Os registros anteriores em `auditoria_cientifica/`, `revisao_didatica/` e outras pastas são históricos e não foram sobrescritos por esta compilação. Não reexecutar seus geradores para fazer parecer que certificam esta versão.

## Normativa oficial

IN nº03/2026/PROACAD, de28/10/2026, íntegra e anexo obtidos no portal UPF:

https://www.upf.br/ppgodonto/normas-regimentos-formularios-e-in

O PDF de5 páginas e as fontes integrais consultadas permanecem em `/tmp/opencode/revisao-final-pa/`, com hashes no manifesto. O relatório registra exigências dos arts.3–8/10–11. Não houve contato com orientador, CEP, ProAcad ou banca, nem emissão de dispensa ou assinatura.

## Procedência e captura

A planilha original recebida e a versão anteriormente corrigida foram preservadas. Nesta rodada não foi alterada nenhuma resposta, data ou categoria. A conferência de estatística e das fixtures conhecidas não confirma que cada registro provenha de participante real. Faltam exportação independente original do Forms, encerramento verificável e commit público exato. Por isso, a descrição do arquivo não é apresentada como resultado empírico confirmado.

A captura disponível de relatório PDF tem o mesmo hash da imagem antes excluída e ainda mostra59,00 MJ/m²/dia. Não foi incorporada nem teve os valores artificialmente modificados.

O esquema de três curvas espectrais foi retirado por falta de fonte específica; os outros esquemas foram preservados. A reconstrução solicitada permanece pendente, não foi substituída por desenho presumido.

## Reproduzir

Após compilar o artigo em diretório separado:

```bash
.venv/bin/python docs/artigo_final/avaliacao_usuarios/scripts/validar_artigo.py --build-dir /tmp/opencode/revisao-final-pa/build --output docs/artigo_final/evidencias/revisao_final_pa/compilacao.json
.venv/bin/python docs/artigo_final/auditoria_cientifica/validar_rodada_pa.py --build-dir /tmp/opencode/revisao-final-pa/build --cache-dir /tmp/opencode/revisao-final-pa
```

A opção de cache acrescenta hashes e acessos, não é necessária para a comparação das fontes com Git. Arquivos privados da planilha são necessários à reconferência e não devem ser publicados automaticamente.

Não foram realizados testes novos da aplicação, deploy, commit ou push nesta rodada. Os números de testes e da demonstração citados no artigo continuam sendo resultados históricos.
