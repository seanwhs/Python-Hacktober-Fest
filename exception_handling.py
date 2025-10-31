# Simple program to demonstrate exception handling using a custom class
class JustNotCoolError(Exception):
    pass

x=2 
try:
    raise JustNotCoolError("This just isn't cool, man")
except NameError:
    print('NameError means something is probably undefeined')
except ZeroDivisionError:
    print('Please do not divide by zero')
except Exception as error:
    print(error)
else:
    print('No errors!')
finally:
    print('Im going to print with or without an error')
