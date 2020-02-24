def factorial(a):
    result = 1
    for i in range(1, a+1):
        result = result * i

    return result

def e(n):
    e = 0.0
    for i in range(0, n + 1):
        e = e + (1/factorial(i))
    return e

def f(x):
#    return(e(10)**x -5*x**2)
#    return (x**3 - 2*(x)**2 - 5)
    return (x**3 - x - 2)


def ff(x):
#    return(e(10)**x - 10*x)
#    return (3*(x)**2 - 4*x)
    return (3*(x)**2 - x)

epsilon = 0.000001

#x = 1
#x = 4
x = 2

x_before = 0

i = 0
while (abs(x - x_before) > epsilon):
    x_before = x
    x = x - f(x)/ff(x)

    print(i, "{0:.6f}".format(x), "{0:.6f}".format(abs(x - x_before)))
    i = i + 1
