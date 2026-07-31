def converter_real_para_dolar(real, dolar_hoje):

    valor_em_dolares = real / dolar_hoje

    return valor_em_dolares

real = float(input("Digite o valor em reais para ser convertido: R$ "))
dolar_hoje = float(input("Digite a cotação dolar hoje: R$ ")) 

conversao = converter_real_para_dolar(real, dolar_hoje)


print(
    f"R$ {real:.2f} equivalem a US$ {conversao:.2f}, "
    f"considerando a cotação de R$ {dolar_hoje:.2f}"
    )