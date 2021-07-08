def read():
    numbers = []
    with open('./archivos/numbers.txt','r',encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


#r -> lectura
#w -> escritura(sobrescribe)
#a -> escritura(agrega al final)
def write():
    names = ['Moco','Maríjo','Ivan','Paco']
    with open('./archivos/names.txt','a',encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')


def run():
    write()


if __name__ == '__main__':
    run()