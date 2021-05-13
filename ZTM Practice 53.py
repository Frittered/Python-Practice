#regex email
import re
def scrape_input(inp):
    regex_email = re.compile(r'([\w]+)@([\w]+)\.([\w]+)')
    match = re.match(regex_email, inp)
    if match:
        return print(match.group(1))
    else:
        return print('no match')
scrape_input(input('Input an email, and output the username: '))
