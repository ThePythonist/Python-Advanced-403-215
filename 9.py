def average(*args):
    args = list(args)
    return sum(args) / len(args)


print(average(30, 20, 10, 40, 50))
