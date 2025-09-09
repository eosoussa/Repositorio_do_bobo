nome = input("qual é o seu nome? ")
idade = int(input("qual sua idade? "))
possui_carteira = input("possui carteira de motorista? \n (1-Sim / 2-Não) ")

if idade >= 18:
    if possui_carteira == "1":
        print("pode dirigir")
    else:
        print("pode dirigir")
else:
    print("menor de idade")