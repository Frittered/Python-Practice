# Print formatting with rangolis

alphabet ='abcdefghijklmnopqrstuvwxyz'
def print_rangoli(n):
    string_slice = alphabet[0:-(len(alphabet)-int(n))]
    string = []
    print_list = []
    for char in string_slice[::-1]: 
       string_mirror = string[::-1]
       string.append(char)
       print_list.append('-'.join(string + string_mirror).center((len(string_slice)*3), '-'))
    list_mirror = print_list[:(len(print_list)-1)]
    print('\n'.join(print_list) + '\n' + '\n'.join(list_mirror[::-1]).replace(' ', ''))
print_rangoli(3) 
