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

start = -0.50
end = 1.50
while start <= end:
    fx = e(10)** start - (5*(start)**2)
    print("{0:.2f}".format(start),"{0:.6f}".format(fx))
    start = start + 0.1
    
#    print(start, fx)

