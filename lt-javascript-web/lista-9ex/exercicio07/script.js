const nomeCliente = prompt("Informe o nome do cliente:");
const valorCompra = Number(prompt("Informe o valor dos produtos:"));
const regiao = prompt("Informe a região de entrega: Centro, Norte ou Sul:").toLowerCase();
const cupom = prompt("Informe o cupom ou deixe em branco:").toUpperCase();
const formaPagamento = prompt("Informe a forma de pagamento:").toUpperCase();

let frete = 0;
let regiaoAtendida = true;

switch (regiao) {
  case "centro":
    frete = 10.00;
    break;
  case "norte":
    frete = 20.00;
    break;
  case "sul":
    frete = 15.00;
    break;
  default:
    regiaoAtendida = false;
}

if (!regiaoAtendida) {
  alert("Região não atendida. O cálculo da compra foi encerrado.");
} else if (valorCompra <= 0) {
  alert("Valor da compra inválido. Informe um valor maior que zero.");
} else {
  let descontoCupom = 0;

  if (cupom === "ADS10" && valorCompra >= 100) {
    descontoCupom = valorCompra * 0.10;
  }

  const produtosAposCupom = valorCompra - descontoCupom;
  let descontoPix = 0;

  if (formaPagamento === "PIX") {
    descontoPix = produtosAposCupom * 0.05;
  }

  if (valorCompra >= 250) {
    frete = 0;
  }

  const valorFinal = produtosAposCupom - descontoPix + frete;

  alert(
    "Cliente: " + nomeCliente +
    "\nValor original dos produtos: R$ " + valorCompra.toFixed(2) +
    "\nDesconto do cupom: R$ " + descontoCupom.toFixed(2) +
    "\nDesconto do PIX: R$ " + descontoPix.toFixed(2) +
    "\nFrete: R$ " + frete.toFixed(2) +
    "\nValor final: R$ " + valorFinal.toFixed(2)
  );
}
