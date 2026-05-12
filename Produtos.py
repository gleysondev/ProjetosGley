produtos = ["Iphone 16", "Iphone 14", "Iphone 12", "Samsung A24", "Xiaomi Poco x7 Pro"]
precos = [8000.00, 5000.00, 3000.00, 1300.00, 3.000]
 
print(produtos)
print(produtos[0])
print(produtos[-1])
 
print(len(produtos))
 
# Para exibir:
print(f"O produto {produtos[0]} custa R${precos[0]}")
 
# Para remover o último produto e preco também:
produtos.remove(produtos[-1])
precos.remove(precos[-1])
 
# Para somar o preco de todos os produtos
total = sum(precos)
print(f"O total deu R${total}")
 
# Lógica condicional if/else para desconto:
if total < 1300:
    exit()
else:
    desconto = 0.95
    total = total * desconto
    print(f'O total agora com desconto é de R${total}.')