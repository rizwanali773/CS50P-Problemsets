from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("I need YoU") == " nd Y"
    assert shorten("Learn with DaViD") == "Lrn wth DVD"
    assert shorten("my twitter username is 123graham") == "my twttr srnm s 123grhm"
    assert shorten("What's your name?") == "Wht's yr nm?"

if __name__ == "__main__":
    main()
