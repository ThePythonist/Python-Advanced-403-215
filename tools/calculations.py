def is_prime(number):
    divs = [i for i in range(1, number + 1) if number % i == 0]
    return True if len(divs) == 2 else False


def is_binary(number):
    for i in number:
        if i not in ("0", "1"):
            return False

    return True
