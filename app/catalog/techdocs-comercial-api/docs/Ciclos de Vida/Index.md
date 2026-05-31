---
tags:
  - trabalho
  - air
  - comercial-api
  - ciclo-de-vida
---
# Ciclos de Vida - comercial-api

Estados e transições das entidades centrais do comercial. Use para entender efeito colateral antes de alterar service, query, payload ou rotina.

| Entidade | Documento | Endpoints principais | Riscos principais |
|---|---|---|---|
| Cliente | [[cliente]] | [[../Endpoints da Collection/get-cliente-por-id|get-cliente-por-id]], [[../Endpoints da Collection/get-cliente-por-cpf|get-cliente-por-cpf]], [[../Endpoints da Collection/get-cliente-contrato|get-cliente-contrato]], [[../Endpoints da Collection/get-cliente-consultar-avisos|get-cliente-consultar-avisos]], [[../Endpoints da Collection/post-oauth-integrar|post-oauth-integrar]] | exposição de PII, estado OAuth incorreto, duplicidade cadastral, contrato associado ao cliente errado |
| Contrato | [[contrato]] | [[../Endpoints da Collection/get-contrato|get-contrato]], [[../Endpoints da Collection/get-cliente-contrato|get-cliente-contrato]], [[../Endpoints da Collection/post-contrato-adicionar-aviso|post-contrato-adicionar-aviso]], [[../Endpoints da Collection/get-migracoes-contrato|get-migracoes-contrato]], [[../Endpoints da Collection/get-contrato-svas-v1|get-contrato-svas-v1]], [[../Endpoints da Collection/ativar-servicos|ativar-servicos]] | mudança de versão indevida, produto/item inconsistente, migração errada, brand incorreta em OAuth |
| Lead | [[lead]] | [[../Endpoints da Collection/post-criar-integracao|post-criar-integracao]], [[../Endpoints da Collection/test-criar-integracao|test-criar-integracao]], [[../Endpoints da Collection/get-cliente-analise-credito|get-cliente-analise-credito]] | dados pessoais no payload, decisão de crédito sobrescrita, lead duplicado por integração repetida |
| Venda | [[venda]] | [[../Endpoints da Collection/post-criar-integracao|post-criar-integracao]], [[../Endpoints da Collection/ativar-servicos|ativar-servicos]], [[../Endpoints da Collection/get-vendas-by-natureza|get-vendas-by-natureza]], [[../Endpoints da Collection/get-vendas-contrato|get-vendas-contrato]] | ativação duplicada, desconto recorrente duplicado, fase incorreta, notificação externa repetida |
