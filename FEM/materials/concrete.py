import json
from material import Material, MaterialFactory


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
            mtrl = Concrete('Concrete', name, rho, E, nu, A, G, fck)
            return mtrl
