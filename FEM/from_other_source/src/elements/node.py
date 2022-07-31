from abc import ABC, abstractmethod
from typing import Tuple
from math import sqrt


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
