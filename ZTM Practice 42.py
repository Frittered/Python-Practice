# Map odd numbers in range
a = print(list(map(lambda x: x**2, filter(lambda y: (y%2 == 0),[i for i in range(1,11)]))))
a
