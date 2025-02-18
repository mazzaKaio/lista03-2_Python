"""
Nas eleições municipais, os munícipios com 200.000 eleitores ou mais, tem segundo turno caso o 1º colocado não tenha mais que 50% dos votos.
Escreva um programa que leia: O nome do munícipio, a quantidade de eleitores e a quantidade de votos do candidato mais votado. 
Informe se haverá segundo turno ou não.
"""

nomeMunicipio = input("Digite o nome do munícipio: ")
qntEleitores = int(input("Digite a quantidade de eleitores: "))
qntVotos = int(input("Digite a quantidade de votos do candidato mais votado: "))

if qntEleitores >= 200000:
    if qntVotos > (qntEleitores*(50/100)):
        print("Não terá segundo terno no munícipio de '{}'!".format(nomeMunicipio))
    else:
        print("Terá segundo turno no munícipio de '{}'!".format(nomeMunicipio))

print("\nFim do programa!")
print("Kaio Gomes do Nascimento Mazza")