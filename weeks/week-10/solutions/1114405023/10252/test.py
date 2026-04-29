from main_simple import solve

def check(name, inp, exp):
    got=solve(inp)
    assert got==exp, f"{name}\nexpected={exp!r}\ngot={got!r}"
    print('[PASS]',name)

check('three points','1\n3\n0 0\n1 1\n2 2\n','4 1')
check('even rectangle','1\n2\n0 0\n2 3\n','5 12')
