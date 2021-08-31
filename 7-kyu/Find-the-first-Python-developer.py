# https://www.codewars.com/kata/5827bc50f524dd029d0005f2/train/python

def get_first_python(users):
    for u in users:
        if u['language'] == 'Python':
            return f'{u["first_name"]}, {u["country"]}'
    
    return 'There will be no Python developers'
