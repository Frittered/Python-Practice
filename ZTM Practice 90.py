# Character count of input

input_string = input('Enter a string for a character count')
char_set = sorted(list(set([i for i in input_string])))
for i in char_set:
    print(i,': ', input_string.count(i))
