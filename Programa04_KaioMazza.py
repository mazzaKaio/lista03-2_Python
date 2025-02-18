"""
No SENAILÂNDIA mulheres e homens podem servir o exército do país. O serviço é opcional e é muito comum que as pessoas se apresentem para o serviço em algum momento da vida.
 Existe uma única restrição para o ingresso, que é a idade da pessoa: 
•	Para mulheres, a idade aceita é entre 21 e 34 anos (>=21 e <=34)
•	Para homens, a idade aceita é entre 18 e 39 anos (>=18 e <=39)
Escreva um programa que leia 3 dados de entrada: Nome da pessoa, idade e gênero. Informe se a pessoa será aceita ou não para o serviço.
	OBS: Para o gênero deve ser lido somente um caractere, que pode ser: ‘f’ ou ‘F’, ‘m’ ou ‘M’. Qualquer coisa diferente, deve ser informado como inválido.
"""

nomeUsuario = input("Digite seu nome: ")
idadeUsuario = int(input("Digite sua idade: "))
generoUsuario = input("Digite seu gênero [M/F]: ").upper()

if generoUsuario.__eq__("M"):
    if idadeUsuario >= 18 and idadeUsuario <= 39:
        isAceito = "ACEITO!"
    else:
        isAceito = "NÂO ACEITO!"

elif generoUsuario.__eq__("F"):
    if idadeUsuario >= 21 and idadeUsuario <= 34:
        isAceito = "ACEITO!"
    else:
        isAceito = "NÂO ACEITO!"
else:
    print("Gênero inserido não aceito!")

print("\nNome informado: {}\nIdade informada: {}\nGênero informado: {}\nAceito ao exército: {}".format(nomeUsuario, idadeUsuario, generoUsuario, isAceito))

print("\nFim do programa!")
print("Kaio Gomes do Nascimento Mazza")