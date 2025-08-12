#n to 1 counting using recursion
def show(n):
    if n == 0:
        print("End of recursion")
        return
    else:
        print(n)
        show(n - 1)

show(5)

#n! function using recursion

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

