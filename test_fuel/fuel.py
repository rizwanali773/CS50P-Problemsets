def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percent = convert(fraction)
            if percent is not None:
                print(gauge(percent))
                break
        except(ValueError, ZeroDivisionError):
            pass


def convert(fraction):
        try:
            x, y = map(int, fraction.split("/"))
            if x > y:
                raise ValueError
            elif y == 0:
                raise ZeroDivisionError
            elif x <= 0 or y <= 0:
                raise ValueError

        except(ValueError, ZeroDivisionError):
            return None

        else:
            return (x / y) * 100


def gauge(percent):
    if percent <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return f"{percent}%"



if __name__ == "__main__":
    main()

