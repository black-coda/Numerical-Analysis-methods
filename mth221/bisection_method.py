def bisection_method(func, a, b, N=100):
    """
    Finds a root of the function func within the interval [a, b].
    
    Parameters:
    - func: A function object representing the equation f(x)=0.
    - a, b: The initial interval [a, b] where the root is expected to lie.
    - tol: The tolerance for the stopping criterion.
    - max_iter: Maximum number of iterations allowed.
    
    Returns:
    - x: The approximate root of the function.
    """

    tol=1e-6
    # Check if the interval does not contain a root
    if func(a) * func(b) > 0:
        raise ValueError("The interval does not contain a root.")
    
    iter_count = 0
    while abs(b - a) > tol and iter_count < N:
        c = (a + b) / 2
        print(f"Iteration {iter_count+1}: Midpoint = {c}")  # Print the midpoint at each iteration
        if func(c) == 0:
            break
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c
        iter_count += 1
    
    return (a + b) / 2

# Example use-case
import math as mt

# Define the function for which we want to find the root
def func(x):
    return x - mt.cos(x)

# Use the bisection method to find the root
root = bisection_method(func, 0, 2)
print(f"\nThe root of the function is approximately {root}\n")
