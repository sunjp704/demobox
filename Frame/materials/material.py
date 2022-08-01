from abc import ABC, abstractmethod


class AbstractMaterial(ABC):
    pass


class MaterialFactory(ABC):

    @staticmethod
    @abstractmethod
    def create_material():
        pass


class Material(AbstractMaterial):

    def __init__(self, mtype=None, name=None, rho=None, E=None, nu=None, A=None, G=None) -> None:
        self._mtype = mtype
        self._name = name
        self._rho = rho
        self._E = E
        self._nu = nu
        self._A = A
        self._G = G

    @property
    def mtype(self):
        return self._mtype

    @property
    def name(self):
        return self._name

    @property
    def rho(self):
        return self._rho

    @property
    def E(self):
        return self._E

    @property
    def A(self):
        return self._A

    @property
    def G(self):
        return self._G
