# print two tuples of a number list in two lines
a = lambda x: print(tuple(x[1:6]),'\n',tuple(x[6:11]))
a([i for i in range(11)])
