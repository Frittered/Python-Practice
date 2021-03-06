# Random even numbers within range 
import random
def random_even_in_range(x, y, iterations):
    "Prints an even number between x and y (iterations) times"
    nums = []
    while len(nums) < iterations:
        random_number = random.randint(x, y+1)
        if not random_number & 2:
            nums.append(random_number)
    return print(nums)
help(random_even_in_range)
x = int(input('Enter lower range '))
y = int(input('Enter Upper range(inclusive) '))
it = int(input('How many iterations would you like? '))
random_even_in_range(x, y, it)
