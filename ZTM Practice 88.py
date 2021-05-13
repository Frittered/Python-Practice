# Duplicates with list comprehension

li1 = [12,24,35,24,88,120,155,88,120,155]
result = list(set([i for i in li1 if li1.count(i)>1]))
print(result)
