class Node(object):

    def __init__(self, key, value, left=None, right=None, parent=None) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    # def copy(self):
    #     return Node(self.key, self.value, self.left, self.right, self.parent)

    def __eq__(self, __other: object) -> bool:

        if isinstance(__other, self.__class__):
            return self.__dict__ == __other.__dict__
        else:
            return False


class BinSchTree(object):

    def __init__(self, node: Node) -> None:
        node.parent = None
        self._root = node

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, val):
        self._root = val

    def is_empty(self):
        return self.root is None

    def __walk(self, node: Node) -> None:
        if node is not None:
            self.__walk(node.left)
            print(str(node.key) + ':\t' + str(node.value))
            self.__walk(node.right)

    def walk(self) -> None:
        self.__walk(self.root)

    def __search(self, node: Node, key):
        # iteration
        while node is not None and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node

        # recursion
        # if node is None or key==node.key:
        #     return node
        # if key<node.key:
        #     return self.__search(node.left,key)
        # else:
        #     return self.__search(node.right, key)

    def search(self, key):
        self.__search(self.root, key)

    def __min(self, node: Node):
        while node.left is not None:
            node = node.left
        return node

    def min(self):
        self.__min(self.root)

    def __max(self, node: Node):
        while node.left is not None:
            node = node.left
        return node

    def max(self):
        self.__max(self.root)

    def successor(self, node: Node):
        if node.right is not None:
            return self.__min(node.right)
        p = node.parent
        while p is not None and node == p.right:
            node = p
            p = p.parent
        return p

    def predecessor(self, node: Node):
        if node.left is not None:
            return self.__max(node.left)
        p = node.parent
        while p is not None and node == p.left:
            node = p
            p = p.parent
        return p

    def insert(self, node: Node) -> None:
        cur = self.root
        p = None
        while cur is not None:
            p = cur
            if node.key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        node.parent = p
        if p is None:
            self.root = node
        elif node.key < p.key:
            p.left = node
        else:
            p.right = node

    def transplant(self, position: Node, plant: Node):
        if position.parent is None:
            self.root = plant
        elif position == position.parent.left:
            position.parent.left = plant
        else:
            position.parent.right = plant
        if plant is not None:
            plant.parent = position.parent

    def delete(self, node: Node):
        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            min = self.__min(node.right)
            if not min.parent == node:
                self.transplant(min, min.right)
                min.right = node.right
                min.right.parent = min
            self.transplant(node, min)
            min.left = node.left
            min.left.parent = min

    def draw(self):
        pass
