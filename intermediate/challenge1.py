def list_multi():
    multi = [i for i in range(1,100000) if i%36==0]
    # multi = [i for i in range(1,100000) if i%4 == 0 and i%6 == 0 and i%9==0]
    return multi

def run():
    print(list_multi())


if __name__ == '__main__':
    run()