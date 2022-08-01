from abc import ABC, abstractmethod
import json


class AbstractMaterial(ABC):
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


class Steel(Material):

    def __init__(self,
                 mtype=None,
                 name=None,
                 rho=None,
                 E=None,
                 nu=None,
                 A=None,
                 G=None,
                 ReH=None,
                 Rm=None) -> None:
        super().__init__(mtype, name, rho, E, nu, A, G)
        self._ReH = ReH
        self._Rm = Rm

    @property
    def ReH(self):
        return self._ReH

    @property
    def Rm(self):
        return self._Rm


class Concrete(Material):

    def __init__(self,
                 mtype=None,
                 name=None,
                 rho=None,
                 E=None,
                 nu=None,
                 A=None,
                 G=None,
                 fck=None) -> None:
        super().__init__(mtype, name, rho, E, nu, A, G)
        self._fck = fck

    @property
    def fck(self):
        return self._fck


class MaterialFactory(ABC):

    @staticmethod
    @abstractmethod
    def create_material(self):
        pass


class SteelFactory(MaterialFactory):

    @staticmethod
    def create_material(name: str):
        with open('materials.json') as f:
            mtrldict = json.load(f)['Steel'][name]
            rho = mtrldict['Density']
            E = mtrldict['ModulusOfElastisity']
            nu = mtrldict['Poisson']
            A = mtrldict['CoefficientOfThermalExpansion']
            G = mtrldict['ShearModulus']
            ReH = mtrldict['YieldStress']
            Rm = mtrldict['TensileStress']
            mtrl = Steel('Steel', name, rho, E, nu, A, G, ReH, Rm)
            return mtrl


class ConcreteFactory(MaterialFactory):

    @staticmethod
    def create_material(name: str):
        with open('materials.json') as f:
            mtrldict = json.load(f)['Concrete'][name]
            rho = mtrldict['Density']
            E = mtrldict['ModulusOfElastisity']
            nu = mtrldict['Poisson']
            A = mtrldict['CoefficientOfThermalExpansion']
            G = mtrldict['ShearModulus']
            fck = mtrldict['CharacteristicCompressiveStrength']
            mtrl = Steel('Concrete', name, rho, E, nu, A, G, fck)
            return mtrl
