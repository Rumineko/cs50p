from um import count

def main():
    test_all

def test_all():
    test_ums

def test_ums():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    #assert count("") ==

if __name__ == "__main__":
    main()
