import numpy as np
def euler_method(func, y0, t0, tn, h):
    """
    Solves a first-order ODE using the Euler method.

    Parameters:
    - func: Function representing the ODE dy/dt = f(t, y).
    - y0: Initial value of y at t0.
    - t0: Initial time.
    - tn: Final time.
    - h: Step size.

    Returns:
    - t_values: Array of time values.
    - y_values: Array of corresponding y values.
    """

    num_steps = int((tn - t0) / h) + 1
    t_values = np.linspace(t0, tn, num_steps)
    y_values = np.zeros(num_steps)
    y_values[0] = y0

    for i in range(1, num_steps):
        y_values[i] = y_values[i - 1] + h * func(t_values[i - 1], y_values[i - 1])

    return t_values, y_values

# Example usage:
# Define the ODE: dy/dt = -2 * t * y
R = lambda x, y: (2*x) + (y)

# Set initial conditions and parameters
initial_time = 1.0
final_time = 1.5
initial_value_y = 1.0
step_size = 0.1

# Solve the ODE using the Euler method
t_values, y_values = euler_method(R, initial_value_y, initial_time, final_time, step_size)

# Print the results
for t, y in zip(t_values, y_values):
    print(f'Time: {t:.2f}, y: {y:.6f}')
