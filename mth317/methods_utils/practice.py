import math as mt
def practice(func, init_value_x, init_value_y, h):
    approximate_function = func(x=init_value_x, y=init_value_y)
    approximate_value_y = init_value_y + h * approximate_function
    print(approximate_value_y)




# Q = lambda x, y: 3 * (x ** 2) * y

def A(x,y):
    return 3 * (x ** 2) * y



practice(func=A, init_value_x=0, init_value_y=1, h=0.1)

