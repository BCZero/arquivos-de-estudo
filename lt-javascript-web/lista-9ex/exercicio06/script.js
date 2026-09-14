const nomeCliente = prompt("Informe o nome do cliente:");
const opcao = Number(prompt(
  "Escolha um serviço:\n" +
  "1 - Instalação elétrica: R$ 150,00\n" +
  "2 - Manutenção hidráulica: R$ 120,00\n" +
  "3 - Configuração de internet: R$ 100,00\n" +
  "4 - Visita técnica: R$ 80,00"
));

let servico = "";
let valorNormal = 0;

switch (opcao) {
  case 1:
    servico = "Instalação elétrica";
    valorNormal = 150.00;
    break;
  case 2:
    servico = "Manutenção hidráulica";
    valorNormal = 120.00;
    break;
  case 3:
    servico = "Configuração de internet";
    valorNormal = 100.00;
    break;
  case 4:
    servico = "Visita técnica";
    valorNormal = 80.00;
    break;
  default:
    alert("Opção inválida. Nenhum preço foi calculado.");
}

if (valorNormal > 0) {
  const respostaUrgente = prompt("O atendimento é urgente? Responda S ou N:").toUpperCase();

  if (respostaUrgente !== "S" && respostaUrgente !== "N") {
    alert("Resposta inválida. Informe S ou N para o atendimento urgente.");
  } else {
    let acrescimo = 0;

    if (respostaUrgente === "S") {
      acrescimo = valorNormal * 0.30;
    }

    const valorTotal = valorNormal + acrescimo;

    alert(
      "Cliente: " + nomeCliente +
      "\nServiço: " + servico +
      "\nValor normal: R$ " + valorNormal.toFixed(2) +
      "\nAcréscimo de urgência: R$ " + acrescimo.toFixed(2) +
      "\nValor total: R$ " + valorTotal.toFixed(2)
    );
  }
}
