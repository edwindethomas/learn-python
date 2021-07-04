def palindromo(cadena1):
    cadena1 = cadena1.replace(' ','').lower()
    cadena_inversa = cadena1[::-1]
    return cadena1 == cadena_inversa


def run():
    palabra = str(input('Ingresa la palabra para comprobar el palindromo: '))
    es_palindromo = palindromo(palabra)
    if es_palindromo:
        print('Es un palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()

