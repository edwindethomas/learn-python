def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)


def run():
    numero = int(input('Ingresa el número para sacar el factorial: '))
    print('El factorial de '+str(numero)+' es : '+str(factorial(numero)))


if __name__ == '__main__':
    run()