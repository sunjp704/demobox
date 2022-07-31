from typing import Tuple
from ..elements.node import Node2D
from load import Load


class ConcendratedForce2D(Load):

    def __init__(self, position: Node2D, quantity: float, direction: Tuple[float, float]) -> None:
        self._position = position
        self._quantity = quantity
        self._direction = direction

    @property
    def position(self):
        return self._position

    @property
    def quantity(self):
        return self._quantity

    @property
    def direction(self):
        return self._direction


# class Case(object):
#
#     def __init__(self, name, load_collection: Optional[list] = None) -> None:
#         self._name = name
#         self._load_collection = load_collection
#         self._prev = None
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def prev(self):
#         return self._prev
#
#     @property
#     def load_collection(self):
#         return self._load_collection
#
#     @prev.setter
#     def prev(self, case):
#         self._prev = case
#
#     def add_load(self, load: Load):
#         self._load_collection.append(load)
