# simple program to demonstrate closure
def outer_fn():
    numbers = []
    def inner_fn(x):
        numbers.append(x)
        print(numbers)
    return inner_fn

enter_num = outer_fn()
enter_num(1)
enter_num(2)
enter_num(3)

# achieve same result as above. 
