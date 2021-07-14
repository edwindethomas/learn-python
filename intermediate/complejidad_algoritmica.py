import time
import sys
sys.setrecursionlimit(100000)

def factorial(n):
    respuesta = 1
    while n>1:
        respuesta *=n
        n-=1
    return respuesta


def factorial_r(n):
    if n==1:
        return 1
    
    return n * factorial_r(n-1)


if __name__ == '__main__':
    n = 10000
    comienzo1 = time.time()
    factorial(n)
    final1 = time.time()
    print(final1-comienzo1)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final-comienzo)