# M09-S02-BusinessDrivers

```
workspace "Rappi B2B Delivery" "Mapa dos Business Drivers para pedidos B2B no app dos entregadores." {

    model {
        loja = person "Loja"
        rappi = softwareSystem "Rappi"
        entregador = person "Entregador"
        cliente = person "Cliente"

        loja -> rappi "Envia pedido"
        rappi -> entregador "Designa entrega"
        entregador -> cliente "Entrega pedido"
        rappi -> loja "Confirma status do pedido"
        cliente -> rappi "Confirma entrega"
    }
    
}

```

<!-- Imagem do diagrama -->

![Diagrama de Business Drivers](./images/structurizr-SystemLandscape-001.png)

- Estratégia e massa de testes: Usar Gherkin Given-When-Then (GWT) ou Jmeter
- Codificação como documentação de testes: Usar Gherkin Given-When-Then (GWT) ou Jmeter
