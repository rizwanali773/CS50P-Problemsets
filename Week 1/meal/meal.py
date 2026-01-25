def main():
    time = input("What time is it? ")
    time = convert(time)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        return


def convert(time):
    h, m = time.split(":")
    h , m = int(h), float(m)
    m /= 60
    return(h+m)


if __name__ == "__main__":
    main()
