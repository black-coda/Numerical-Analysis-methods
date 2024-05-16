import math as mt


def euler_method(func, init_value_x, init_value_y, h, N):
    count = 0

    print("\n\nS/N \t|\t Y_approx \t|\t Y_exact \t|\t Abs Error \t|\t Rel Error")
    print("-------------------------------------------------------------------")
    # print(f"y_{count} \t|\t {init_value_y:.6f} \t|\t {0:.6f} \t|\t {0:.6f} \t|\t {0:.6f}")

    while count != N:
        approximate_function = func(x=init_value_x, y=init_value_y)
        print(approximate_function)
        approximate_value_y = init_value_y + h * approximate_function
        exact_value = mt.exp(init_value_x ** 3)
        absolute = abs(exact_value - approximate_value_y)
        rel = absolute / exact_value

        print(f"y_{count + 1} \t|\t {init_value_y:.6f} \t|\t {exact_value:.6f} \t|\t {absolute:.6f} \t|\t {rel:.6f}")

        count += 1
        init_value_x += h
        init_value_y = approximate_value_y
