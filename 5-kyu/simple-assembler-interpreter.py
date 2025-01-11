# https://www.codewars.com/kata/58e24788e24ddee28e000053/train/python

def val(table, x):
    if x.lstrip('-+').isdigit():
        return int(x)
    return table[x]

def mov(table, x, y):
    table[x] = val(table, y)

def inc(table, x):
    table[x]+=1

def dec(table, x):
    table[x]-=1

def jnz(table, x, y):
    if val(table, x) != 0:
        return val(table, y)
    return 0
 
def simple_assembler(program):
    registers_table = {}
    instr_table = {
        'mov': mov,
        'inc': inc,
        'dec': dec,
        'jnz': jnz,
    }
    i = 0
    while 1:
        try:
            line = program[i]
        except IndexError:
            return registers_table 
        instr, *args = line.split()
        move_i = instr_table.get(instr)(registers_table, *args) or 1
        i += move_i
    return registers_table
