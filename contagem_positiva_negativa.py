

lista = [10, -5, 3, -8, 2, -6]
for i in lista:
    positivo = sum(1 for i in lista if i > 0)
    negativo = sum(1 for i in lista if i < 0)
print(f'A quantidade de números positivos é {positivo} e a quantidade de números negativos é {negativo}')