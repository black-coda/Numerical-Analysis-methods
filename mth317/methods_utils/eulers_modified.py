import math as mt

# Q = lambda x, y: 3 * (x ** 2) * y
def euler_modified_method(func, init_value_y, init_value_x, h, N):
    count = 0
    while count != N:
        k1 = func(x=init_value_x, y=init_value_y)
        value_x_arg = init_value_x + (h / 2)
        value_y_arg = init_value_y + (h / 2) * k1
        k2 = func(value_x_arg, value_y_arg)

        next_value_of_yn = init_value_y + (h * k2)
        next_value_of_xn = init_value_x + h

        # print(next_value_of_yn)
        exact = mt.exp(init_value_x**3)
        absolute = abs(exact - next_value_of_yn)
        rel = absolute / exact

        init_value_x = next_value_of_xn
        init_value_y = next_value_of_yn

        print("\n\nS/N \t|\t Y_approx \t|\t Y_exact \t|\t Abs Error \t|\t Rel Error")
        print("----------------------------------------------------------------------------------------------------")

        print(f"y_{count+1} \t|\t {next_value_of_yn:.6f} \t|\t {exact:.6f} \t|\t {absolute:.6f} \t|\t {rel:.6f}")
        
        count += 1 



# R = lambda x,y: x+(3*y)
Q = lambda x, y: 3 * (x ** 2) * y
euler_modified_method(Q, 1, 0, 0.1, 10)


