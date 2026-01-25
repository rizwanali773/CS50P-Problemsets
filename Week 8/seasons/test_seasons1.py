from seasons import minutes_lived

def main();
    test_1()
    test_2()


def test_1():
    assert minutes_lived(2003, 5, 17) == "Eleven million, eight hundred sixty-two thousand, seven hundred twenty minutes"
    assert minutes_lived(2000, 2, 1) == "Twelve million, five hundred thirty-nine thousand, five hundred twenty minutes"

def test_2():
    assert minutes_lived(23, 1, 2000) == "Invalid Date"

if __name__ == "__main__":
    main()
