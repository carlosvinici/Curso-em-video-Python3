from datetime import date
a = int(input('Quer ano você quer analisar? Para o ano atual digite 0: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano é BISSEXTO!')
else:
    print('O ano não é BISSEXTO!')
