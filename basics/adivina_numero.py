import random


def run():
    num_aleatorio = random.randint(1,100)
    numero = int(input('Elige un número del 1 al 100: '))
    while numero != num_aleatorio:
        if numero<num_aleatorio:
            print('Es un numero mas grande')
        else:
            print('Es un número mas pequeño')
        numero = int(input('Elige otro número: '))
    print('¡Ganaste!')


if __name__ == '__main__':
    run()