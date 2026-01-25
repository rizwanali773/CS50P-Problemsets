camel = input("camelCase: ")
print("snake_case: ", end="")

for _ in camel:
    if _.isupper():
        print("_", end="")
        _ = _.lower()
    print(_, end="")
print("")

