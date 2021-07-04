import random


def generar_contrasena():
    mayus = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    minus = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    simbol = ['!','#','$','&','/','(',')','*']
    nums = ['1','2','3','4','5','6','7','8','9','0']

    caracs = mayus+minus+simbol+nums

    contrasena = []
    
    for i in range(15):
        caracter_random = random.choice(caracs)
        contrasena.append(caracter_random)
    return ''.join(contrasena)


def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: '+ contrasena)


if __name__ == '__main__':
    run()