from abc import ABC


class Solver(ABC):
    pass


class LinearStatic(Solver):

    def assemble():
        pass

    def condense():
        pass

    def run():
        pass


class Modal(Solver):
    pass


class Nonlinear(Solver):
    pass
