inp= input()
num_set = []
for i in inp.split(','):
    z = int(i,2)
    if int(z)%5 == 0:
        num_set.append(i)
print(*num_set, sep=',')
