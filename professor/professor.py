import random


def main():
    correct = 0

    level = get_level()
    i = 0
    while(i < 10):
        x = generate_integer(level)
        y = generate_integer(level)
        sum = x + y
        for j in range(4):
            if j == 3:
                print(f"{x} + {y} = {sum}")
                break
            try:
                print(f"{x} + {y} = ", end="")
                user_ans = int(input())
                if user_ans == sum:
                    correct += 1
                    break
                else:
                    raise Exception
            except (ValueError, Exception):
                print("EEE")
        i += 1
    print(f"Correct: {correct}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
            else:
                raise ValueError
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randrange(10)
    if level == 2:
        return random.randrange(10, 100)
    if level == 3:
        return random.randrange(100, 1000)



if __name__ == "__main__":
    main()
