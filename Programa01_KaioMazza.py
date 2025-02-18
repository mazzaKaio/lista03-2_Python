"""
Escreva um programa que forneça um tipo de aplicação financeira adequado a um investidor a partir de 2 dados fornecidos: O grau de aceitação de risco e o valor a ser investido.
Deve ser lido no teclado na forma BX ou AL risco. Se for fornecido algo diferente disso, o programa deve mostrar uma mensagem indicando que foi fornecido um dado inválido.
Para o valor, deve ser um número real.
"""

grauRisco = input("Digite o grau de risco desejado ['BX' ou 'AL']: ").upper()
investimentoDesejado = float(input("Digite o valor que você deseja investir: "))

if grauRisco.__eq__("BX"):
    if investimentoDesejado < 1000.00:
        print("Recomendamos que você invista na POUPANÇA!")
    else:
        print("Recomendamos que você invista na RENDA FIXA!")

elif grauRisco.__eq__("AL"):
    if investimentoDesejado < 1000.00:
        print("Recomendamos que você invista em BITCOINS!")
    else:
        print("Recomendamos que você invista em AÇÕES!")

else:
    print("Grau de risco inválido!")