valor_total  = float(input("Digite o valor total da compra: "))

if valor_total > 200:
    print(f"Valor original: R$ {valor_total:.2f}")
    print("Porcentagem desconto: 15%")
    print(f"Valor com desconto: R$ {(valor_total * 0.85):.2f}")
elif valor_total >= 100:
    print(f"Valor original: R$ {valor_total:.2f}")
    print("Porcentagem desconto: 10%")
    print(f"Valor com desconto: R$ {(valor_total 0.9):.2f}")
else:
    print(f"Valor da compra: R$ {valor_total:.2f}")
    print("Essa compra não tem desconto.")