# Sum of increasing fractions function
def fractions_from_half(itr):
    total = 0
    for i in range(int(itr)):
        x = lambda x, y, z: x/y + z
        total = x(i+1, i+2,total)
    return print(total)
    
fractions_from_half(input('How many iterations would you like:  '))
