def factorial(a):
    result = 1
    for i in range(1, a+1):
        result = result * i

    return result

def e(n):
    e = 0.0
    for i in range(0, n + 1):
        e = e + (1/factorial(i))
#    print("iteration -", i, " ", e)

    return e
#print(e(10))

def f(x):
#    return (e(10)**x) - (5*(x)**2)
#    return(x**3 - 2*(x)**2 - 5)
    return (x**3 - x - 2)

EPSILON1 = 0.00001;
EPSILON2 = 0.000001;

#a = 0
#b = 1

#a = 2
#b = 3

a = 1
b = 2    
        
c = b - (f(b) * (b-a)/(f(b) - f(a)))

count = 0
lebar = c
#while count <= 21:
while abs(a-b) >= EPSILON1:
    c = b - (f(b) * (b-a)/(f(b) - f(a)))

    if abs(f(c)) < EPSILON2:
        a = c
        b = c
    else:
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    
    print(count, "{0:.6f}".format(a), "{0:.6f}".format(c), "{0:.6f}".format(b),"{0:.6f}".format(f(a)), "{0:.6f}".format(f(c)), "{0:.6f}".format(f(b)), "{0:.6f}".format(lebar))
    lebar = abs(a - b)
    count = count + 1    

    

