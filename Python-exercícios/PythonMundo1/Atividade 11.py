l = float(input('Digite a largura da parede:'))
a = float(input('Digite a altura da parede:'))
D = l * a
T = D / 2
#print('Sua parede tem dimensão de {} x {} e sua área é {}m².'.format(l, a, D))
#print('Para pintar a parede você precisará de {}L de tinta.'.format(T))
print('Sua parede tem dimensão de {} x {} e sua área é {:.3f}m²'.format(l, a, l * a))
print('Para pintar a parede você precisará de {:.3f}L de tinta.'.format(l * a / 2))