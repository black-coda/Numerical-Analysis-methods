import math as mt


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