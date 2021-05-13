# Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
# How many rabbits and how many chickens do we have?
from sympy import Eq, solve
from sympy.abc import x, y
eq1 = Eq((x*2 + y*4), 94)
eq2 = Eq(x+y, 35)
print(solve((eq1, eq2), (x,y)))
