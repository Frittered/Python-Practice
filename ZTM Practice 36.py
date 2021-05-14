#print square values except 5
def print_sq_values_except_5():
    sq_list = [[i,i**2] for i in range(1,21)]
    print(sq_list[:4],sq_list[5:])
print_sq_values_except_5()
