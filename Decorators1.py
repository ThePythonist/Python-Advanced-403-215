# def increase(x):
#     return x + 1
#
#
# def decrease(x):
#     return x - 1
#
#
# def operate(func, x):  # avali taabe - dovomi adad
#     result = func(x)  # khoroji ejraye taabe be ezaye arguman
#     return result
#
#
# print(operate(increase, 10))


def prettier(func):
    def wrapper():
        print("----------------")
        func()
        print("----------------")

    return wrapper


# def say_hello():
#     print("Hello!")
#
#
# d = prettier(say_hello)
# d()

@prettier
def say_hello():
    print("Hello!")


say_hello()
