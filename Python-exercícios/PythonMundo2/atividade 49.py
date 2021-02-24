import time
v = int(input('Qual é a casa da tabuada que você quer ver?: '))
for a in range(1, 11):
    print('{} x {} = {}'.format(v, a, v * a))