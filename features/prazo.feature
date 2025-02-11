Feature: Monitoramento de Prazo de Entrega

  Scenario: % de pedidos que passam do prazo de entrega
    Given que o "Restaurante Top Sabor" está autenticado
    When o cliente solicitar um pedido do restaurante "Restaurante Top Sabor" com os itens "Calabresa Acebolada, Frango à Parmegiana"
    And a entrega é designada a um entregador
    When o tempo de entrega estimado é de "45 minutos"
    And o pedido é entregue após "60 minutos"
    Then o sistema deverá registrar o pedido como fora do prazo de entrega
    And o percentual de pedidos fora do prazo deverá ser recalculado