from main import solve

def test_sample():
    data = """4 4
*...
....
.*..
....
3 5
**...
.....
.*...
0 0
"""
    expected = """Field #1:
*100
2210
1*10
1110

Field #2:
**100
33200
1*100"""
    assert solve(data) == expected

if __name__ == "__main__":
    test_sample()
    print("10189 tests passed")
