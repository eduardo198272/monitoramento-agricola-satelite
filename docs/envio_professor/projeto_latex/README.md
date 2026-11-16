# Sistema de Monitoramento Agrícola por Imagens de Satélite

Projeto LaTeX de Eduardo Steffens Hoppen, com orientação de Rafael Rieder.

## Compilação

- Documento principal: `Relatorio_Final.tex`.
- Compilador recomendado no editor online: **XeLaTeX**.
- Bibliografia: **BibTeX**, estilo `dcu`, base `referencias_institucionais.bib`.
- Preserve os nomes e a estrutura das subpastas.

O editor deve executar o BibTeX e as passagens adicionais automaticamente.
Em uma instalação local de TeX Live com os pacotes da classe:

```sh
latexmk -xelatex Relatorio_Final.tex
```

Alternativamente, com Tectonic:

```sh
tectonic -X compile Relatorio_Final.tex
```

A compilação isolada foi verificada localmente com Tectonic. Não foi realizada
uma compilação na conta do Overleaf, Texpage ou Prism.

## Arquivos

- `final_*.tex`: seções do artigo.
- `CC-EC_TF-TC.cls`: classe institucional ativa, preservada sem alterações.
- `autoria.tex`, `normalizacao.tex`, `figuras_relatorio.tex`: configuração
  vigente do trabalho; não reaplicar ajustes antigos de normalização.
- `fig/`: diagramas e imagens efetivamente utilizados.
- `avaliacao_usuarios/`: somente figuras e tabelas agregadas utilizadas.
- `referencias_institucionais.bib`: base pronta para a compilação com dcu.
- `MANIFESTO_SHA256.json`: identificação dos arquivos copiados.

Não é necessário executar Python, instalar a aplicação ou configurar
credenciais do Earth Engine para compilar o artigo.

Esta é uma cópia independente para revisão compartilhada. Alterações na
bibliografia podem ser feitas diretamente no `.bib` incluído; sua integração
posterior com a base estruturada do repositório deve ser coordenada pelo autor.
O conteúdo científico, a declaração de IA e a configuração de autoria foram
mantidos como na versão de origem.
