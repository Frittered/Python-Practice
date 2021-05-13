print(sorted.__doc__)
print(set.__doc__)
def janky_prime_counter(num_range):
    """
    Bootleg function to find primes.
Usable for small numbers  under 1000.
    
Takes an integer as an argument.
    """
    primes = []
    for i in range(1, int(num_range)):
        factors = []
        for x in range(2,1000):
            if x != i:
                if i % x == 0:
                    factors.append(x)
        if len(factors) == 0:
            primes.append(i)
    return print(primes)
print(janky_prime_counter.__doc__)
janky_prime_counter(int(input('Enter a range to find primes:  ')))
