from abc import abstractmethod
from typing import Optional, Tuple
from scipy.sparse import lil_array, dia_array
from element import Element, ElementFactory
from node import Node2D
from ..materials.material import Material
from ..sections.section import Section


class Beam2D(Element):

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
        self._k = None
        self._m = None
        self._c = None

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
    def k(self):
        return self._k

    @property
    def release(self):
        return self._release

    @abstractmethod
    def element_stiffness_matrix(self):
        pass

    @abstractmethod
    def element_mass_matrix(self):
        pass

    @abstractmethod
    def element_damping_matrix(self):
        pass


class EulerBernoulliBeam2D(Element):

    def __init__(self, id, end_i, end_j, release, material, section) -> None:
        super().__init__(id, end_i, end_j, release, material, section)

    def element_stiffness_matrix(self: Beam2D):
        if self._material is None or self._section is None:
            return None
        else:
            E = self._material.E
            A = self._material.A
            Iz = self._section.Iz
            L = self._length
            k_up = lil_array([[E * A / L, 0, 0, -E * A / L, 0, 0],
                              [0, 12 * E * Iz / L**3, 6 * E * Iz / L**2, 0, -12 * E * Iz / L**3, 6 * E * Iz / L**2],
                              [0, 0, 4 * E * Iz / L, 0, -6 * E * Iz / L**2, 2 * E * Iz / L], [0, 0, 0, E * A / L, 0, 0],
                              [0, 0, 0, 0, 12 * E * Iz / L**3, -6 * E * Iz / L**2], [0, 0, 0, 0, 0, 4 * E * Iz / L]])
            k = k_up + k_up.transpose() - dia_array((k_up.diagonal(), 0), shape=(6, 6))
            self._k = k

    def element_mass_matrix(self: Beam2D):
        if self._material is None or self._section is None:
            return None
        else:
            m = self._material.rho * self._section.A * self._length
            self._m = 0.5 * dia_array(([m, m, 0, m, m, 0], 0), shape=(6, 6))

    def element_damping_matrix(self: Beam2D):
        if self._material is None or self._section is None:
            return None
        else:
            return None


class TimoshenkoBeam2D(Element):
    pass


class Beam2DFactory(ElementFactory):

    @staticmethod
    def create_EulerBernoulliBeam(id: int,
                                  end_i: Node2D,
                                  end_j: Node2D,
                                  release: Optional[Tuple[bool, bool, bool, bool, bool, bool]] = None,
                                  material: Optional[Material] = None,
                                  section: Optional[Section] = None):
        return EulerBernoulliBeam2D(id, end_i, end_j, release, material, section)

    def create_TimoshenkoBeam():
        return TimoshenkoBeam2D()
