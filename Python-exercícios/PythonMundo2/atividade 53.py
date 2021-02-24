from datetime import date
totma = 0
totme= 0
atual = date.today().year
for pess in range(1, 8):
    idade = int(input('Qual ano a {}º pessoa nasceu: '.format(pess)))
    anos = atual - idade
    if anos <= 21:
        totme += 1
    else:
        totma += 1
print('Maiores {}'.format(totma))
print('Menores {}'.format(totme))
