lista = [0,4,5,6]

for produtos in lista:
    if produtos <= 0:
        print(f'Nenhum produto {produtos} comprado!')
    elif produtos <= 5:
        print(f'Poucos produtos {produtos} comprados!')
    else:
        print(f'Muitos produtos {produtos} comprados!')