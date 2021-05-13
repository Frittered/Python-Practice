class GeneratorMultiplier:
    def generator(self, n):
        for i in range(0,n):
            if i%7 == 0:
                yield i
a = GeneratorMultiplier()
final_generation = a.generator(int(input('Enter a range for the search.  ')))
for x in final_generation:
    print(x)
