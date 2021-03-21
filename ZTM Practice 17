total = 0
user_input = ' '
strip_input = lambda x: int(x.replace('D','').replace('W',''))
while len(user_input) != 0:
    user_input = input('Write W/D then a number')
    if 'D' in user_input:
        total += strip_input(user_input)
    elif 'W' in user_input:
        total -= strip_input(user_input)
print(total)
