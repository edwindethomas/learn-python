def dict_cubic():
    dictionary = {i:i**3 for i in range(1,101) if i%3!=0}
    return dictionary


def run():
    print(dict_cubic())


if __name__ == '__main__':
    run()