const nomeEstudante = prompt("Informe o nome do estudante:");
const nota1 = Number(prompt("Informe a primeira nota:"));
const nota2 = Number(prompt("Informe a segunda nota:"));
const frequencia = Number(prompt("Informe o percentual de frequência:"));

if (nota1 < 0 || nota1 > 10 || nota2 < 0 || nota2 > 10 || frequencia < 0 || frequencia > 100) {
  alert("Dados inválidos. As notas devem estar entre 0 e 10 e a frequência entre 0% e 100%.");
} else {
  const media = (nota1 + nota2) / 2;
  let situacao;

  if (frequencia < 75) {
    situacao = "Reprovado por falta";
  } else if (media >= 7) {
    situacao = "Aprovado";
  } else if (media >= 5) {
    situacao = "Recuperação";
  } else {
    situacao = "Reprovado por nota";
  }

  alert(
    "Estudante: " + nomeEstudante +
    "\nMédia: " + media.toFixed(2) +
    "\nFrequência: " + frequencia.toFixed(1) + "%" +
    "\nSituação: " + situacao
  );
}
