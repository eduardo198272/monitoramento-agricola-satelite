# Spec: Localizações Salvas

## Propósito

Permitir que o usuário nomeie e salve uma área desenhada no mapa e a restaure
posteriormente por uma opção apresentada abaixo do campo de pesquisa. Ao
selecionar uma localização salva, a aplicação deve restaurar a geometria e
centralizar o mapa sem chamar o geocodificador.

## Escopo e pressupostos

- Uma localização salva representa uma seleção geográfica desenhada (Feature ou
  Geometry GeoJSON válida), não apenas o centro de uma cidade pesquisada.
- A persistência inicial é local à instalação da aplicação e compartilhada por
  quem acessa essa mesma instância; autenticação e isolamento por usuário não
  fazem parte desta entrega, pois o produto ainda não possui identidade de
  usuário.
- O armazenamento inicial deve usar SQLite da biblioteca padrão, com caminho
  configurável por `SAVED_LOCATIONS_DB_PATH` e padrão fora de diretórios
  temporários. O diretório precisa existir/criar-se com permissões restritas.
- O armazenamento contém metadados e GeoJSON, não objetos Earth Engine
  serializados; `ee.Geometry` é reconstruída a partir do GeoJSON validado quando
  uma área é restaurada.

## Interface e contratos

```python
def save_location(name: str, geojson: dict) -> dict
```

Valida nome/geometria, persiste localização e retorna registro com `id`, `name`,
`geojson`, `center`, `created_at`, `updated_at`. Nome normalizado duplicado deve
produzir erro de domínio tratável pela UI.

```python
def list_saved_locations() -> list[dict]
```

Retorna registros resumidos ordenados por nome normalizado (ou ordem explícita
registrada), incluindo `id`, `name`, `center` e metadados para apresentação.

```python
def get_saved_location(location_id: str) -> dict | None
```

Retorna a geometria GeoJSON e os dados necessários para restaurar uma localização,
ou `None` se o identificador não existir.

```python
def delete_saved_location(location_id: str) -> bool
```

Remove o registro identificado; retorna `False` se inexistente.

As assinaturas podem ser adaptadas aos módulos atuais, mas o acesso ao SQLite deve
ficar encapsulado fora da camada de renderização Streamlit e ser testável com
banco temporário.

## Regras de negócio

- A ação `Salvar localização` só fica disponível quando houver seleção de
  polígono válida capturada no mapa.
- Ao acionar salvar, exibir formulário/modal de nome com confirmação e
  cancelamento; não persistir antes da confirmação.
- Nome é obrigatório após trim, limitado a 100 caracteres e não diferencia
  maiúsculas/minúsculas para detectar duplicatas; espaços consecutivos são
  normalizados para comparação.
- A geometria deve passar pela mesma validação GeoJSON do fluxo de análise:
  geometria Polygon válida, anel fechado, ao menos três vértices distintos,
  coordenadas finitas dentro dos limites geográficos e área maior que zero.
- Guardar GeoJSON em JSON UTF-8 sem simplificação/perda de coordenadas. Não
  persistir objetos `ee.Geometry`, chaves ou dados de autenticação.
- A lista é carregada do armazenamento persistente, não somente de
  `st.session_state`; reruns e reinício do processo não removem registros.
- Mostrar opções salvas abaixo da busca enquanto o usuário interage com o campo,
  incluindo estado vazio e mensagens de erro do armazenamento.
- Selecionar um item salvo restaura GeoJSON, cria/recria `ee.Geometry`, atualiza
  centro e zoom para enquadrar os limites do polígono e reexibe desenho/marcadores
  no mapa; não faz request ao geocodificador.
- Restaurar uma localização limpa resultados de análise incompatíveis com a
  nova geometria e usa o fluxo já existente de validação/execução da análise.
- Não iniciar análise automaticamente ao restaurar a localização.
- Selecionar uma localização não deve salvar outra cópia nem modificar a
  geometria persistida.
- Erros de banco, JSON inválido ou registro corrompido devem ser tratados sem
  encerrar a aplicação; o registro inválido não deve ser convertido em geometria
  silenciosamente.
- Exclusão, se implementada nesta entrega, exige confirmação e não remove
  geometrias atualmente carregadas da sessão. Renomeação fica fora do escopo
  inicial.

## Critérios de aceitação

1. Dado um polígono válido selecionado, quando o usuário salvar e confirmar um
   nome válido, então o registro persiste e aparece na lista abaixo da pesquisa.
2. Dado que o usuário abra e cancele o formulário, então nenhum registro novo é
   criado.
3. Dado nome vazio, maior que 100 caracteres ou duplicado após normalização,
   então o registro é recusado com mensagem orientativa e os existentes são
   preservados.
4. Dada uma geometria inválida, quando o usuário tentar salvá-la, então não há
   gravação nem conversão para geometria analisável.
5. Dado um registro persistido, quando o processo Streamlit reiniciar, então o
   registro continua listado e pode ser recuperado do SQLite.
6. Dada uma localização na lista, quando o usuário selecioná-la, então o mapa
   centraliza/enquadra o polígono, desenha/restaura sua geometria e atualiza o
   estado de seleção coerentemente.
7. Ao selecionar uma localização salva, então o geocodificador não é chamado e
   a análise não começa automaticamente.
8. Ao restaurar outra geometria, então resultados vinculados à seleção anterior
   são limpos para impedir exportar/exibir dados de uma área diferente.
9. Dado banco ausente, inacessível ou com um registro inválido, então a UI
   apresenta erro/estado recuperável sem encerrar ou corromper outros registros.
10. Testes automatizados com SQLite temporário cobrem criação, listagem,
    duplicidade, validação, exclusão (se implementada), persistência após nova
    conexão, restauração de sessão e ausência de geocodificação.

## Dependências

- `10-mapas-interacao/spec-mapa-interacao.md` — busca, geometria, mapa e estado.
- `04-mapas/spec-selecao-area.md` — captura e validação da seleção.
- `15-ui-v2-dashboard-parity/spec-ui-dashboard-parity.md` — localização atual
  dos controles e ciclo de análise.

## Tasks relacionadas

- SPEC-17-01 a SPEC-17-09 — `tasks-localizacoes-salvas.md`.
