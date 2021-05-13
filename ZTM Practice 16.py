user_input = input('Input a string of comma separated numbers: ')
def sq_odd(inp):        
    out = []
    for i in inp.split(','):
        if int(i) % 2 != 0:
            out.append(str(int(i)**2))
    return print(','.join(out))
            
sq_odd(user_input)
