print('BANCO DE CODÉDEX')

pin = int(input('Entre su PIN: '))

while pin != 1234:
  pin = int(input('PIN Incorrecto. Entre su PIN nuevamente: '))

  if pin == 1234:
    print('PIN correcto!')