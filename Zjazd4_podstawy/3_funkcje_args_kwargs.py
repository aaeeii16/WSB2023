def my_arg_function(*args):
    print(args[2])
    for arg in args:
        if arg > 0:
            print(f'{arg} * 2 to {arg * 2}')
        
