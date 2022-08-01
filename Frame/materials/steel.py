import json
from material import Material, MaterialFactory


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
