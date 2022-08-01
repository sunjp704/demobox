from typing import Optional


class EE(object):

    def __init__(self, id: int, section: Optional[float] = None) -> None:
        self._id = id
        self._section = section
        self._K = self.element_stiffness_matrix()

    def element_stiffness_matrix(self):
        if self._section is None:
            return None
        else:
            return 2 * self._section


class FF(EE):
    pass
