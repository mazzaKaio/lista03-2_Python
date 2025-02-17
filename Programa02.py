"""
Escreva um programa para exibir na tela o nome e a categoria de um lutador, o programa deve ler uma string para o nome e um número real para o peso.
"""

nomeLutador = input("Digite o nome do lutador: ")
pesoLutador = float(input("Digite o peso do lutador: "))

if pesoLutador < 52:
    categoria = "invalido"

elif pesoLutador >= 52 and pesoLutador < 65:
    categoria = "Peso Pena"

elif pesoLutador >= 65 and pesoLutador < 72:
    categoria = "Peso Leve"

elif pesoLutador >= 72 and pesoLutador < 79:
    categoria = "Peso Ligeiro"

elif pesoLutador >= 79 and pesoLutador < 86:
    categoria = "Peso Meio-Médio"

elif pesoLutador >= 52 and pesoLutador < 65:
    categoria = "Peso Médio"

elif pesoLutador >= 52 and pesoLutador < 65:
    categoria = "Peso Meio-Pesado"

else:
    categoria = "Peso Pesado"

print("\nLutador: {}\nCom {} kilos!\nNa sua categoria de: {}".format(nomeLutador, pesoLutador, categoria))