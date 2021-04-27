'''Write a function that takes a string as an argument and tests its likeness against a list of strings. If the characters and order match to a specified degree, then the
function returns the appropriate boolean. If true, print the strings likeness'''

list_repository = ['grass', 'goose', 'gassy', 'gorse']

def likeness_function(test_string):
    highest_likeness = 0
    match = None
    for likeness in list_repository:
        raw_likeness = 0
        ordered_likeness = 0
        for i in range(len(test_string)):
            if i < len(likeness):
                if test_string[i] == likeness[i]:
                    ordered_likeness += 1
            raw_likeness += test_string.count(test_string[i]) - abs(
                test_string.count(test_string[i]) - [
                    x for x in list_repository[1]].count(f'{test_string[i]}'))
        print(raw_likeness, ordered_likeness)
        if (raw_likeness+ordered_likeness)/(2*len(test_string))> highest_likeness:
            highest_likeness = (raw_likeness+ordered_likeness)/(2*len(test_string))
            match = likeness
    if highest_likeness >= 0.7:
        print(f'{test_string} Matched with {match}')
        return True
    else:
        print('No match')
        return False
likeness_function('gross')
