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