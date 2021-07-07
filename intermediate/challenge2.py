def dict_sqrt():
    dictionary = {i:i**0.5 for i in range(1,1001)}
    return dictionary


def run():
    print(dict_sqrt())


if __name__=='__main__':
    run()