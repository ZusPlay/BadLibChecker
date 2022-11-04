import os

BAD_LIBRARIES = ['algorithmic', 'colorsama', 'colorwin', 'curlapi', 'cypress', 'duonet', 'faq', 'fatnoob', 
                'felpesviadinho', 'iao', 'incrivelsim', 'installpy', 'oiu', 'pydprotect', 'pyhints', 'pyptext', 
                'pyslyte', 'pystyle', 'pystyte', 'pyurllib', 'requests-httpx', 'shaasigma', 'strinfer', 'stringe', 
                'sutiltype', 'twyne', 'type-color', 'typestring', 'typesutil']

def create_requirements(req_file_name: str):
    try:
        os.system('pip3 freeze > {}'.format(req_file_name))
    except:
        try:
            os.system('pip freeze > {}'.format(req_file_name))
        except:
            print('You have no pip. So no pip, no problem!')
            input()
            exit()

def checker():
    libraries = []
    find_bad_libraries = []
    req_file = 'requirements.txt'

    create_requirements(req_file)

    with open(req_file, 'r') as file:
        for lib in file.readlines():
            libraries.append(lib.replace('\n', '').split('==')[0])

    for lib in libraries:
        if lib in BAD_LIBRARIES:
            find_bad_libraries.append(lib)

    os.remove(req_file)

    return find_bad_libraries

if __name__ == '__main__':
    libs = checker()
    if libs:
        print(f'I`m find {", ".join(libs)}!\nPlease remove this!!!')
    else:
        print('All clear!\nGood luck :)')
