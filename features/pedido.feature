Feature: Pedido B2B

  Scenario: Taxa de pedidos B2B concluídos com sucesso
    Given que o "Restaurante Top Sabor" está autenticado
    When o cliente solicitar um pedido do restaurante "Restaurante Top Sabor" com os itens "Calabresa Acebolada, Frango à Parmegiana"
    And a entrega é designada a um entregador
    And o entregador confirma a entrega
    Then o sistema deverá confirmar o pedido B2B como concluído