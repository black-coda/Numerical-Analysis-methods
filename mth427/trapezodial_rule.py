class TrapezoidalRule():
    def __init__(self, func, a, b) -> None:
        self.a = a
        self.b = b
        self.func = func 

    def single_trapezoidal(self):
        I = (b-a)*(func(a)+func(b))/2
        return I
    
    def composite_trapezoidal(self, n):

        """
        Computes the definite integral of a function using the composite trapezoidal method.

        Parameters:
            f (function): The integrand function.
            a (float): The lower limit of integration.
            b (float): The upper limit of integration.
            n (int): The number of sub-intervals for the composite trapezoidal method.

        Returns:
            float: The approximate value of the definite integral.
        """
        h = (b - a) / n
        integral = 0.5 * (f(a) + f(b))  # Initialize integral with the endpoints

        for i in range(1, n):
            x_i = a + i * h
            integral += f(x_i)

        integral *= h
        return integral

def func(x):
    return 0.2 + 25*x 

a = 0
b = 2
trapezoidal_rule = TrapezoidalRule(func, a, b)
ans = trapezoidal_rule.single_trapezoidal(a,b,func)
print(ans)




# Example usage:
def f(x):
    return x**2

a = 0  # Lower limit
b = 1  # Upper limit
n = 100  # Number of sub-intervals

result = trapezoidal_rule.composite_trapezoidal(f, a, b, n)
print("Approximate integral:", result)
