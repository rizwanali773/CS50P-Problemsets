from plates import is_valid

def main():
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()

def test_1():
    assert is_valid("50") == False
    assert is_valid("cs") == True

def test_2():
    assert is_valid("CS") == True
    assert is_valid("CSPython") == False
    assert is_valid("Grapes") == True

def test_3():
    assert is_valid("aaa222") == True
    assert is_valid("ab36c3") == False

def test_4():
    assert is_valid("Adn790") == True
    assert is_valid("Adn051") == False

def test_5():
    assert is_valid("ad.n50") == False
    assert is_valid("adn 50") == False
    assert is_valid('"ad n"') == False
    assert is_valid("pi3.14") == False
    

if __name__ == "__main__":
    main()
