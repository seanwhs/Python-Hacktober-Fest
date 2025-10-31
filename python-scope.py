# simple program to demo scope in python
name = 'James'

def greeting(name): #param is local scoped
    color = 'blue'
    print(color)
    print(name)

greeting('Paul')

def another():
    greeting('Sean')

print('**********************')
another()
