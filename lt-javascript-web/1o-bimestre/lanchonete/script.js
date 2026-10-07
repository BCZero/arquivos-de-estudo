/* início de seção de comentário

let tentativa= 1;

while (tentativa <=10) {
    if (tentativa % 2==1) {
        alert("O número" + tentativa + "é ímpar!");
    }
    tentativa++;
}//fim do while 
// 

fim de seção de comentário */

/*let tentativa= 1;

let nome= 'Mariana';

alert(nome.length);

let senha = prompt("Digite uma senha com 8 caracteres: ");

while (senha.length != 8) {
    alert("A senha deve possuir exatamente 8 caracteres");
    senha = prompt("Digite uma senha de 8 caracteres")
}

alert("Senha cadastrada com sucesso") */

/* início do trecho comentado

let opcao;
let saldo= 0;
let nome = "Maria";

do{

    opcao = Number(prompt("========Menu========\n"+
        "1 - Ver Saldo\n"+
        "2 - Fazer Depósito\n"+
        "3 - Sair" 
    ));

    if (opcao==1) {
        alert("O Saldo de" + nome + "é " + saldo);
    }

    else if(opcao==2)
    {
        let valor=Number(prompt("Digite o valor do depósito: "))
        while(valor < 1){
            valor=Number(prompt("Digite um valor válido: "))
        }
        saldo = saldo + valor;
    }//fim do else if
    else if(opcao!=3) {
        alert("Opção inválida!")
    }//fim do else if
} while(opcao!=0); //fim do menu

alert("Programa encerrando...");

fim do trecho comentado */

/* 

let qtProdutos = Number(prompt("Informe a quantidade de produtos: "));

while (qtProdutos <1) {
    qtProdutos = Number(prompt("Informe a quantidade de produtos: "));
    }
    totalValor=0;

    for(let i=1; i <= qtProdutos; i++){
        preco= Number(prompt("Informe o preço do produto" + i + ":"));

        while(preco < 0) {
            preco = Number(prompt("Preço inválido! Informe um valor maior ou igual a zero: "));
            }

        totalValor= totalValor + preco;

    }//fim do for

    alert("O valor total é: " + totalValor)

    */


let produtos = Number(prompt("Digite quantos produtos serão comprados: "));
totalValor = 0

while(produtos < 1) {
    alert("A quantidade informada é inválida! Digite um valor acima de um.")
}

    for(let i=1; i <= produtos; i++){
        preco = Number(prompt("Informe o preço do produto" + i + ":"));

        while(preco < 0) {
            preco = Number(prompt("Preço inválido! Informe um valor maior ou igual a zero: "));
            }

        totalValor= totalValor + preco;

            }//fim do for

    alert("O valor total é: " + totalValor)