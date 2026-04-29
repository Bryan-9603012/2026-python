from main_simple import solve

def check(name, inp, exp):
    got=solve(inp)
    assert got==exp, f"{name}\nexpected={exp!r}\ngot={got!r}"
    print('[PASS]',name)

check('N=3 no restriction','3\n0\n0\n0\n','ABC\nCB\nBAC\nCA\nCAB\nBA')
check('A cannot pos1','3\n1 0\n0\n0\n','BAC\nCA\nCAB\nBA')
