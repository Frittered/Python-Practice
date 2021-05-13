# More random module practice
import random
def print_in_range(x, y):
        return print(random.randint(int(x),int(y)+1))
print_in_range = lambda x, y: print(random.randint(x,y+1))
print_in_range(7,15)
