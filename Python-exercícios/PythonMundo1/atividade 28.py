s = float(input('Digite o salário do funcionário: '))
if s >= 1.250:
    vf = s * 0.15 + s
else:
    vf = s * 0.10 + s
print('O salário {} com aumento ficará {}$'.format(s, vf))



