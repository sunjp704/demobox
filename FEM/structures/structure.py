from abc import ABC


class Structure(ABC):

    def __init__(self, name, nodes, elements) -> None:
        self._name = name
        self._nodes = nodes
        self._elements = elements


class StructureFactory(ABC):
    pass
