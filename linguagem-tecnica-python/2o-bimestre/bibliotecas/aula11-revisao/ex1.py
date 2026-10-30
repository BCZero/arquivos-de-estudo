medicoes = [70, 85, 96]
servidor = {"nome": "Servidor A", "medicoes": medicoes}

def media(valores):
    return sum(valores) / len(valores)

resultado = media(servidor["medicoes"])
print(resultado) # 60.0

valores = []
for numero in medicoes:
    valores.append(numero)
    
if media(valores) > 80:
    print("Acima do limite")
else:
    print("Dentro do limite")