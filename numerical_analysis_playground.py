import math as mt
from methods_utils.eulers_method import euler_method
from methods_utils.fourth_order_runge_kuttas_method import fourth_order_runge_kuttas_method
from methods_utils.heuns_method import heuns_method
from methods_utils.eulers_modified import euler_modified_method


Q = lambda x, y: 3 * (x ** 2) * y
R = lambda x, y: (x) + (y)

euler_method(func=Q, init_value_x=0, init_value_y=1, h=0.1, N=5)




euler_modified_method(Q, 1, 0, 0.1, 5)




heuns_method(Q, 1, 0, 0.1, 5)




fourth_order_runge_kuttas_method(Q, 1, 0, 0.1, 5)
