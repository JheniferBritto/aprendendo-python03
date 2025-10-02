nota = [10,6,5,4,3]

for notas in nota:
    if notas >= 7:
        print(f"Aluno aprovado com nota {notas}")
    elif notas >= 5:
        print(f"Aluno em recuperação com nota {notas}")
    else:
        print(f"Aluno reprovado com nota {notas}")
        