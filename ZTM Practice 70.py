# random.choice() and list comprehension 
import random 
def print_random_factor_of_2():
    return print(random.choice([x for x in range(1,100) if not x%2]))
print_random_factor_of_2()
