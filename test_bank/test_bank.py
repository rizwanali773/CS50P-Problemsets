from bank import value

def main():
    test_hello()
    test_startswith_h()
    test_others()

def test_hello():
    assert value('hello') == 0
    assert value('Hello') == 0

def test_startswith_h():
    assert value('Hi..jinx') == 20
    assert value('hi Johanna') == 20
    assert value('HoW Are You Ad.n?') == 20

def test_others():
    assert value('What\'s your name buddy?') == 100
    assert value('Good Morning, Harry!') == 100

if __name__ == "__main__":
    main()
