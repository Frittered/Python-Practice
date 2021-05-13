# Second highest number
string = '''5
2 3 6 6 5'''
li = string.replace('\n',' ').split(' ')

def second_highest(li):
    li_copy = [i for i in li if i != max(li)]
    second = list(set([y for y in li if y == max(li_copy)]))[0]
    second_index = [x for x in range(len(li)) if li[x] == second]
    return print(f'The runner up, number {second_index} scored {second}')
second_highest(li)
