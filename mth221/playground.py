# Example use-case
import math as mt
from newton_raph import newton_raphson
from bisection_method import bisection_method

# Define the function for which we want to find the root
def func(x):
    return x - mt.cos(x)

def func_prime(x):
    return 1 + mt.sin(x)

# Use the bisection method to find the root
root = bisection_method(func, 0, 2)
nr_root = newton_raphson(f=func, f_prime=func_prime, x0=1)
print(f"\nThe root of the function is approximately {nr_root}\n")


# This is the code playground

