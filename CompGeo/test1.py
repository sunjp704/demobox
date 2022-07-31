class Haha(object):

    def __init__(self, a, b) -> None:
        try:
            self.a = a
            self.b = b
            if a <= 4:
                raise Exception('要大于4')
        except Exception as e:
            print(e)

    def __str__(self) -> None:
        return str(self.a) + '\t' + str(self.b)

    def __eq__(self, __other) -> bool:
        return self.__dict__ == __other.__dict__


v1 = Haha(1, 2)
v2 = Haha(3, 4)
v3 = Haha(5, 6)
v4 = Haha(7, 8)
v5 = Haha(9, 10)

T1 = Haha(v1, v2)
T2 = Haha(v3, v4)
