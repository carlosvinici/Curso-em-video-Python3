p = float(input('Qual preço do produto?'))
vf = p - (0.05 * p)
print('O produto que custava {}R$, na promação de 5% vai custar {:.2f}R$.'.format(p, vf))
