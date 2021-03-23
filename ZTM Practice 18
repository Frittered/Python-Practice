import re
inp = input('Enter your password: ')
def re_check(passwd):
    feed = passwd.split(',')
    returned_list = []
    for i in feed:
        regex = re.match(r'(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[1-9])(?=.*?[@#$]).{6,12}', i)
        if bool(regex) == True:
            returned_list.append(i)
    return print(','.join(returned_list))
re_check(inp)
