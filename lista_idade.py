idade = [7,17,50,60]

for idades in idade:
    if idades <= 14:
        print(f'Com {idades} anos: Você é uma criança!')
    elif idades  <= 17:
        print(f'Com {idades} anos: Você é um adolecente!')
    elif idades  <= 59:
        print(f'Com {idades} anos: Você é um adulto!')
    else:
        print(f'Com {idades} anos: Você é um idoso!')
        