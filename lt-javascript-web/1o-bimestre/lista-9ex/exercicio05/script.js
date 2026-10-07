const tipoVeiculo = prompt("Informe o tipo do veículo: carro, motocicleta ou utilitário:").toLowerCase();
const horas = Number(prompt("Informe a quantidade de horas de permanência:"));
let tarifaPorHora = 0;
let categoriaValida = true;

switch (tipoVeiculo) {
  case "carro":
    tarifaPorHora = 8.00;
    break;
  case "motocicleta":
    tarifaPorHora = 4.00;
    break;
  case "utilitário":
  case "utilitario":
    tarifaPorHora = 12.00;
    break;
  default:
    categoriaValida = false;
}

if (!categoriaValida || horas <= 0) {
  alert("Dado inválido. Verifique o tipo do veículo e a quantidade de horas.");
} else {
  const valorSemDesconto = tarifaPorHora * horas;
  let desconto = 0;

  if (horas > 8) {
    desconto = valorSemDesconto * 0.15;
  }

  const valorFinal = valorSemDesconto - desconto;

  alert(
    "Categoria: " + tipoVeiculo +
    "\nPermanência: " + horas + " hora(s)" +
    "\nValor sem desconto: R$ " + valorSemDesconto.toFixed(2) +
    "\nDesconto: R$ " + desconto.toFixed(2) +
    "\nValor final: R$ " + valorFinal.toFixed(2)
  );
}
