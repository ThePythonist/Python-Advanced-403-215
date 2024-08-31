import random


def irancell():
    codes = ["0930", "0939", "0902", "0903"]
    pn = f"{random.choice(codes)}"
    for i in range(7):
        pn += str(random.randint(0, 9))

    print(pn)


def hamrahaval():
    codes = ["0911", "0912", "0910", "0919"]
    pn = f"{random.choice(codes)}"
    for i in range(7):
        pn += str(random.randint(0, 9))

    print(pn)


def rightell():
    codes = ["0921", "0922", "0923"]
    pn = f"{random.choice(codes)}"
    for i in range(7):
        pn += str(random.randint(0, 9))

    print(pn)


if __name__ == "__main__":
    irancell()
    hamrahaval()
    rightell()
