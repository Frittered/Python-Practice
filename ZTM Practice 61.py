# Fibonacci Recursion 
n = input('To what numeral is Fibonnaci\'s N: ')
fib = lambda x: fib(x-1)+fib(x-2) if x > 1 else (0 if x== 0 else 1)
answer = fib(int(n))
print(f'Fibonacci Divineth:  {answer}')
