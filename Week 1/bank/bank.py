greet = input("Greeting: ").lower().strip()

if greet.startswith("hello"):
    print("$0", end="")
elif greet.startswith("h") and greet.startswith('hello'):
    print("$20", end="")
else:
    print("$100", end="")
