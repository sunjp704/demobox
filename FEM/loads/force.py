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
