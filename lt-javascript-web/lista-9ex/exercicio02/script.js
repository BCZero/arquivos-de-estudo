const nomePassageiro = prompt("Informe o nome do passageiro:");
const distancia = Number(prompt("Informe a distância da viagem em quilômetros:"));

if (distancia <= 0) {
  alert("Distância inválida. Informe um valor maior que zero.");
} else {
  const tarifaInicial = 6.00;
  const valorPorQuilometro = 2.80;
  const valorCalculado = tarifaInicial + distancia * valorPorQuilometro;
  let desconto = 0;

  if (distancia > 20) {
    desconto = valorCalculado * 0.10;
  }

  const valorFinal = valorCalculado - desconto;
  let informacaoDesconto = "Desconto não aplicado";

  if (desconto > 0) {
    informacaoDesconto = "Desconto de 10% aplicado: R$ " + desconto.toFixed(2);
  }

  alert(
    "Passageiro: " + nomePassageiro +
    "\nDistância: " + distancia + " km" +
    "\nValor calculado: R$ " + valorCalculado.toFixed(2) +
    "\n" + informacaoDesconto +
    "\nValor final: R$ " + valorFinal.toFixed(2)
  );
}
