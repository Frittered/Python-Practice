# Binary Search Function for Object Index 
search_list = sorted([0, 2023,42,98,542,1314,23,5123,99,32])

def binary_search_index(match, search_list):
    if match not in search_list:
        return print('Match is not in list')
    low = 0
    high = len(search_list)-1
    while low < high: 
        print(low, high)
        mid = (high+low)//2
        if search_list[mid] == match:
            return print(mid)
        elif search_list[mid] > match:
            high = mid
        else:
            low = mid

search_parameter = input('What number would you like to know the index of?  ')
binary_search_index(int(search_parameter), search_list)
