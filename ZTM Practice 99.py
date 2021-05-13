# Symmetric difference of list of lists

inp = '''4
2 4 5 9
4
2 4 11 12'''
def set_difference(inp):
    lines = [i.split(' ') for i in inp.split('\n')]
    m = [i for x in lines[:2] for i in x]
    n = [i for x in lines[2:4] for i in x]
    print('\n'.join(list(set(m) - set(n))
          + list(set(n)- 
                     set(m))))
set_difference(inp)
