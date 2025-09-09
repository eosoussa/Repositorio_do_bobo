numero = int(input("Digite o número da tabuada: "))
inicio = int(input("Digite de onde começa o contador: "))
final = int(input("Digite até onde vai o contador: "))



for i in range(inicio,final + 1):
    print(f" {i} x {numero} = {i * numero}")