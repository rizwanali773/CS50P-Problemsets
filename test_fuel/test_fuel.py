import pytest
from fuel import convert, gauge

def main():
    test_fuel()
    test_gauge()
    test_error()

def test_fuel():
    assert convert('1/1') == 100
    assert convert('0/1') == 0
    assert convert('1/3') == 33  # round kiya hai
    assert convert('1/2') == 50

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(57) == "57%"

def test_error():
    with pytest.raises(ValueError):
        convert('cat/dog')
    with pytest.raises(ValueError):
        convert('4/2')
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
    with pytest.raises(ValueError):
        convert('-1/3')
    with pytest.raises(ValueError):
        convert('-4/-2')

if __name__ == "__main__":
    main()

