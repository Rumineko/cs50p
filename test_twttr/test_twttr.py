from twttr import shorten

def test_twttr():
    assert shorten("ligma") == "lgm"
    assert shorten("WAKANDA") == "WKND"
    assert shorten("AEIOU") == ""
    assert shorten("42.answer") == "42.nswr"

def main():
    test_twttr()

if __name__ == "__main__":
    main()