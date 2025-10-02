pessoas = [
    {"nome": "Ana", "idade": 10, "estudante": True},
    {"nome": "Bruno", "idade": 16, "estudante": False},
    {"nome": "Carlos", "idade": 25, "estudante": True},
    {"nome": "Dora", "idade": 65, "estudante": False}
]

for estudante in pessoas:
    if estudante['idade'] <= 15 and estudante['estudante'] == True:
        print(f"{estudante['nome']} é uma criança  tem direito a desconto.")
    elif estudante['idade'] <= 18 and estudante['estudante'] == False:
        print(f"{estudante['nome']} é um adolescente não tem direito a desconto.")
    elif  estudante['idade'] <= 64 and estudante['estudante'] == True:
        print(f"{estudante['nome']} é um adulto tem direito a desconto.")
    else:
        print(f"{estudante['nome']} é um idoso não tem direito a desconto.")