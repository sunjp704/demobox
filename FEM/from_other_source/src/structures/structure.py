from abc import ABC, abstractmethod
from math import sqrt
from typing import Optional, Tuple

import numpy as np

from src.material import Material
from src.section import Section


def gauss_jordan(A, i):
    A[i, :] = A[i, :] / A[i, i]
    _r = list(range(A.shape[0]))
    _r.remove(i)
    _c = list(range(A.shape[1]))
    _c.remove(i)
    A[_r, _c] = A[_r, _c] - A[_r, [i]] * A[[i], _c]


class AbstractNode(ABC):

    @classmethod
    @abstractmethod
    def distance(cls):
        pass


class Node(AbstractNode):

    def __init__(self, info: Tuple[str | int, str | float, str | float]) -> None:
        self._id = int(info[0])
        self._coordinate = tuple(map(float, info[1:]))

    @property
    def id(self):
        return self._id

    @property
    def coordinate(self):
        return self._coordinate


class Node2D(Node):

    @classmethod
    def distance(cls, node1: Node, node2: Node):
        return sqrt((node1.coordinate[0] - node2.coordinate[0])**2 +
                    (node1.coordinate[1] - node2.coordinate[1])**2)


class Node3D(Node):

    @classmethod
    def distance(cls, node1: Node, node2: Node):
        return sqrt((node1.coordinate[0] - node2.coordinate[0])**2 +
                    (node1.coordinate[1] - node2.coordinate[1])**2 +
                    (node1.coordinate[2] - node2.coordinate[2])**2)


class AbstractElement(ABC):
    pass


class Element2D(AbstractElement):

    @abstractmethod
    def element_stiffness_matrix(self):
        pass

    def condense(self):
        pass


class Element3D(AbstractElement):

    @abstractmethod
    def element_stiffness_matrix(self):
        pass

    def condense(self):
        pass


class EulerBernoulliBeam2D(Element2D):

    def __init__(self,
                 id: int,
                 end_i: Node2D,
                 end_j: Node2D,
                 release: Optional[Tuple[bool, bool, bool, bool, bool, bool]] = None,
                 material: Optional[Material] = None,
                 section: Optional[Section] = None) -> None:
        self._id = id
        self._end_i = end_i
        self._end_j = end_j
        self._length = Node2D.distance(end_i, end_j)
        self._release = release
        self._material = material
        self._section = section
        self._K = self.element_stiffness_matrix()

    @property
    def length(self):
        return self._length

    @property
    def material(self):
        return self._material

    @property
    def section(self):
        return self._section

    @property
    def K(self):
        return self._K

    @property
    def release(self):
        return self._release

    def element_stiffness_matrix(self):
        if self._material is None or self._section is None:
            return None
        else:
            E = self._material.E
            A = self._material.A
            Iz = self._section.Iz
            L = self._length
            k_up = np.array([[E * A / L, 0, 0, -E * A / L, 0, 0],
                             [
                                 0, 12 * E * Iz / L**3, 6 * E * Iz / L**2, 0, -12 * E * Iz / L**3,
                                 6 * E * Iz / L**2
                             ], [0, 0, 4 * E * Iz / L, 0, -6 * E * Iz / L**2, 2 * E * Iz / L],
                             [0, 0, 0, E * A / L, 0, 0],
                             [0, 0, 0, 0, 12 * E * Iz / L**3, -6 * E * Iz / L**2],
                             [0, 0, 0, 0, 0, 4 * E * Iz / L]])
            k = k_up + k_up.T - np.diag(k_up.diagonal())
            return k


#    def condense(self):
#        if self.release is not None:
#            for dof in range(6):
#                if self.release[dof]:
#                    gauss_jordan(np.hstack((self.K, self.P)), dof)
#            self.K_P = None
#


class EulerBernoulliBeam3D(Element3D):

    def __init__(self, id, material: Material, section: Section) -> None:
        self._id = id
        self._material = material
        self._sec = section
        self._K_e = self.element_stiffness_matrix()

    def element_stiffness_matrix(self):
        pass


class TimoshenkoBeam2D(Element2D):
    pass


class ElementFactory(ABC):

    @staticmethod
    @abstractmethod
    def create_EulerBernoulliBeam():
        pass

    @abstractmethod
    def create_TimoshenkoBeam():
        pass


class Element2DFactory(ElementFactory):

    @staticmethod
    def create_EulerBernoulliBeam(id: int,
                                  end_i: Node2D,
                                  end_j: Node2D,
                                  release: Optional[Tuple[bool, bool, bool, bool, bool,
                                                          bool]] = None,
                                  material: Optional[Material] = None,
                                  section: Optional[Section] = None):
        return EulerBernoulliBeam2D(id, end_i, end_j, release, material, section)

    def create_TimoshenkoBeam():
        return TimoshenkoBeam2D()


class Element3DFactory(ElementFactory):

    def create_EulerBernoulliBeam():
        return EulerBernoulliBeam3D()


# class Beam(Element):
#
#     def __init__(self, name, id) -> None:
#         self._name = name
#         self._id = id
#         self._k = None
#         self._mass = None
#         self._id = None
#
#     def assemble(self, struc: Structure):
#         pass

# class Shell(Element):
#
#     def __init__(self, name, id) -> None:
#         self._name = name
#         self._id = id
#         self._k = None
#         self._mass = None
#         self._id = None
#
#     def assemble(self, struc: Structure):
#         pass

# class Link(Element):
#
#     def __init__(self, name, id) -> None:
#         self._name = name
#         self._id = id
#         self._k = None
#         self._mass = None
#         self._id = None
#
#     def assemble(self, struc: Structure):
#         pass


class Structure(ABC):
    pass


class Structure2D(Structure):
    pass


class Structure3D(Structure):
    pass


class Frame2D(Structure2D):

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


class Frame3D(Structure3D):
    pass


class Conductor2D(Structure2D):
    pass


class Conductor3D(Structure3D):
    pass


class StructureFactory(ABC):

    @abstractmethod
    def frame_from_file():
        pass

    def conductor_from_file():
        pass


class StructureFactory2D(StructureFactory):

    @staticmethod
    def frame_from_file(name, node_info: Tuple[str, int], conn_info: Tuple[str, int]):
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
            _factory = Element2DFactory()
            for line in f.readlines():
                _info = line.split()
                if len(_info) == 3 or _info[3] == 'Euler-Bernuoli':
                    element_collection.append(
                        _factory.create_EulerBernoulliBeam(int(_info[0]),
                                                           node_collection[int(_info[1]) + 1],
                                                           node_collection[int(_info[2]) + 1]))
                elif _info[3] == 'Timoshenko':
                    raise RuntimeError('undefined beam element type')
                    # element_collection.append(_factory.create_TimoshenkoBeam())
                else:
                    raise RuntimeError('undefined beam element type')
        return Frame2D(name, node_collection, element_collection)

    def conductor_from_file():
        return Conductor2D()


class StructureFactory3D(StructureFactory):

    def frame_from_file():
        return Frame3D()

    def conductor_from_file():
        return Conductor3D()
