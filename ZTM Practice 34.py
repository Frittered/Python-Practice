# Print square values up to 5 from a list
def print_sq_values_to_5():
    sq_list = [i**2 for i in range(1,21)]
    print(sq_list[:5])
print_sq_values_to_5()
