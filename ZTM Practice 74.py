import random
def random_even_in_range(x, y, iterations):
    "Prints a number divisible by 5 and 7, with range (x, y) (iterations) times"
    nums = []
    while len(nums) < iterations:
        random_number = random.randint(x, y+1)
        if  not random_number % (5 or 7):
            nums.append(random_number)
    return print(nums)
help(random_even_in_range)
x = int(input('Enter lower range '))
y = int(input('Enter Upper range(inclusive) '))
it = int(input('How many iterations would you like? '))
random_even_in_range(x, y, it)
