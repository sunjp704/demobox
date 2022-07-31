def gauss_jordan(A, i):
    A[i, :] = A[i, :] / A[i, i]
    _r = list(range(A.shape[0]))
    _r.remove(i)
    _c = list(range(A.shape[1]))
    _c.remove(i)
    A[_r, _c] = A[_r, _c] - A[_r, [i]] * A[[i], _c]


def assemble():
    pass


def condense():
    pass
