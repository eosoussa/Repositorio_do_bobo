valor_total = input("valor total: ")
valor_parte = float(input("valor parte: "))
porcentagem = float(input("porcentagem: "))

print("valor total: ")
input(valor_total)

print("porcentagem: ")
input(porcentagem)

resultado = (porcentagem/100) * valor_parte, valor_total
print(f"{porcentagem}% de {valor_total} é {resultado}")

print(resultado)