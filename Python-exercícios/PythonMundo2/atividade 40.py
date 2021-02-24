nota = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota + nota2) / 2
if media > 6:
    print('Sua média é {}, Parabens você passou!'.format(media))
elif media < 6:
    print('Sua média é {}. Você está reprovado!'.format(media))
else:
    print('Sua nota é {}. Você está de recuperação. Estude mais...'.format(media))


