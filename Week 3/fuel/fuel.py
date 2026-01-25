def main():
    z = get_fraction()
    z = type_integer(z)
    if z <= 1:
        print("E")
    elif z >= 99:
        print("F")
    else:
        print(f"{z}%")


def get_fraction():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            z = float(int(x) / int(y))
            if z < 0 or z > 1:
                raise ValueError
        except(ValueError, ZeroDivisionError):
            pass
        else:
            return z


def type_integer(z):
    z *= 100
    z = round(z)
    return int(z)


main()
