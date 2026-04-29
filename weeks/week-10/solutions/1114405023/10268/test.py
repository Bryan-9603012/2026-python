from main_simple import solve

def check(name, inp, exp):
    got=solve(inp)
    assert got==exp, f"{name}\nexpected={exp!r}\ngot={got!r}"
    print('[PASS]',name)

check('one ball','1 10\n0 0\n','10')
check('two balls','2 14\n0 0\n','5')
check('over 63','1 100\n0 0\n','More than 63 trials needed.')
