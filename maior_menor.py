"""Crie uma lista com 6 números.
Percorra a lista e encontre:
O maior número
O menor número
Mostre os dois valores no final.
"""

lista = [10, 5, 3, 8, 2, 6]
for n in lista:
    maior = max(lista)
    menor = min(lista)
print(f'O maior número é {maior} e o menor número é {menor}')