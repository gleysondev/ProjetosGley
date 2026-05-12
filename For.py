produtos = ["Iphone 16", "Iphone 14", "Iphone 12", "Samsung A24", "Xiaomi Poco x7 Pro"]
precos = [8000.00, 5000.00, 3000.00, 1300.00, 3000.00]
quantidades = [5, 7, 5, 9, 4]
subtotais = []
 
for indice, produto in enumerate(produtos):
    preco = precos[indice]
    quantidade = quantidades[indice]
    subtotal = preco * quantidade
    subtotais.append(subtotal)

    
    mensagem = f"""
-----------------------------------
Produto: {produto}
Quantidade: {quantidade}
Valor unitário: R${preco:.2f}
Subtotal: R${subtotal:.2f}
-----------------------------------
"""
    
    print(mensagem)
    