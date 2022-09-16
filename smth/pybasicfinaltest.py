import re
import string
import random as rand

def get_lines(file: str) -> list:
    with open(file, 'r') as f:
        return [
            line.split(", ")
            for line in f
            if re.match(r"(?:,\s+)|(['""].+['""])(?:,\s+)", line) and
            line.split(", ").count("") == 1
        ]

def gen_mail(fname: str, lname: str) -> str:
    return f"{fname}-{lname[:1]}{rand.randint(1, 5)}@company.co"

def gen_pwd(lenn: int = 16) -> str:
    chars = list(string.ascii_letters + string.digits +
            "!@#$%^&*(){}:[]-=`")
    rand.shuffle(chars)
    pwd = ""

    for i in range(lenn):
        pwd += rand.choice(chars)

    return pwd



def main():
    filename = "task_file.txt"
    lines = get_lines(filename)
    
    wf = open(filename, 'w')
    for line in lines:
        line[0] = gen_mail(line[1], line[2])
        line[-1] = line[-1][:-1]
        line.append(gen_pwd()) 

        sline = ", ".join(line) + '\n'
        wf.write(sline)

    wf.close()

if __name__ == "__main__":
    main()

