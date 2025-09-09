nome = input("Digite o nome do aluno: ")
altura = float(input("Digite a altura do aluno: "))
peso = float(input("Digite o peso do aluno: ")) 

imc = peso / (altura ** peso)


if altura >= 162:
    print("Altura média")
elif peso >= 65:
    print("Na média, tudo bem em manter")
elif peso <= 50:
    print("Perto do mínimo, pode manter mas seria bom estar na média")
else:
    print("Abaixo do peso mínimo")

if altura >= 175:
    print("Altura boa")
elif peso >= 70:
    print("Na média tudo bem em manter")
elif peso <= 58:
    print("Perto do mínimo, pode manter mas seria melhor estar na média")
else:
    print("Abaixo do peso mínimo")
