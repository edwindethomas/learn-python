from random import choice
import os
dic = {}
contador = 0


def clear_console():
    command = 'clear'
    if os.name in ('nt','dos'):
        command = 'cls'
    os.system(command)


def comprobar(letra,palabra):
    for le in palabra:
        if(le == letra):
            dic[le] = True
        else:
            contador+=1
            
def print_lines(data):
    cadena = ''
    for elem in data:
        if dic[elem] == True:
            cadena = cadena+elem+' '
        else:
            cadena = cadena+'_ '
    print(cadena)
            


def read():
    data = []
    with open('./data/data.txt','r',encoding='utf-8') as f:
        for line in f:
            data_line = line.replace('\n', '')
            data.append(data_line)
    return data


def print_hangman(data):
    print("   _    _")
    print("  | |  | |  ")
    print("  | |__| |  ____ _   _ ___    ____ _   _ ___ ___    ____ _   _ ___  ")
    print("  |  __  | /  _ ` | | '__ \  /  _ ` | | '__ ` _ \  /  _ ` | | '__ \ ")
    print("  | |  | | | (_)  | | |  | | | (_)  | | |  | | | | | (_)  | | |  | |")
    print("  |_|  |_| \____,_| |_|  |_| \____, | |_|  |_| |_| \____,_| |_|  |_|")
    print("                                  | |")
    print("                                __/ /")  
    print("                               |___/")
    print("                           +------------+")
    print("                           |           ||")
    print("                           o           ||")
    print("                          /|\          ||")
    print("                          / \          ||")
    print("                                       ||")
    print("                                       ||")
    print("                         ______________||______")
    print("                        |______________________|")
    for elem in data:
        dic[elem] = False


def hangman_main():

    data = read()
    data = choice(list(enumerate(data,1)))
    data = data[1]
    while(contador<6):
        clear_console()
        print_hangman(data)
        print_lines(data)
        letra = input('Ingresa una letra: ')
        comprobar(letra,data)



def run():
    hangman_main()


if __name__ == '__main__':
    run()