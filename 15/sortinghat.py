"""
🦁 Gryffindor
🦅 Ravenclaw
🦡 Hufflepuff
🐍 Slytherin

Q1) ¿Te gusta el amanecer o el anochecer?
    1) amanecer
    2) Anochecer

Si la respuesta es igual a 1, Gryffindor y Ravenclaw obtienen un +1.
De lo contrario, si la respuesta es igual a 2, Hufflepuff y Slytherin obtienen un +1.
De lo contrario, emite el mensaje "Entrada incorrecta".


Q2) Cuando esté muerto, quiero que la gente me recuerde como:
    1) El Bien
    2) El Grande
    3) El Sabio
    4) El audaz

Si la respuesta es 1, Hufflepuff +1.
De lo contrario, si la respuesta es 2, Slytherin +1.
De lo contrario, si la respuesta es 3, Ravenclaw +1.
De lo contrario, si la respuesta es 4, Gryffindor +1.
De lo contrario, emite el mensaje "Entrada incorrecta".

Q3) ¿Qué tipo de instrumento agrada más a tu oído?
    1) El violin
    2) La trompeta
    3) El  piano
    4) El tambor

Si la respuesta es 1, Slytherin +1.
De lo contrario, si la respuesta es 2, Hufflepuff +1.
De lo contrario, si la respuesta es 3, Ravenclaw +1.
De lo contrario, si la respuesta es 4, Gryffindor +1.
De lo contrario, emite "Entrada incorrecta".
"""
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print('Q1) ¿Te gusta el amanecer o el anochecer?')
print('    1) amanecer')
print('    2) Anochecer')
q1 = int(input('Respuesta: '))

if(q1 == 1):
    print('Gryffindor y Ravenclaw obtienen un +1')
    gryffindor = gryffindor + 1
    ravenclaw = ravenclaw + 1
elif(q1 == 2):
    print('Hufflepuff y Slytherin obtienen un +1')
    hufflepuff = hufflepuff + 1
    slytherin = slytherin + 1
else:
    print('Entrada incorrecta')

print('\nQ2) Cuando esté muerto, quiero que la gente me recuerde como:')
print('    1) El Bien')
print('    2) El Grande')
print('    3) El Sabio')
print('    4) El audaz')
q2 = int(input('Respuesta: '))


if(q2 == 1):
    print('Hufflepuff obtiene +1')
    hufflepuff = hufflepuff + 1
elif(q2 == 2):
    print('Slytherin obtiene +1.')
    slytherin = slytherin + 1 
elif(q2 == 3):
    print('Ravenclaw obtiene +1.')
    ravenclaw = ravenclaw + 1
elif(q2 == 4):
    print('Gryffindor obtiene +1.')
    gryffindor = gryffindor + 1
else:
    print('Entrada incorrecta')


print('\nQ3) ¿Qué tipo de instrumento agrada más a tu oído?')
print('    1) El violin')
print('    2) La trompeta')
print('    3) El  piano')
print('    4) El tambor')
q3 = int(input('Respuesta: '))

if(q3 == 1):
    print('Slytherin obtiene +1.')
    slytherin = slytherin + 1 
elif(q3 == 2):
    print('Hufflepuff obtiene +1.')
    hufflepuff = hufflepuff + 1
elif(q3 == 3):
    print('Ravenclaw obtiene +1.')
    ravenclaw = ravenclaw + 1
elif(q3 == 4):
    print('Gryffindor obtiene +1.')
    gryffindor = gryffindor + 1
else:
    print('Entrada incorrecta')


if (gryffindor > ravenclaw) and (gryffindor > hufflepuff) and (gryffindor > slytherin):
    print('Gana la Casa de 🦁 Gryffindor!')
elif (ravenclaw > gryffindor) and (ravenclaw > hufflepuff) and (ravenclaw > slytherin):
    print('Gana la Casa de 🦅 Ravenclaw!')
elif (hufflepuff > gryffindor) and (hufflepuff > ravenclaw) and (hufflepuff > slytherin):
    print('Gana la Casa de 🦡 Hufflepuff!')
else:
    print('Gana la Casa de 🐍 Slytherin!')