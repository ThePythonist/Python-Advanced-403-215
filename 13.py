def factorial(x):
    if x == 1:
        return 1  # or x
    else:
        return x * factorial(x - 1)


n = int(input("Enter any number : "))

if n < 0:
    print("Factorial doesnt exist")
elif n == 0:
    print("Factorial of zero is one")
else:
    print(factorial(n))
