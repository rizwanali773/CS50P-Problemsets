import sys

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
else:
    if not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit(1)
    else:
        lines_of_code = 0
        try:
            with open(sys.argv[1], "r") as file:
                for line in file:
                    stripped_line = line.rstrip("\n")
                    if line.lstrip() == "" or line.lstrip().startswith("#"):
                        pass
                    else:
                        lines_of_code += 1
                print(lines_of_code)
        except FileNotFoundError:
            print("File does not exist")
            sys.exit(1)
