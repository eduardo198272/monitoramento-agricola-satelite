# Fluxo de Desenvolvimento

## Objetivo

Cada tarefa deve ser desenvolvida de forma isolada, reproduzivel e revisavel por
meio de uma worktree propria, uma branch propria e um Pull Request direcionado
para `dev`.

## Regras obrigatorias

- Nunca desenvolver diretamente em `dev`, `hml` ou `main`.
- Cada tarefa deve ter uma worktree exclusiva.
- Cada tarefa deve ter uma branch exclusiva.
- A branch da tarefa deve ser criada a partir de `dev` atualizado.
- Toda alteracao deve entrar em `dev` por Pull Request.
- Nao misturar tarefas diferentes na mesma branch ou Pull Request.
- Nao remover, descartar ou sobrescrever alteracoes existentes de outro autor.

## Inicio de uma tarefa

O checkout principal deve permanecer associado a `dev` e ser usado para
sincronizacao. Antes de iniciar cada tarefa:

```powershell
git switch dev
git fetch origin
git pull --ff-only origin dev
```

Se o checkout principal tiver alteracoes nao commitadas, elas devem ser
identificadas e preservadas. Nao executar `reset`, `checkout --` ou qualquer
comando destrutivo para liberar a arvore sem autorizacao explicita.

Depois, criar uma worktree fora do diretorio principal. O nome da branch deve
seguir o formato `task/<ID>-<descricao-curta>`:

```powershell
git worktree add -b task/TASK-XXX-descricao ..\worktrees\TASK-XXX dev
Set-Location ..\worktrees\TASK-XXX
```

Para especificacoes que nao usam `TASK-XXX`, usar o identificador da spec, por
exemplo `task/SPEC-14-05-busca-workspace`.

## Desenvolvimento

Dentro da worktree da tarefa:

1. Ler a spec e os criterios de aceitacao correspondentes.
2. Criar ou atualizar os testes antes da implementacao.
3. Confirmar que os testes novos falham pelo motivo esperado.
4. Implementar somente a tarefa atual.
5. Executar a suite relevante e a suite completa quando aplicavel.
6. Verificar o diff e confirmar que nao existem alteracoes nao relacionadas.

## Commit e Pull Request

Somente apos os testes passarem:

```powershell
git status
git diff --check
git add <arquivos-da-tarefa>
git commit -m "feat: implement <tarefa>"
git push -u origin task/TASK-XXX-descricao
gh pr create --base dev --head task/TASK-XXX-descricao
```

O Pull Request deve informar:

- Identificador e objetivo da tarefa.
- Spec e criterios de aceitacao atendidos.
- Testes executados e resultado.
- Limitacoes ou pendencias conhecidas.

Nao fazer merge direto em `dev`. O merge deve ocorrer pelo Pull Request, apos a
revisao e as verificacoes exigidas pelo repositorio.

## Encerramento

Depois que o Pull Request for merged, remover a worktree e a branch local:

```powershell
Set-Location <checkout-principal>
git worktree remove ..\worktrees\TASK-XXX
git branch -d task/TASK-XXX-descricao
git switch dev
git pull --ff-only origin dev
```

Se o Pull Request ainda nao tiver sido merged, manter a worktree e a branch
disponiveis para ajustes solicitados na revisao.
