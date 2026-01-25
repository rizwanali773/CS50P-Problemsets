def main():
    plates = input("Plate: ")
    if is_valid(plates):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    zero_index = s[2:].find("0")
    if 6 <= len(s) <= 2 and s[:2].isalpha() and s.isalnum() and zero_index != 0:
        for i in s[2:]:
            if i.isdigit():
                index = s.index(i)
                if s[index:].isdigit():
                    return True
                else:
                    return False
        return True



if __name__=="__main__":
    main()
