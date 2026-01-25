def main():
    word = input("Input: ")
    newWord = shorten(word)
    print(f"Output: {newWord}")


def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    newWord = ""
    for letter in word:
        if not letter.lower() in vowels:
            newWord += letter
    return newWord


if __name__ == "__main__":
    main()
