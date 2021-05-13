# List Comprehesion with indexes
li = [12,24,35,70,88,120,155]
limiter = [0,2,4,6]
print([li[i] for i in range(len(li)) if i not in limiter])
