# Print formatting

import textwrap
input_string = '''ABCDEFGHIJKLIMNOQRSTUVWXYZ
4'''
def format_input(string):
    string = string.split('\n')
    print_list = []
    for i in range(len(string[0])):      
        if i == len(string[0])-1:
            print_list.append(string[0][i])
            print(''.join(print_list))
        elif len(print_list) < 3:
            print_list.append(string[0][i])
        else:
            print_list.append(string[0][i])
            print(''.join(print_list))
            print_list =[]

format_input(input_string)
print('\nOr, an alternative,\n')
print('\n'.join(textwrap.wrap(input_string.split('\n')[0], width=4, break_long_words=True)))
