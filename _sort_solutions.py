import requests
import os

files = [file for file in os.listdir('.') 
        if os.path.isfile(file) and not file.startswith('_') and file.endswith(('.py', '.js', '.sql'))]

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


def main():
    for f in files:
        with open(f, 'r') as _f:
            try:
                link = get_link(_f)
                print(link)
            except ValueError as e :
                print(e, f)

if __name__ == '__main__':
    main()

