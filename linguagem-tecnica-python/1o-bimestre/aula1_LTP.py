#print(123)

#print(123, 45)

#print(123, 45, sep='-')

#print(123, 45, sep='-', end="!")

#print(123, 45, 96, sep=', ', end=".")

#Técnica de escape das aspas: aspas simples + aspas duplas | ou inverter a ordem das aspas
#print('"Faculdade Senac"')

#print("'Faculdade Senac'")

#print("Faculdade\'Senac\'")

#print(type("senac"))

#print(type(100))

#print(type(100.25))

#print(10==11)

# Quando tiver o type, leia de dentro dos parêntes ao lado de type para fora do type = resolva o que type estiver 'abraçando' e só então classifique o tipo de dado
# print(type("True"))

#Esse exemplo abaixo é bem relevante: primeiro resolva 2 <= 3, que é um bool
# print(type(2 <= 3))

#coerção de tipo
#print(1+1)
#print('a'+'b')

#Repare no código abaixo: 
#print(int('1'), type (int('1')))


#print(float('1'), type(float('1')))

#print(bool(''))

#print(bool(' '))

#Concatenação de resultados
#print(str(11) + 'b')


"""nome= "Maria Francisca"
somaValores= 2 + 2
idade= 30
isJovem = idade < 30
salario = 234.1
print("Nome: ", nome, "Idade: ", idade, "Salário: ", salario)
print("É jovem? ", isJovem)"""


# Qualquer número com divisão com módulo terá resto igual a zero ou um
#modulo = 9 % 2
#print("Módulo = ", modulo)

"""out2= "A" * 10
print(out2)
print(type(out2))"""

"""nome= "Maria Francisca"
altura = 1.60
peso = 55
imc = peso / altura**2

linha= f'{nome} tem {altura:.1f} de altura, pesa {peso} quilos e seu IMC é {imc:.4f}'
print(linha)"""

matriculado = input("Você está matriculado? (true/false:): ")
matriculado= matriculado.strip().lower() == 'true'
print(matriculado)