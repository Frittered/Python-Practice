n = input('What would you like your n to be?:  ')
def generator(number):
    number_list = [x for x in range(int(number)+1) if not x%2]
    for i in range(len(number_list)):
        yield number_list[i]
print([x for x in generator(n)])
