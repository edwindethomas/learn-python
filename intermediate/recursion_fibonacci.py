def fibonacci(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)


def run():
    numero = int(input('Ingrega el valor n para ver el Fibonacci: '))
    print('El fibonaci de '+str(numero)+' es '+str(fibonacci(numero)))


if __name__ == "__main__":
    run()