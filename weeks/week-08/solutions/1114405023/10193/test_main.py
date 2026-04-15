from main import min_b_plus_c

def brute(a: int) -> int:
    best = None
    for b in range(1, 300):
        for c in range(1, 300):
            if (b + c) * a == b * c - 1:
                s = b + c
                if best is None or s < best:
                    best = s
    return best

def test_small():
    for a in range(1, 21):
        assert min_b_plus_c(a) == brute(a)

if __name__ == "__main__":
    test_small()
    print("10193 tests passed")
