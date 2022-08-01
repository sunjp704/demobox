from typing import Optional
from loads.load import Load

from solver import Solver
from ..structures.structure import Structure


class Case(object):

    def __init__(self, structure: Structure, load_collection: Optional[list] = None) -> None:
        self._stucture = structure
        self._loads = load_collection
        self._prev = None

    @property
    def structure(self):
        return self._stucture
    @property
    def prev(self):
        return self._prev

    @property
    def load_collection(self):
        return self._loads

    @prev.setter
    def prev(self, case):
        self._prev = case

    def add_load(self, load: Load):
        self._loads.append(load)

    def create_solver(self):
        pass


class LinearStatic(Solver):

    def __init__(self, case: Case) -> None:
        self._case = case
    @property
    def case(self):
        return self._case

    def assemble(self):
        for ele in self.case.structure.

    def condensen():
        pass

    def solve():
        pass
