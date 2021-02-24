print('+-'*5, 'Tabuada', '+-'*5)
while True:
    casa = int(input('Qual casa você quer ver? '))
    if casa < 0:
        break
    for b in range(1, 11):
        print(f'{casa} x {b} = {casa * b}')
print('programa encerrado... volte sempre...')