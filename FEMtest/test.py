import concurrent.futures
from multiprocessing import shared_memory
import ctypes


class Data(object):

    def __init__(self, dname, value) -> None:
        self._dname = dname
        self._value = value

    @property
    def dname(self):
        return self._dname

    @property
    def value(self):
        return self._value

    @dname.setter
    def dname(self, dname):
        self._dname = dname

    def plus1(self, i):
        self._value[i] = 1


def main():
    mymodel = Data('sapmodel', [0, 0, 0, 0])
    address = id(mymodel)
    a1 = shared_memory.ShareableList([address])

    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        executor.submit(ctypes.cast(shared_memory.ShareableList(name=a1.shm.name)[0], ctypes.py_object).value.plus1(0))
        executor.submit(ctypes.cast(shared_memory.ShareableList(name=a1.shm.name)[0], ctypes.py_object).value.plus1(1))
        executor.submit(ctypes.cast(shared_memory.ShareableList(name=a1.shm.name)[0], ctypes.py_object).value.plus1(2))
        executor.submit(ctypes.cast(shared_memory.ShareableList(name=a1.shm.name)[0], ctypes.py_object).value.plus1(3))

    # executor.submit(ctypes.cast(shared_memory.ShareableList(name=a1.shm.name)[0], ctypes.py_object).value.plus1(3))
    a1.shm.unlink()
    print(mymodel.value)


if __name__ == '__main__':
    main()
