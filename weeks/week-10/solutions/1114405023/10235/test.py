from main_simple import solve

def check(name, inp, exp):
    got=solve(inp)
    assert got==exp, f"{name}\nexpected={exp!r}\ngot={got!r}"
    print('[PASS]',name)

check('1x1 free','1\n1 1\n1\n','Case 1: 0')
check('2x2 all free','1\n2 2\n1 1\n1 1\n','Case 1: 1')
check('all sockets','1\n2 2\n0 0\n0 0\n','Case 1: 1')
