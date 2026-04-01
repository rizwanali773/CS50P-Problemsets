def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    x , z = int(x), float(z)
    if y == '+':
        print(x + z)
    elif y == '-':
        print(x - z)
    elif y == '/':
        result = x / z
        print(f"{result:.1f}")
    elif y == '*':
        print(x * z)
    else:
        print("Expresion is undefined")

main()
