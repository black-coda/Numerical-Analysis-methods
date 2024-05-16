class TrapezodialRule():
    def __init__(self, func, a, b) -> None:
        self.a = a
        self.b = b
        self.func = func 




def trape(a,b, func):
    I = (b-a)*(func(a)+func(b))/2
    return I

def func(x):
    return 0.2 + 25*x 

a = 0
b = 2

ans = trape(a,b,func)
print(ans)