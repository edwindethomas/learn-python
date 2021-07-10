from random import choice
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def print_hang():
    print('   +-------++')
    print('   |       ||')
    print('   o       ||')
    print('  /|\      ||')
    print('  / \      ||')
    print('           ||')
    print('  _________||')
    print(' |__________|')

def guess_view(guess):
    print('Las letras ya dichas son:')
    s = str(guess).replace('[', '')
    s = s.replace(']', '')
    print(s)


def read():
    data = []
    with open('./data/data.txt','r',encoding='utf-8') as f:
        for line in f:
            data_line = line.replace('\n', '')
            data.append(data_line)
    return data


def hangman_logic(word):
    guess = []
    allow_err = 7
    done = False
    while not done:
        clearConsole()
        print_hang()
        for letter in word:
            if letter.lower() in guess:
                print(letter,end=' ')
            else:
                print('_',end=' ')
        print('')
        guess_view(guess)
        print('')
        let = input('Ingresa una letra: ')
        guess.append(let.lower())
        if let.lower() not in word.lower():
            allow_err -=1
            if allow_err == 0:
                break
        done= True
        for letter in word:
            if letter.lower() not in guess:
                done = False
    
    if done:
        print("Ganaste!! Felicitaciones, la palabra es "+word)
    else:
        print('Game over!!! la palabra era '+word)

def hangman_main():

    data = read()
    word = choice(data)
    hangman_logic(word)
    





def run():
    hangman_main()


if __name__ == '__main__':
    run()