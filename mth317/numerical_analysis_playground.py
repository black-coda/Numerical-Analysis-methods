import math as mt
from methods_utils.eulers_method import euler_method
from methods_utils.fourth_order_runge_kuttas_method import fourth_order_runge_kuttas_method



Q = lambda x, y: x + (y**2)
R = lambda x, y: (x**3) * (mt.exp((-1*2)*x)) - 2*y
Y = lambda x, y: 1 / 5 *(-(x**2) + (y**2))
QU = lambda x, y: 3*(x**2)*y


# euler_method(func=QU, init_value_x=0, init_value_y=1, h=0.1, N=5)
# euler_method(func=R, init_value_x=1, init_value_y=1, h=0.1, N=6)



# euler_modified_method(Q, 1, 0, 0.1, 5)


# heuns_method(Q, 1, 0, 0.1, 5)



fourth_order_runge_kuttas_method(QU, 1, 0, 0.1, 5)
