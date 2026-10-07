#Script Python para verificação de idade

#O usuário insere pelo teclado a sua idade, que é convertida para número inteiro
idade = int(input("Digite sua idade: "))

#O sistema realiza uma série de comparações, encadeadas, uma condição por vez
#O sistema testa cada condição, que quando é False, segue para a próxima, até encerrar o código
if idade < 12:
    print("Você ainda é criança")
elif 12 <= idade <= 17:
    print("Adolescente")
elif 18 <= idade <= 59:
    print("Adulto")
else: 
    print("Idoso")
print("Fim do código")