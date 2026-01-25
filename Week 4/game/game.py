import random


def main():
    n = get_level()
    x = random.randint(1, n)
    guess(x)


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n < 0:
                raise ValueError
            else:
                return n
        except ValueError:
            pass


def guess(x):
    while True:
        try:
            num = int(input("Guess: "))
            if num <= 0:
                raise Exception
            else:
                if num > x:
                    print("Too Large!")
                elif num < x:
                    print("Too Small!")
                else:
                    print("Just Right!")
                    return
        except:
            pass


main()
