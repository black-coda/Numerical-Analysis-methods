import math as math


def bisection_method(func, a, b, N=20):
 
    tol=1e-6
    # Check if the interval does not contain a root
    if func(a) * func(b) > 0:
        raise ValueError("The interval does not contain a root.")
    
    print("\n\n Iteration \t|\t Roots")
    print("--------------------------------")

    iter_count = 0
    while abs(b - a) > tol and iter_count < N:
        c = (a + b) / 2
        print(f"\t {iter_count} \t|\t {c:.6f}")

        if func(c) == 0:
            break
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c
        iter_count += 1
    
    return (a + b) / 2


def newton_raphson(f, f_prime, x0,N=20):
    tol=1e-4
    count = 1

    print("\n\n Iteration \t|\t Roots")
    print("--------------------------------")

    while count < N:
        fx = f(x0)
        fpx = f_prime(x0)
        if abs(fpx) < tol:
            raise RuntimeError("Derivative is zero, can't continue.")
        x_new = x0 - (fx / fpx)
        print(f" {count} iteration\t|\t{x_new : .6f}")
        # if abs(x_new - x0) < tol:
        #   return (x_new,count)
        x0 = x_new
        count+=1

  

  # raise RuntimeError("Maximum iterations reached without convergence.")


def secant_method(f, x0, x1, tol=1e-6, max_iter=100):

    print("\n\n Iteration \t|\t Roots")
    print("--------------------------------")
    for i in range(max_iter):
        # Calculate the value of the function at the initial guesses
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        # Check if the denominator is zero to avoid division by zero error
        if f_x1 - f_x0 == 0:
            print("Error: Division by zero in the Secant method.")
            return None
        
        # Calculate the next approximation using the Secant method formula
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        print(f"\t {i} \t|\t {x2:.6f}")
        
        # Check for convergence
        if abs(x2 - x1) < tol:
            print(f"Converged in {i+1} iterations.")
            return x2
        
        # Update the guesses for the next iteration
        x0, x1 = x1, x2
    
    print("Warning: Maximum number of iterations reached. Solution may not have converged.")
    return x1


def func(x):
    return x - math.cos(x)

def func_prime(x):
    return 1 + math.sin(x)




a = 0.7
b = 0.8
print("\n Bisection")
bisection_method(func=func, a=a, b=b)


print("\n Newton Raphson")
newton_raphson(f=func, f_prime=func_prime, x0=1,N=10)


print("\n Secant method")
secant_method(func,a,b,max_iter=20)
