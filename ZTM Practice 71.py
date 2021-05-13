# more random.choice() list comprehension 
import random 
def print_random_factor_of_5_and_7():
    return print(random.choice([x for x in range(10,150) if (not x%5 and not x%7)]))
print_random_factor_of_5_and_7()
