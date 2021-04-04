    
def divisible_number_generator(number_range):
    for i in range(int(number_range)):
        if not i % 5 and not i % 7:
            yield i
inp = input('What would you like your number range to be? ')
answer = [x for x in divisible_number_generator(inp)]
for i in answer:
    assert not i % 5 
    assert not i % 7
