from typing import Tuple
from structure import Structure, StructureFactory
from ..elements.node import Node2D
from ..elements.beam2d import Beam2DFactory


class Frame2D(Structure):

    def __init__(self, name, nodes, elements) -> None:
        self._name = name
        self._nodes = nodes
        self._elements = elements

    @property
    def name(self):
        return self._name

    @property
    def nodes(self):
        return self._nodes

    @property
    def elements(self):
        return self._elements

    @classmethod
    def from_file(cls, name, node_info: Tuple[str, int], conn_info: Tuple[str, int]):
        _n_fname = node_info[0]
        _n_header = node_info[1]
        node_collection = []
        with open(_n_fname) as f:
            while _n_header:
                next(f)
                _n_header -= 1
            for line in f.readlines():
                _info = line.split()
                node_collection.append(Node2D(_info))

        _c_fname = conn_info[0]
        _c_header = conn_info[1]
        element_collection = []
        with open(_c_fname) as f:
            while _c_header:
                next(f)
                _c_header -= 1
            _factory = Beam2DFactory()
            for line in f.readlines():
                _info = line.split()
                if len(_info) == 3 or _info[3] == 'Euler-Bernuoli':
                    element_collection.append(
                        _factory.create_EulerBernoulliBeam(int(_info[0]), node_collection[int(_info[1]) + 1],
                                                           node_collection[int(_info[2]) + 1]))
                elif _info[3] == 'Timoshenko':
                    raise RuntimeError('undefined beam element type')
                    # element_collection.append(_factory.create_TimoshenkoBeam())
                else:
                    raise RuntimeError('undefined beam element type')
        return Frame2D(name, node_collection, element_collection)


class Frame2DFactory(StructureFactory):

    @staticmethod
    def create_frame(name, node_info: Tuple[str, int], conn_info: Tuple[str, int]):
        Frame2D.from_file(name, node_info, conn_info)
