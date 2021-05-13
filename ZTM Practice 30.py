which_string_is_longer = lambda a, b: print(a) if len(a)>len(b) else (print(b) if len(b)>len(a) else print(f'{a} and {b} are both {len(a)} long'))
which_string_is_longer(input('a:  '), input('b:  '))
    
