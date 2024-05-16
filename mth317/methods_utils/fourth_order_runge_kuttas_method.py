import math as mt


def fourth_order_runge_kuttas_method(func, init_value_y, init_value_x, h, N):
    count = 0
    anwer = []
    while count != N:
        first_func = func(x=init_value_x, y=init_value_y)
        print(first_func)
        k1 = first_func

        
        second_func = func(x=init_value_x + (h / 2), y=init_value_y + (k1 / 2) * h)
        k2 = second_func

        
        third_func = func(x=(init_value_x + (h / 2)), y=(init_value_y + (k2 / 2) * h))
        k3 = third_func

        
        k4 = func(init_value_x + h, init_value_y + k3 * h)

        
        next_value_of_yn = init_value_y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        
        # exact = mt.e()

        anwer.append(next_value_of_yn)

    

        init_value_y = next_value_of_yn
        init_value_x += h

        count += 1

    print(anwer)