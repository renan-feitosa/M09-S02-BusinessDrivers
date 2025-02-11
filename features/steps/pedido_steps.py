from behave import given, when, then
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@given('que o "Restaurante Top Sabor" está autenticado')
def step_restaurante_autenticado(context):
    context.restaurante = {
        "nome": "Restaurante Top Sabor",
        "id": 1
    }
    logging.info('Restaurante "Top Sabor" autenticado.')

@when('o cliente solicitar um pedido do restaurante "Restaurante Top Sabor" com os itens "{itens}"')
def step_solicitar_pedido_cliente(context, itens):
    lista_itens = [item.strip() for item in itens.split(',')]
    context.pedido = {
        "restaurante": "Restaurante Top Sabor",
        "itens": lista_itens,
        "status": "solicitado",
        "tempo_entrega_estimado": None
    }
    logging.info(f"Pedido solicitado para o restaurante 'Top Sabor' com itens: {lista_itens}")

@when('a entrega é designada a um entregador')
def step_designa_entrega_entregador(context):
    context.pedido["entregador"] = "Entregador João"
    logging.info(f"Entrega designada ao entregador {context.pedido['entregador']}")

@when('o entregador confirma a entrega')
def step_confirma_entrega_entregador(context):
    time.sleep(1)
    context.pedido["status"] = "entregue"
    logging.info("Entregador confirmou a entrega.")

@then('o sistema deverá confirmar o pedido B2B como concluído')
def step_confirmar_pedido_b2b(context):
    assert context.pedido["status"] == "entregue", "O pedido B2B não foi concluído com sucesso."
    logging.info("Pedido B2B concluído com sucesso.")

@when('o tempo de entrega estimado é de "{tempo_estimado}"')
def step_tempo_entrega_estimado(context, tempo_estimado):
    context.pedido["tempo_entrega_estimado"] = tempo_estimado
    logging.info(f"Tempo estimado de entrega: {tempo_estimado}")

@when('o pedido é entregue após "{tempo_real}"')
def step_tempo_entrega_real(context, tempo_real):
    context.pedido["tempo_entrega_real"] = tempo_real
    logging.info(f"Tempo real de entrega: {tempo_real}")
    context.pedido["status"] = "entregue"

@then('o sistema deverá registrar o pedido como fora do prazo de entrega')
def step_registrar_fora_do_prazo(context):
    tempo_estimado = int(context.pedido["tempo_entrega_estimado"].split()[0])  # Converte os minutos estimados para int
    tempo_real = int(context.pedido["tempo_entrega_real"].split()[0])  # Converte os tempo real de entrega para int

    if tempo_real > tempo_estimado:
        context.pedido["fora_do_prazo"] = True
        logging.info("Pedido registrado como fora do prazo de entrega.")
    else:
        context.pedido["fora_do_prazo"] = False
        logging.info("Pedido entregue dentro do prazo.")

@then('o percentual de pedidos fora do prazo deverá ser recalculado')
def step_recalcular_percentual_pedidos(context):

    if not hasattr(context, "historico_pedidos"): # Se não existir o histórico de pedidos, cria uma lista vazia
        context.historico_pedidos = []

    context.historico_pedidos.append(context.pedido)

    total_pedidos = len(context.historico_pedidos)
    pedidos_fora_do_prazo = sum(1 for pedido in context.historico_pedidos if pedido.get("fora_do_prazo"))

    percentual_fora_do_prazo = (pedidos_fora_do_prazo / total_pedidos) * 100 if total_pedidos > 0 else 0
    context.percentual_fora_do_prazo = percentual_fora_do_prazo

    logging.info(f"Percentual de pedidos fora do prazo atualizado: {percentual_fora_do_prazo:.2f}%")