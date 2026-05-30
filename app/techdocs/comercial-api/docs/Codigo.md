---
tags: [trabalho, air, api, documentacao, comercial-api, codigo]
gerado_em: 2026-05-29 21:07:41
---
# Codigo

## Resumo

| Item | Quantidade |
|---|---:|
| Classes/interfaces/enums | 825 |
| Linhas com indicio de SQL nativo | 174 |

## Annotations principais

| Annotation | Ocorrencias |
|---|---:|
| Data | 232 |
| XmlType | 171 |
| XmlAccessorType | 162 |
| Getter | 97 |
| Service | 93 |
| Setter | 90 |
| Entity | 81 |
| Table | 81 |
| NoArgsConstructor | 64 |
| AllArgsConstructor | 59 |
| RestController | 58 |
| RequestMapping | 58 |
| CrossOrigin | 54 |
| Builder | 51 |
| RequiredArgsConstructor | 42 |
| Descricao | 31 |
| Slf4j | 28 |
| Log | 27 |
| Component | 16 |
| XmlSeeAlso | 13 |
| XmlEnum | 9 |
| Accessors | 8 |
| Configuration | 7 |
| ToString | 6 |
| Repository | 6 |
| JsonInclude | 4 |
| EqualsAndHashCode | 3 |
| Api | 2 |
| EntityListeners | 2 |
| PrimaryKeyJoinColumn | 2 |
| Embeddable | 2 |
| SpringBootApplication | 1 |
| EnableAsync | 1 |
| EnableCaching | 1 |
| EnableScheduling | 1 |
| ComponentScan | 1 |
| EnableJpaRepositories | 1 |
| EnableJpaAuditing | 1 |
| PropertySource | 1 |
| EnableWebSocketMessageBroker | 1 |
| ConfigurationProperties | 1 |
| FunctionalInterface | 1 |
| Inheritance | 1 |
| JsonIgnoreProperties | 1 |
| RestControllerAdvice | 1 |
| WebService | 1 |
| SOAPBinding | 1 |
| WebServiceClient | 1 |
| XmlRegistry | 1 |
| Controller | 1 |

## Pacotes com mais classes

| Pacote | Classes |
|---|---:|
| br.net.air.spc.soap | 177 |
| br.net.air.cliente.dto | 68 |
| br.net.air.cliente.model | 42 |
| br.net.air.cliente.repository | 36 |
| br.net.air.venda.dto | 36 |
| br.net.air.cliente.service | 31 |
| br.net.air.clean_arch.application.dto | 29 |
| br.net.air.venda.model | 20 |
| br.net.air.configuracoes.service | 16 |
| br.net.air.venda.repository | 16 |
| br.net.air.configuracoes.controller | 15 |
| br.net.air.configuracoes.repository | 15 |
| br.net.air.configuracoes.model | 14 |
| br.net.air.configuracoes.dto | 13 |
| br.net.air.venda.service | 13 |
| br.net.air | 10 |
| br.net.air.composicao.dto | 10 |
| br.net.air.venda.dto.analisecreditolead | 10 |
| br.net.air.cliente.controller | 9 |
| br.net.air.clean_arch.infra.gateways | 8 |
| br.net.air.exception | 8 |
| br.net.air.clean_arch.domain.models.responses | 7 |
| br.net.air.integracao.dto | 7 |
| br.net.air.notification.dto | 7 |
| br.net.air.cliente.event | 6 |
| br.net.air.configuracoes.googleplace.model | 6 |
| br.net.air.ecare.dto | 6 |
| br.net.air.migracao.dto | 6 |
| br.net.air.venda.controller | 6 |
| br.net.air.venda.dto.analisecreditolead.projection | 6 |
| br.net.air.clean_arch.application.services | 5 |
| br.net.air.clean_arch.domain.usecases | 5 |
| br.net.air.clean_arch.infra.gateways.adapters | 5 |
| br.net.air.cliente.projection | 5 |
| br.net.air.composicao.model | 5 |
| br.net.air.composicao.repository | 5 |
| br.net.air.clean_arch.application.enuns | 4 |
| br.net.air.clean_arch.infra.gateways.request.link_shortener | 4 |
| br.net.air.clean_arch.validator | 4 |
| br.net.air.ecare.client | 4 |
| br.net.air.financeiro.controller | 4 |
| br.net.air.financeiro.dto | 4 |
| br.net.air.financeiro.model | 4 |
| br.net.air.financeiro.repository | 4 |
| br.net.air.financeiro.service | 4 |
| br.net.air.util | 4 |
| br.net.air.app.controller | 3 |
| br.net.air.app.dto | 3 |
| br.net.air.app.model | 3 |
| br.net.air.app.repository | 3 |

## Inventario de classes

| Classe | Tipo | Pacote | Annotations | Arquivo |
|---|---|---|---|---|
| `App` | class | `br.net.air` | @SpringBootApplication | `comercial-api/src/main/java/br/net/air/App.java` |
| `AppConfiguration` | class | `br.net.air` | @Configuration, @Slf4j, @EnableAsync, @EnableCaching, @EnableScheduling, @ComponentScan, @EnableJpaRepositories, @EnableJpaAuditing, @PropertySource | `comercial-api/src/main/java/br/net/air/AppConfiguration.java` |
| `ApplicationController` | class | `br.net.air` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/ApplicationController.java` |
| `Constantes` | class | `br.net.air` |  | `comercial-api/src/main/java/br/net/air/Constantes.java` |
| `MetricsConfig` | class | `br.net.air` | @Configuration | `comercial-api/src/main/java/br/net/air/MetricsConfig.java` |
| `MetricsController` | class | `br.net.air` | @RestController, @RequestMapping, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/MetricsController.java` |
| `SydleConnection` | class | `br.net.air` | @Log, @Service | `comercial-api/src/main/java/br/net/air/SydleConnection.java` |
| `UserCodeMetricsInterceptor` | class | `br.net.air` | @Component, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/UserCodeMetricsInterceptor.java` |
| `WebMvcConfig` | class | `br.net.air` | @Configuration, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/WebMvcConfig.java` |
| `WebSocketConfiguration` | class | `br.net.air` | @Configuration, @EnableWebSocketMessageBroker | `comercial-api/src/main/java/br/net/air/WebSocketConfiguration.java` |
| `AppAdicionalController` | class | `br.net.air.app.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/app/controller/AppAdicionalController.java` |
| `AppUpgradeController` | class | `br.net.air.app.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/app/controller/AppUpgradeController.java` |
| `AppVendaController` | class | `br.net.air.app.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/app/controller/AppVendaController.java` |
| `AppAdicionalDTO` | class | `br.net.air.app.dto` | @Data | `comercial-api/src/main/java/br/net/air/app/dto/AppAdicionalDTO.java` |
| `AppUpgradeDTO` | class | `br.net.air.app.dto` | @Data | `comercial-api/src/main/java/br/net/air/app/dto/AppUpgradeDTO.java` |
| `AppVendaDTO` | class | `br.net.air.app.dto` | @Data | `comercial-api/src/main/java/br/net/air/app/dto/AppVendaDTO.java` |
| `AppAdicional` | class | `br.net.air.app.model` | @Entity, @Getter, @Setter, @Descricao, @Table | `comercial-api/src/main/java/br/net/air/app/model/AppAdicional.java` |
| `AppUpgrade` | class | `br.net.air.app.model` | @Entity, @Getter, @Setter, @Descricao, @Table | `comercial-api/src/main/java/br/net/air/app/model/AppUpgrade.java` |
| `AppVenda` | class | `br.net.air.app.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/app/model/AppVenda.java` |
| `AppAdicionalRepository` | interface | `br.net.air.app.repository` |  | `comercial-api/src/main/java/br/net/air/app/repository/AppAdicionalRepository.java` |
| `AppUpgradeRepository` | interface | `br.net.air.app.repository` |  | `comercial-api/src/main/java/br/net/air/app/repository/AppUpgradeRepository.java` |
| `AppVendaRepository` | interface | `br.net.air.app.repository` |  | `comercial-api/src/main/java/br/net/air/app/repository/AppVendaRepository.java` |
| `AppAdicionalService` | class | `br.net.air.app.service` | @Service | `comercial-api/src/main/java/br/net/air/app/service/AppAdicionalService.java` |
| `AppUpgradeService` | class | `br.net.air.app.service` | @Service | `comercial-api/src/main/java/br/net/air/app/service/AppUpgradeService.java` |
| `AppVendaService` | class | `br.net.air.app.service` | @Service | `comercial-api/src/main/java/br/net/air/app/service/AppVendaService.java` |
| `AssineController` | class | `br.net.air.assine.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/assine/controller/AssineController.java` |
| `RelatorioLomadeeDTO` | class | `br.net.air.assine.dto` | @Data, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/assine/dto/RelatorioLomadeeDTO.java` |
| `AssineService` | class | `br.net.air.assine.service` | @Service, @Log | `comercial-api/src/main/java/br/net/air/assine/service/AssineService.java` |
| `ContractApiV1` | interface | `br.net.air.clean_arch.application.controllers` |  | `comercial-api/src/main/java/br/net/air/clean_arch/application/controllers/ContractApiV1.java` |
| `ContractsControllerV1` | class | `br.net.air.clean_arch.application.controllers` | @RestController, @RequiredArgsConstructor, @CrossOrigin, @RequestMapping | `comercial-api/src/main/java/br/net/air/clean_arch/application/controllers/ContractsControllerV1.java` |
| `ContactApiV1` | interface | `br.net.air.clean_arch.application.controllers.contactController` |  | `comercial-api/src/main/java/br/net/air/clean_arch/application/controllers/contactController/ContactApiV1.java` |
| `ContactControllerV1` | class | `br.net.air.clean_arch.application.controllers.contactController` | @RestController, @RequiredArgsConstructor, @CrossOrigin, @RequestMapping | `comercial-api/src/main/java/br/net/air/clean_arch/application/controllers/contactController/ContactControllerV1.java` |
| `CustomerApiV1` | interface | `br.net.air.clean_arch.application.controllers.customerController` |  | `comercial-api/src/main/java/br/net/air/clean_arch/application/controllers/customerController/CustomerApiV1.java` |
| `CustomerControllerV1` | class | `br.net.air.clean_arch.application.controllers.customerController` | @RestController, @RequiredArgsConstructor, @CrossOrigin, @RequestMapping | `comercial-api/src/main/java/br/net/air/clean_arch/application/controllers/customerController/CustomerControllerV1.java` |
| `InvoiceApiV1` | interface | `br.net.air.clean_arch.application.controllers.invoiceController` |  | `comercial-api/src/main/java/br/net/air/clean_arch/application/controllers/invoiceController/InvoiceApiV1.java` |
| `InvoiceControllerV1` | class | `br.net.air.clean_arch.application.controllers.invoiceController` | @CrossOrigin, @RestController, @RequiredArgsConstructor, @RequestMapping | `comercial-api/src/main/java/br/net/air/clean_arch/application/controllers/invoiceController/InvoiceControllerV1.java` |
| `NotificationApiV1` | interface | `br.net.air.clean_arch.application.controllers.notificationController` |  | `comercial-api/src/main/java/br/net/air/clean_arch/application/controllers/notificationController/NotificationApiV1.java` |
| `NotificationControllerV1` | class | `br.net.air.clean_arch.application.controllers.notificationController` | @CrossOrigin, @RestController, @RequiredArgsConstructor, @RequestMapping | `comercial-api/src/main/java/br/net/air/clean_arch/application/controllers/notificationController/NotificationControllerV1.java` |
| `AirContractChangePlanDto` | class | `br.net.air.clean_arch.application.dto` | @Data, @Getter, @Setter, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/AirContractChangePlanDto.java` |
| `BearerTokenDto` | class | `br.net.air.clean_arch.application.dto` | @Data | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/BearerTokenDto.java` |
| `BucketProperties` | class | `br.net.air.clean_arch.application.dto` | @Data, @Component, @ConfigurationProperties | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/BucketProperties.java` |
| `ChangePlanRequestDto` | class | `br.net.air.clean_arch.application.dto` | @Data, @Getter, @Setter, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/ChangePlanRequestDto.java` |
| `ChangeProductRequestDto` | class | `br.net.air.clean_arch.application.dto` | @Data, @Getter, @Setter, @NoArgsConstructor, @AllArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/ChangeProductRequestDto.java` |
| `ProdutoPacote` | class | `br.net.air.clean_arch.application.dto` | @Data, @Getter, @Setter, @NoArgsConstructor, @AllArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/ChangeProductRequestDto.java` |
| `ProdutosAdicionais` | class | `br.net.air.clean_arch.application.dto` | @Data, @Getter, @Setter, @NoArgsConstructor, @AllArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/ChangeProductRequestDto.java` |
| `ClienteResumoAvisoDTO` | class | `br.net.air.clean_arch.application.dto` | @Data, @NoArgsConstructor, @AllArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/ClienteResumoAvisoDTO.java` |
| `ContractDetailAdditionalTvPointDataDto` | class | `br.net.air.clean_arch.application.dto` | @Data, @Builder, @AllArgsConstructor, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/ContractDetailAdditionalTvPointDataDto.java` |
| `ContractItemAdditionalDto` | class | `br.net.air.clean_arch.application.dto` | @Data, @Builder, @AllArgsConstructor, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/ContractItemAdditionalDto.java` |
| `ContractItemDto` | class | `br.net.air.clean_arch.application.dto` | @Data, @Builder, @AllArgsConstructor, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/ContractItemDto.java` |
| `ContratoPacoteDTO` | class | `br.net.air.clean_arch.application.dto` | @Data, @AllArgsConstructor, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/ContratoPacoteDTO.java` |
| `CustomerContact` | class | `br.net.air.clean_arch.application.dto` | @Data, @Builder, @AllArgsConstructor, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/CustomerContact.java` |
| `CustomerContactRequestDto` | class | `br.net.air.clean_arch.application.dto` | @Data, @Builder, @AllArgsConstructor, @NoArgsConstructor, @JsonInclude | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/CustomerContactRequestDto.java` |
| `ContactType` | enum | `br.net.air.clean_arch.application.dto` |  | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/CustomerContactRequestDto.java` |
| `DiscountChangePlanDto` | class | `br.net.air.clean_arch.application.dto` | @Data, @Getter, @Setter, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/DiscountChangePlanDto.java` |
| `NotificationDto` | class | `br.net.air.clean_arch.application.dto` | @Data, @NoArgsConstructor, @AllArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/NotificationDto.java` |
| `PackageComponentDto` | class | `br.net.air.clean_arch.application.dto` | @Data | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/PackageComponentDto.java` |
| `PrincipalContactDto` | class | `br.net.air.clean_arch.application.dto` | @Data | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/PrincipalContactDto.java` |
| `RespObjSvasDtoV2` | class | `br.net.air.clean_arch.application.dto` | @Data | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/RespObjSvasDtoV2.java` |
| `RespSvaCredentialsDto` | class | `br.net.air.clean_arch.application.dto` | @Data | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/RespSvaCredentialsDto.java` |
| `RespSvasDtoV2` | class | `br.net.air.clean_arch.application.dto` | @Data | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/RespSvasDtoV2.java` |
| `SecondCopyBilletDto` | class | `br.net.air.clean_arch.application.dto` | @Data | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/SecondCopyBilletDto.java` |
| `SecondCopyDto` | class | `br.net.air.clean_arch.application.dto` | @Data | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/SecondCopyDto.java` |
| `SecondCopyInvoiceDataDto` | class | `br.net.air.clean_arch.application.dto` | @Data | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/SecondCopyInvoiceDataDto.java` |
| `SendDisputeComunicationDto` | class | `br.net.air.clean_arch.application.dto` | @Data, @NoArgsConstructor, @AllArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/SendDisputeComunicationDto.java` |
| `SendDisputeComunicationRequest` | class | `br.net.air.clean_arch.application.dto` |  | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/SendDisputeComunicationRequest.java` |
| `TelevisionInfoApiDto` | class | `br.net.air.clean_arch.application.dto` | @Builder, @Data, @AllArgsConstructor, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/TelevisionInfoApiDto.java` |
| `WhatsappMessageRequestDto` | class | `br.net.air.clean_arch.application.dto` | @Data, @NoArgsConstructor, @AllArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/WhatsappMessageRequestDto.java` |
| `GetSecondCopyOfDigitalInvoiceResponse` | class | `br.net.air.clean_arch.application.dto.invoice` | @Data, @JsonInclude | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/invoice/GetSecondCopyOfDigitalInvoiceResponse.java` |
| `SendPaidInvoiceResponse` | class | `br.net.air.clean_arch.application.dto.invoice` | @Data | `comercial-api/src/main/java/br/net/air/clean_arch/application/dto/invoice/SendPaidInvoiceResponse.java` |
| `ContractItemType` | enum | `br.net.air.clean_arch.application.enuns` | @Getter, @AllArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/application/enuns/ContractItemType.java` |
| `ContractStatus` | enum | `br.net.air.clean_arch.application.enuns` | @Getter, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/application/enuns/ContractStatus.java` |
| `DocumentType` | enum | `br.net.air.clean_arch.application.enuns` |  | `comercial-api/src/main/java/br/net/air/clean_arch/application/enuns/DocumentType.java` |
| `EventType` | enum | `br.net.air.clean_arch.application.enuns` | @AllArgsConstructor, @Getter | `comercial-api/src/main/java/br/net/air/clean_arch/application/enuns/EventType.java` |
| `ContactServiceV1` | class | `br.net.air.clean_arch.application.services` | @Slf4j, @Service, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/application/services/ContactServiceV1.java` |
| `ContractServiceV1` | class | `br.net.air.clean_arch.application.services` | @Slf4j, @Service, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/application/services/ContractServiceV1.java` |
| `CustomerServiceV1` | class | `br.net.air.clean_arch.application.services` | @Service, @AllArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/application/services/CustomerServiceV1.java` |
| `InvoiceServiceV1` | class | `br.net.air.clean_arch.application.services` | @Service, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/application/services/InvoiceServiceV1.java` |
| `NotificationServiceV1` | class | `br.net.air.clean_arch.application.services` | @Service, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/application/services/NotificationServiceV1.java` |
| `CrmProvider` | interface | `br.net.air.clean_arch.domain.gateways` |  | `comercial-api/src/main/java/br/net/air/clean_arch/domain/gateways/CrmProvider.java` |
| `FinancialProvider` | interface | `br.net.air.clean_arch.domain.gateways` |  | `comercial-api/src/main/java/br/net/air/clean_arch/domain/gateways/FinancialProvider.java` |
| `NotificationProvider` | interface | `br.net.air.clean_arch.domain.gateways` |  | `comercial-api/src/main/java/br/net/air/clean_arch/domain/gateways/NotificationProvider.java` |
| `ChangePlanResponse` | class | `br.net.air.clean_arch.domain.models.responses` | @Data, @Getter, @Setter, @Builder | `comercial-api/src/main/java/br/net/air/clean_arch/domain/models/responses/ChangePlanResponse.java` |
| `CheckContractTrustEnablementBalanceResponse` | class | `br.net.air.clean_arch.domain.models.responses` | @Data, @Getter, @Setter, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/domain/models/responses/CheckContractTrustEnablementBalanceResponse.java` |
| `CustomerBasicInfoDto` | class | `br.net.air.clean_arch.domain.models.responses` | @Data, @Builder, @AllArgsConstructor, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/domain/models/responses/CustomerBasicInfoDto.java` |
| `CustomerBasicInfoQueryDto` | class | `br.net.air.clean_arch.domain.models.responses` | @Data, @AllArgsConstructor, @NoArgsConstructor, @Builder | `comercial-api/src/main/java/br/net/air/clean_arch/domain/models/responses/CustomerBasicInfoQueryDto.java` |
| `CustomerContactResponseDto` | class | `br.net.air.clean_arch.domain.models.responses` | @Data, @Builder, @AllArgsConstructor, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/domain/models/responses/CustomerContactResponseDto.java` |
| `GetSvasDto` | class | `br.net.air.clean_arch.domain.models.responses` | @Data, @Builder, @AllArgsConstructor, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/domain/models/responses/GetSvasDto.java` |
| `SydleContractTrustEnablementBalanceResponse` | class | `br.net.air.clean_arch.domain.models.responses` | @Data, @Getter, @Setter, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/domain/models/responses/SydleContractTrustEnablementBalanceResponse.java` |
| `ContactUseCase` | interface | `br.net.air.clean_arch.domain.usecases` |  | `comercial-api/src/main/java/br/net/air/clean_arch/domain/usecases/ContactUseCase.java` |
| `ContractUseCase` | interface | `br.net.air.clean_arch.domain.usecases` |  | `comercial-api/src/main/java/br/net/air/clean_arch/domain/usecases/ContractUseCase.java` |
| `CustomerUseCase` | interface | `br.net.air.clean_arch.domain.usecases` |  | `comercial-api/src/main/java/br/net/air/clean_arch/domain/usecases/CustomerUseCase.java` |
| `InvoiceUseCase` | interface | `br.net.air.clean_arch.domain.usecases` |  | `comercial-api/src/main/java/br/net/air/clean_arch/domain/usecases/InvoiceUseCase.java` |
| `NotificationUseCase` | interface | `br.net.air.clean_arch.domain.usecases` |  | `comercial-api/src/main/java/br/net/air/clean_arch/domain/usecases/NotificationUseCase.java` |
| `AirTvProvider` | class | `br.net.air.clean_arch.infra.gateways` | @Component | `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/AirTvProvider.java` |
| `CrmServiceProvider` | class | `br.net.air.clean_arch.infra.gateways` | @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/CrmServiceProvider.java` |
| `CrmServiceProviderBeanConfiguration` | class | `br.net.air.clean_arch.infra.gateways` | @Configuration | `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/CrmServiceProviderBeanConfiguration.java` |
| `FinancialServiceProvider` | class | `br.net.air.clean_arch.infra.gateways` | @Slf4j | `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/FinancialServiceProvider.java` |
| `FinancialServiceProviderBeanConfiguration` | class | `br.net.air.clean_arch.infra.gateways` | @Configuration | `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/FinancialServiceProviderBeanConfiguration.java` |
| `LinkShortenerProvider` | class | `br.net.air.clean_arch.infra.gateways` | @Slf4j, @Component | `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/LinkShortenerProvider.java` |
| `NotificationApiProvider` | class | `br.net.air.clean_arch.infra.gateways` | @Slf4j | `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/NotificationApiProvider.java` |
| `NotificationApiProviderBeanConfiguration` | class | `br.net.air.clean_arch.infra.gateways` | @Configuration | `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/NotificationApiProviderBeanConfiguration.java` |
| `ContractAdapter` | class | `br.net.air.clean_arch.infra.gateways.adapters` | @RequiredArgsConstructor, @Component | `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/adapters/ContractAdapter.java` |
| `CustomerContactAdapter` | class | `br.net.air.clean_arch.infra.gateways.adapters` | @Component, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/adapters/CustomerContactAdapter.java` |
| `LinkShortenerAdapter` | class | `br.net.air.clean_arch.infra.gateways.adapters` |  | `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/adapters/LinkShortenerAdapter.java` |
| `NotificationApiAdapter` | class | `br.net.air.clean_arch.infra.gateways.adapters` | @Slf4j, @Component | `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/adapters/NotificationApiAdapter.java` |
| `MessageBuilder` | interface | `br.net.air.clean_arch.infra.gateways.adapters` | @FunctionalInterface | `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/adapters/NotificationApiAdapter.java` |
| `CustomerContactRequestDto` | class | `br.net.air.clean_arch.infra.gateways.request.contact` | @Data, @Builder, @AllArgsConstructor, @NoArgsConstructor, @JsonInclude | `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/request/contact/CustomerContactRequestDto.java` |
| `UpdatePasswordRequestDto` | class | `br.net.air.clean_arch.infra.gateways.request.customer` |  | `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/request/customer/UpdatePasswordRequestDto.java` |
| `LinkShortenerRequestDto` | class | `br.net.air.clean_arch.infra.gateways.request.link_shortener` | @Data, @Builder, @NoArgsConstructor, @AllArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/request/link_shortener/LinkShortenerRequestDto.java` |
| `DynamicLinkInfo` | class | `br.net.air.clean_arch.infra.gateways.request.link_shortener` | @Data, @Builder, @JsonInclude | `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/request/link_shortener/LinkShortenerRequestDto.java` |
| `AndroidInfo` | class | `br.net.air.clean_arch.infra.gateways.request.link_shortener` | @Data, @Builder | `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/request/link_shortener/LinkShortenerRequestDto.java` |
| `IosInfo` | class | `br.net.air.clean_arch.infra.gateways.request.link_shortener` | @Data, @Builder | `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/request/link_shortener/LinkShortenerRequestDto.java` |
| `WhatsappNotificationRequest` | class | `br.net.air.clean_arch.infra.gateways.request.notificationApi` | @Data, @Builder, @NoArgsConstructor, @AllArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/request/notificationApi/WhatsappNotificationRequest.java` |
| `ContactMessageWhatsappRequestDTO` | class | `br.net.air.clean_arch.infra.gateways.request.notificationApi` | @Data, @Builder, @NoArgsConstructor, @AllArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/request/notificationApi/WhatsappNotificationRequest.java` |
| `LinkShortenerResponseDto` | class | `br.net.air.clean_arch.infra.gateways.responses.link_shortener` | @Data | `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/responses/link_shortener/LinkShortenerResponseDto.java` |
| `UrlShortenerResponse` | class | `br.net.air.clean_arch.infra.gateways.responses.link_shortener` | @Data | `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/responses/link_shortener/UrlShortenerResponse.java` |
| `ArgumentErrorDto` | class | `br.net.air.clean_arch.validator` |  | `comercial-api/src/main/java/br/net/air/clean_arch/validator/ArgumentErrorDto.java` |
| `ArgumentErrorDtoBuilder` | class | `br.net.air.clean_arch.validator` |  | `comercial-api/src/main/java/br/net/air/clean_arch/validator/ArgumentErrorDto.java` |
| `CustomerContactValidator` | class | `br.net.air.clean_arch.validator` | @Component, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/clean_arch/validator/CustomerContactValidator.java` |
| `DocumentValidator` | class | `br.net.air.clean_arch.validator` |  | `comercial-api/src/main/java/br/net/air/clean_arch/validator/DocumentValidator.java` |
| `ContratoBuilder` | class | `br.net.air.cliente.builder` | @Component | `comercial-api/src/main/java/br/net/air/cliente/builder/ContratoBuilder.java` |
| `BlacklistController` | class | `br.net.air.cliente.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/cliente/controller/BlacklistController.java` |
| `ClienteAnexoController` | class | `br.net.air.cliente.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/cliente/controller/ClienteAnexoController.java` |
| `ClienteContatoController` | class | `br.net.air.cliente.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/cliente/controller/ClienteContatoController.java` |
| `ClienteController` | class | `br.net.air.cliente.controller` | @Slf4j, @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/cliente/controller/ClienteController.java` |
| `ContratoAvisoController` | class | `br.net.air.cliente.controller` | @CrossOrigin, @RestController, @RequestMapping, @Api | `comercial-api/src/main/java/br/net/air/cliente/controller/ContratoAvisoController.java` |
| `ContratoController` | class | `br.net.air.cliente.controller` | @Slf4j, @CrossOrigin, @RestController, @RequestMapping, @Api | `comercial-api/src/main/java/br/net/air/cliente/controller/ContratoController.java` |
| `ContratoEnderecoController` | class | `br.net.air.cliente.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/cliente/controller/ContratoEnderecoController.java` |
| `ContratoReajusteController` | class | `br.net.air.cliente.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/cliente/controller/ContratoReajusteController.java` |
| `ContratoRetencaoController` | class | `br.net.air.cliente.controller` | @Slf4j, @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/cliente/controller/ContratoRetencaoController.java` |
| `AlterarCepDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/AlterarCepDTO.java` |
| `AlterarFormaPagamentoSydleDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/AlterarFormaPagamentoSydleDTO.java` |
| `AlterarPlanoSydleDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/AlterarPlanoSydleDTO.java` |
| `Anexo` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/Anexo.java` |
| `AtivacaoSemValidacaoSydleDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/AtivacaoSemValidacaoSydleDTO.java` |
| `AuditoriaHabilitarConfiancaDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/AuditoriaHabilitarConfiancaDTO.java` |
| `AvisoRedeContratoDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/AvisoRedeContratoDTO.java` |
| `AvisoRedeDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/AvisoRedeDTO.java` |
| `AvisoRedeExternaDto` | class | `br.net.air.cliente.dto` | @Data, @Builder | `comercial-api/src/main/java/br/net/air/cliente/dto/AvisoRedeExternaDto.java` |
| `BlacklistDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/BlacklistDTO.java` |
| `BuscarOSDTO` | class | `br.net.air.cliente.dto` | @Data, @AllArgsConstructor | `comercial-api/src/main/java/br/net/air/cliente/dto/BuscarOSDTO.java` |
| `BuscarOSResponseDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/BuscarOSResponseDTO.java` |
| `CadastrarIntegracaoDTO` | class | `br.net.air.cliente.dto` | @Data, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/cliente/dto/CadastrarIntegracaoDTO.java` |
| `CancelarContratoDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/CancelarContratoDTO.java` |
| `ChamadoDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/ChamadoDTO.java` |
| `ClassificarRiscoDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/ClassificarRiscoDTO.java` |
| `ClienteAnexoDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/ClienteAnexoDTO.java` |
| `ClienteContatoDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/ClienteContatoDTO.java` |
| `ClienteDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/ClienteDTO.java` |
| `ClienteEventoDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/ClienteEventoDTO.java` |
| `ClienteLeadCarteiraDto` | class | `br.net.air.cliente.dto` | @Data, @NoArgsConstructor, @AllArgsConstructor, @Builder | `comercial-api/src/main/java/br/net/air/cliente/dto/ClienteLeadCarteiraDto.java` |
| `ClienteLeadDto` | class | `br.net.air.cliente.dto` | @Data, @AllArgsConstructor | `comercial-api/src/main/java/br/net/air/cliente/dto/ClienteLeadDto.java` |
| `ClienteLeadFisicoDto` | class | `br.net.air.cliente.dto` | @Data, @EqualsAndHashCode | `comercial-api/src/main/java/br/net/air/cliente/dto/ClienteLeadFisicoDto.java` |
| `ClienteLeadIntegracaoDto` | class | `br.net.air.cliente.dto` | @Data, @NoArgsConstructor, @AllArgsConstructor, @Builder | `comercial-api/src/main/java/br/net/air/cliente/dto/ClienteLeadIntegracaoDto.java` |
| `ClienteLeadIntegracaoSydleDto` | class | `br.net.air.cliente.dto` | @Data, @NoArgsConstructor, @AllArgsConstructor, @Builder | `comercial-api/src/main/java/br/net/air/cliente/dto/ClienteLeadIntegracaoSydleDto.java` |
| `ClienteLeadJuridicoDto` | class | `br.net.air.cliente.dto` | @Data, @EqualsAndHashCode | `comercial-api/src/main/java/br/net/air/cliente/dto/ClienteLeadJuridicoDto.java` |
| `ClienteLeadVendedorDto` | class | `br.net.air.cliente.dto` | @Data, @NoArgsConstructor, @AllArgsConstructor, @Builder | `comercial-api/src/main/java/br/net/air/cliente/dto/ClienteLeadVendedorDto.java` |
| `ClienteResumoDTO` | class | `br.net.air.cliente.dto` | @Builder, @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/ClienteResumoDTO.java` |
| `ConsultaCircuitIDResponse` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/ConsultaCircuitIDResponse.java` |
| `ContractAddressResponseDto` | class | `br.net.air.cliente.dto` | @Data, @AllArgsConstructor, @NoArgsConstructor, @Builder | `comercial-api/src/main/java/br/net/air/cliente/dto/ContractAddressResponseDto.java` |
| `ContratoAvisoOnuDTO` | class | `br.net.air.cliente.dto` | @Data, @Builder, @AllArgsConstructor, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/cliente/dto/ContratoAvisoOnuDTO.java` |
| `ContratoEntregaDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/ContratoEntregaDTO.java` |
| `ContratoFormaPagamentoDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/ContratoFormaPagamentoDTO.java` |
| `ContratoMarcadorDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/ContratoMarcadorDTO.java` |
| `ContratoProdutoDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/ContratoProdutoDTO.java` |
| `ContratoRetencaoContatoDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/ContratoRetencaoContatoDTO.java` |
| `ContratoRetencaoDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/ContratoRetencaoDTO.java` |
| `CriarDescontoRecorrenteDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/CriarDescontoRecorrenteDTO.java` |
| `CupomDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/CupomDTO.java` |
| `EnderecoClienteCidadeDto` | class | `br.net.air.cliente.dto` | @Data, @NoArgsConstructor, @AllArgsConstructor, @Builder | `comercial-api/src/main/java/br/net/air/cliente/dto/EnderecoClienteCidadeDto.java` |
| `EnderecoClienteDto` | class | `br.net.air.cliente.dto` | @Data, @NoArgsConstructor, @AllArgsConstructor, @Builder | `comercial-api/src/main/java/br/net/air/cliente/dto/EnderecoClienteDto.java` |
| `EnderecoCondominioDto` | class | `br.net.air.cliente.dto` | @Data, @NoArgsConstructor, @AllArgsConstructor, @Builder | `comercial-api/src/main/java/br/net/air/cliente/dto/EnderecoCondominioDto.java` |
| `EnderecoDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/EnderecoDTO.java` |
| `EnderecoViabilidadeDto` | class | `br.net.air.cliente.dto` | @Data, @NoArgsConstructor, @AllArgsConstructor, @Builder | `comercial-api/src/main/java/br/net/air/cliente/dto/EnderecoViabilidadeDto.java` |
| `EventoONUDetailsDTO` | class | `br.net.air.cliente.dto` | @Data, @Builder | `comercial-api/src/main/java/br/net/air/cliente/dto/EventoONUDetailsDTO.java` |
| `EventosONUDTO` | class | `br.net.air.cliente.dto` | @Data, @Builder | `comercial-api/src/main/java/br/net/air/cliente/dto/EventosONUDTO.java` |
| `HabilitarConfiancaDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/HabilitarConfiancaDTO.java` |
| `HabilitarConfiancaRetornoSydleDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/HabilitarConfiancaRetornoSydleDTO.java` |
| `HabilitarConfiancaSydleDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/HabilitarConfiancaSydleDTO.java` |
| `IdSuporteVirtualDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/IdSuporteVirtualDTO.java` |
| `IntegracaoEnderecoCidadeDTO` | class | `br.net.air.cliente.dto` | @Data, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/cliente/dto/IntegracaoEnderecoCidadeDTO.java` |
| `IntegracaoOrdemServicoDTO` | class | `br.net.air.cliente.dto` | @Data, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/cliente/dto/IntegracaoOrdemServicoDTO.java` |
| `LinkContratoAutoISPDTO` | class | `br.net.air.cliente.dto` | @Getter, @Setter | `comercial-api/src/main/java/br/net/air/cliente/dto/LinkContratoAutoISPDTO.java` |
| `MarcadoresClientesDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/MarcadoresClientesDTO.java` |
| `MarcadoresContratoDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/MarcadoresContratoDTO.java` |
| `MotivoHabilitacaoConfiancaDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/MotivoHabilitacaoConfiancaDTO.java` |
| `OnuDTO` | class | `br.net.air.cliente.dto` | @Data, @Builder, @AllArgsConstructor, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/cliente/dto/OnuDTO.java` |
| `OutrosMarcadoresDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/OutrosMarcadoresDTO.java` |
| `PerfilacaoCobrancaDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/PerfilacaoCobrancaDTO.java` |
| `PerfilacaoOuvidoriaDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/PerfilacaoOuvidoriaDTO.java` |
| `PerfilacaoRetencaoDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/PerfilacaoRetencaoDTO.java` |
| `ReajusteDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/ReajusteDTO.java` |
| `ReajusteResponseDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/ReajusteResponseDTO.java` |
| `RenovarSaldoConfiancaSydleDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/RenovarSaldoConfiancaSydleDTO.java` |
| `ReqTrocaEmailDTO` | class | `br.net.air.cliente.dto` | @Data, @Builder | `comercial-api/src/main/java/br/net/air/cliente/dto/ReqTrocaEmailDTO.java` |
| `RespTrocaEmailDTO` | class | `br.net.air.cliente.dto` | @Data, @NoArgsConstructor, @AllArgsConstructor | `comercial-api/src/main/java/br/net/air/cliente/dto/RespTrocaEmailDTO.java` |
| `ReverterEnderecoDTO` | class | `br.net.air.cliente.dto` | @Data | `comercial-api/src/main/java/br/net/air/cliente/dto/ReverterEnderecoDTO.java` |
| `SapServicoDTO` | class | `br.net.air.cliente.dto` | @Getter, @Setter, @EqualsAndHashCode | `comercial-api/src/main/java/br/net/air/cliente/dto/SapServicoDTO.java` |
| `AvisoEvent` | class | `br.net.air.cliente.event` | @Data, @Builder | `comercial-api/src/main/java/br/net/air/cliente/event/AvisoEvent.java` |
| `Gravidade` | enum | `br.net.air.cliente.event` |  | `comercial-api/src/main/java/br/net/air/cliente/event/AvisoEvent.java` |
| `Tipo` | enum | `br.net.air.cliente.event` |  | `comercial-api/src/main/java/br/net/air/cliente/event/AvisoEvent.java` |
| `ClienteEvent` | class | `br.net.air.cliente.event` | @Data, @Builder | `comercial-api/src/main/java/br/net/air/cliente/event/ClienteEvent.java` |
| `Tipo` | enum | `br.net.air.cliente.event` |  | `comercial-api/src/main/java/br/net/air/cliente/event/ClienteEvent.java` |
| `ClienteListener` | class | `br.net.air.cliente.event` | @Component | `comercial-api/src/main/java/br/net/air/cliente/event/ClienteListener.java` |
| `BlacklistException` | class | `br.net.air.cliente.exception` |  | `comercial-api/src/main/java/br/net/air/cliente/exception/BlacklistException.java` |
| `ContratoException` | class | `br.net.air.cliente.exception` |  | `comercial-api/src/main/java/br/net/air/cliente/exception/ContratoException.java` |
| `EnderecoInvalidoException` | class | `br.net.air.cliente.exception` |  | `comercial-api/src/main/java/br/net/air/cliente/exception/EnderecoInvalidoException.java` |
| `AuditoriaHabilitarConfianca` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/AuditoriaHabilitarConfianca.java` |
| `AvisoMigracao` | class | `br.net.air.cliente.model` | @Getter, @Setter, @Entity, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/AvisoMigracao.java` |
| `Blacklist` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table, @Descricao | `comercial-api/src/main/java/br/net/air/cliente/model/Blacklist.java` |
| `BlacklistEvento` | class | `br.net.air.cliente.model` | @Entity, @Setter, @Getter, @Table, @EntityListeners | `comercial-api/src/main/java/br/net/air/cliente/model/BlacklistEvento.java` |
| `ClassificarRisco` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/ClassificarRisco.java` |
| `Cliente` | class | `br.net.air.cliente.model` | @Getter, @Setter, @ToString, @Entity, @Table, @Inheritance | `comercial-api/src/main/java/br/net/air/cliente/model/Cliente.java` |
| `ClienteAnexo` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/ClienteAnexo.java` |
| `ClienteContato` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @ToString, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/ClienteContato.java` |
| `ClienteEvento` | class | `br.net.air.cliente.model` | @Entity, @Setter, @Getter, @Table, @EntityListeners | `comercial-api/src/main/java/br/net/air/cliente/model/ClienteEvento.java` |
| `ClienteFisico` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @ToString, @Table, @PrimaryKeyJoinColumn | `comercial-api/src/main/java/br/net/air/cliente/model/ClienteFisico.java` |
| `ClienteJuridico` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @ToString, @Table, @PrimaryKeyJoinColumn | `comercial-api/src/main/java/br/net/air/cliente/model/ClienteJuridico.java` |
| `ClienteOrientacoes` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/ClienteOrientacoes.java` |
| `Contrato` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/Contrato.java` |
| `Status` | enum | `br.net.air.cliente.model` |  | `comercial-api/src/main/java/br/net/air/cliente/model/Contrato.java` |
| `ContratoAvisoOnu` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/ContratoAvisoOnu.java` |
| `ContratoCampanha` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/ContratoCampanha.java` |
| `ContratoEntrega` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/ContratoEntrega.java` |
| `ContratoFormaPagamento` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/ContratoFormaPagamento.java` |
| `Status` | enum | `br.net.air.cliente.model` |  | `comercial-api/src/main/java/br/net/air/cliente/model/ContratoFormaPagamento.java` |
| `ContratoItem` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/ContratoItem.java` |
| `ContratoMigracao` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/ContratoMigracao.java` |
| `ContratoProduto` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/ContratoProduto.java` |
| `ContratoReajuste` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Builder, @NoArgsConstructor, @AllArgsConstructor, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/ContratoReajuste.java` |
| `ContratoRetencao` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table, @Descricao | `comercial-api/src/main/java/br/net/air/cliente/model/ContratoRetencao.java` |
| `Status` | enum | `br.net.air.cliente.model` |  | `comercial-api/src/main/java/br/net/air/cliente/model/ContratoRetencao.java` |
| `ContratoRetencaoContato` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table, @Descricao | `comercial-api/src/main/java/br/net/air/cliente/model/ContratoRetencaoContato.java` |
| `ContratoSap` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/ContratoSap.java` |
| `ContratoSuspensao` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/ContratoSuspensao.java` |
| `ContratoTarefaSuspensao` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/ContratoTarefaSuspensao.java` |
| `Status` | enum | `br.net.air.cliente.model` |  | `comercial-api/src/main/java/br/net/air/cliente/model/ContratoTarefaSuspensao.java` |
| `ControleIntegracaoSydle` | class | `br.net.air.cliente.model` | @Data, @Embeddable | `comercial-api/src/main/java/br/net/air/cliente/model/ControleIntegracaoSydle.java` |
| `Endereco` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table, @Descricao | `comercial-api/src/main/java/br/net/air/cliente/model/Endereco.java` |
| `EnderecoViabilidade` | class | `br.net.air.cliente.model` | @Getter, @Setter, @Embeddable | `comercial-api/src/main/java/br/net/air/cliente/model/EnderecoViabilidade.java` |
| `EventoFatura` | class | `br.net.air.cliente.model` | @Getter, @Setter, @Entity, @Descricao, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/EventoFatura.java` |
| `EventosSite` | class | `br.net.air.cliente.model` | @Entity, @Table, @Getter, @Setter, @ToString, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/cliente/model/EventosSite.java` |
| `HabilitarConfianca` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/HabilitarConfianca.java` |
| `MarcadorContrato` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/MarcadorContrato.java` |
| `OutrosMarcadores` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/OutrosMarcadores.java` |
| `PerfilacaoCobranca` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/PerfilacaoCobranca.java` |
| `PerfilacaoOuvidoria` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/PerfilacaoOuvidoria.java` |
| `PerfilacaoRetencao` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/PerfilacaoRetencao.java` |
| `RouteThis` | class | `br.net.air.cliente.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/cliente/model/RouteThis.java` |
| `ClienteProjectionDto` | interface | `br.net.air.cliente.projection` |  | `comercial-api/src/main/java/br/net/air/cliente/projection/ClienteProjectionDto.java` |
| `CustomerBasicInfoProjection` | interface | `br.net.air.cliente.projection` |  | `comercial-api/src/main/java/br/net/air/cliente/projection/CustomerBasicInfoProjection.java` |
| `EnderecoContratoProjectionDto` | interface | `br.net.air.cliente.projection` |  | `comercial-api/src/main/java/br/net/air/cliente/projection/EnderecoContratoProjectionDto.java` |
| `EnderecoContratoSimplifiedDTO` | interface | `br.net.air.cliente.projection` |  | `comercial-api/src/main/java/br/net/air/cliente/projection/EnderecoContratoSimplifiedDTO.java` |
| `EnderecoProjectionDto` | interface | `br.net.air.cliente.projection` |  | `comercial-api/src/main/java/br/net/air/cliente/projection/EnderecoProjectionDto.java` |
| `AuditoriaHabilitarConfiancaRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/AuditoriaHabilitarConfiancaRepository.java` |
| `AvisoMigracaoRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/AvisoMigracaoRepository.java` |
| `BlacklistEventoRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/BlacklistEventoRepository.java` |
| `BlacklistRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/BlacklistRepository.java` |
| `ClassificarRiscoRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/ClassificarRiscoRepository.java` |
| `ClienteAnexoRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteAnexoRepository.java` |
| `ClienteContatoRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteContatoRepository.java` |
| `ClienteEventoRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteEventoRepository.java` |
| `ClienteFisicoRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteFisicoRepository.java` |
| `ClienteJuridicoRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteJuridicoRepository.java` |
| `ClienteOrientacoesRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteOrientacoesRepository.java` |
| `ClienteRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteRepository.java` |
| `ContratoAvisoOnuRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoAvisoOnuRepository.java` |
| `ContratoCampanhaRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoCampanhaRepository.java` |
| `ContratoEntregaRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoEntregaRepository.java` |
| `ContratoFormaPagamentoRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoFormaPagamentoRepository.java` |
| `ContratoItemRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoItemRepository.java` |
| `ContratoMigracaoRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoMigracaoRepository.java` |
| `ContratoProdutoRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoProdutoRepository.java` |
| `ContratoReajusteRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoReajusteRepository.java` |
| `ContratoRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRepository.java` |
| `ContratoRetencaoContatoRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRetencaoContatoRepository.java` |
| `ContratoRetencaoRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRetencaoRepository.java` |
| `ContratoSapRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoSapRepository.java` |
| `ContratoSuspensaoRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoSuspensaoRepository.java` |
| `ContratoTarefaSuspensaoRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoTarefaSuspensaoRepository.java` |
| `EventoFaturaRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/EventoFaturaRepository.java` |
| `EventosSiteRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/EventosSiteRepository.java` |
| `HabilitarConfiancaRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/HabilitarConfiancaRepository.java` |
| `JdbcRepository` | class | `br.net.air.cliente.repository` | @Repository, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/cliente/repository/JdbcRepository.java` |
| `MarcadorContratoRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/MarcadorContratoRepository.java` |
| `OutrosMarcadoresRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/OutrosMarcadoresRepository.java` |
| `PerfilacaoCobrancaRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/PerfilacaoCobrancaRepository.java` |
| `PerfilacaoOuvidoriaRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/PerfilacaoOuvidoriaRepository.java` |
| `PerfilacaoRetencaoRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/PerfilacaoRetencaoRepository.java` |
| `RouteThisRepository` | interface | `br.net.air.cliente.repository` |  | `comercial-api/src/main/java/br/net/air/cliente/repository/RouteThisRepository.java` |
| `RotinaRemocaoMarcadoresExpirados` | class | `br.net.air.cliente.rotinas` | @Log, @Service | `comercial-api/src/main/java/br/net/air/cliente/rotinas/RotinaRemocaoMarcadoresExpirados.java` |
| `AuditoriaHabilitarConfiancaService` | class | `br.net.air.cliente.service` | @Log, @Service | `comercial-api/src/main/java/br/net/air/cliente/service/AuditoriaHabilitarConfiancaService.java` |
| `BlacklistService` | class | `br.net.air.cliente.service` | @Service | `comercial-api/src/main/java/br/net/air/cliente/service/BlacklistService.java` |
| `ClassificarRiscoService` | class | `br.net.air.cliente.service` | @Log, @Service | `comercial-api/src/main/java/br/net/air/cliente/service/ClassificarRiscoService.java` |
| `ClienteAnexoService` | class | `br.net.air.cliente.service` | @Service | `comercial-api/src/main/java/br/net/air/cliente/service/ClienteAnexoService.java` |
| `ClienteContatoService` | class | `br.net.air.cliente.service` | @Service | `comercial-api/src/main/java/br/net/air/cliente/service/ClienteContatoService.java` |
| `ClienteEventoService` | class | `br.net.air.cliente.service` | @Service | `comercial-api/src/main/java/br/net/air/cliente/service/ClienteEventoService.java` |
| `ClienteFisicoService` | class | `br.net.air.cliente.service` | @Service | `comercial-api/src/main/java/br/net/air/cliente/service/ClienteFisicoService.java` |
| `ClienteJuridicoService` | class | `br.net.air.cliente.service` | @Service | `comercial-api/src/main/java/br/net/air/cliente/service/ClienteJuridicoService.java` |
| `ClienteService` | class | `br.net.air.cliente.service` | @Slf4j, @Service | `comercial-api/src/main/java/br/net/air/cliente/service/ClienteService.java` |
| `ConnectionService` | class | `br.net.air.cliente.service` | @Service | `comercial-api/src/main/java/br/net/air/cliente/service/ConnectionService.java` |
| `ContratoAvisoOnuService` | class | `br.net.air.cliente.service` | @Slf4j, @Service | `comercial-api/src/main/java/br/net/air/cliente/service/ContratoAvisoOnuService.java` |
| `ContratoCampanhaService` | class | `br.net.air.cliente.service` | @Service | `comercial-api/src/main/java/br/net/air/cliente/service/ContratoCampanhaService.java` |
| `ContratoEntregaService` | class | `br.net.air.cliente.service` | @Service | `comercial-api/src/main/java/br/net/air/cliente/service/ContratoEntregaService.java` |
| `ContratoItemService` | class | `br.net.air.cliente.service` | @Slf4j, @Service | `comercial-api/src/main/java/br/net/air/cliente/service/ContratoItemService.java` |
| `ContratoMigracaoService` | class | `br.net.air.cliente.service` | @Service | `comercial-api/src/main/java/br/net/air/cliente/service/ContratoMigracaoService.java` |
| `ContratoProdutoService` | class | `br.net.air.cliente.service` | @Slf4j, @Service | `comercial-api/src/main/java/br/net/air/cliente/service/ContratoProdutoService.java` |
| `ContratoReajusteService` | class | `br.net.air.cliente.service` | @Service | `comercial-api/src/main/java/br/net/air/cliente/service/ContratoReajusteService.java` |
| `ContratoRetencaoContatoService` | class | `br.net.air.cliente.service` | @Service | `comercial-api/src/main/java/br/net/air/cliente/service/ContratoRetencaoContatoService.java` |
| `ContratoRetencaoService` | class | `br.net.air.cliente.service` | @Service | `comercial-api/src/main/java/br/net/air/cliente/service/ContratoRetencaoService.java` |
| `ContratoSapService` | class | `br.net.air.cliente.service` | @Service | `comercial-api/src/main/java/br/net/air/cliente/service/ContratoSapService.java` |
| `ContratoService` | class | `br.net.air.cliente.service` | @Log, @Service | `comercial-api/src/main/java/br/net/air/cliente/service/ContratoService.java` |
| `ContratoSuspensaoService` | class | `br.net.air.cliente.service` | @Service | `comercial-api/src/main/java/br/net/air/cliente/service/ContratoSuspensaoService.java` |
| `ContratoTarefaSuspensaoService` | class | `br.net.air.cliente.service` | @Service | `comercial-api/src/main/java/br/net/air/cliente/service/ContratoTarefaSuspensaoService.java` |
| `EnderecoService` | class | `br.net.air.cliente.service` | @Log, @Service | `comercial-api/src/main/java/br/net/air/cliente/service/EnderecoService.java` |
| `EventoSiteService` | class | `br.net.air.cliente.service` | @Service, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/cliente/service/EventoSiteService.java` |
| `HabilitarConfiancaService` | class | `br.net.air.cliente.service` | @Log, @Service | `comercial-api/src/main/java/br/net/air/cliente/service/HabilitarConfiancaService.java` |
| `PerfilacaoCobrancaService` | class | `br.net.air.cliente.service` | @Log, @Service | `comercial-api/src/main/java/br/net/air/cliente/service/PerfilacaoCobrancaService.java` |
| `PerfilacaoOuvidoriaService` | class | `br.net.air.cliente.service` | @Log, @Service | `comercial-api/src/main/java/br/net/air/cliente/service/PerfilacaoOuvidoriaService.java` |
| `PerfilacaoRetencaoService` | class | `br.net.air.cliente.service` | @Log, @Service | `comercial-api/src/main/java/br/net/air/cliente/service/PerfilacaoRetencaoService.java` |
| `RouteThisService` | class | `br.net.air.cliente.service` | @Log, @Service | `comercial-api/src/main/java/br/net/air/cliente/service/RouteThisService.java` |
| `ViabilidadeTeoricaService` | class | `br.net.air.cliente.service` | @Service | `comercial-api/src/main/java/br/net/air/cliente/service/ViabilidadeTeoricaService.java` |
| `ItemSapController` | class | `br.net.air.composicao.controller` | @CrossOrigin, @RequiredArgsConstructor, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/composicao/controller/ItemSapController.java` |
| `PacoteSapController` | class | `br.net.air.composicao.controller` | @CrossOrigin, @RequiredArgsConstructor, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/composicao/controller/PacoteSapController.java` |
| `ProdutoSapController` | class | `br.net.air.composicao.controller` | @CrossOrigin, @RequiredArgsConstructor, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/composicao/controller/ProdutoSapController.java` |
| `ItemDTO` | class | `br.net.air.composicao.dto` | @Data | `comercial-api/src/main/java/br/net/air/composicao/dto/ItemDTO.java` |
| `ItemUpdateDTO` | class | `br.net.air.composicao.dto` | @Data | `comercial-api/src/main/java/br/net/air/composicao/dto/ItemUpdateDTO.java` |
| `PacoteConsultaDTO` | class | `br.net.air.composicao.dto` | @Data | `comercial-api/src/main/java/br/net/air/composicao/dto/PacoteConsultaDTO.java` |
| `PacoteCreateDTO` | class | `br.net.air.composicao.dto` | @Data | `comercial-api/src/main/java/br/net/air/composicao/dto/PacoteCreateDTO.java` |
| `PacoteDTO` | class | `br.net.air.composicao.dto` | @Data | `comercial-api/src/main/java/br/net/air/composicao/dto/PacoteDTO.java` |
| `PacoteUpdateDTO` | class | `br.net.air.composicao.dto` | @Data | `comercial-api/src/main/java/br/net/air/composicao/dto/PacoteUpdateDTO.java` |
| `ProdutoCreateDTO` | class | `br.net.air.composicao.dto` | @Data | `comercial-api/src/main/java/br/net/air/composicao/dto/ProdutoCreateDTO.java` |
| `ProdutoDTO` | class | `br.net.air.composicao.dto` | @Data | `comercial-api/src/main/java/br/net/air/composicao/dto/ProdutoDTO.java` |
| `ProdutoUpdateDTO` | class | `br.net.air.composicao.dto` | @Data | `comercial-api/src/main/java/br/net/air/composicao/dto/ProdutoUpdateDTO.java` |
| `ServicoConsultaDTO` | class | `br.net.air.composicao.dto` | @Accessors, @Data | `comercial-api/src/main/java/br/net/air/composicao/dto/ServicoConsultaDTO.java` |
| `GrupoItens` | enum | `br.net.air.composicao.enums` | @Getter, @AllArgsConstructor | `comercial-api/src/main/java/br/net/air/composicao/enums/GrupoItens.java` |
| `ItemSap` | class | `br.net.air.composicao.model` | @Accessors, @Getter, @Setter, @ToString, @RequiredArgsConstructor, @Entity, @Table | `comercial-api/src/main/java/br/net/air/composicao/model/ItemSap.java` |
| `PacoteProdutoSap` | class | `br.net.air.composicao.model` | @Accessors, @Data, @Entity, @Table | `comercial-api/src/main/java/br/net/air/composicao/model/PacoteProdutoSap.java` |
| `PacoteSap` | class | `br.net.air.composicao.model` | @Accessors, @Data, @Entity, @Table | `comercial-api/src/main/java/br/net/air/composicao/model/PacoteSap.java` |
| `ProdutoItemSap` | class | `br.net.air.composicao.model` | @Entity, @Data, @Accessors, @Table, @AllArgsConstructor, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/composicao/model/ProdutoItemSap.java` |
| `ProdutoSap` | class | `br.net.air.composicao.model` | @Accessors, @Data, @Entity, @Table | `comercial-api/src/main/java/br/net/air/composicao/model/ProdutoSap.java` |
| `ItemSapRepository` | interface | `br.net.air.composicao.repository` |  | `comercial-api/src/main/java/br/net/air/composicao/repository/ItemSapRepository.java` |
| `PacoteProdutoSapRepository` | interface | `br.net.air.composicao.repository` |  | `comercial-api/src/main/java/br/net/air/composicao/repository/PacoteProdutoSapRepository.java` |
| `PacoteSapRepository` | interface | `br.net.air.composicao.repository` |  | `comercial-api/src/main/java/br/net/air/composicao/repository/PacoteSapRepository.java` |
| `ProdutoItemSapRepository` | interface | `br.net.air.composicao.repository` |  | `comercial-api/src/main/java/br/net/air/composicao/repository/ProdutoItemSapRepository.java` |
| `ProdutoSapRepository` | interface | `br.net.air.composicao.repository` |  | `comercial-api/src/main/java/br/net/air/composicao/repository/ProdutoSapRepository.java` |
| `ItemSapService` | class | `br.net.air.composicao.service` | @RequiredArgsConstructor, @Service | `comercial-api/src/main/java/br/net/air/composicao/service/ItemSapService.java` |
| `PacoteSapService` | class | `br.net.air.composicao.service` | @RequiredArgsConstructor, @Service | `comercial-api/src/main/java/br/net/air/composicao/service/PacoteSapService.java` |
| `ProdutoSapService` | class | `br.net.air.composicao.service` | @RequiredArgsConstructor, @Service | `comercial-api/src/main/java/br/net/air/composicao/service/ProdutoSapService.java` |
| `CampanhaController` | class | `br.net.air.configuracoes.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/configuracoes/controller/CampanhaController.java` |
| `CampanhaPacoteAdicionalController` | class | `br.net.air.configuracoes.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/configuracoes/controller/CampanhaPacoteAdicionalController.java` |
| `CampanhaPacoteController` | class | `br.net.air.configuracoes.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/configuracoes/controller/CampanhaPacoteController.java` |
| `CarteiraController` | class | `br.net.air.configuracoes.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/configuracoes/controller/CarteiraController.java` |
| `CondominioController` | class | `br.net.air.configuracoes.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/configuracoes/controller/CondominioController.java` |
| `EnderecoBairroController` | class | `br.net.air.configuracoes.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/configuracoes/controller/EnderecoBairroController.java` |
| `EnderecoCidadeController` | class | `br.net.air.configuracoes.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/configuracoes/controller/EnderecoCidadeController.java` |
| `EnderecoController` | class | `br.net.air.configuracoes.controller` | @Slf4j, @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/configuracoes/controller/EnderecoController.java` |
| `EnderecoEstadoController` | class | `br.net.air.configuracoes.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/configuracoes/controller/EnderecoEstadoController.java` |
| `EnderecoLogradouroController` | class | `br.net.air.configuracoes.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/configuracoes/controller/EnderecoLogradouroController.java` |
| `ProdutoController` | class | `br.net.air.configuracoes.controller` | @RestController | `comercial-api/src/main/java/br/net/air/configuracoes/controller/ProdutoController.java` |
| `RegraSuspensaoController` | class | `br.net.air.configuracoes.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/configuracoes/controller/RegraSuspensaoController.java` |
| `TermoController` | class | `br.net.air.configuracoes.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/configuracoes/controller/TermoController.java` |
| `VendedorControllerV2` | class | `br.net.air.configuracoes.controller.V2` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/configuracoes/controller/V2/VendedorControllerV2.java` |
| `VencimentoController` | class | `br.net.air.configuracoes.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/configuracoes/controller/VencimentoController.java` |
| `VendedorController` | class | `br.net.air.configuracoes.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/configuracoes/controller/VendedorController.java` |
| `AtualizacaoCoordenadasDTO` | class | `br.net.air.configuracoes.dto` | @Data | `comercial-api/src/main/java/br/net/air/configuracoes/dto/AtualizacaoCoordenadasDTO.java` |
| `CampanhaDTO` | class | `br.net.air.configuracoes.dto` | @Data | `comercial-api/src/main/java/br/net/air/configuracoes/dto/CampanhaDTO.java` |
| `CampanhaPacoteAdicionalDTO` | class | `br.net.air.configuracoes.dto` | @Data | `comercial-api/src/main/java/br/net/air/configuracoes/dto/CampanhaPacoteAdicionalDTO.java` |
| `CampanhaPacoteDTO` | class | `br.net.air.configuracoes.dto` | @Data | `comercial-api/src/main/java/br/net/air/configuracoes/dto/CampanhaPacoteDTO.java` |
| `CondominioDTO` | class | `br.net.air.configuracoes.dto` | @Data | `comercial-api/src/main/java/br/net/air/configuracoes/dto/CondominioDTO.java` |
| `EnderecoBairroDTO` | class | `br.net.air.configuracoes.dto` | @Data | `comercial-api/src/main/java/br/net/air/configuracoes/dto/EnderecoBairroDTO.java` |
| `EnderecoCidadeDTO` | class | `br.net.air.configuracoes.dto` | @Data | `comercial-api/src/main/java/br/net/air/configuracoes/dto/EnderecoCidadeDTO.java` |
| `EnderecoContratoDTO` | class | `br.net.air.configuracoes.dto` | @Data | `comercial-api/src/main/java/br/net/air/configuracoes/dto/EnderecoContratoDTO.java` |
| `EnderecoLogradouroDTO` | class | `br.net.air.configuracoes.dto` | @Data | `comercial-api/src/main/java/br/net/air/configuracoes/dto/EnderecoLogradouroDTO.java` |
| `RegraSuspensaoDTO` | class | `br.net.air.configuracoes.dto` | @Data | `comercial-api/src/main/java/br/net/air/configuracoes/dto/RegraSuspensaoDTO.java` |
| `TermoDTO` | class | `br.net.air.configuracoes.dto` | @Data | `comercial-api/src/main/java/br/net/air/configuracoes/dto/TermoDTO.java` |
| `VencimentoDTO` | class | `br.net.air.configuracoes.dto` | @Data | `comercial-api/src/main/java/br/net/air/configuracoes/dto/VencimentoDTO.java` |
| `VendedorDTO` | class | `br.net.air.configuracoes.dto` | @Data, @Builder, @AllArgsConstructor, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/configuracoes/dto/VendedorDTO.java` |
| `CondominioEvent` | class | `br.net.air.configuracoes.event` | @Data, @Builder, @NoArgsConstructor, @AllArgsConstructor | `comercial-api/src/main/java/br/net/air/configuracoes/event/CondominioEvent.java` |
| `Tipo` | enum | `br.net.air.configuracoes.event` |  | `comercial-api/src/main/java/br/net/air/configuracoes/event/CondominioEvent.java` |
| `CondominioEventListener` | class | `br.net.air.configuracoes.event` | @Component | `comercial-api/src/main/java/br/net/air/configuracoes/event/CondominioEventListener.java` |
| `LogradouroController` | class | `br.net.air.configuracoes.googleplace.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/configuracoes/googleplace/controller/LogradouroController.java` |
| `EnderecoGoogleDTO` | class | `br.net.air.configuracoes.googleplace.dto` | @Data | `comercial-api/src/main/java/br/net/air/configuracoes/googleplace/dto/EnderecoGoogleDTO.java` |
| `AddressComponents` | class | `br.net.air.configuracoes.googleplace.model` | @Data | `comercial-api/src/main/java/br/net/air/configuracoes/googleplace/model/AddressComponents.java` |
| `Logradouro` | class | `br.net.air.configuracoes.googleplace.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/configuracoes/googleplace/model/Logradouro.java` |
| `Predictions` | class | `br.net.air.configuracoes.googleplace.model` | @Data | `comercial-api/src/main/java/br/net/air/configuracoes/googleplace/model/Predictions.java` |
| `Result` | class | `br.net.air.configuracoes.googleplace.model` | @Data | `comercial-api/src/main/java/br/net/air/configuracoes/googleplace/model/Result.java` |
| `ResultadoGoogle` | class | `br.net.air.configuracoes.googleplace.model` | @Data | `comercial-api/src/main/java/br/net/air/configuracoes/googleplace/model/ResultadoGoogle.java` |
| `StructuredFormatting` | class | `br.net.air.configuracoes.googleplace.model` | @Data | `comercial-api/src/main/java/br/net/air/configuracoes/googleplace/model/StructuredFormatting.java` |
| `Campanha` | class | `br.net.air.configuracoes.model` | @Entity, @Getter, @Setter, @Table, @Descricao | `comercial-api/src/main/java/br/net/air/configuracoes/model/Campanha.java` |
| `CampanhaPacote` | class | `br.net.air.configuracoes.model` | @Entity, @Getter, @Setter, @Table, @Descricao | `comercial-api/src/main/java/br/net/air/configuracoes/model/CampanhaPacote.java` |
| `CampanhaPacoteAdicional` | class | `br.net.air.configuracoes.model` | @Entity, @Getter, @Setter, @Table, @Descricao | `comercial-api/src/main/java/br/net/air/configuracoes/model/CampanhaPacoteAdicional.java` |
| `Carteira` | class | `br.net.air.configuracoes.model` | @Entity, @Getter, @Setter, @Table, @Descricao | `comercial-api/src/main/java/br/net/air/configuracoes/model/Carteira.java` |
| `Condominio` | class | `br.net.air.configuracoes.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/configuracoes/model/Condominio.java` |
| `CondominioEvento` | class | `br.net.air.configuracoes.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/configuracoes/model/CondominioEvento.java` |
| `EnderecoBairro` | class | `br.net.air.configuracoes.model` | @Entity, @Getter, @Setter, @Table, @Descricao | `comercial-api/src/main/java/br/net/air/configuracoes/model/EnderecoBairro.java` |
| `EnderecoCidade` | class | `br.net.air.configuracoes.model` | @Entity, @Getter, @Setter, @Table, @Descricao | `comercial-api/src/main/java/br/net/air/configuracoes/model/EnderecoCidade.java` |
| `EnderecoLogradouro` | class | `br.net.air.configuracoes.model` | @Entity, @Getter, @Setter, @Table, @Descricao | `comercial-api/src/main/java/br/net/air/configuracoes/model/EnderecoLogradouro.java` |
| `Estado` | class | `br.net.air.configuracoes.model` | @Entity, @Getter, @Setter, @Table, @Descricao | `comercial-api/src/main/java/br/net/air/configuracoes/model/Estado.java` |
| `RegraSuspensao` | class | `br.net.air.configuracoes.model` | @Entity, @Getter, @Setter, @Table, @Descricao | `comercial-api/src/main/java/br/net/air/configuracoes/model/RegraSuspensao.java` |
| `Termo` | class | `br.net.air.configuracoes.model` | @Entity, @Getter, @Setter, @Table, @Descricao | `comercial-api/src/main/java/br/net/air/configuracoes/model/Termo.java` |
| `Vencimento` | class | `br.net.air.configuracoes.model` | @Entity, @Getter, @Setter, @Table, @Descricao | `comercial-api/src/main/java/br/net/air/configuracoes/model/Vencimento.java` |
| `Vendedor` | class | `br.net.air.configuracoes.model` | @Entity, @Getter, @Setter, @Table, @Descricao | `comercial-api/src/main/java/br/net/air/configuracoes/model/Vendedor.java` |
| `CarteiraProjectionDto` | interface | `br.net.air.configuracoes.projection` |  | `comercial-api/src/main/java/br/net/air/configuracoes/projection/CarteiraProjectionDto.java` |
| `CampanhaPacoteAdicionalRepository` | interface | `br.net.air.configuracoes.repository` |  | `comercial-api/src/main/java/br/net/air/configuracoes/repository/CampanhaPacoteAdicionalRepository.java` |
| `CampanhaPacoteRepository` | interface | `br.net.air.configuracoes.repository` |  | `comercial-api/src/main/java/br/net/air/configuracoes/repository/CampanhaPacoteRepository.java` |
| `CampanhaRepository` | interface | `br.net.air.configuracoes.repository` |  | `comercial-api/src/main/java/br/net/air/configuracoes/repository/CampanhaRepository.java` |
| `CarteiraRepository` | interface | `br.net.air.configuracoes.repository` |  | `comercial-api/src/main/java/br/net/air/configuracoes/repository/CarteiraRepository.java` |
| `CondominioEventRepository` | interface | `br.net.air.configuracoes.repository` |  | `comercial-api/src/main/java/br/net/air/configuracoes/repository/CondominioEventRepository.java` |
| `CondominioRepository` | interface | `br.net.air.configuracoes.repository` |  | `comercial-api/src/main/java/br/net/air/configuracoes/repository/CondominioRepository.java` |
| `EnderecoBairroRepository` | interface | `br.net.air.configuracoes.repository` |  | `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoBairroRepository.java` |
| `EnderecoCidadeRepository` | interface | `br.net.air.configuracoes.repository` |  | `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoCidadeRepository.java` |
| `EnderecoEstadoRepository` | interface | `br.net.air.configuracoes.repository` |  | `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoEstadoRepository.java` |
| `EnderecoLogradouroRepository` | interface | `br.net.air.configuracoes.repository` |  | `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoLogradouroRepository.java` |
| `EnderecoRepository` | interface | `br.net.air.configuracoes.repository` |  | `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoRepository.java` |
| `RegraSuspensaoRepository` | interface | `br.net.air.configuracoes.repository` |  | `comercial-api/src/main/java/br/net/air/configuracoes/repository/RegraSuspensaoRepository.java` |
| `TermoRepository` | interface | `br.net.air.configuracoes.repository` |  | `comercial-api/src/main/java/br/net/air/configuracoes/repository/TermoRepository.java` |
| `VencimentoRepository` | interface | `br.net.air.configuracoes.repository` |  | `comercial-api/src/main/java/br/net/air/configuracoes/repository/VencimentoRepository.java` |
| `VendedorRepository` | interface | `br.net.air.configuracoes.repository` |  | `comercial-api/src/main/java/br/net/air/configuracoes/repository/VendedorRepository.java` |
| `CampanhaPacoteAdicionalService` | class | `br.net.air.configuracoes.service` | @Service | `comercial-api/src/main/java/br/net/air/configuracoes/service/CampanhaPacoteAdicionalService.java` |
| `CampanhaPacoteService` | class | `br.net.air.configuracoes.service` | @Service | `comercial-api/src/main/java/br/net/air/configuracoes/service/CampanhaPacoteService.java` |
| `CampanhaService` | class | `br.net.air.configuracoes.service` | @Service | `comercial-api/src/main/java/br/net/air/configuracoes/service/CampanhaService.java` |
| `CarteiraService` | class | `br.net.air.configuracoes.service` | @Service | `comercial-api/src/main/java/br/net/air/configuracoes/service/CarteiraService.java` |
| `CondominioEventService` | class | `br.net.air.configuracoes.service` | @Service | `comercial-api/src/main/java/br/net/air/configuracoes/service/CondominioEventService.java` |
| `CondominioService` | class | `br.net.air.configuracoes.service` | @Service | `comercial-api/src/main/java/br/net/air/configuracoes/service/CondominioService.java` |
| `EnderecoBairroService` | class | `br.net.air.configuracoes.service` | @Service | `comercial-api/src/main/java/br/net/air/configuracoes/service/EnderecoBairroService.java` |
| `EnderecoCidadeService` | class | `br.net.air.configuracoes.service` | @Service | `comercial-api/src/main/java/br/net/air/configuracoes/service/EnderecoCidadeService.java` |
| `EnderecoEstadoService` | class | `br.net.air.configuracoes.service` | @Service | `comercial-api/src/main/java/br/net/air/configuracoes/service/EnderecoEstadoService.java` |
| `EnderecoLogradouroService` | class | `br.net.air.configuracoes.service` | @Service | `comercial-api/src/main/java/br/net/air/configuracoes/service/EnderecoLogradouroService.java` |
| `OperacaoService` | class | `br.net.air.configuracoes.service` | @Service, @Log | `comercial-api/src/main/java/br/net/air/configuracoes/service/OperacaoService.java` |
| `ProdutoService` | class | `br.net.air.configuracoes.service` | @Service | `comercial-api/src/main/java/br/net/air/configuracoes/service/ProdutoService.java` |
| `RegraSuspensaoService` | class | `br.net.air.configuracoes.service` | @Service | `comercial-api/src/main/java/br/net/air/configuracoes/service/RegraSuspensaoService.java` |
| `TermoService` | class | `br.net.air.configuracoes.service` | @Service | `comercial-api/src/main/java/br/net/air/configuracoes/service/TermoService.java` |
| `VencimentoService` | class | `br.net.air.configuracoes.service` | @Service | `comercial-api/src/main/java/br/net/air/configuracoes/service/VencimentoService.java` |
| `VendedorService` | class | `br.net.air.configuracoes.service` | @Slf4j, @Service | `comercial-api/src/main/java/br/net/air/configuracoes/service/VendedorService.java` |
| `ConnectMasterController` | class | `br.net.air.connectmaster.controller` | @Log, @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/connectmaster/controller/ConnectMasterController.java` |
| `ReservaDTO` | class | `br.net.air.connectmaster.dto` | @Data | `comercial-api/src/main/java/br/net/air/connectmaster/dto/ReservaDTO.java` |
| `ViabilidadeConsultaDTO` | class | `br.net.air.connectmaster.dto` | @Data | `comercial-api/src/main/java/br/net/air/connectmaster/dto/ViabilidadeConsultaDTO.java` |
| `ViabilidadeRetornoDTO` | class | `br.net.air.connectmaster.dto` | @Data | `comercial-api/src/main/java/br/net/air/connectmaster/dto/ViabilidadeRetornoDTO.java` |
| `DadosReserva` | class | `br.net.air.connectmaster.retornos` | @Getter, @Setter | `comercial-api/src/main/java/br/net/air/connectmaster/retornos/DadosReserva.java` |
| `RotinaCancelamento` | class | `br.net.air.connectmaster.rotina` | @Log, @Service | `comercial-api/src/main/java/br/net/air/connectmaster/rotina/RotinaCancelamento.java` |
| `ConnectMasterIntegracaoService` | class | `br.net.air.connectmaster.service` | @Log, @Service | `comercial-api/src/main/java/br/net/air/connectmaster/service/ConnectMasterIntegracaoService.java` |
| `ConnectMasterRotinaService` | class | `br.net.air.connectmaster.service` | @Log, @Service | `comercial-api/src/main/java/br/net/air/connectmaster/service/ConnectMasterRotinaService.java` |
| `EcareClient` | interface | `br.net.air.ecare.client` |  | `comercial-api/src/main/java/br/net/air/ecare/client/EcareClient.java` |
| `EcareClientImpl` | class | `br.net.air.ecare.client` | @Slf4j, @Service, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/ecare/client/EcareClientImpl.java` |
| `KeycloakAuthClient` | interface | `br.net.air.ecare.client` |  | `comercial-api/src/main/java/br/net/air/ecare/client/KeycloakAuthClient.java` |
| `KeycloakAuthClientImpl` | class | `br.net.air.ecare.client` | @Slf4j, @Service, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/ecare/client/KeycloakAuthClientImpl.java` |
| `HistoricoAlarmesONUDto` | class | `br.net.air.ecare.dto` | @Data, @JsonIgnoreProperties | `comercial-api/src/main/java/br/net/air/ecare/dto/HistoricoAlarmesONUDto.java` |
| `Event` | class | `br.net.air.ecare.dto` | @Data | `comercial-api/src/main/java/br/net/air/ecare/dto/HistoricoAlarmesONUDto.java` |
| `Incident` | class | `br.net.air.ecare.dto` | @Data | `comercial-api/src/main/java/br/net/air/ecare/dto/HistoricoAlarmesONUDto.java` |
| `Task` | class | `br.net.air.ecare.dto` | @Data | `comercial-api/src/main/java/br/net/air/ecare/dto/HistoricoAlarmesONUDto.java` |
| `KeycloakAuthDTO` | class | `br.net.air.ecare.dto` | @Data | `comercial-api/src/main/java/br/net/air/ecare/dto/KeycloakAuthDTO.java` |
| `LoginPPPoEDTO` | class | `br.net.air.ecare.dto` | @Data | `comercial-api/src/main/java/br/net/air/ecare/dto/LoginPPPoEDTO.java` |
| `EventoOnuMapper` | class | `br.net.air.ecare.mapper` |  | `comercial-api/src/main/java/br/net/air/ecare/mapper/EventoOnuMapper.java` |
| `ArgumentsValidationException` | class | `br.net.air.exception` |  | `comercial-api/src/main/java/br/net/air/exception/ArgumentsValidationException.java` |
| `CustomException` | class | `br.net.air.exception` |  | `comercial-api/src/main/java/br/net/air/exception/CustomException.java` |
| `CustomerContactUpdateException` | class | `br.net.air.exception` |  | `comercial-api/src/main/java/br/net/air/exception/CustomerContactUpdateException.java` |
| `GlobalExceptionHandler` | class | `br.net.air.exception` | @Slf4j | `comercial-api/src/main/java/br/net/air/exception/GlobalExceptionHandler.java` |
| `MultiReadHttpServletRequest` | class | `br.net.air.exception` |  | `comercial-api/src/main/java/br/net/air/exception/MultiReadHttpServletRequest.java` |
| `RequestBodyHolder` | class | `br.net.air.exception` |  | `comercial-api/src/main/java/br/net/air/exception/RequestBodyHolder.java` |
| `RequestLoggingFilter` | class | `br.net.air.exception` | @Component | `comercial-api/src/main/java/br/net/air/exception/RequestLoggingFilter.java` |
| `RequestTimeInterceptor` | class | `br.net.air.exception` | @Component | `comercial-api/src/main/java/br/net/air/exception/RequestTimeInterceptor.java` |
| `NativeDBFactory` | class | `br.net.air.factory` | @Component | `comercial-api/src/main/java/br/net/air/factory/NativeDBFactory.java` |
| `CobrancaPontualController` | class | `br.net.air.financeiro.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/financeiro/controller/CobrancaPontualController.java` |
| `ContratoFaturamentoController` | class | `br.net.air.financeiro.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/financeiro/controller/ContratoFaturamentoController.java` |
| `DashboardController` | class | `br.net.air.financeiro.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/financeiro/controller/DashboardController.java` |
| `DescontoController` | class | `br.net.air.financeiro.controller` | @Slf4j, @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/financeiro/controller/DescontoController.java` |
| `CobrancaPontualDTO` | class | `br.net.air.financeiro.dto` | @Data | `comercial-api/src/main/java/br/net/air/financeiro/dto/CobrancaPontualDTO.java` |
| `DescontoDTO` | class | `br.net.air.financeiro.dto` | @Data | `comercial-api/src/main/java/br/net/air/financeiro/dto/DescontoDTO.java` |
| `DocumentoFiscalDTO` | class | `br.net.air.financeiro.dto` | @Data | `comercial-api/src/main/java/br/net/air/financeiro/dto/DocumentoFiscalDTO.java` |
| `TituloDTO` | class | `br.net.air.financeiro.dto` | @Data | `comercial-api/src/main/java/br/net/air/financeiro/dto/TituloDTO.java` |
| `CobrancaPontual` | class | `br.net.air.financeiro.model` | @Entity, @Getter, @Setter, @Table, @Descricao | `comercial-api/src/main/java/br/net/air/financeiro/model/CobrancaPontual.java` |
| `ContratoFaturamento` | class | `br.net.air.financeiro.model` | @Entity, @Getter, @Setter, @Table, @Descricao | `comercial-api/src/main/java/br/net/air/financeiro/model/ContratoFaturamento.java` |
| `Desconto` | class | `br.net.air.financeiro.model` | @Entity, @Getter, @Setter, @Table, @Descricao | `comercial-api/src/main/java/br/net/air/financeiro/model/Desconto.java` |
| `EventoFinanceiro` | class | `br.net.air.financeiro.model` | @Entity, @Getter, @Setter, @Table, @Descricao | `comercial-api/src/main/java/br/net/air/financeiro/model/EventoFinanceiro.java` |
| `CobrancaPontualRepository` | interface | `br.net.air.financeiro.repository` |  | `comercial-api/src/main/java/br/net/air/financeiro/repository/CobrancaPontualRepository.java` |
| `ContratoFaturamentoRepository` | interface | `br.net.air.financeiro.repository` |  | `comercial-api/src/main/java/br/net/air/financeiro/repository/ContratoFaturamentoRepository.java` |
| `DescontoRepository` | interface | `br.net.air.financeiro.repository` |  | `comercial-api/src/main/java/br/net/air/financeiro/repository/DescontoRepository.java` |
| `EventoFinanceiroRepository` | interface | `br.net.air.financeiro.repository` |  | `comercial-api/src/main/java/br/net/air/financeiro/repository/EventoFinanceiroRepository.java` |
| `CobrancaPontualService` | class | `br.net.air.financeiro.service` | @Service, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/financeiro/service/CobrancaPontualService.java` |
| `ContratoFaturamentoService` | class | `br.net.air.financeiro.service` | @Service | `comercial-api/src/main/java/br/net/air/financeiro/service/ContratoFaturamentoService.java` |
| `DescontoService` | class | `br.net.air.financeiro.service` | @Service | `comercial-api/src/main/java/br/net/air/financeiro/service/DescontoService.java` |
| `TituloService` | class | `br.net.air.financeiro.service` | @Service, @Log | `comercial-api/src/main/java/br/net/air/financeiro/service/TituloService.java` |
| `IntegracaoController` | class | `br.net.air.integracao.controller` | @RestController, @RequestMapping, @RequiredArgsConstructor, @Slf4j | `comercial-api/src/main/java/br/net/air/integracao/controller/IntegracaoController.java` |
| `IntegracaoControllerExceptionHandler` | class | `br.net.air.integracao.controller` | @RestControllerAdvice, @RequestMapping | `comercial-api/src/main/java/br/net/air/integracao/controller/IntegracaoControllerExceptionHandler.java` |
| `ClienteIntegracaoDTO` | class | `br.net.air.integracao.dto` | @Data | `comercial-api/src/main/java/br/net/air/integracao/dto/ClienteIntegracaoDTO.java` |
| `ContatoIntegracaoDTO` | class | `br.net.air.integracao.dto` | @Data | `comercial-api/src/main/java/br/net/air/integracao/dto/ContatoIntegracaoDTO.java` |
| `Tipo` | enum | `br.net.air.integracao.dto` |  | `comercial-api/src/main/java/br/net/air/integracao/dto/ContatoIntegracaoDTO.java` |
| `ContratoIntegracaoDTO` | class | `br.net.air.integracao.dto` | @Data | `comercial-api/src/main/java/br/net/air/integracao/dto/ContratoIntegracaoDTO.java` |
| `DescontoIntegracaoDTO` | class | `br.net.air.integracao.dto` | @Data | `comercial-api/src/main/java/br/net/air/integracao/dto/DescontoIntegracaoDTO.java` |
| `EnderecoIntegracaoDTO` | class | `br.net.air.integracao.dto` | @Data | `comercial-api/src/main/java/br/net/air/integracao/dto/EnderecoIntegracaoDTO.java` |
| `WhatsappIntegracaoDTO` | class | `br.net.air.integracao.dto` | @Data | `comercial-api/src/main/java/br/net/air/integracao/dto/WhatsappIntegracaoDTO.java` |
| `IntegracaoService` | class | `br.net.air.integracao.service` | @Slf4j, @Service, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/integracao/service/IntegracaoService.java` |
| `MigracaoController` | class | `br.net.air.migracao.controller` | @RestController, @RequestMapping, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/migracao/controller/MigracaoController.java` |
| `ClienteMigracaoDTO` | class | `br.net.air.migracao.dto` | @Data | `comercial-api/src/main/java/br/net/air/migracao/dto/ClienteMigracaoDTO.java` |
| `ContratoAssociacaoDTO` | class | `br.net.air.migracao.dto` | @Data | `comercial-api/src/main/java/br/net/air/migracao/dto/ContratoAssociacaoDTO.java` |
| `ContratoMigracaoDTO` | class | `br.net.air.migracao.dto` | @Data | `comercial-api/src/main/java/br/net/air/migracao/dto/ContratoMigracaoDTO.java` |
| `EnderecoMigracaoDTO` | class | `br.net.air.migracao.dto` | @Data | `comercial-api/src/main/java/br/net/air/migracao/dto/EnderecoMigracaoDTO.java` |
| `InternetMigracaoDTO` | class | `br.net.air.migracao.dto` | @Data | `comercial-api/src/main/java/br/net/air/migracao/dto/InternetMigracaoDTO.java` |
| `MigracaoResponseDTO` | class | `br.net.air.migracao.dto` | @Data | `comercial-api/src/main/java/br/net/air/migracao/dto/MigracaoResponseDTO.java` |
| `MigracaoService` | class | `br.net.air.migracao.service` | @Slf4j, @Service, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/migracao/service/MigracaoService.java` |
| `MigracaoValidadorService` | class | `br.net.air.migracao.service` | @Service | `comercial-api/src/main/java/br/net/air/migracao/service/MigracaoValidadorService.java` |
| `NotificationController` | class | `br.net.air.notification.controller` | @Log, @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/notification/controller/NotificationController.java` |
| `ContatoBaseDTO` | class | `br.net.air.notification.dto` | @Data, @NoArgsConstructor, @AllArgsConstructor | `comercial-api/src/main/java/br/net/air/notification/dto/ContatoBaseDTO.java` |
| `ContatoCompletoDTO` | class | `br.net.air.notification.dto` | @Getter, @NoArgsConstructor, @AllArgsConstructor | `comercial-api/src/main/java/br/net/air/notification/dto/ContatoCompletoDTO.java` |
| `ContatoFavoritoDTO` | class | `br.net.air.notification.dto` | @Getter, @NoArgsConstructor, @AllArgsConstructor | `comercial-api/src/main/java/br/net/air/notification/dto/ContatoFavoritoDTO.java` |
| `LoginDTO` | class | `br.net.air.notification.dto` | @Data | `comercial-api/src/main/java/br/net/air/notification/dto/LoginDTO.java` |
| `NovoContatoDTO` | class | `br.net.air.notification.dto` | @Data | `comercial-api/src/main/java/br/net/air/notification/dto/NovoContatoDTO.java` |
| `SegundaViaDTO` | class | `br.net.air.notification.dto` | @Data | `comercial-api/src/main/java/br/net/air/notification/dto/SegundaViaDTO.java` |
| `SegundaViaFaturaUnicaDTO` | class | `br.net.air.notification.dto` | @Data | `comercial-api/src/main/java/br/net/air/notification/dto/SegundaViaFaturaUnicaDTO.java` |
| `DTOValidator` | class | `br.net.air.notification.service` |  | `comercial-api/src/main/java/br/net/air/notification/service/DTOValidator.java` |
| `NotificationIntegracaoService` | class | `br.net.air.notification.service` | @Log, @Service | `comercial-api/src/main/java/br/net/air/notification/service/NotificationIntegracaoService.java` |
| `OauthController` | class | `br.net.air.oauth.Controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/oauth/Controller/OauthController.java` |
| `IntegracaoRequest` | class | `br.net.air.oauth.dto` | @Data | `comercial-api/src/main/java/br/net/air/oauth/dto/IntegracaoRequest.java` |
| `IntegracaoResponse` | class | `br.net.air.oauth.dto` | @Data, @Builder | `comercial-api/src/main/java/br/net/air/oauth/dto/IntegracaoResponse.java` |
| `RotinaIntegracao` | class | `br.net.air.oauth.rotina` | @Log, @Service, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/oauth/rotina/RotinaIntegracao.java` |
| `OauthIntegracaoService` | class | `br.net.air.oauth.service` | @Log, @Service | `comercial-api/src/main/java/br/net/air/oauth/service/OauthIntegracaoService.java` |
| `MotivoController` | class | `br.net.air.perfilador.controller` | @CrossOrigin, @RestController, @RequestMapping, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/perfilador/controller/MotivoController.java` |
| `SubmotivoController` | class | `br.net.air.perfilador.controller` | @CrossOrigin, @RestController, @RequestMapping, @RequiredArgsConstructor | `comercial-api/src/main/java/br/net/air/perfilador/controller/SubmotivoController.java` |
| `MotivoDTO` | class | `br.net.air.perfilador.dto` | @Data | `comercial-api/src/main/java/br/net/air/perfilador/dto/MotivoDTO.java` |
| `SubmotivoDTO` | class | `br.net.air.perfilador.dto` | @Data | `comercial-api/src/main/java/br/net/air/perfilador/dto/SubmotivoDTO.java` |
| `Motivo` | class | `br.net.air.perfilador.model` | @Entity, @Getter, @Setter, @Table, @Descricao | `comercial-api/src/main/java/br/net/air/perfilador/model/Motivo.java` |
| `Submotivo` | class | `br.net.air.perfilador.model` | @Entity, @Getter, @Setter, @Table, @Descricao | `comercial-api/src/main/java/br/net/air/perfilador/model/Submotivo.java` |
| `MotivoRepository` | interface | `br.net.air.perfilador.repository` | @Repository | `comercial-api/src/main/java/br/net/air/perfilador/repository/MotivoRepository.java` |
| `SubmotivoRepository` | interface | `br.net.air.perfilador.repository` | @Repository | `comercial-api/src/main/java/br/net/air/perfilador/repository/SubmotivoRepository.java` |
| `MotivoService` | class | `br.net.air.perfilador.service` | @Service | `comercial-api/src/main/java/br/net/air/perfilador/service/MotivoService.java` |
| `SubmotivoService` | class | `br.net.air.perfilador.service` | @Service | `comercial-api/src/main/java/br/net/air/perfilador/service/SubmotivoService.java` |
| `ConnectionTokenManager` | class | `br.net.air.restPattern.ConnectionTokenManager` | @Data, @Service, @NoArgsConstructor, @AllArgsConstructor | `comercial-api/src/main/java/br/net/air/restPattern/ConnectionTokenManager/ConnectionTokenManager.java` |
| `Rest` | class | `br.net.air.restPattern` | @Service | `comercial-api/src/main/java/br/net/air/restPattern/Rest.java` |
| `RestHeaderRequestInterceptor` | class | `br.net.air.restPattern` |  | `comercial-api/src/main/java/br/net/air/restPattern/RestHeaderRequestInterceptor.java` |
| `SoapRepository` | class | `br.net.air.spc.repository` | @Repository | `comercial-api/src/main/java/br/net/air/spc/repository/SoapRepository.java` |
| `RotinaConsultaSPC` | class | `br.net.air.spc.rotina` |  | `comercial-api/src/main/java/br/net/air/spc/rotina/RotinaConsultaSPC.java` |
| `AbstractInsumoSPCAuto` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType, @XmlSeeAlso | `comercial-api/src/main/java/br/net/air/spc/soap/AbstractInsumoSPCAuto.java` |
| `AgenciaContaDocumentoDiferente` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/AgenciaContaDocumentoDiferente.java` |
| `Alinea` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/Alinea.java` |
| `AssinanteTelefone` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/AssinanteTelefone.java` |
| `Banco` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/Banco.java` |
| `BaseExternaAgente` | enum | `br.net.air.spc.soap` | @XmlType, @XmlEnum | `comercial-api/src/main/java/br/net/air/spc/soap/BaseExternaAgente.java` |
| `CartaAnuencia` | enum | `br.net.air.spc.soap` | @XmlType, @XmlEnum | `comercial-api/src/main/java/br/net/air/spc/soap/CartaAnuencia.java` |
| `Cartorio` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/Cartorio.java` |
| `CartorioObito` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/CartorioObito.java` |
| `Cheque` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType, @XmlSeeAlso | `comercial-api/src/main/java/br/net/air/spc/soap/Cheque.java` |
| `ChequeContraOrdem` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/ChequeContraOrdem.java` |
| `ChequeFiltro` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/ChequeFiltro.java` |
| `ChequeFinal` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/ChequeFinal.java` |
| `ChequeLojista` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/ChequeLojista.java` |
| `Cidade` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/Cidade.java` |
| `Cnpj` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/Cnpj.java` |
| `was` | class | `br.net.air.spc.soap` |  | `comercial-api/src/main/java/br/net/air/spc/soap/ConsultaWebService.java` |
| `ConsultaWebService` | interface | `br.net.air.spc.soap` | @WebService, @SOAPBinding, @XmlSeeAlso | `comercial-api/src/main/java/br/net/air/spc/soap/ConsultaWebService.java` |
| `was` | class | `br.net.air.spc.soap` |  | `comercial-api/src/main/java/br/net/air/spc/soap/ConsultaWebService_Service.java` |
| `ConsultaWebService_Service` | class | `br.net.air.spc.soap` | @WebServiceClient | `comercial-api/src/main/java/br/net/air/spc/soap/ConsultaWebService_Service.java` |
| `Cpf` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/Cpf.java` |
| `DadosAgenciaBancaria` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/DadosAgenciaBancaria.java` |
| `DadosBancarios` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/DadosBancarios.java` |
| `Detalhe1QuadroSocialMaisCompletoPJ` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/Detalhe1QuadroSocialMaisCompletoPJ.java` |
| `Detalhe2QuadroSocialMaisCompletoPJ` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/Detalhe2QuadroSocialMaisCompletoPJ.java` |
| `Endereco` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType, @XmlSeeAlso | `comercial-api/src/main/java/br/net/air/spc/soap/Endereco.java` |
| `EnderecoAssinanteTelefone` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/EnderecoAssinanteTelefone.java` |
| `EnderecoOcorrenciaConsumidor` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/EnderecoOcorrenciaConsumidor.java` |
| `Estado` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/Estado.java` |
| `EstadoCivil` | enum | `br.net.air.spc.soap` | @XmlType, @XmlEnum | `comercial-api/src/main/java/br/net/air/spc/soap/EstadoCivil.java` |
| `FaixaRendaPresumida` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/FaixaRendaPresumida.java` |
| `FiltroConsulta` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/FiltroConsulta.java` |
| `FiltroConsultaComplementar` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/FiltroConsultaComplementar.java` |
| `FiltroConsultaScore` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/FiltroConsultaScore.java` |
| `GrafiaPJ` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/GrafiaPJ.java` |
| `InformacoesAdicionais1Socios` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InformacoesAdicionais1Socios.java` |
| `InformacoesAdicionais2Socios` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InformacoesAdicionais2Socios.java` |
| `InformacoesAdicionais3Socios` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InformacoesAdicionais3Socios.java` |
| `InsumoAcao` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoAcao.java` |
| `InsumoAlertaDocumento` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoAlertaDocumento.java` |
| `InsumoAlertaIdentidade` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoAlertaIdentidade.java` |
| `InsumoAlertaObito` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoAlertaObito.java` |
| `InsumoAntecessora` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoAntecessora.java` |
| `InsumoAtividadeEmpresa` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoAtividadeEmpresa.java` |
| `InsumoCCF` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoCCF.java` |
| `InsumoCapitalSocial` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoCapitalSocial.java` |
| `InsumoChequeConsultaOnlineSRS` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoChequeConsultaOnlineSRS.java` |
| `InsumoChequeLojista` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoChequeLojista.java` |
| `InsumoChequeOutrasOcorrenciasSRS` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoChequeOutrasOcorrenciasSRS.java` |
| `InsumoChequeSemFundoAchei` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoChequeSemFundoAchei.java` |
| `InsumoChequeSemFundoAcheiCCF` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoChequeSemFundoAcheiCCF.java` |
| `InsumoChequeSemFundoVarejo` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoChequeSemFundoVarejo.java` |
| `InsumoComprometimentoRendaMensalPF` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoComprometimentoRendaMensalPF.java` |
| `InsumoConsultaRealizada` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoConsultaRealizada.java` |
| `InsumoConsultaRealizadaCheque` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoConsultaRealizadaCheque.java` |
| `InsumoContraOrdem` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType, @XmlSeeAlso | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoContraOrdem.java` |
| `InsumoContraOrdemAgenciaContaDiferente` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoContraOrdemAgenciaContaDiferente.java` |
| `InsumoContraOrdemAgenciaDiferente` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoContraOrdemAgenciaDiferente.java` |
| `InsumoContraOrdemDocumentoDiferente` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType, @XmlSeeAlso | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoContraOrdemDocumentoDiferente.java` |
| `InsumoContraOrdemDocumentoDiferenteSRS` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoContraOrdemDocumentoDiferenteSRS.java` |
| `InsumoContraOrdemSRS` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType, @XmlSeeAlso | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoContraOrdemSRS.java` |
| `InsumoContumacia` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoContumacia.java` |
| `InsumoContumaciaSRS` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType, @XmlSeeAlso | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoContumaciaSRS.java` |
| `InsumoCreditoConcedido` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoCreditoConcedido.java` |
| `InsumoDadosTelefoneConsultado` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoDadosTelefoneConsultado.java` |
| `InsumoDividaVencida` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoDividaVencida.java` |
| `InsumoDpvat` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoDpvat.java` |
| `InsumoEnderecoCEPConsultado` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoEnderecoCEPConsultado.java` |
| `InsumoFaturamentoPresumido` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoFaturamentoPresumido.java` |
| `InsumoFilial` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoFilial.java` |
| `InsumoGastoEstimadoPF` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoGastoEstimadoPF.java` |
| `InsumoGastoEstimadoPJ` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoGastoEstimadoPJ.java` |
| `InsumoGravame` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoGravame.java` |
| `InsumoHistoricoCheque` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType, @XmlSeeAlso | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoHistoricoCheque.java` |
| `InsumoHistoricoChequeDocumentoDiferente` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoHistoricoChequeDocumentoDiferente.java` |
| `InsumoHistoricoContaCorrente` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoHistoricoContaCorrente.java` |
| `InsumoHistoricoPagamento` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoHistoricoPagamento.java` |
| `InsumoIncorporacaoFusaoCisao` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoIncorporacaoFusaoCisao.java` |
| `InsumoIndiceRelacionamentoMercadoPF` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoIndiceRelacionamentoMercadoPF.java` |
| `InsumoIndiceRelacionamentoMercadoPJ` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoIndiceRelacionamentoMercadoPJ.java` |
| `InsumoInformacaoPoderJudiciario` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoInformacaoPoderJudiciario.java` |
| `InsumoInformacoesAdicionais` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoInformacoesAdicionais.java` |
| `InsumoInformacoesComplementares` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoInformacoesComplementares.java` |
| `InsumoLimiteCreditoPJ` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoLimiteCreditoPJ.java` |
| `InsumoLimiteCreditoSugerido` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoLimiteCreditoSugerido.java` |
| `InsumoObito` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoObito.java` |
| `InsumoOcorrenciaConsumidor` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoOcorrenciaConsumidor.java` |
| `InsumoOcupacao` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoOcupacao.java` |
| `InsumoParticipacaoEmpresas` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoParticipacaoEmpresas.java` |
| `InsumoParticipacaoFalencia` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoParticipacaoFalencia.java` |
| `InsumoPendenciaFinanceira` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoPendenciaFinanceira.java` |
| `InsumoPerfilFinanceiroPJ` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoPerfilFinanceiroPJ.java` |
| `InsumoPrincipaisProdutos` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoPrincipaisProdutos.java` |
| `InsumoProduto` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoProduto.java` |
| `InsumoProtesto` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoProtesto.java` |
| `InsumoQuadroAdministrativo` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoQuadroAdministrativo.java` |
| `InsumoQuadroSocialMaisCompletoPJ` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoQuadroSocialMaisCompletoPJ.java` |
| `InsumoQuadroSocietario` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType, @XmlSeeAlso | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoQuadroSocietario.java` |
| `InsumoReferenciaisNegocios` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoReferenciaisNegocios.java` |
| `InsumoRegistroConsultas` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoRegistroConsultas.java` |
| `InsumoRelacionamentoMaisAntigoComFornecedores` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoRelacionamentoMaisAntigoComFornecedores.java` |
| `InsumoRenavamEstadual` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoRenavamEstadual.java` |
| `InsumoRenavamFederal` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoRenavamFederal.java` |
| `InsumoRendaPresumidaSpc` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoRendaPresumidaSpc.java` |
| `InsumoRestricaoFinanceira` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoRestricaoFinanceira.java` |
| `InsumoRg` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoRg.java` |
| `InsumoRiscoCreditoPJ` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoRiscoCreditoPJ.java` |
| `InsumoRiskscoring12Meses` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoRiskscoring12Meses.java` |
| `InsumoRiskscoring6Meses` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType, @XmlSeeAlso | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoRiskscoring6Meses.java` |
| `InsumoRouboFurto` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoRouboFurto.java` |
| `InsumoSPC` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoSPC.java` |
| `InsumoSPCAutoLocaliza` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoSPCAutoLocaliza.java` |
| `InsumoSPCScore12Meses` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoSPCScore12Meses.java` |
| `InsumoSPCScore3Meses` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoSPCScore3Meses.java` |
| `InsumoTelefoneAlternativo` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoTelefoneAlternativo.java` |
| `InsumoTelefoneConsultado` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoTelefoneConsultado.java` |
| `InsumoTelefoneVinculadoAssinanteConsultado` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoTelefoneVinculadoAssinanteConsultado.java` |
| `InsumoTelefoneVinculadoConsumidor` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType, @XmlSeeAlso | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoTelefoneVinculadoConsumidor.java` |
| `InsumoUltimasConsultas` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/InsumoUltimasConsultas.java` |
| `LimiteCreditoSugeridoSar` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/LimiteCreditoSugeridoSar.java` |
| `ListaProduto` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/ListaProduto.java` |
| `MensagemBaseExterna` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/MensagemBaseExterna.java` |
| `MensagemComplementar` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/MensagemComplementar.java` |
| `MensagemComprometimentoRendaMensalPF` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/MensagemComprometimentoRendaMensalPF.java` |
| `MensagemGastoEstimadoPF` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/MensagemGastoEstimadoPF.java` |
| `MensagemGastoEstimadoPJ` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/MensagemGastoEstimadoPJ.java` |
| `MensagemIndiceRelacionamentoMercadoPF` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/MensagemIndiceRelacionamentoMercadoPF.java` |
| `MensagemIndiceRelacionamentoMercadoPJ` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/MensagemIndiceRelacionamentoMercadoPJ.java` |
| `MensagemRiskscoring` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/MensagemRiskscoring.java` |
| `Moeda` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/Moeda.java` |
| `NaturezaAnotacao` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/NaturezaAnotacao.java` |
| `NaturezaJuridica` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/NaturezaJuridica.java` |
| `and` | interface | `br.net.air.spc.soap` |  | `comercial-api/src/main/java/br/net/air/spc/soap/ObjectFactory.java` |
| `ObjectFactory` | class | `br.net.air.spc.soap` | @XmlRegistry | `comercial-api/src/main/java/br/net/air/spc/soap/ObjectFactory.java` |
| `ObservacaoAlertaObito` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/ObservacaoAlertaObito.java` |
| `OcorrenciaRechequeOnline` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/OcorrenciaRechequeOnline.java` |
| `Operador` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/Operador.java` |
| `Pais` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/Pais.java` |
| `ParametroProduto` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/ParametroProduto.java` |
| `PerfilFinanceiroContasAtivo` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/PerfilFinanceiroContasAtivo.java` |
| `PerfilFinanceiroContasPassivo` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/PerfilFinanceiroContasPassivo.java` |
| `PerfilFinanceiroFraseConclusao` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/PerfilFinanceiroFraseConclusao.java` |
| `PerfilFinanceiroIdentificacaoBalanco` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/PerfilFinanceiroIdentificacaoBalanco.java` |
| `PerfilFinanceiroIdentificacaoEmpresa` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/PerfilFinanceiroIdentificacaoEmpresa.java` |
| `PerfilFinanceiroIndicesFinanceiroIntegrado` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/PerfilFinanceiroIndicesFinanceiroIntegrado.java` |
| `PerfilFinanceiroResultado` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/PerfilFinanceiroResultado.java` |
| `PessoaFisica` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/PessoaFisica.java` |
| `PessoaJuridica` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/PessoaJuridica.java` |
| `Produto` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/Produto.java` |
| `ProtocoloConsulta` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/ProtocoloConsulta.java` |
| `QuadroAdministrativoQuadroSocialMaisCompletoPJ` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/QuadroAdministrativoQuadroSocialMaisCompletoPJ.java` |
| `RamoAtividade` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/RamoAtividade.java` |
| `ReferenciaComercial` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/ReferenciaComercial.java` |
| `RegistroQuadroSocialMaisCompletoPJ` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/RegistroQuadroSocialMaisCompletoPJ.java` |
| `Restricao` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/Restricao.java` |
| `ResultadoConsulta` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/ResultadoConsulta.java` |
| `ResultadoConsultaScore` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/ResultadoConsultaScore.java` |
| `ResultadoConsumidor` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/ResultadoConsumidor.java` |
| `ResultadoInsumo` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType, @XmlSeeAlso | `comercial-api/src/main/java/br/net/air/spc/soap/ResultadoInsumo.java` |
| `ResultadoInsumoConsultaRealizada` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/ResultadoInsumoConsultaRealizada.java` |
| `ResultadoInsumoContraOrdem` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/ResultadoInsumoContraOrdem.java` |
| `ResultadoInsumoContumacia` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/ResultadoInsumoContumacia.java` |
| `ResumoInsumo` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/ResumoInsumo.java` |
| `SemRestricao` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/SemRestricao.java` |
| `Sexo` | enum | `br.net.air.spc.soap` | @XmlType, @XmlEnum | `comercial-api/src/main/java/br/net/air/spc/soap/Sexo.java` |
| `Signo` | enum | `br.net.air.spc.soap` | @XmlType, @XmlEnum | `comercial-api/src/main/java/br/net/air/spc/soap/Signo.java` |
| `SimNao` | enum | `br.net.air.spc.soap` | @XmlType, @XmlEnum | `comercial-api/src/main/java/br/net/air/spc/soap/SimNao.java` |
| `SituacaoDocumentoWS` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/SituacaoDocumentoWS.java` |
| `Subjudice` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/Subjudice.java` |
| `Telefone` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/Telefone.java` |
| `TelefoneFiltro` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/TelefoneFiltro.java` |
| `TipoAcao` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/TipoAcao.java` |
| `TipoAssinanteTelefone` | enum | `br.net.air.spc.soap` | @XmlType, @XmlEnum | `comercial-api/src/main/java/br/net/air/spc/soap/TipoAssinanteTelefone.java` |
| `TipoClienteScore` | enum | `br.net.air.spc.soap` | @XmlType, @XmlEnum | `comercial-api/src/main/java/br/net/air/spc/soap/TipoClienteScore.java` |
| `TipoDocumentoAlerta` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/TipoDocumentoAlerta.java` |
| `TipoPessoa` | enum | `br.net.air.spc.soap` | @XmlType, @XmlEnum | `comercial-api/src/main/java/br/net/air/spc/soap/TipoPessoa.java` |
| `Vara` | class | `br.net.air.spc.soap` | @XmlAccessorType, @XmlType | `comercial-api/src/main/java/br/net/air/spc/soap/Vara.java` |
| `CpfCnpjHelper` | class | `br.net.air.util` |  | `comercial-api/src/main/java/br/net/air/util/CpfCnpjHelper.java` |
| `DataUtil` | class | `br.net.air.util` |  | `comercial-api/src/main/java/br/net/air/util/DataUtil.java` |
| `FormatNumericoUtil` | class | `br.net.air.util` | @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/util/FormatNumericoUtil.java` |
| `MetricsUtil` | class | `br.net.air.util` | @Slf4j | `comercial-api/src/main/java/br/net/air/util/MetricsUtil.java` |
| `VendaBuilder` | class | `br.net.air.venda.builder` | @Component | `comercial-api/src/main/java/br/net/air/venda/builder/VendaBuilder.java` |
| `AnaliseCreditoController` | class | `br.net.air.venda.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/venda/controller/AnaliseCreditoController.java` |
| `BloqueioGenericoController` | class | `br.net.air.venda.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/venda/controller/BloqueioGenericoController.java` |
| `LeadController` | class | `br.net.air.venda.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/venda/controller/LeadController.java` |
| `LeadObsController` | class | `br.net.air.venda.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/venda/controller/LeadObsController.java` |
| `RenegociacaoController` | class | `br.net.air.venda.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/venda/controller/RenegociacaoController.java` |
| `VendaController` | class | `br.net.air.venda.controller` | @Slf4j, @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/venda/controller/VendaController.java` |
| `AdicionalDTO` | class | `br.net.air.venda.dto` | @Data, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/venda/dto/AdicionalDTO.java` |
| `AnaliseCreditoDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/AnaliseCreditoDTO.java` |
| `AtivacaoNotificationDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/AtivacaoNotificationDTO.java` |
| `AtivacaoNotificationItemDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/AtivacaoNotificationItemDTO.java` |
| `CancelarVendaAtivacaoDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/CancelarVendaAtivacaoDTO.java` |
| `CarteiraDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/CarteiraDTO.java` |
| `DadosCadastraisDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/DadosCadastraisDTO.java` |
| `DescontoCRMDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/DescontoCRMDTO.java` |
| `EnderecoViabilidadeDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/EnderecoViabilidadeDTO.java` |
| `EnviarFaturaSalesforce` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/EnviarFaturaSalesforce.java` |
| `FaturaLoteDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/FaturaLoteDTO.java` |
| `FaturaSimplesDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/FaturaSimplesDTO.java` |
| `FinalizarVendaOSDTO` | class | `br.net.air.venda.dto` | @Data, @NoArgsConstructor, @AllArgsConstructor, @Builder | `comercial-api/src/main/java/br/net/air/venda/dto/FinalizarVendaOSDTO.java` |
| `IntegracaoDescontoDTO` | class | `br.net.air.venda.dto` | @Data, @NoArgsConstructor, @AllArgsConstructor | `comercial-api/src/main/java/br/net/air/venda/dto/IntegracaoDescontoDTO.java` |
| `IntegracaoEnderecoDTO` | class | `br.net.air.venda.dto` | @Data, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/venda/dto/IntegracaoEnderecoDTO.java` |
| `IntegracaoLeadDTO` | class | `br.net.air.venda.dto` | @Data, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/venda/dto/IntegracaoLeadDTO.java` |
| `LeadDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/LeadDTO.java` |
| `LeadObsDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/LeadObsDTO.java` |
| `OrdemServicoDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/OrdemServicoDTO.java` |
| `PerfilacaoComercialDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/PerfilacaoComercialDTO.java` |
| `ProdutoItemSapDTO` | class | `br.net.air.venda.dto` | @Data, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/venda/dto/ProdutoItemSapDTO.java` |
| `ProdutoSapDTO` | class | `br.net.air.venda.dto` | @Data, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/venda/dto/ProdutoSapDTO.java` |
| `RenegociacaoDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/RenegociacaoDTO.java` |
| `RenegociacaoTituloDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/RenegociacaoTituloDTO.java` |
| `RespostaAnaliseDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/RespostaAnaliseDTO.java` |
| `ResultadoValidacaoDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/ResultadoValidacaoDTO.java` |
| `SegundaViaNotificationDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/SegundaViaNotificationDTO.java` |
| `SegundaViaNotificationItemDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/SegundaViaNotificationItemDTO.java` |
| `SerasaDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/SerasaDTO.java` |
| `SpcDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/SpcDTO.java` |
| `TarefaDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/TarefaDTO.java` |
| `VendaDTO` | class | `br.net.air.venda.dto` | @Data, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/venda/dto/VendaDTO.java` |
| `VendaIdProjection` | interface | `br.net.air.venda.dto` |  | `comercial-api/src/main/java/br/net/air/venda/dto/VendaIdProjection.java` |
| `VendaNotificationDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/VendaNotificationDTO.java` |
| `VendaNotificationItemDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/VendaNotificationItemDTO.java` |
| `ViabilidadeTecnicaDTO` | class | `br.net.air.venda.dto` | @Data | `comercial-api/src/main/java/br/net/air/venda/dto/ViabilidadeTecnicaDTO.java` |
| `AnaliseCreditoAtributoDto` | class | `br.net.air.venda.dto.analisecreditolead` | @Builder, @Data, @AllArgsConstructor, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/venda/dto/analisecreditolead/AnaliseCreditoAtributoDto.java` |
| `AnaliseCreditoDto` | class | `br.net.air.venda.dto.analisecreditolead` | @Builder, @Data, @AllArgsConstructor, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/venda/dto/analisecreditolead/AnaliseCreditoDto.java` |
| `AnaliseCreditoProjectionDto` | interface | `br.net.air.venda.dto.analisecreditolead` |  | `comercial-api/src/main/java/br/net/air/venda/dto/analisecreditolead/AnaliseCreditoProjectionDto.java` |
| `AnaliseCreditoRestricaoDto` | class | `br.net.air.venda.dto.analisecreditolead` | @Builder, @Data, @AllArgsConstructor, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/venda/dto/analisecreditolead/AnaliseCreditoRestricaoDto.java` |
| `EnderecoBairroDto` | class | `br.net.air.venda.dto.analisecreditolead` | @Builder, @Data, @AllArgsConstructor, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/venda/dto/analisecreditolead/EnderecoBairroDto.java` |
| `EnderecoLogradouroDto` | class | `br.net.air.venda.dto.analisecreditolead` | @Builder, @Data, @AllArgsConstructor, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/venda/dto/analisecreditolead/EnderecoLogradouroDto.java` |
| `IntegracaoDto` | class | `br.net.air.venda.dto.analisecreditolead` | @Builder, @Data, @AllArgsConstructor, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/venda/dto/analisecreditolead/IntegracaoDto.java` |
| `LeadCidadeDto` | class | `br.net.air.venda.dto.analisecreditolead` | @Builder, @Data, @AllArgsConstructor, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/venda/dto/analisecreditolead/LeadCidadeDto.java` |
| `LeadDto` | class | `br.net.air.venda.dto.analisecreditolead` | @Builder, @Data, @AllArgsConstructor, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/venda/dto/analisecreditolead/LeadDto.java` |
| `LeadViabilidadeDto` | class | `br.net.air.venda.dto.analisecreditolead` | @Builder, @Data, @AllArgsConstructor, @NoArgsConstructor | `comercial-api/src/main/java/br/net/air/venda/dto/analisecreditolead/LeadViabilidadeDto.java` |
| `AnaliseCreditoAtributoProjectionDto` | interface | `br.net.air.venda.dto.analisecreditolead.projection` |  | `comercial-api/src/main/java/br/net/air/venda/dto/analisecreditolead/projection/AnaliseCreditoAtributoProjectionDto.java` |
| `AnaliseCreditoRestricaoProjectionDto` | interface | `br.net.air.venda.dto.analisecreditolead.projection` |  | `comercial-api/src/main/java/br/net/air/venda/dto/analisecreditolead/projection/AnaliseCreditoRestricaoProjectionDto.java` |
| `CidadeLeadProjectionDto` | interface | `br.net.air.venda.dto.analisecreditolead.projection` |  | `comercial-api/src/main/java/br/net/air/venda/dto/analisecreditolead/projection/CidadeLeadProjectionDto.java` |
| `EnderecoBairroProjectionDto` | interface | `br.net.air.venda.dto.analisecreditolead.projection` |  | `comercial-api/src/main/java/br/net/air/venda/dto/analisecreditolead/projection/EnderecoBairroProjectionDto.java` |
| `EnderecoCondominioProjection` | interface | `br.net.air.venda.dto.analisecreditolead.projection` |  | `comercial-api/src/main/java/br/net/air/venda/dto/analisecreditolead/projection/EnderecoCondominioProjection.java` |
| `EnderecoLogradouroProjectionDto` | interface | `br.net.air.venda.dto.analisecreditolead.projection` |  | `comercial-api/src/main/java/br/net/air/venda/dto/analisecreditolead/projection/EnderecoLogradouroProjectionDto.java` |
| `LeadEvent` | class | `br.net.air.venda.event` | @Data, @Builder | `comercial-api/src/main/java/br/net/air/venda/event/LeadEvent.java` |
| `LeadListener` | class | `br.net.air.venda.event` | @Component | `comercial-api/src/main/java/br/net/air/venda/event/LeadListener.java` |
| `AirAssinanteGigaTv` | class | `br.net.air.venda.model` | @Entity, @Getter, @Setter, @Accessors, @Table | `comercial-api/src/main/java/br/net/air/venda/model/AirAssinanteGigaTv.java` |
| `AirAssinanteGloboplay` | class | `br.net.air.venda.model` | @Entity, @Getter, @Setter, @Accessors, @Table | `comercial-api/src/main/java/br/net/air/venda/model/AirAssinanteGloboplay.java` |
| `AnaliseCredito` | class | `br.net.air.venda.model` | @Entity, @Getter, @Setter, @Table, @Descricao | `comercial-api/src/main/java/br/net/air/venda/model/AnaliseCredito.java` |
| `AnaliseCreditoAtributo` | class | `br.net.air.venda.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/venda/model/AnaliseCreditoAtributo.java` |
| `Tipo` | enum | `br.net.air.venda.model` | @Getter | `comercial-api/src/main/java/br/net/air/venda/model/AnaliseCreditoAtributo.java` |
| `AnaliseCreditoRestricao` | class | `br.net.air.venda.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/venda/model/AnaliseCreditoRestricao.java` |
| `BloqueioGenerico` | class | `br.net.air.venda.model` | @Entity, @Getter, @Setter, @Table, @Descricao | `comercial-api/src/main/java/br/net/air/venda/model/BloqueioGenerico.java` |
| `HistoricoViabilidadesVenda` | class | `br.net.air.venda.model` | @Entity, @Getter, @Setter, @Descricao, @Table | `comercial-api/src/main/java/br/net/air/venda/model/HistoricoViabilidadesVenda.java` |
| `Lead` | class | `br.net.air.venda.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/venda/model/Lead.java` |
| `Qualificacao` | enum | `br.net.air.venda.model` |  | `comercial-api/src/main/java/br/net/air/venda/model/Lead.java` |
| `LeadObs` | class | `br.net.air.venda.model` | @Entity, @Getter, @Setter, @Descricao, @Table | `comercial-api/src/main/java/br/net/air/venda/model/LeadObs.java` |
| `PerfilacaoComercial` | class | `br.net.air.venda.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/venda/model/PerfilacaoComercial.java` |
| `Renegociacao` | class | `br.net.air.venda.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/venda/model/Renegociacao.java` |
| `RenegociacaoTitulo` | class | `br.net.air.venda.model` | @Entity, @Getter, @Setter, @Descricao, @Table | `comercial-api/src/main/java/br/net/air/venda/model/RenegociacaoTitulo.java` |
| `Venda` | class | `br.net.air.venda.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/venda/model/Venda.java` |
| `Natureza` | enum | `br.net.air.venda.model` |  | `comercial-api/src/main/java/br/net/air/venda/model/Venda.java` |
| `Fase` | enum | `br.net.air.venda.model` |  | `comercial-api/src/main/java/br/net/air/venda/model/Venda.java` |
| `VendaAdicional` | class | `br.net.air.venda.model` | @Entity, @Getter, @Setter, @Descricao, @Table | `comercial-api/src/main/java/br/net/air/venda/model/VendaAdicional.java` |
| `VendaFase` | class | `br.net.air.venda.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/venda/model/VendaFase.java` |
| `VendaOrigem` | class | `br.net.air.venda.model` | @Entity, @Getter, @Setter, @Table | `comercial-api/src/main/java/br/net/air/venda/model/VendaOrigem.java` |
| `AirAssinanteGigaTvRepository` | interface | `br.net.air.venda.repository` | @Repository | `comercial-api/src/main/java/br/net/air/venda/repository/AirAssinanteGigaTvRepository.java` |
| `AirAssinanteGloboplayRepository` | interface | `br.net.air.venda.repository` | @Repository | `comercial-api/src/main/java/br/net/air/venda/repository/AirAssinanteGloboplayRepository.java` |
| `AnaliseCreditoAtributoRepository` | interface | `br.net.air.venda.repository` |  | `comercial-api/src/main/java/br/net/air/venda/repository/AnaliseCreditoAtributoRepository.java` |
| `AnaliseCreditoRepository` | interface | `br.net.air.venda.repository` |  | `comercial-api/src/main/java/br/net/air/venda/repository/AnaliseCreditoRepository.java` |
| `AnaliseCreditoRestricaoRepository` | interface | `br.net.air.venda.repository` |  | `comercial-api/src/main/java/br/net/air/venda/repository/AnaliseCreditoRestricaoRepository.java` |
| `BloqueioGenericoRepository` | interface | `br.net.air.venda.repository` |  | `comercial-api/src/main/java/br/net/air/venda/repository/BloqueioGenericoRepository.java` |
| `HistoricoViabilidadesVendaRepository` | interface | `br.net.air.venda.repository` |  | `comercial-api/src/main/java/br/net/air/venda/repository/HistoricoViabilidadesVendaRepository.java` |
| `LeadObsRepository` | interface | `br.net.air.venda.repository` |  | `comercial-api/src/main/java/br/net/air/venda/repository/LeadObsRepository.java` |
| `LeadRepository` | interface | `br.net.air.venda.repository` |  | `comercial-api/src/main/java/br/net/air/venda/repository/LeadRepository.java` |
| `PerfilacaoComercialRepository` | interface | `br.net.air.venda.repository` |  | `comercial-api/src/main/java/br/net/air/venda/repository/PerfilacaoComercialRepository.java` |
| `RenegociacaoRepository` | interface | `br.net.air.venda.repository` |  | `comercial-api/src/main/java/br/net/air/venda/repository/RenegociacaoRepository.java` |
| `RenegociacaoTituloRepository` | interface | `br.net.air.venda.repository` |  | `comercial-api/src/main/java/br/net/air/venda/repository/RenegociacaoTituloRepository.java` |
| `VendaAdicionalRepository` | interface | `br.net.air.venda.repository` |  | `comercial-api/src/main/java/br/net/air/venda/repository/VendaAdicionalRepository.java` |
| `VendaFaseRepository` | interface | `br.net.air.venda.repository` |  | `comercial-api/src/main/java/br/net/air/venda/repository/VendaFaseRepository.java` |
| `VendaOrigemRepository` | interface | `br.net.air.venda.repository` |  | `comercial-api/src/main/java/br/net/air/venda/repository/VendaOrigemRepository.java` |
| `VendaRepository` | interface | `br.net.air.venda.repository` |  | `comercial-api/src/main/java/br/net/air/venda/repository/VendaRepository.java` |
| `AnaliseCreditoService` | class | `br.net.air.venda.service` | @Slf4j, @Service | `comercial-api/src/main/java/br/net/air/venda/service/AnaliseCreditoService.java` |
| `BloqueioGenericoService` | class | `br.net.air.venda.service` | @Service, @Log | `comercial-api/src/main/java/br/net/air/venda/service/BloqueioGenericoService.java` |
| `ChamadoService` | class | `br.net.air.venda.service` | @Service, @Log | `comercial-api/src/main/java/br/net/air/venda/service/ChamadoService.java` |
| `HistoricoViabilidadesVendaService` | class | `br.net.air.venda.service` | @Log, @Service | `comercial-api/src/main/java/br/net/air/venda/service/HistoricoViabilidadesVendaService.java` |
| `LeadObsService` | class | `br.net.air.venda.service` | @Service | `comercial-api/src/main/java/br/net/air/venda/service/LeadObsService.java` |
| `LeadService` | class | `br.net.air.venda.service` | @Service | `comercial-api/src/main/java/br/net/air/venda/service/LeadService.java` |
| `NotificationService` | class | `br.net.air.venda.service` | @Slf4j, @Service | `comercial-api/src/main/java/br/net/air/venda/service/NotificationService.java` |
| `PerfilacaoComercialService` | class | `br.net.air.venda.service` | @Log, @Service | `comercial-api/src/main/java/br/net/air/venda/service/PerfilacaoComercialService.java` |
| `RenegociacaoService` | class | `br.net.air.venda.service` | @Service, @Log | `comercial-api/src/main/java/br/net/air/venda/service/RenegociacaoService.java` |
| `VendaAdicionalService` | class | `br.net.air.venda.service` | @Service | `comercial-api/src/main/java/br/net/air/venda/service/VendaAdicionalService.java` |
| `VendaFaseService` | class | `br.net.air.venda.service` | @Service | `comercial-api/src/main/java/br/net/air/venda/service/VendaFaseService.java` |
| `VendaOrigemService` | class | `br.net.air.venda.service` | @Service | `comercial-api/src/main/java/br/net/air/venda/service/VendaOrigemService.java` |
| `VendaService` | class | `br.net.air.venda.service` | @Slf4j, @Service | `comercial-api/src/main/java/br/net/air/venda/service/VendaService.java` |
| `ViabilidadeController` | class | `br.net.air.viabilidadeTeorica.controller` | @CrossOrigin, @RestController, @RequestMapping | `comercial-api/src/main/java/br/net/air/viabilidadeTeorica/controller/ViabilidadeController.java` |
| `WebSocketController` | class | `br.net.air.webSocket` | @Controller | `comercial-api/src/main/java/br/net/air/webSocket/WebSocketController.java` |

## SQL nativo no codigo

Limite desta secao: primeiras 500 linhas com indicio de SQL. Use o arquivo fonte para revisar o bloco completo.

| Arquivo | Linha |
|---|---|
| `comercial-api/src/main/java/br/net/air/app/controller/AppAdicionalController.java:57` | `//        service.delete(entity);` |
| `comercial-api/src/main/java/br/net/air/app/controller/AppUpgradeController.java:63` | `//        service.delete(entity);` |
| `comercial-api/src/main/java/br/net/air/app/controller/AppVendaController.java:76` | `//        service.delete(entity);` |
| `comercial-api/src/main/java/br/net/air/clean_arch/application/controllers/contactController/ContactApiV1.java:19` | `@PutMapping("/update/{contactId}")` |
| `comercial-api/src/main/java/br/net/air/clean_arch/application/controllers/contactController/ContactApiV1.java:22` | `@DeleteMapping("/delete/{contactId}")` |
| `comercial-api/src/main/java/br/net/air/clean_arch/application/controllers/contactController/ContactControllerV1.java:48` | `@PutMapping("/update/{contactId}")` |
| `comercial-api/src/main/java/br/net/air/clean_arch/application/controllers/contactController/ContactControllerV1.java:56` | `@DeleteMapping("/delete/{contactId}")` |
| `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/NotificationApiProvider.java:199` | `message.put("from", "552220418549");` |
| `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/NotificationApiProvider.java:234` | `message.put("from", "552220418556");` |
| `comercial-api/src/main/java/br/net/air/clean_arch/infra/gateways/adapters/NotificationApiAdapter.java:79` | `CompletableFuture.allOf(futures.toArray(new CompletableFuture[0])).join();` |
| `comercial-api/src/main/java/br/net/air/cliente/controller/ClienteAnexoController.java:72` | `service.delete(entity);` |
| `comercial-api/src/main/java/br/net/air/cliente/controller/ClienteContatoController.java:51` | `service.delete(entity);` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteContatoRepository.java:33` | `@Query("SELECT new br.net.air.clean_arch.application.dto.CustomerContact(c.id, c.cliente.id ,c.contato, c.tipo, c.ativo, c.confirmado, c.status, c.favorito) " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteContatoRepository.java:34` | `"FROM ClienteContato c WHERE c.id = :id AND c.cliente.id = :clienteId AND c.excluido = false")` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteContatoRepository.java:36` | `@Query("SELECT c.cliente.id FROM ClienteContato c WHERE c.id = :contatoId AND c.excluido = false")` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteContatoRepository.java:41` | `@Query("UPDATE ClienteContato c SET c.favorito = false, c.dataAlteracao = NOW() WHERE c.cliente.id = :idCliente AND c.tipo = :tipo AND c.favorito = true")` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteContatoRepository.java:46` | `@Query("UPDATE ClienteContato c SET c.favorito = true, c.status = 'VALIDO', c.dataAlteracao = NOW() WHERE c.id = :id")` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteContatoRepository.java:49` | `@Query("SELECT new br.net.air.clean_arch.application.dto.CustomerContact(c.id, c.cliente.id, c.contato, c.tipo, c.ativo, c.confirmado, c.status, c.favorito) " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteContatoRepository.java:50` | `"FROM ClienteContato c WHERE c.cliente.id = :customerId AND c.tipo = :contactType AND c.contato = :contact AND c.excluido = false")` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteContatoRepository.java:57` | `@Query("SELECT COUNT(c) > 0 FROM ClienteContato c WHERE c.cliente.id = :customerId AND c.tipo = :contactType AND c.favorito = true AND c.excluido = false")` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteContatoRepository.java:65` | `@Query(value = "INSERT INTO tbl_cliente_contato (id_cliente, tipo, contato, ativo, confirmado, status, favorito, excluido, " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteContatoRepository.java:79` | `@Query(value = "SELECT id FROM tbl_cliente_contato WHERE id_cliente = :clienteId AND tipo = :tipo AND contato = :contato " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteContatoRepository.java:88` | `@Query(value = "UPDATE tbl_cliente_contato SET " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteContatoRepository.java:109` | `@Query("SELECT new br.net.air.clean_arch.application.dto.CustomerContact(c.id, c.cliente.id, c.contato, c.tipo, c.ativo, c.confirmado, c.status, c.favorito) " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteContatoRepository.java:110` | `"FROM ClienteContato c WHERE c.cliente.id = :id AND c.tipo = :s AND c.id = :contactId AND c.excluido = false")` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteContatoRepository.java:118` | `"SELECT new br.net.air.clean_arch.application.dto.CustomerContact(" +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteContatoRepository.java:120` | `" FROM ClienteContato c" +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteContatoRepository.java:132` | `@Query(value = "UPDATE tbl_cliente_contato SET data_alteracao = NOW(), "` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteRepository.java:19` | `@Query(value = " SELECT " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteRepository.java:62` | `" FROM tbl_cliente cliente " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteRepository.java:63` | `" left outer join tbl_cliente_fisico clienteFisico on cliente.id = clienteFisico.id_cliente " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteRepository.java:64` | `" left outer join tbl_cliente_juridico clienteJuridico on cliente.id = clienteJuridico.id_cliente  " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteRepository.java:70` | `@Query("SELECT cl " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteRepository.java:71` | `"FROM Contrato ct " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteRepository.java:72` | `"JOIN ct.cliente cl " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteRepository.java:79` | `@Query("SELECT new br.net.air.clean_arch.application.dto.ClienteResumoAvisoDTO(" +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteRepository.java:83` | `"FROM Cliente c " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ClienteRepository.java:90` | `value = "UPDATE air_comercial.tbl_cliente SET senha_sac = :password, integracao_status = :updateStatus, integracao_status_sydle = :updateStatus WHERE id = :customerId",` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoItemRepository.java:16` | `@Query("SELECT ci FROM ContratoItem ci WHERE ci.produto.id = :produtoId")` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoProdutoRepository.java:16` | `@Query("SELECT cp FROM ContratoProduto cp WHERE cp.contrato.id = :idContrato AND cp.versaoContrato = :versaoContrato AND cp.excluido = false")` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRepository.java:28` | `@Query("SELECT new br.net.air.clean_arch.application.dto.ContractItemDto( " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRepository.java:35` | `" FROM ContratoItem item " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRepository.java:36` | `" INNER JOIN item.produto produto " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRepository.java:37` | `" INNER JOIN produto.contrato contrato " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRepository.java:45` | `@Query("SELECT new br.net.air.clean_arch.application.dto.ContratoPacoteDTO(c.pacoteNome, c.valorFinal, c.status, c.vencimento.dia) " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRepository.java:46` | `"FROM Contrato c WHERE c.id = :id")` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRepository.java:51` | `@Query("SELECT c.id FROM Contrato c WHERE c.cliente.id = :clienteId")` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRepository.java:54` | `@Query(value = "SELECT " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRepository.java:61` | `"FROM air_comercial.tbl_contrato co " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRepository.java:62` | `"INNER JOIN air_comercial.tbl_cliente c ON co.id_cliente = c.id " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRepository.java:63` | `"LEFT JOIN air_comercial.tbl_cliente_fisico cf ON cf.id_cliente = c.id " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRepository.java:64` | `"LEFT JOIN air_comercial.tbl_cliente_juridico cj ON cj.id_cliente = c.id " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRepository.java:69` | `@Query(value = "SELECT " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRepository.java:76` | `"FROM air_comercial.tbl_cliente c " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRepository.java:77` | `"INNER JOIN air_comercial.tbl_cliente_fisico cf ON cf.id_cliente = c.id " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRepository.java:82` | `@Query(value = "SELECT " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRepository.java:89` | `"FROM air_comercial.tbl_cliente c " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/ContratoRepository.java:90` | `"INNER JOIN air_comercial.tbl_cliente_juridico cj ON cj.id_cliente = c.id " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/EventosSiteRepository.java:12` | `@Query(value = "INSERT INTO air_comercial.tbl_eventos_site (data_criacao, id_cliente, tipo_evento, valor_alterado) " +` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/MarcadorContratoRepository.java:18` | `@Query("DELETE FROM MarcadorContrato o WHERE o.dataValidade < CURRENT_DATE")` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/OutrosMarcadoresRepository.java:14` | `final String queryFindByClientIdsAndMarcador = "SELECT tom.* "` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/OutrosMarcadoresRepository.java:15` | `+ "FROM tbl_outros_marcadores tom "` |
| `comercial-api/src/main/java/br/net/air/cliente/repository/OutrosMarcadoresRepository.java:32` | `@Query("DELETE FROM OutrosMarcadores o WHERE o.dataValidade < CURRENT_DATE")` |
| `comercial-api/src/main/java/br/net/air/cliente/service/ClienteContatoService.java:53` | `public void delete(ClienteContato entity) {` |
| `comercial-api/src/main/java/br/net/air/cliente/service/ClienteService.java:222` | `outrosMarcadoresRepository.delete(outrosMarcadores);` |
| `comercial-api/src/main/java/br/net/air/cliente/service/ClienteService.java:236` | `String obs = String.join(", ", dto.getDesmarcados());` |
| `comercial-api/src/main/java/br/net/air/cliente/service/ClienteService.java:240` | `String obs = String.join(", ", dto.getMarcados());` |
| `comercial-api/src/main/java/br/net/air/cliente/service/ClienteService.java:865` | `//        contratos.forEach(c -> mySqlRepository.executar("Assinante.update.senhaMotv", c));` |
| `comercial-api/src/main/java/br/net/air/cliente/service/ClienteService.java:1176` | `savedFile.delete();` |
| `comercial-api/src/main/java/br/net/air/cliente/service/ClienteService.java:1232` | `this.outrosMarcadoresRepository.delete(outrosMarcadores);` |
| `comercial-api/src/main/java/br/net/air/cliente/service/ClienteService.java:1245` | `String sql = "INSERT INTO tbl_outros_marcadores (id_cliente, marcador) VALUES (?, ?) ";` |
| `comercial-api/src/main/java/br/net/air/cliente/service/ClienteService.java:1301` | `savedFile.delete();` |
| `comercial-api/src/main/java/br/net/air/cliente/service/ClienteService.java:1360` | `this.marcadorContratoRepository.delete(marcadorContrato);` |
| `comercial-api/src/main/java/br/net/air/cliente/service/ContratoCampanhaService.java:60` | `contratoCampanha.setPacoteUpVigencia(Date.from(up.atStartOfDay().atZone(ZoneId.systemDefault()).toInstant()));` |
| `comercial-api/src/main/java/br/net/air/cliente/service/ContratoCampanhaService.java:81` | `contratoCampanha.setRecorrenciaVigencia(Date.from(recorrencia.atStartOfDay().atZone(ZoneId.systemDefault()).toInstant()));` |
| `comercial-api/src/main/java/br/net/air/cliente/service/ContratoEntregaService.java:33` | `super.delete(entrega);` |
| `comercial-api/src/main/java/br/net/air/cliente/service/ContratoService.java:711` | `enderecoService.delete(contrato.getEnderecoCobranca());` |
| `comercial-api/src/main/java/br/net/air/cliente/service/ContratoService.java:720` | `enderecoService.delete(contratoEntrega.getEndereco());` |
| `comercial-api/src/main/java/br/net/air/cliente/service/ContratoService.java:721` | `contratoEntregaService.delete(contratoEntrega);` |
| `comercial-api/src/main/java/br/net/air/cliente/service/ContratoService.java:1102` | `allFutures.join();` |
| `comercial-api/src/main/java/br/net/air/cliente/service/ContratoService.java:1123` | `//            contratoProdutoService.delete(produto);` |
| `comercial-api/src/main/java/br/net/air/cliente/service/ContratoService.java:1124` | `//            contratoItemRepository.findByProduto(produto).forEach(item -> contratoItemService.delete(item));` |
| `comercial-api/src/main/java/br/net/air/cliente/service/ContratoService.java:1132` | `//        vendaAdicionais.forEach(item -> adicionalService.delete(item));` |
| `comercial-api/src/main/java/br/net/air/cliente/service/ContratoService.java:1285` | `//        enderecoService.delete(contratoEntrega.getEndereco());` |
| `comercial-api/src/main/java/br/net/air/cliente/service/ContratoService.java:1286` | `//        contratoEntregaService.delete(contratoEntrega);` |
| `comercial-api/src/main/java/br/net/air/cliente/service/ContratoService.java:1536` | `enderecoService.delete(contratoEntrega.getEndereco());` |
| `comercial-api/src/main/java/br/net/air/cliente/service/ContratoService.java:1537` | `contratoEntregaService.delete(contratoEntrega);` |
| `comercial-api/src/main/java/br/net/air/composicao/service/ItemSapService.java:52` | `itemRepository.delete(itemToDelete);` |
| `comercial-api/src/main/java/br/net/air/composicao/service/PacoteSapService.java:66` | `pacoteProdutoRepository.delete(composicao);` |
| `comercial-api/src/main/java/br/net/air/composicao/service/PacoteSapService.java:69` | `pacoteRepository.delete(pacoteToDelete);` |
| `comercial-api/src/main/java/br/net/air/composicao/service/PacoteSapService.java:105` | `if (!produtosComposicao.isEmpty()) pacoteProdutoRepository.delete(produtosComposicao);` |
| `comercial-api/src/main/java/br/net/air/composicao/service/ProdutoSapService.java:62` | `if (prodToDelete != null) produtoRepository.delete(prodToDelete);` |
| `comercial-api/src/main/java/br/net/air/composicao/service/ProdutoSapService.java:66` | `if (!prodComposicaoToDelete.isEmpty()) produtoItemRepository.delete(prodComposicaoToDelete);` |
| `comercial-api/src/main/java/br/net/air/composicao/service/ProdutoSapService.java:101` | `if (!itensComposicao.isEmpty()) produtoItemRepository.delete(itensComposicao);` |
| `comercial-api/src/main/java/br/net/air/configuracoes/controller/CampanhaController.java:77` | `//        service.delete(entity);` |
| `comercial-api/src/main/java/br/net/air/configuracoes/controller/CampanhaPacoteAdicionalController.java:43` | `//        service.delete(entity);` |
| `comercial-api/src/main/java/br/net/air/configuracoes/controller/CampanhaPacoteController.java:70` | `service.delete(entity);` |
| `comercial-api/src/main/java/br/net/air/configuracoes/controller/EnderecoBairroController.java:52` | `//        service.delete(entity);` |
| `comercial-api/src/main/java/br/net/air/configuracoes/controller/EnderecoCidadeController.java:96` | `//        service.delete(entity);` |
| `comercial-api/src/main/java/br/net/air/configuracoes/controller/EnderecoLogradouroController.java:33` | `//        service.delete(entity);` |
| `comercial-api/src/main/java/br/net/air/configuracoes/controller/RegraSuspensaoController.java:48` | `//        service.delete(entity);` |
| `comercial-api/src/main/java/br/net/air/configuracoes/controller/TermoController.java:69` | `//        service.delete(entity);` |
| `comercial-api/src/main/java/br/net/air/configuracoes/controller/VencimentoController.java:47` | `service.delete(entity);` |
| `comercial-api/src/main/java/br/net/air/configuracoes/controller/VendedorController.java:65` | `service.delete(entity);` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/CampanhaPacoteAdicionalRepository.java:17` | `//    @Query("DELETE FROM CampanhaPacoteAdicional WHERE pacote = :pacote")` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/CarteiraRepository.java:18` | `@Query(value = " SELECT " +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/CarteiraRepository.java:47` | `" FROM tbl_carteira carteira " +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/CarteiraRepository.java:48` | `" left outer join tbl_vendedor vendedor on carteira.id_vendedor = vendedor.id " +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/CarteiraRepository.java:49` | `" left outer join tbl_vendedor supervisor on vendedor.id_supervisor = supervisor.id  " +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/CondominioRepository.java:16` | `@Query(value =  " SELECT " +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/CondominioRepository.java:75` | `" FROM air_comercial.tbl_condominio co " +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoBairroRepository.java:17` | `@Query(value = "  SELECT bair.nome," +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoBairroRepository.java:19` | `" FROM tbl_endereco_bairro bair " +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoCidadeRepository.java:20` | `@Query(value = " SELECT unidades.unidades as unidade FROM tbl_endereco_cidade_unidade unidades WHERE unidades.id_cidade = :codigoCidade", nativeQuery = true)` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoCidadeRepository.java:23` | `@Query(value = " SELECT " +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoCidadeRepository.java:35` | `" FROM tbl_endereco_cidade c " +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoCidadeRepository.java:40` | `@Query(value = "select * from air_comercial.tbl_endereco_cidade tec" +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoCidadeRepository.java:41` | `" inner join air_comercial.tbl_endereco_cidade_unidade tecu on tec.id = tecu.id_cidade" +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoLogradouroRepository.java:17` | `@Query(value = " SELECT " +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoLogradouroRepository.java:24` | `" FROM tbl_endereco_logradouro logr " +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoRepository.java:22` | `@Query(value = " SELECT " +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoRepository.java:119` | `" FROM air_comercial.tbl_endereco e" +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoRepository.java:120` | `" INNER JOIN tbl_endereco_cidade c ON c.id = e.id_cidade" +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoRepository.java:121` | `" LEFT JOIN air_comercial.tbl_condominio co ON co.id = e.id_condominio" +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoRepository.java:126` | `@Query(value = "SELECT " +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoRepository.java:132` | `"FROM air_comercial.tbl_contrato contrato " +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoRepository.java:133` | `"INNER JOIN air_comercial.tbl_contrato_entrega ctre ON ctre.id_contrato = contrato.id AND !ctre.excluido " +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoRepository.java:134` | `"INNER JOIN air_comercial.tbl_endereco endereco ON ctre.id_endereco = endereco.id AND !endereco.excluido " +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoRepository.java:135` | `"INNER JOIN air_comercial.tbl_endereco_cidade cidade ON endereco.id_cidade = cidade.id " +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoRepository.java:141` | `//    @Query(value = "SELECT " +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoRepository.java:152` | `//            "FROM air_comercial.tbl_contrato contrato " +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoRepository.java:153` | `//            "INNER JOIN air_comercial.tbl_endereco endereco ON endereco.id = ( " +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoRepository.java:154` | `//            "    SELECT MAX(inner_end.id) FROM air_comercial.tbl_endereco inner_end " +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoRepository.java:157` | `//            "        SELECT inner_entreg.id_endereco FROM air_comercial.tbl_contrato_entrega inner_entreg " +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoRepository.java:161` | `//            "INNER JOIN air_comercial.tbl_endereco_cidade cidade ON endereco.id_cidade = cidade.id " +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/repository/EnderecoRepository.java:162` | `//            "LEFT JOIN air_base.tbl_catalogo_item tipo ON tipo.codigo = endereco.logradouro_tipo " +` |
| `comercial-api/src/main/java/br/net/air/configuracoes/service/CampanhaPacoteService.java:23` | `public void delete(CampanhaPacote entity) {` |
| `comercial-api/src/main/java/br/net/air/configuracoes/service/CampanhaPacoteService.java:25` | `campanhaPacoteAdicionalRepository.delete(cp));` |
| `comercial-api/src/main/java/br/net/air/configuracoes/service/CampanhaPacoteService.java:27` | `this.repository.delete(entity.getId());` |
| `comercial-api/src/main/java/br/net/air/configuracoes/service/EnderecoBairroService.java:29` | `public void delete(EnderecoBairro entity) {` |
| `comercial-api/src/main/java/br/net/air/configuracoes/service/EnderecoBairroService.java:31` | `enderecoLogradouroRepository.delete(e));` |
| `comercial-api/src/main/java/br/net/air/configuracoes/service/EnderecoBairroService.java:33` | `this.repository.delete(entity.getId());` |
| `comercial-api/src/main/java/br/net/air/configuracoes/service/RegraSuspensaoService.java:29` | `public void delete(RegraSuspensao entity) {` |
| `comercial-api/src/main/java/br/net/air/configuracoes/service/RegraSuspensaoService.java:30` | `super.delete(entity);` |
| `comercial-api/src/main/java/br/net/air/configuracoes/service/TermoService.java:75` | `public void delete(Termo entity) {` |
| `comercial-api/src/main/java/br/net/air/configuracoes/service/TermoService.java:76` | `super.delete(entity);` |
| `comercial-api/src/main/java/br/net/air/configuracoes/service/VencimentoService.java:36` | `public void delete(Vencimento entity) {` |
| `comercial-api/src/main/java/br/net/air/configuracoes/service/VencimentoService.java:37` | `super.delete(entity);` |
| `comercial-api/src/main/java/br/net/air/financeiro/controller/CobrancaPontualController.java:59` | `service.delete(entity);` |
| `comercial-api/src/main/java/br/net/air/financeiro/controller/DescontoController.java:55` | `//        service.delete(entity);` |
| `comercial-api/src/main/java/br/net/air/financeiro/repository/DescontoRepository.java:21` | `@Query("SELECT SUM(d.desconto) FROM Desconto d " +` |
| `comercial-api/src/main/java/br/net/air/financeiro/service/DescontoService.java:26` | `public void delete(Desconto entity) {` |
| `comercial-api/src/main/java/br/net/air/notification/service/NotificationIntegracaoService.java:136` | `delete(url);` |
| `comercial-api/src/main/java/br/net/air/notification/service/NotificationIntegracaoService.java:222` | `private void delete(String url) {` |
| `comercial-api/src/main/java/br/net/air/notification/service/NotificationIntegracaoService.java:224` | `restTemplateAuthed.delete(url);` |
| `comercial-api/src/main/java/br/net/air/oauth/service/OauthIntegracaoService.java:66` | `@Value("${sql.update.cliente.oauth}")` |
| `comercial-api/src/main/java/br/net/air/oauth/service/OauthIntegracaoService.java:71` | `@Value("${oauth.user-delete.url}")` |
| `comercial-api/src/main/java/br/net/air/oauth/service/OauthIntegracaoService.java:294` | `List<NativeEntity> nes = nativeDB.select(sqlCustomerBrands, cliente.getId());` |
| `comercial-api/src/main/java/br/net/air/oauth/service/OauthIntegracaoService.java:328` | `restTemplate.delete(url, entity, body);` |
| `comercial-api/src/main/java/br/net/air/oauth/service/OauthIntegracaoService.java:409` | `HttpMethod.DELETE,` |
| `comercial-api/src/main/java/br/net/air/venda/controller/LeadController.java:176` | `service.delete(entity);` |
| `comercial-api/src/main/java/br/net/air/venda/controller/LeadObsController.java:31` | `//        service.delete(entity);` |
| `comercial-api/src/main/java/br/net/air/venda/repository/AnaliseCreditoAtributoRepository.java:13` | `@Query(value = " SELECT " +` |
| `comercial-api/src/main/java/br/net/air/venda/repository/AnaliseCreditoAtributoRepository.java:18` | `" FROM tbl_analise_credito_atributo taca " +` |
| `comercial-api/src/main/java/br/net/air/venda/repository/AnaliseCreditoRepository.java:20` | `@Query(value = " SELECT " +` |
| `comercial-api/src/main/java/br/net/air/venda/repository/AnaliseCreditoRepository.java:111` | `" FROM " +` |
| `comercial-api/src/main/java/br/net/air/venda/repository/AnaliseCreditoRepository.java:112` | `"     tbl_analise_credito ac inner join tbl_lead ld on ac.id_lead = ld.id  " +` |
| `comercial-api/src/main/java/br/net/air/venda/repository/AnaliseCreditoRestricaoRepository.java:13` | `@Query(value = " SELECT  " +` |
| `comercial-api/src/main/java/br/net/air/venda/repository/AnaliseCreditoRestricaoRepository.java:22` | `" FROM tbl_analise_credito_restricao tacr  " +` |
| `comercial-api/src/main/java/br/net/air/venda/repository/VendaRepository.java:35` | `value = "SELECT " +` |
| `comercial-api/src/main/java/br/net/air/venda/repository/VendaRepository.java:39` | `"FROM air_comercial.tbl_venda v " +` |
| `comercial-api/src/main/java/br/net/air/venda/repository/VendaRepository.java:40` | `"LEFT JOIN air_comercial.tbl_contrato c ON v.id_contrato = c.id " +` |
| `comercial-api/src/main/java/br/net/air/venda/repository/VendaRepository.java:41` | `"LEFT JOIN air_chamado.tbl_chd_chamado ch ON v.id_contrato = ch.codigo_contrato " +` |
| `comercial-api/src/main/java/br/net/air/venda/repository/VendaRepository.java:42` | `"LEFT JOIN air_chamado.tbl_os os ON ch.id = os.id_chamado " +` |
