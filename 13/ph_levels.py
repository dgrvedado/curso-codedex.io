ph = int(input('Entre el PH (0 - 14): '))

if (ph > 7) and (ph <= 14):
    print('Basico')
elif (ph < 7) and (ph >= 0):
    print('Acido')
elif ph == 7:
    print('Neutro')
else:
    print('Valor fuera de rango (0 - 14)')