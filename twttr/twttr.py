phrase = input("Input: ")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
print("Output: ", end="")
for _ in phrase:
    if _ in vowels:
        temp = _
        _ = ""
    print(_, end="")
print("")
