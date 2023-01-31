invitado = 0
tries = 0

while invitado != 6 and tries < 3:
    invitado = int(input("Numero de invitado:  "))
    tries += 1
    
if invitado == 6:
    print("Ya lo tienes!!!")
elif tries == 3 and invitado != 6:
    print('Alcanzó el máximo de intentos!!!')

    
    


