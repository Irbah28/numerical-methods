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

epsilon = 0.00001

'''
x = 4
x_before = 0
x0 = 2
x1 = 4


x = 4
x_before = 0
x0 = 2
x1 = 4

'''
x = 4
x_before = 0
x0 = 2
x1 = 4


i = 0
while (abs(x - x_before) > epsilon):
    x_before = x1
    x = x - (f(x1)*(x1 - x0))/(f(x1)-f(x0))
    x0 = x1
    x1 = x

    print(i, "{0:.6f}".format(x), "{0:.6f}".format(abs(x - x_before)))
    i = i + 1
