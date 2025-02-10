// features/steps/steps_b2b.js
const { Given, When, Then } = require('@cucumber/cucumber');
const assert = require('assert');

let metrics = {};
let order = {};

Given('que o sistema possui {int} pedidos B2B processados e {int} foram concluídos com sucesso', function (totalPedidos, pedidosSucesso) {
    metrics = {
        totalPedidos,
        pedidosSucesso,
        taxaSucesso: 0
    };
    console.log(`Total de pedidos: ${totalPedidos}, Pedidos com sucesso: ${pedidosSucesso}`);
});

When('a taxa de sucesso é calculada', function () {
    const { totalPedidos, pedidosSucesso } = metrics;
    metrics.taxaSucesso = totalPedidos > 0 ? (pedidosSucesso / totalPedidos) * 100 : 0;
    console.log(`Taxa de sucesso calculada: ${metrics.taxaSucesso}%`);
});

Then('a taxa de sucesso deve ser maior ou igual a {float}%', function (taxaEsperada) {
    assert(metrics.taxaSucesso >= taxaEsperada, `Taxa de sucesso esperada: ${taxaEsperada}%, obtida: ${metrics.taxaSucesso}%`);
    console.log("A taxa de sucesso atende aos critérios esperados.");
});

Given('que um pedido foi criado com prazo de entrega de {int} minutos', function (tempoEstimado) {
    order = {
        status: "em andamento",
        tempoEstimado,
        tempoReal: null
    };
    console.log(`Pedido criado com prazo estimado de ${tempoEstimado} minutos.`);
});

When('o pedido é entregue após {int} minutos', function (tempoReal) {
    order.tempoReal = tempoReal;
    console.log(`Pedido entregue em ${tempoReal} minutos.`);
});

Then('o pedido deve ser classificado como {string}', function (statusEsperado) {
    const { tempoReal, tempoEstimado } = order;
    order.status = tempoReal <= tempoEstimado ? "pontual" : "atrasado";

    assert.strictEqual(order.status, statusEsperado, `Status esperado: ${statusEsperado}, obtido: ${order.status}`);
    console.log(`Status do pedido verificado: ${order.status}.`);
});