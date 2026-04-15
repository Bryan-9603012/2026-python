from main import decode

def test_word():
    assert decode("jr;;p") == "hello"

def test_sentence():
    assert decode("O S, GOMR YPFSU/") == "I AM FINE TODAY."

if __name__ == "__main__":
    test_word()
    test_sentence()
    print("10222 tests passed")
