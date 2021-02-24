print('='*5, 'PA', '='*5)
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = p
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print('{}_'.format(termo), end='')
        cont += 1
        termo += r
    print('pausa')
    mais = int(input('Qantos PA vc quer mostar a mais?: '))
print('O programa mostou {} PA.'.format(total))
print('fim'
      '')





