from abc import ABC, abstractmethod
from math import pi
from numpy import interp


class Section(ABC):

    def __init__(self) -> None:
        self._A = self.area()
        self._Iz = self.moment_of_inertia_z()
        self._Iy = self.moment_of_inertia_y()
        self._J = self.torsional_moment_of_inertia()

    @property
    def A(self):
        return self._A

    @property
    def Iz(self):
        return self._Iz

    @property
    def Iy(self):
        return self._Iy

    @property
    def J(self):
        return self._J

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def moment_of_inertia_z(self):
        pass

    @abstractmethod
    def moment_of_inertia_y(self):
        pass

    @abstractmethod
    def torsional_moment_of_inertia(self):
        pass


class Circle(Section):

    def __init__(self, d) -> None:
        self._d = d
        super().__init__()

    @property
    def d(self):
        return self._d

    def area(self):
        return pi * pow(self.d, 2) / 4

    def moment_of_inertia_z(self):
        return pi * pow(self.d, 4) / 64

    def moment_of_inertia_y(self):
        return pi * pow(self.d, 4) / 64

    def torsional_moment_of_inertia(self):
        return pi * pow(self.d, 4) / 32


class Rectangle(Section):

    def __init__(self, b, h) -> None:

        self._b = b
        self._h = h
        super().__init__()

    @property
    def b(self):
        return self._b

    @property
    def h(self):
        return self._h

    def area(self):
        return self.b * self.h

    def moment_of_inertia_z(self):
        return self.b * pow(self.h, 3) / 12

    def moment_of_inertia_y(self):
        return self.h * pow(self.b, 3) / 12

    def torsional_moment_of_inertia(self):
        _h_b = [1.0, 1.2, 1.5, 2.0, 2.5, 3.0, 4.0, 6.0, 8.0, 10.0]
        # _alpha = [0.208, 0.219, 0.231, 0.246, 0.258, 0.267, 0.282, 0.299, 0.307, 0.313, 0.333]
        _beta = [0.141, 0.166, 0.196, 0.229, 0.249, 0.263, 0.281, 0.299, 0.307, 0.313, 0.333]
        # _gamma = [1.000, 0.930, 0.858, 0.796, 0.767, 0.753, 0.745, 0.743, 0.743, 0.743, 0.743]
        h = max(self.h, self.b)
        b = min(self.h, self.b)
        beta = interp(h / b, _h_b, _beta[0:-1], right=_beta[-1])
        return beta * h * pow(b, 3)
