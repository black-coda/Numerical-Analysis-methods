import math as mt


def euler_method(func, init_value_x, init_value_y, h, N):
    count = 0

    print("\n\nS/N \t|\t Y_approx \t|\t Y_exact \t|\t Abs Error \t|\t Rel Error")
    print("-------------------------------------------------------------------")
    # print(f"y_{count} \t|\t {init_value_y:.6f} \t|\t {0:.6f} \t|\t {0:.6f} \t|\t {0:.6f}")

    while count != N:
        approximate_function = func(x=init_value_x, y=init_value_y)
        approximate_value_y = init_value_y + h * approximate_function
        exact_value = mt.exp(init_value_x ** 3)
        absolute = abs(exact_value - approximate_value_y)
        rel = absolute / exact_value

        print(f"y_{count + 1} \t|\t {init_value_y:.6f} \t|\t {exact_value:.6f} \t|\t {absolute:.6f} \t|\t {rel:.6f}")

        count += 1
        init_value_x += h
        init_value_y = approximate_value_y


Q = lambda x, y: 3 * (x ** 2) * y

euler_method(func=Q, init_value_x=0, init_value_y=1, h=0.1, N=5)


def euler_modified_method(func, init_value_y, init_value_x, h, N):
    count = 0
    while count != N:
        k1 = func(x=init_value_x, y=init_value_y)
        value_x_arg = init_value_x + (h / 2)
        value_y_arg = init_value_y + (h / 2) * k1
        k2 = func(value_x_arg, value_y_arg)

        next_value_of_yn = init_value_y + (h * k2)
        next_value_of_xn = init_value_x + h

        print(next_value_of_yn)

        init_value_x = next_value_of_xn
        init_value_y = next_value_of_yn
        count += 1 


euler_modified_method(Q, 1, 0, 0.1, 5)


def heuns_method(func, init_value_y, init_value_x, h, N):
    count = 0

    while count != N:
        k1 = func(x=init_value_x, y=init_value_y)
        k2 = func(x=init_value_x + (2 * h) / 3, y=init_value_y + (2 * k1 * h) / 3)

        next_value_of_yn = init_value_y + (h / 4) * (k1 + 3 * k2)
        print("\n")
        print(next_value_of_yn)
        next_value_of_xn = init_value_x + h

        init_value_y = next_value_of_yn
        init_value_x = next_value_of_xn
        count += 1


heuns_method(Q, 1, 0, 0.1, 5)


def fourth_order_runge_kuttas_method(func, init_value_y, init_value_x, h, N):
    count = 0
    while count != N:
        first_func = func(x=init_value_x, y=init_value_y)
        k1 = h * first_func
        # print(k1)
        # print('\n')
        second_func = func(x=init_value_x + (h / 2), y=init_value_y + (k1 / 2))
        k2 = h * second_func
        # print(k2)
        # print('\n')
        third_func = func(x=(init_value_x + (h / 2)), y=(init_value_y + (k2 / 2)))
        k3 = h * third_func
        # print(k3)
        # print('\n')
        k4 = h * func(init_value_x + h, init_value_y + k3)
        # print(k4)
        # print('\n')
        next_value_of_yn = init_value_y + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

        print(next_value_of_yn)

        init_value_y = next_value_of_yn
        init_value_x += h
        count += 1


R = lambda x, y: (x) + (y)

fourth_order_runge_kuttas_method(Q, 1, 0, 0.1, 5)
