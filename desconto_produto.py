lista = [50, 120, 30, 200]

for preco in lista: 
    if preco > 100:
        print(  f'O desconto é 20% no valor de {preco}')
    elif preco <= 100:
        print(  f'O desconto é 10% no valor de {preco}')