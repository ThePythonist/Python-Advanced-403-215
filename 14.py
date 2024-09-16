def multiplier(x, y):  # zarb konande
    if y == 1:  # shart payan
        return x
    else:  # shart edame
        return x + multiplier(x, y - 1)


print(multiplier(5, 11))
