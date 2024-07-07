def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Solve f(x) = 0 using the Secant method.
    
    Parameters:
    f (function): The function for which we are trying to find a root.
    x0 (float): The first initial guess.
    x1 (float): The second initial guess.
    tol (float): The tolerance for stopping the iteration. Default is 1e-6.
    max_iter (int): The maximum number of iterations. Default is 100.
    
    Returns:
    float: The estimated root.
    """
    
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
        
        # Check for convergence
        if abs(x2 - x1) < tol:
            print(f"Converged in {i+1} iterations.")
            return x2
        
        # Update the guesses for the next iteration
        x0, x1 = x1, x2
    
    print("Warning: Maximum number of iterations reached. Solution may not have converged.")
    return x1

