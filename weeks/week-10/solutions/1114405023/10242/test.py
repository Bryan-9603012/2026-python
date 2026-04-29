from main_simple import solve

def check(name, inp, exp):
    got=solve(inp)
    assert got==exp, f"{name}\nexpected={exp!r}\ngot={got!r}"
    print('[PASS]',name)

check('linear', """3 2
1 2
2 3
5
6
7
1 1
3
""",'18')
check('cycle plus bar', """5 5
1 2
2 3
3 1
3 4
4 5
10
20
30
40
50
1 1
5
""",'150')
