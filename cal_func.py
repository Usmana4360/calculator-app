def do_addition(a,b):
    return a+b

def do_subtraction(a,b):
    return a-b

def do_diviion(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        return "can not divide by zero"