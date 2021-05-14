#print tuple of even numbers from a range
a = lambda x:  print(tuple(x))
a([i for i in range(1,11) if i%2 == 0])
