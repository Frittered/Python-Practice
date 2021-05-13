# timeit module function wrapping
from timeit import timeit

def basic_function():
    for i in range(100):
        1+1
        
def timeit_wrapper(function):
    return print(timeit(str(function)))
    
timeit_wrapper(basic_function())
