def run():
    my_list = [1,'Hello',True,4.50]
    my_dict = {'firstname':'Edwin','lastname':'De Thomas'}
    super_list = [
        {'firstname':'Edwin','lastname':'De Thomas'},
        {'firstname':'Ivan','lastname':'Agame'},
        {'firstname':'Maria Jose','lastname':'Calvo'},
        {'firstname':'Francisco','lastname':'Morales'},
        {'firstname':'Rosalia','lastname':'Luna'},
    ]
    super_dict = {
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-1,-2,0,1,2],
        "floating_nums":[1.1,4.5,6.43],
    }
    for key,value in super_dict.items():
        print(key,'-',value)
    
    print('\n')

    for i in super_list:
        print(i)


if __name__ == '__main__':
    run()