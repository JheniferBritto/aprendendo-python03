print('------> Relatório de Alunos e Produtos <------')


print('Cadastro nomes dos Alunos')

nomes = ['paulo', 'douglas', 'paloma','jhenifer', 'roberta']

for nome in nomes:
    print(f' Aluno {nome.title()}')

print('----> Materia Python <---')

primeiro_semestre = [8,7.5,3.6,4.9,7]
segundo_semestre = [5,9,7.5,4,3]
soma_medias = 0

for indice, (nome, primeiro, segundo) in enumerate(zip(nomes,primeiro_semestre,segundo_semestre)):
    media = (primeiro + segundo) 
    soma_medias += media /2
    media_geral = soma_medias / len(nomes) 

    if media >= 7:
        print('Aprovado')
    elif media  >= 6  and  media < 7:
        print('Recuperação')
    else:
        print('Reprovado')
    
print('-----> Controle de Produtos <-----')

produtos = ['calça', 'camisa', 'blusa', 'sapato','sandalha','tenis']
quantidade = [20,39,0,5,3,10]

soma = 0
for indice, (produto, qts) in enumerate(zip(produtos, quantidade)):
    
    soma += qts
    if qts == 0:
        print('Sem estoque')
    elif qts < 5:
        print("Estoque baixo")
    elif qts < 20:
        print("Estoque médio")
    else: 
        print("Estoque alto")

print('****** Relatório Final ******')

print(f'Media geral de nota de todos os alunos foi {media_geral:.2f}')

    
print(f'Media geral de nota de todos os alunos foi {media}')



