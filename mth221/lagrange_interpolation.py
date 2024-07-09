def lagrange_interpolation(x_points, y_points, x):
    n = len(x_points)
    interpolated_value = 0.0

    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if j != i:
                term = term * (x - x_points[j]) / (x_points[i] - x_points[j])
        interpolated_value += term

    return interpolated_value

# Example usage
x_points = [1, 1.5, 2.0]
y_points = [0.0, 0.4055, 0.6931]
x = 1.2

print(f"Interpolated value at x = {x}: {lagrange_interpolation(x_points, y_points, x)}")
