numero = [10,18,6,7,3,9]
soma = 0
contador = 0
for n in numero:
    if n % 2 == 0:
        soma += n
        contador += 1
    media = soma / contador
print(f'A soma dos números pares é {soma} e a média é {round(media,2)}')