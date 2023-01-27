yuan = float(input('Entre el tipo de cambio USD/YUAN: '))
yen = float(input('Entre el tipo de cambio USD/YEN: '))
won = float(input('Entre el tipo de cambio USD/WON: '))

yuanes = int(input('Cuántos Yuanes tienes? '))
yenes = int(input('Cuántos Yenes tienes? '))
wones = int(input('Cuántos Wones tienes? '))

total = (yuanes/yuan) + (yenes/yen) + (wones/won)

print(total)