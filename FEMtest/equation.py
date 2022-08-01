from abc import ABC, abstractmethod
from typing import Tuple
import numpy as np
import scipy.sparse as ss
import scipy.sparse.linalg as sl


class Element(ABC):
    @abstractmethod
    def jj():
        pass
    


class Element(object):
    def __init__(self,name,id) -> None:
        self._name = name
        self._id = id
        self._k = None
        self._mass = None
        self._id = None

class Element(object):
    def __init__(self,name,id) -> None:
        self._name = name
        self._id = id
        self._k = None
        self._mass = None
        self._id = None

class Element(object):
    def __init__(self,name,id) -> None:
        self._name = name
        self._id = id
        self._k = None
        self._mass = None
        self._id = None


class Structure(object):
    def __init__(self,name) -> None:
        self._name = name

    @classmethod
    def assmble(cls,ele:Element):








class EquAxb(object):

    def __init__(self, name, dim) -> None:
        self._name = name
        self._dim = dim
        self._A = None
        self._b = None

    @property
    def name(self):
        return self._name

    @property
    def dim(self):
        return self._dim

    @property
    def A(self):
        return self._A

    @property
    def b(self):
        return self._b

    @A.setter
    def A1(self, data: np.array, i: np.array, j: np.array):
        self._A = ss.coo_array((data, (i, j)), (self.dim, self.dim))

    @A.setter
    def A2(self, data: np.array):
        self._A = data

    @A.setter
    def A_from_file(self, ind: Tuple[int, int, int], fname: str, header: int):

        data = np.empty(self.dim, dtype=float)
        i = np.empty(self.dim, dtype=int)
        j = np.empty(self.dim, dtype=int)
        count = 0
        with open(fname, 'r') as f:
            while header:
                next(f)
                header -= 1

            for count in range(self.dim):
                line = f.readlines()[count]
                info = line.split()
                data[count] = float(info[ind[0]])
                i[count] = float(info[ind[0]])
                j[count] = float(info[ind[0]])

        self._A = ss.coo_array((data, (i, j)), (self.dim, self.dim))

    @b.setter
    def b_from_data(self):
        pass

    @b.setter
    def b_from_file(self):
        pass

    def solve(self):
        pass


a = EquAxb('test', 3)
data = np.array([5, 5, 5])
i = np.array([0, 1, 2])
j = np.array([0, 1, 2])
