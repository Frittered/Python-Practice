# uses Pwned Passwords API to check if your password has been compromised.

import requests
import hashlib
import sys
passw = sys.argv[1:]


def read_request(page, tail):
    hashes = page.text
    line_list = hashes.splitlines()
    found = False
    for line in line_list:
        split_line = line.split(':')
        if tail in split_line:
            print(f'your password has been breached {split_line[1]} times.')
            print('You should consider changing it immediately.')
            found = True

def api_request(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    r = requests.get(url)
    if r.status_code != 200:
        print('This password was not found. Congratulations, your password is secure!')
    return r

def password_breach_detection(inp):
    raw = (hashlib.sha1(inp.encode('utf-8')).hexdigest().upper())
    lead, tail= raw[0:5], raw[5:]
    request = api_request(lead)
    breach_quantity = read_request(request, tail)
    return breach_quantity
if __name__ == '__main__':
    for i in passw:
        password_breach_detection(str(i))
    sys.exit()
