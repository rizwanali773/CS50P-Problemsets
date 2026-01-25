def main():
    greeting = input("Greeting: ").lower().strip()
    reward = value(greeting)
    print(f"${reward}")

def value(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h") and greeting != 'hello':
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
