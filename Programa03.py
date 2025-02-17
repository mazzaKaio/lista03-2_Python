"""
Uma empresa financeira consegue empréstimo a pessoas físicas, quando o valor da parcela é menor que 8% do salário da pessoa. Escreva um programa que leia 2 números reais: 
O valor do salário e o valor da parcela.
E informe se o empréstimo será concedido ou não.
"""

salarioUsuario = float(input("Digite seu salário: "))
valorParcela = float(input("Digite o valor da parcela: "))

porcentagemSalario = salarioUsuario * (8/100)

if valorParcela < porcentagemSalario:
    print("Empréstimo concedido!")
else:
    print("Empréstimo não concedido!")