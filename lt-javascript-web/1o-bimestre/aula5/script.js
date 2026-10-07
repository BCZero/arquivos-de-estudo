let nomes = ["Frederico", "Josimar", "Pedro"];

let nome = prompt("Digite um nome para acrescentar à lista: ");
nomes.push(nome); //adiciona o nome informado pelo usuário

let consulta = prompt("Digite um nome para consultar se existe na lista: ");

if (nomes.includes(consulta)) {
    alert(consulta)
}

alert("Os nomes da lista são"+" "+nomes);

alert("Tamanho da estrutura de dados: " +nomes.length);