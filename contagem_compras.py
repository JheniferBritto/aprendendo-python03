lista = [0, 2, 5, 7, 1]

for compras in range(len(lista)):
    if compras <= 0:
        print(f'Nenhum produto {compras} comprado!')
    elif compras <=5:
        print(f'Poucos produtos {compras} comprados!')
    else:
        print(f'Muitos produtos {compras} comprados!')