def newton_raphson(f, f_prime, x0, tol=1e-6, N=100):
  """
  This function implements the Newton-Raphson method to find the root of a function.

  Arguments:
      f: The function for which we want to find a root.
      f_prime: The derivative of the function f.
      x0: The initial guess for the root.
      tol: The tolerance for convergence (default 1e-6).
      max_iter: The maximum number of iterations (default 100).

  Returns:
      The approximation of the root or None if convergence is not achieved.
  """

  
  count = 0

  while count < N:
    fx = f(x0)
    fpx = f_prime(x0)
    if abs(fpx) < tol:
      raise RuntimeError("Derivative is zero, can't continue.")
    x_new = x0 - (fx / fpx)
    if abs(x_new - x0) < tol:

      return (x_new,count)
    x0 = x_new
    count+=1

  

  raise RuntimeError("Maximum iterations reached without convergence.")


