import types


def plus1(x):
    x += 1


a = 1
a.plus1 = types.MethodType(a, plus1)
a.plus1(a)
