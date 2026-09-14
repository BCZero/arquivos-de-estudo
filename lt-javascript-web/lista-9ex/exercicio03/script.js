const nomePaciente = prompt("Informe o nome do paciente:");
const idade = Number(prompt("Informe a idade do paciente:"));
const estaGravida = prompt("A paciente está grávida? Responda S ou N:").toUpperCase();
const possuiDeficiencia = prompt("O paciente possui alguma deficiência? Responda S ou N:").toUpperCase();

if (idade < 0 || (estaGravida !== "S" && estaGravida !== "N") || (possuiDeficiencia !== "S" && possuiDeficiencia !== "N")) {
  alert("Dados inválidos. Verifique a idade e responda S ou N às perguntas.");
} else {
  let tipoAtendimento = "Atendimento comum";

  if (idade >= 60 || estaGravida === "S" || possuiDeficiencia === "S") {
    tipoAtendimento = "Atendimento prioritário";
  }

  alert(
    "Paciente: " + nomePaciente +
    "\nIdade: " + idade + " anos" +
    "\nClassificação: " + tipoAtendimento
  );
}
