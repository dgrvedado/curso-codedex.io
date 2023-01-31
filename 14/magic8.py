import random

respuestas = [
    'Si - definitivamewnte.',
    'Es decididamente así.',
    'Sin duda.',
    'Respuesta confusa, intenta otra vez.',
    'Pregunta de nuevo más tarde.',
    'Mejor no decirte ahora.',
    'Mis fuentes dicen que no.',
    'Perspectiva no tan bueno.',
    'Muy dudoso.',
]

input('Pregunta: ')
respuesta = random.choice(respuestas)
print('Respuesta: ' + respuesta)