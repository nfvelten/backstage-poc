# ADR 0002 - Nao documentar dados reais de producao

## Status

Aceita.

## Contexto

Algumas queries da `comercial-api` retornam dados pessoais, contato, documento, endereço, credenciais indiretas ou informação de crédito. Documentar linhas reais de produção no vault aumentaria risco de vazamento e tornaria o material inadequado para consulta ampla.

## Decisão

Usar o banco de produção apenas para metadados:

- schema, tabelas, colunas, índices e FKs;
- shape de SELECT via consulta sem linhas, como `LIMIT 0`;
- status de introspecção da query.

Não registrar payload real, linha real, token, senha, segredo, CPF, CNPJ, e-mail, telefone ou endereço completo em Markdown.

## Consequências

- A documentação mostra estrutura e impacto sem expor dados sensíveis.
- Debug com dados reais continua sendo feito em ferramenta autorizada e contexto apropriado.
- Quando um campo sensível aparecer, a documentação deve registrar categoria, não valor.
