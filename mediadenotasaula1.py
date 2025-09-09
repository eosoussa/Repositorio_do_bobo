nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))

media = (nota1+nota2+nota3)/3


if media >= 7:
    print("Aprovado!")
elif media >= 4:
    print("Recuperação")
else:
    print("Está reprovado")