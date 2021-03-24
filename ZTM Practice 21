import math
start = [0,0]
movement = ' '
while movement != '':
    movement = input('Enter a direction and distance  ')
    read_input = movement.split(' ')
    if read_input[0].upper() == 'UP':
        start[1] += int(read_input[1])
    if read_input[0].upper() == 'DOWN':
        start[1] -= int(read_input[1])
    if read_input[0].upper() == 'RIGHT':
        start[0] += int(read_input[1])
    if read_input[0].upper() == 'LEFT':
        start[0] -= int(read_input[1])
    
    print(f'New Position is {start}, total distance is {math.sqrt(abs(start[0]**2)+abs(start[1]**2))}')
