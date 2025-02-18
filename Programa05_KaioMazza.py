"""
No comércio o conceito de margem bruta é uma porcentagem que é aplicada ao preço de custo para se obter o preço de venda. 
Uma loja tem como política comercial, aplicar uma margem bruta de 45%, quando o preço de custo é <= R$100,00. Se o produto custa mais que isso, a margem de lucro é 35%.
Escreva um programa que leia o preço do produto e mostre seu preço de venda. 
"""

precoProduto = float(input("Digite o preço bruto do produto: "))

if precoProduto <= 100:
    margemBruta = 45/100
else:
    margemBruta = 35/100

precoVenda = precoProduto + (precoProduto * margemBruta)
print("\nO preço do produto é: {}\nO preço de venda segunda a margem bruta é: {:1}".format(precoProduto, precoVenda))

print("\nFim do programa!")
print("Kaio Gomes do Nascimento Mazza")