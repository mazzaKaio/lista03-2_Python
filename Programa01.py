grauRisco = input("Digite o grau de risco desejado ['BX' ou 'AL']: ").casefold()
if grauRisco != 'BX' or 'AL':
    print("Grau de risco não identificado!")

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