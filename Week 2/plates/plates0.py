def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (1 < len(s) < 7 and (s[0:2].isalpha() or s[-1:-5].isdigit()) and s.isalnum()):
        for i in s[2:]:
            for j in s[3:]:
                if (i.isalpha() and j.isdigit() and j.startswith("0")):
                    return True
                else:
                    return False
    else:
        return False


if __name__ == "__main__"
    main()
