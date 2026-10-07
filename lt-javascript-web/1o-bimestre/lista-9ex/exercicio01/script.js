const nomeLanche = prompt("Informe o nome do lanche:");
const precoUnitario = Number(prompt("Informe o preço unitário do lanche:"));
const quantidade = Number(prompt("Informe a quantidade desejada:"));

if (precoUnitario <= 0 || quantidade <= 0) {
  alert("Dados inválidos. O preço e a quantidade devem ser maiores que zero.");
} else {
  const subtotal = precoUnitario * quantidade;
  let embalagem = 0;

  if (quantidade < 3) {
    embalagem = 2.50;
  }

  const valorFinal = subtotal + embalagem;

  alert(
    "Lanche: " + nomeLanche +
    "\nQuantidade: " + quantidade +
    "\nSubtotal: R$ " + subtotal.toFixed(2) +
    "\nEmbalagem: R$ " + embalagem.toFixed(2) +
    "\nValor final: R$ " + valorFinal.toFixed(2)
  );
}
