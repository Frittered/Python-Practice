inp= '0100,0011,1010,1001'
inp = inp.split(',')
num_set = []
for i in inp:
    z = i
    #if z[0] == '0':
        #z = z[1:]
    if int(z)%5 == 0:
        num_set.append(i)
print(*num_set, sep=',')
