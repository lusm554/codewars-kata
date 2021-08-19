import requests
import os
import shutil
from urllib.parse import urlparse

files = [file for file in os.listdir('.') 
        if os.path.isfile(file) and not file.startswith('_') 
        and file.endswith(('.py', '.js', '.sql'))]

def val_link(s):
    try:
        return s[s.index('https://'):].strip()
    except ValueError:
        return False

def get_link(f):
    l = f.readline()
    while l:
        link = val_link(l)
        if link:
            return link
        l = f.readline()
    raise ValueError('Link not found')

def get_info(link):
    id = urlparse(link).path.split('/')[2]
    r = requests.get(f'https://www.codewars.com/api/v1/code-challenges/{id}')
    if r.status_code == 200:
        json = r.json()
        folder_name = json['rank']['name'].replace(' ', '-').strip()
        return folder_name
    raise ValueError(f'request failed, status code {r.status_code}')

def move_to(dirn, file):
    if not os.path.exists(dirn):
        os.makedirs(dirn)
    shutil.move(file, os.path.join(dirn, file))

def main():
    for f in files:
        with open(f, 'r') as _f:
            try:
                link = get_link(_f)
                dirn = get_info(link)
                move_to(dirn, f)
            except ValueError as e :
                print(e, f)
                if str(e).startswith('Link not found'):
                    move_to('smth', f)

if __name__ == '__main__':
    main()

