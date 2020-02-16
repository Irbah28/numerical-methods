def factorial(a):
    result = 1
    for i in range(1, a+1):
        result = result * i

    return result

n = input("How many iteration? ")
int_n = int(n)

e = 0.0
for i in range(0, int_n + 1):
    e = e  + (1/factorial(i))
    print("iteration -", i, " ", e)
