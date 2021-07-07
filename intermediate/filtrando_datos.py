DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    # all_python_devs = [worker['name'] for worker in DATA if worker['language']== 'python']
    #all_platzi_workers = [worker['name'] for worker in DATA if worker['organization']== 'Platzi']
    #adults = list(filter(lambda  wo:wo['age']>18, DATA))
    #adults = list(map(lambda wo: wo['name'],adults))
    #old_people = list(map(lambda wo: wo | {'old':wo['age']>70}, DATA))

    all_python_devs = list(filter(lambda wo:wo['language']=='python', DATA))
    all_python_devs = list(map(lambda wo:wo['name'], all_python_devs))
    all_platzi_workers = list(filter(lambda wo:wo['organization']=='Platzi', DATA))
    all_platzi_workers = list(map(lambda wo:wo['name'], all_platzi_workers))
    adults = [wo['name'] for wo in DATA if wo['age']>18]
    old_people = [wo | {'old':wo['age']>70}for wo in DATA]

    for worker in old_people:
        print(worker)


if __name__ == '__main__':
    run()