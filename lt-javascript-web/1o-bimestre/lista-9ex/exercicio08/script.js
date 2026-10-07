const nomeHospede = prompt("Informe o nome do hóspede:");
const tipoQuarto = Number(prompt(
  "Escolha o tipo de quarto:\n" +
  "1 - Standard: R$ 180,00 por diária\n" +
  "2 - Família: R$ 280,00 por diária\n" +
  "3 - Suíte: R$ 420,00 por diária"
));
const quantidadeDiarias = Number(prompt("Informe a quantidade de diárias:"));
const quantidadeHospedes = Number(prompt("Informe a quantidade de hóspedes:"));

let nomeQuarto = "";
let valorDiaria = 0;
let capacidade = 0;

switch (tipoQuarto) {
  case 1:
    nomeQuarto = "Standard";
    valorDiaria = 180.00;
    capacidade = 2;
    break;
  case 2:
    nomeQuarto = "Família";
    valorDiaria = 280.00;
    capacidade = 4;
    break;
  case 3:
    nomeQuarto = "Suíte";
    valorDiaria = 420.00;
    capacidade = 2;
    break;
  default:
    alert("Opção de quarto inválida.");
}

if (valorDiaria > 0) {
  if (quantidadeDiarias <= 0 || quantidadeHospedes <= 0) {
    alert("Reserva recusada. A quantidade de diárias e de hóspedes deve ser maior que zero.");
  } else if (quantidadeHospedes > capacidade) {
    alert("Reserva recusada. O quarto " + nomeQuarto + " acomoda no máximo " + capacidade + " hóspede(s).");
  } else {
    const respostaCafe = prompt("Deseja incluir café da manhã? Responda S ou N:").toUpperCase();
    const formaPagamento = prompt("Informe a forma de pagamento: à vista ou outra:").toLowerCase();

    if (respostaCafe !== "S" && respostaCafe !== "N") {
      alert("Resposta inválida para o café da manhã. Informe S ou N.");
    } else {
      const valorOriginalDiarias = valorDiaria * quantidadeDiarias;
      let descontoDiarias = 0;

      if (quantidadeDiarias >= 7) {
        descontoDiarias = valorOriginalDiarias * 0.12;
      }

      const valorDiarias = valorOriginalDiarias - descontoDiarias;
      let valorCafe = 0;

      if (respostaCafe === "S") {
        valorCafe = 35.00 * quantidadeHospedes * quantidadeDiarias;
      }

      const subtotal = valorDiarias + valorCafe;
      let descontoAVista = 0;

      if (formaPagamento === "à vista" || formaPagamento === "a vista") {
        descontoAVista = subtotal * 0.05;
      }

      const valorFinal = subtotal - descontoAVista;

      alert(
        "Hóspede: " + nomeHospede +
        "\nTipo de quarto: " + nomeQuarto +
        "\nHóspedes: " + quantidadeHospedes +
        "\nDiárias: " + quantidadeDiarias +
        "\nValor original das diárias: R$ " + valorOriginalDiarias.toFixed(2) +
        "\nDesconto nas diárias: R$ " + descontoDiarias.toFixed(2) +
        "\nValor das diárias após desconto: R$ " + valorDiarias.toFixed(2) +
        "\nCafé da manhã: R$ " + valorCafe.toFixed(2) +
        "\nDesconto à vista: R$ " + descontoAVista.toFixed(2) +
        "\nValor final: R$ " + valorFinal.toFixed(2)
      );
    }
  }
}
