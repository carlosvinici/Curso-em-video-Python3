km = float(input('Qual a distância que você vai percorrer:'))
print('Você está preste a começar uma viagem de {}km'.format(km))
p = km * 0.50 if km <= 200 else km * 0.45
print('O preço de sua passagem será {:.2f}$'.format(p))



