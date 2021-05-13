def f(x):
    try:
        print(5/int(x))
    except ZeroDivisionError:
        print('Please don\'t enter zero')
f(input('Divide 5 by a number:  '))
