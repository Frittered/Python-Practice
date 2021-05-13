import re
inp = input()
let = len(re.findall(r'\w', inp)) 
dig = len(re.findall(r'\d', inp)) 
print(f'LETTERS: {let} DIGITS: {dig}')
