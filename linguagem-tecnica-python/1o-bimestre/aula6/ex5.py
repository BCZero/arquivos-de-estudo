maiorNota=0
menorNota=0
qtdReprovado=0
qtAprovado=0
for i in range(5):
    nota= float(input(f"Digite a nota {i+1}:"))
    if i==0:#fcondição da primeira rodada
        maiorNota=nota
        menorNota=nota
    else:
        if nota > maiorNota:
            maiorNota= nota
       
        if nota < menorNota:
            menorNota= nota
   
    #estou fazendo fora do if e  do else
    if nota >=6:
        qtAprovado+=1
    else:
        qtdReprovado+=1


print ("=============================================")
print (f"Quantidade de aprovado(s):{qtAprovado}")
print (f"Quantidade de reprovado(s):{qtdReprovado}")
print (f"Maior Nota:{maiorNota}")
print (f"Maior Nota:{menorNota}")
print ("=============================================")