# Scrape numbers with regex
import re

def scrape_input(inp):
    regex_numbers = re.compile(r'([\d]+)')
    matches = re.findall(regex_numbers, inp)
    if matches:
        return print(matches)
    else:
        return print('no match')
    
scrape_input(input('Input text, and output the numbers: '))
