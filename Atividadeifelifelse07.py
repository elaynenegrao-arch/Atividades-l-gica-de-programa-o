quantidade= int(input("Digite a quantidade de maças compradas: "))
if quantidade >=12:
    preco_unitario= 1.0
else:
    preco_unitario= 1.30
total= quantidade*preco_unitario
print(f"Quantidade: {quantidade}")
print(f"Valor total da compra:R${total:.2f}")