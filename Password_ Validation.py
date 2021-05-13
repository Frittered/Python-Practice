import re
password_regex = re.compile(r'([A-Z+a-z+0-9+][@$!&%]*){8,}\Z') #password parameters

def user_presence(): #changes user presence in a binary fashion
  global is_user
  if is_user == False:
    is_user = True
    return True
  is_user = False
  return False



def submit_password():
    while not password_truthy:
        text = input('''Input your password. It must be longer than 8 characters
         and must include uppercase and lowercase letters and a number 
         it also may include the characters"@%$&!":''')
        p = password_regex.search(text)
        try:
            verified_password = p.group()
            with open('password_user%s.txt'%(user_id), 'w') as password:
                password.write(verified_password)
            print('You have successfully saved your password. Please remember it for future reference')
            password_truthy = True
        except NoneType:
            print('Your password does not meet the criteria.')
            continue


user_id = 0
password_truthy = False
is_user = True

while is_user:
    submit_password()
    user_presence()

