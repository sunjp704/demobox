from abc import ABC, abstractmethod


class AbstractElement(ABC):
    pass


class ElementFactory(ABC):

    @abstractmethod
    def create_element():
        pass


class Element(AbstractElement):
    pass
