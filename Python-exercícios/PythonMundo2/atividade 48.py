cont = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma dos {} é igual à {}.'.format(cont, soma))