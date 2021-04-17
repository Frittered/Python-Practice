# Please write a program which prints all permutations of [1,2,3]
li = [1,2,3]
output_list =[]
def permutate_list(li):
    import random
    import math
    output_list.append(li)
    while len(output_list) < math.factorial(len(li)):
        new_list = li.copy()
        random.shuffle(new_list)
        if new_list not in output_list:
            output_list.append(new_list)
        print(output_list)
    return output_list
print(permutate_list(li))
