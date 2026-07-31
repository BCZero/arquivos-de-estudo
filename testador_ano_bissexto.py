ano_escolhido = int(input("Descubra se um ano é bissexto. Digite um ano do calendário gregoriano: "))

if ano_escolhido % 4 == 0 and ano_escolhido % 100 != 0:
    print("O ano escolhido é bissexto")
    
elif ano_escolhido % 400 == 0:
    print("O ano escolhido é bissexto")

else:
    print("O ano escolhido não é bissexto.")

print("Fim do programa")    