a=['I','You']
b=['play', 'love']
c =['Football','Hockey']

def all_combinations(a,b,c):
    for x in a:
        for y in b:
            for z in c:
                print(" ".join((x,y,z)))
all_combinations(a,b,c)
