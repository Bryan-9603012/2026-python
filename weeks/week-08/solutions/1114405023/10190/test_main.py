from main import parse

def test_parse():
    data = """2 10 5 3
0 4 1
3 2 -1
"""
    n, w, t, v, umbrellas = parse(data)
    assert (n, w, t, v) == (2, 10, 5, 3)
    assert umbrellas[0].x == 0
    assert umbrellas[0].length == 4
    assert umbrellas[0].speed == 1
    assert umbrellas[1].x == 3
    assert umbrellas[1].length == 2
    assert umbrellas[1].speed == -1

if __name__ == "__main__":
    test_parse()
    print("10190 parse scaffold test passed")
