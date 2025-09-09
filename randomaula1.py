import random

numero_magico = random.randint(1,100)
numero_adivinhado = 0
tentativas = 0

while numero_adivinhado != numero_magico:
    numero_adivinhado = int(input("Chute um número entre 1 e 100: "))
    if numero_adivinhado > numero_magico:
        print("O número mágico é menor.")
    elif numero_adivinhado == numero_magico:
        print("Parabéns você acertou com {tentativas} tentativas!")
    else:
        print("O número mágico é maior.")
    tentativas += 1