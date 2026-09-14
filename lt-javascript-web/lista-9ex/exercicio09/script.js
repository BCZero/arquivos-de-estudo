let confirmar = "N";

do {

    // ======================================
    // ENTRADA DE DADOS
    // ======================================

    let nome = prompt("Nome do cliente:");

    let idade = Number(
        prompt("Idade do motorista:")
    );

    let tipoVeiculo = Number(
        prompt(
            "Tipo de veículo:\n" +
            "1 - Econômico\n" +
            "2 - Sedan\n" +
            "3 - SUV\n" +
            "4 - Executivo"
        )
    );

    let diarias = Number(
        prompt("Quantidade de diárias:")
    );

    let kmPrevista = Number(
        prompt("Quilometragem prevista:")
    );

    let seguro = prompt(
        "Deseja contratar seguro? (S/N)"
    ).toUpperCase();

    let cupom = prompt(
        "Cupom promocional:"
    ).toUpperCase();

    let pagamento = Number(
        prompt(
            "Forma de pagamento:\n" +
            "1 - PIX\n" +
            "2 - Débito\n" +
            "3 - Crédito"
        )
    );

    // ======================================
    // VEÍCULO
    // ======================================

    let nomeVeiculo = "";
    let valorDiaria = 0;
    let valorSeguroDiaria = 0;
    let valorKmExcedente = 0;

    switch (tipoVeiculo) {

        case 1:
            nomeVeiculo = "Econômico";
            valorDiaria = 120;
            valorSeguroDiaria = 25;
            valorKmExcedente = 0.80;
            break;

        case 2:
            nomeVeiculo = "Sedan";
            valorDiaria = 180;
            valorSeguroDiaria = 35;
            valorKmExcedente = 1.00;
            break;

        case 3:
            nomeVeiculo = "SUV";
            valorDiaria = 260;
            valorSeguroDiaria = 45;
            valorKmExcedente = 1.30;
            break;

        case 4:
            nomeVeiculo = "Executivo";
            valorDiaria = 350;
            valorSeguroDiaria = 60;
            valorKmExcedente = 1.60;
            break;
    }

    // ======================================
    // VALIDAÇÕES
    // ======================================

    if (idade < 21) {

        alert(
            "Locação recusada.\n" +
            "Motorista deve ter 21 anos ou mais."
        );

        continue;
    }

    if (diarias <= 0) {

        alert(
            "Quantidade de diárias inválida."
        );

        continue;
    }

    if (kmPrevista <= 0) {

        alert(
            "Quilometragem inválida."
        );

        continue;
    }

    if (valorDiaria === 0) {

        alert(
            "Tipo de veículo inválido."
        );

        continue;
    }

    // ======================================
    // CÁLCULOS
    // ======================================

    let valorOriginalDiarias =
        valorDiaria * diarias;

    // DESCONTO POR DIÁRIAS

    let percentualDesconto = 0;

    if (diarias >= 4 && diarias <= 6) {
        percentualDesconto = 5;
    }
    else if (diarias >= 7 && diarias <= 10) {
        percentualDesconto = 10;
    }
    else if (diarias > 10) {
        percentualDesconto = 15;
    }

    let descontoDiarias =
        valorOriginalDiarias *
        percentualDesconto / 100;

    let valorDiariasComDesconto =
        valorOriginalDiarias -
        descontoDiarias;

    // CUPOM

    let descontoCupom = 0;
    let cupomValido = false;

    if (
        cupom === "ADS15" &&
        diarias >= 5 &&
        valorOriginalDiarias >= 900
    ) {

        descontoCupom =
            valorDiariasComDesconto *
            0.15;

        valorDiariasComDesconto -=
            descontoCupom;

        cupomValido = true;
    }

    // MOTORISTA JOVEM

    let taxaJovem = 0;

    if (
        idade >= 21 &&
        idade <= 24
    ) {

        taxaJovem =
            diarias * 40;
    }

    // SEGURO

    let valorSeguro = 0;

    if (seguro === "S") {

        valorSeguro =
            valorSeguroDiaria *
            diarias;
    }

    // KM EXCEDENTE

    let kmIncluidos =
        diarias * 150;

    let kmExcedidos = 0;

    if (kmPrevista > kmIncluidos) {

        kmExcedidos =
            kmPrevista -
            kmIncluidos;
    }

    let valorExcedente =
        kmExcedidos *
        valorKmExcedente;

    // SUBTOTAL

    let subtotal =
        valorDiariasComDesconto +
        taxaJovem +
        valorSeguro +
        valorExcedente;

    // PAGAMENTO

    let nomePagamento = "";
    let ajustePagamento = 0;

    switch (pagamento) {

        case 1:

            nomePagamento = "PIX";

            ajustePagamento =
                subtotal * 0.05;

            subtotal -=
                ajustePagamento;

            break;

        case 2:

            nomePagamento =
                "Débito";

            break;

        case 3:

            nomePagamento =
                "Crédito";

            ajustePagamento =
                subtotal * 0.03;

            subtotal +=
                ajustePagamento;

            break;

        default:

            nomePagamento =
                "Inválido";
    }

    let valorFinal = subtotal;

    // ======================================
    // PRÉVIA DA RESERVA
    // ======================================

    let resumo =

        "========== RESUMO ==========\n\n" +

        "Cliente: " + nome + "\n" +
        "Idade: " + idade + "\n" +
        "Veículo: " + nomeVeiculo + "\n" +
        "Diárias: " + diarias + "\n" +
        "KM Prevista: " + kmPrevista + "\n" +
        "Seguro: " + seguro + "\n" +
        "Cupom: " + cupom + "\n" +
        "Pagamento: " + nomePagamento + "\n\n" +

        "Valor Original: R$ " +
        valorOriginalDiarias.toFixed(2) +
        "\n" +

        "Desconto Diárias: R$ " +
        descontoDiarias.toFixed(2) +
        "\n" +

        "Desconto Cupom: R$ " +
        descontoCupom.toFixed(2) +
        "\n" +

        "Taxa Jovem: R$ " +
        taxaJovem.toFixed(2) +
        "\n" +

        "Seguro: R$ " +
        valorSeguro.toFixed(2) +
        "\n" +

        "KM Excedidos: " +
        kmExcedidos + "\n" +

        "Valor Excedente: R$ " +
        valorExcedente.toFixed(2) +
        "\n\n" +

        "VALOR FINAL: R$ " +
        valorFinal.toFixed(2);

    alert(resumo);

    // ======================================
    // CONFIRMAÇÃO
    // ======================================

    confirmar = prompt(
        resumo +
        "\n\nConfirma que está tudo certo? (S/N)"
    ).toUpperCase();

    // ======================================
    // RELATÓRIO FINAL
    // ======================================

    if (confirmar === "S") {

        document.write(
            "<h1>Reserva Confirmada</h1>"
        );

        document.write(
            "<pre>" +
            resumo +
            "</pre>"
        );

        document.write(
            "<h2>Reserva realizada com sucesso!</h2>"
        );

        break;
    }

    alert(
        "Voltando ao início para uma nova locação..."
    );

}
while (confirmar !== "S");