import hashlib
import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'

data_repository = {}

username = input('What would you like your username to be?')
password = input('Type a unique password')

def encrypt(user, passw):
    user_salt_key = ''
    def mod_key():
        mod = random.randint(0, 100)
        return mod
    def salt_key(key, mod_key):
        salt_key = [i for i in alphabet][mod_key % 25]
        insertion = mod_key % (len(key) - 1)
        salted_key = key[:insertion] + salt_key + key[insertion:]
        salted_key = salted_key.encode(encoding='utf-8')
        a = hashlib.sha1()
        a.update(salted_key)
        a.hexdigest()
        return a.hexdigest()
    user_mod_key = mod_key()
    user_salt_key += str(user_mod_key)
    user = salt_key(user, user_mod_key)
    user_salt_key += 'a'
    passw_mod_key = mod_key()
    user_salt_key += str(passw_mod_key)
    passw = salt_key(passw, passw_mod_key)
    print(f'store this important user key for later use: {user_salt_key}')
    data_repository[user] = passw


encrypt(username, password)


def verify_encrypted_item(user, passw, salt_key):
    a = None
    b = None
    for i in range(len(salt_key)):
        if salt_key[i] == 'a':
            a = int(salt_key[:i])
            b = int(salt_key[(i + 1):])

    def pre_salted_key(key, salt_subkey):
        mod = salt_subkey
        salt_key = [i for i in alphabet][mod % 25]
        insertion = mod % (len(key) - 1)
        salted_key = key[:insertion] + salt_key + key[insertion:]
        salted_key = salted_key.encode(encoding='utf-8')
        a = hashlib.sha1()
        a.update(salted_key)
        return a.hexdigest()
    user = pre_salted_key(user, a)
    passw = pre_salted_key(passw, b)
    return print(bool(data_repository[user] == passw))


print('Welcome Back!')
a = input('What is your username')
b = input('What is your password')
c = input('Enter your user key')
verify_encrypted_item(a, b, c)
