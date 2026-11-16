# Auditoria científica — 15/11/2026

**Estado vigente: quarta rodada, conjunto definitivo de 32 respostas reprocessado.** O [relatório consolidado](AUDITORIA_CIENTIFICA.md) e as [pendências](PENDENCIAS_AUTOR.md) apresentam os resultados atuais. Software e respostas originais preservados. Não se presume aprovação institucional.

**Validação atual:** `../evidencias/quarta_rodada/`. Os relatórios receberam complementos no início; JSONs, logs, contagens e perguntas de defesa anteriores são históricos e devem ser lidos com as atualizações vigentes.

- [Originalidade preliminar](AUDITORIA_ORIGINALIDADE.md)
- [Registro de IA](../REGISTRO_USO_IA.md)
- [Minuta independente conforme anexo UPF](../DECLARACAO_USO_IA.tex)

## Documentos principais

1. [Relatório e critérios de aceite](AUDITORIA_CIENTIFICA.md)
2. [Matriz de rastreabilidade](MATRIZ_RASTREABILIDADE_CIENTIFICA.md)
3. [Referências: parecer por entrada](AUDITORIA_REFERENCIAS.md)
4. [Equações e regressão](AUDITORIA_EQUACOES.md)
5. [Pendências do autor/orientador](PENDENCIAS_AUTOR.md)
6. [Alterações antes/depois](CHANGELOG_ARTIGO.md)

## Evidências

- `CONSULTAS_FONTES.json` / `CONSULTAS_COMPLEMENTARES.json`: respostas HTTP/metadados; não são certificados de suporte.
- `INVENTARIO.json`: contagens, hashes e estados da matriz. Ela contém 197 blocos, dos quais 178 permanecem parcialmente validados; isso não deve ser ocultado pela existência da matriz.
- `TESTES_PYTHON.txt` / `TESTES_JAVASCRIPT.txt`: execuções desta rodada, separadas do histórico citado no artigo.
- `COMPILACAO.json` / `COMPILACAO.log`: 33 páginas, 27 figuras, cinco tabelas, 45 chaves citadas e nenhuma referência indefinida; aviso de cabeçalho preservado.
- `VALIDACAO_FINAL.json`: ambiente, hashes do software/testes e confirmação da planilha analisada, sem divulgar respostas individuais.

Os 24 problemas do relatório são agrupamentos conceituais; não se confundem com os 197 blocos da matriz ou com o número de hunks do diff. Há 14 lacunas corrigidas no escopo descrito e dez agrupamentos ainda parciais/pendentes.

## Reexecução

Na raiz do repositório:

```bash
.venv/bin/python docs/artigo_final/auditoria_cientifica/consolidar_auditoria.py --baseline /tmp/opencode/auditoria-cientifica/baseline.json
.venv/bin/python docs/artigo_final/avaliacao_usuarios/scripts/validar_artigo.py --build-dir /tmp/opencode/auditoria-cientifica/build --output docs/artigo_final/auditoria_cientifica/COMPILACAO.json
```

A consolidação depende da linha de base local preservada antes da auditoria. Não recriar essa linha de base com o artigo já alterado: isso apagaria a distinção antes/depois. O changelog conserva os diffs e o inventário conserva os hashes. Arquivar o backup local antes de limpar o diretório temporário.

`registrar_fontes.py` refaz consultas e sobrescreve o registro principal: preservar o JSON anterior antes de uma nova rodada; metadados e páginas dinâmicas podem mudar. PDFs de terceiros permanecem no cache local, não foram incorporados ao Git. Inspeção visual ampliada e aprovação científica/institucional continuam pendentes.
