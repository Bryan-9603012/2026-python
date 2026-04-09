

import timeit


parts = [f"item{i}" for i in range(1000)]


def bad_concat():
    s = ""
    for p in parts:
        s += p
    return s


def good_join():
    return "".join(parts)


t1 = timeit.timeit(bad_concat, number=500)
t2 = timeit.timeit(good_join, number=500)
print(f"+串接: {t1:.3f}s  join: {t2:.3f}s")


class SafeSub(dict):
    def __missing__(self, key: str) -> str:
        return "{" + key + "}"


name = "Guido"
s = "{name} has {n} messages."
print(s.format_map(SafeSub(vars())))


a = "Hello"
b = b"Hello"
print(a[0])
print(b[0])


print("{:10s} {:5d}".format("ACME", 100).encode("ascii"))
