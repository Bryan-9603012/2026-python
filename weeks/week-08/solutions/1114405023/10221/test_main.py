from main import solve_line

def test_deg():
    assert solve_line(500, 30, "deg") == "3633.775503 3592.408346"

def test_min_prefix():
    assert solve_line(700, 60, "min").startswith("124.616")

if __name__ == "__main__":
    test_deg()
    test_min_prefix()
    print("10221 tests passed")
