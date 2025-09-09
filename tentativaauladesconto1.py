meia = float(input("valor da meia que receber desconto: "))
calca  = float(input("valor da calça que receber desconto: "))
cinto = float(input("valor do cinto que recebeir desconto: "))

if meia <= 100:
    print("Sem desconto.")
elif calca >= 200:
    print("10% de desconto")
    resultado = (calca/10) * 200
    print(f"{10}% de {200} é {resultado}")
elif cinto >= 200:
    print("15% de desconto")
    resultado = (cinto/15) * 200
    print(f"{15}% de {cinto} é {resultado}")


print(resultado)