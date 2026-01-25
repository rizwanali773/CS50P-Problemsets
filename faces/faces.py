def main():
    x = input()
    x = convert(x)
    print(x)

def convert(x):
    x = x.replace(":)", "🙂")
    x = x.replace(":(", "🙁")
    return x

main()
