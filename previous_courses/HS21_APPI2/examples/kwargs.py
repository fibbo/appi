eng2de = {"one": "Eins", "two": "Zwei"}

for key, value in eng2de.items():
    print(key, value)

# print(1, 2, 3, 4, end="\n")


def without_star2(x=0, y=0):
    print(x, y)


def with_star2(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


kw = {}
if x != 0:
    kw["x"] = x
if y != 0:
    kw["y"] = y

with_star2(kw)

if x != 0:
    if y != 0:
        without_star2(x=x, y=y)
    else:
        without_star2(x=x)
else:
    if y != 0:
        without_star2(y=y)
