from math import exp

print("DVC CLASS EXAMPLE \n y' = 3(x**2)y ; y(0) = 1 given y = exp(x**3) with h = 0.01, 0.001, 0.00001")
ans = int(input("how many iterations do you want: \n"))
h = float(input("Enter te Value of 'h': "))

x = 0
y = 1
count = 0

print("\n\nS/N \t|\t Y_approx \t|\t Y_exact \t|\t Abs Error \t|\t Rel Error")
print("----------------------------------------------------------------------")

for b in range(1, ans):
    approx = y + h * (3 * (x**2) * y)
    exact = exp(x**3)
    absolute = abs(exact - approx)
    rel = absolute / exact

    print(f"y_{count+1} \t|\t {y:.6f} \t|\t {exact:.6f} \t|\t {absolute:.6f} \t|\t {rel:.6f}")
    if h <= absolute:
        break

    x = x + 0.1
    count = count + 1
    y = approx
