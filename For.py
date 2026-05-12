produtos = ["Iphone 16", "Iphone 14", "Iphone 12", "Samsung A24", "Xiaomi Poco x7 Pro"]
precos = [8000.00, 5000.00, 3000.00, 1300.00, 3000.00]
quantidades = [5, 7, 5, 9, 4]
 
for indice, produto in enumerate(produtos):
    preco = precos[indice]
    quantidade = quantidades[indice]
    print(f"O produto {produto} custa R${preco}.")

