def es_primo(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True


def run():
    num = int(input('Escribe un numero: '))
    if es_primo(num):
        print('Es primo')
    else:
        print('No es primo')


if __name__ == '__main__':
    run()