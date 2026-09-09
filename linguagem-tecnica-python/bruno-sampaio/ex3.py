#Script Python Teste de número Positivo, Negativo ou Zero

#O usuário insere um valor numérico, que é convertido para inteiro
numero = int(input("Digite um número inteiro: "))

#São testadas as condiçoes a seguir:
if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("O número informado é zero!")
print("Fim do código")