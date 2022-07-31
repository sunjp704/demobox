class Node(object):

    def __init__(self, key, value, left=None, right=None) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BST(object):

    def __init__(self):
        self.root = None

    def isEmpty(self, root):
        return self.root is not None

    def clear(self):
        if self is not None:
            self.root = None
            self = None
        return

    def heightOfBST(self):  # 左右子树中最高的一个的高度+1
        if self.root is None:
            return 0
        if self.root.left is None and self.root.right is None:
            return 1
        if self.root.left is None and self.root.right:
            return self.root.right.heightOfBST() + 1
        if self.root.right is None and self.root.left:
            return self.root.left.heightOfBST() + 1
        else:
            HL = self.root.left.heightOfBST()
            HR = self.root.right.heightOfBST()
            if HL > HR:
                return HL + 1
            else:
                return HR + 1

    def printInOrder(self):  # 按顺序输出即中序遍历：左-根-右
        result = []
        if self.root is None:
            return
        if self.root.left is not None and self.root.left.printInOrder() is not None:
            # print([self.root.key,self.root.value])
            for i in self.root.left.printInOrder():
                result.append(i)
        result.append(self.root.key)
        result.append(self.root.value)
        if self.root.right is not None and self.root.right.printInOrder() is not None:
            # print(self.root.key,self.root.value)
            for i in self.root.right.printInOrder():
                result.append(i)
        return result

    def numOfNodes(self):
        numOfNode = 0
        if self.root is None:
            return numOfNode
        numOfNode = 1
        # numOfNode = numOfNode+1
        if self.root.left is not None:
            numOfNode = numOfNode + self.root.left.numOfNodes()
        if self.root.right is not None:
            numOfNode = numOfNode + self.root.right.numOfNodes()
        return numOfNode

    def showStructure(self):
        print('-' * 28)
        # print('There are {} nodes in this BST'.format(self.numOfNodes()))
        print('There are {} nodes in this BST'.format(int(len(self.printInOrder()) / 2)))
        print('The height of this BST is', self.heightOfBST())
        print('-' * 28)

    def search(self, key):
        if self.root is None:  # 二叉树为空
            print('search unsuccessful --' + key)
            return
        elif self.root.key == key:
            print('search success --' + key + ' ' + self.root.value)
            return True
        elif self.root.left is not None and key < self.root.key:
            return self.root.left.search(key)
        elif self.root.right is not None and key > self.root.key:
            return self.root.right.search(key)
        else:
            print('search unsuccessful --' + key)
            return

    def update(self, key, value):
        if self.root is None:  # 二叉树为空
            return False
        elif self.root.key == key:
            self.root.value = value
            print('update success --' + key + ' ' + value)
            return self.root
        elif key < self.root.key:
            if self.root.left is not None:
                if self.root.left.root is not None:
                    self.root.left.update(key, value)
        elif key > self.root.key:
            if self.root.right is not None:
                if self.root.right.root is not None:
                    self.root.right.update(key, value)
        else:
            print('update unsuccessful --' + key)
            return

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
            # print(self.root.key,self.root.value)
            # print('insert success --'+key)
            return
        elif self.root is not None:  # 二叉树非空
            if key < self.root.key:
                if self.root.left is None:
                    new_tree = BST()
                    new_tree.insert(key, value)
                    self.root.left = new_tree
                    # print('insert success --'+key)
                    return
                else:
                    self.root.left.insert(key, value)
            elif key > self.root.key:
                if self.root.right is None:
                    new_tree = BST()
                    new_tree.insert(key, value)
                    self.root.right = new_tree
                    # print('insert success --'+key)
                    return
                else:
                    self.root.right.insert(key, value)
            else:  # key值相同，无需再加入
                self.root = self.update(key, value)
                print('insert success --' + key)
                return

    def remove(self, key):
        # 首先寻找节点
        if self.root is None:  # 二叉树为空
            print('remove unsuccessful --' + key)
            return
        elif self.root.key == key:
            # 情况1：被删除的节点没有子节点
            if self.root.left is None and self.root.right is None:
                # print('aaaaaaaa')
                print('remove success --' + self.root.value)
                self.root = None
                return
            # 情况2：被删除的节点仅有一个子节点
            elif self.root.left is None:
                # print('bbbbbbbb')
                print('remove success --' + self.root.value)
                self = self.root.right
                return
            elif self.root.right is None:
                # print('cccccccc')
                print('remove success --' + self.root.value)
                # print(self.root.left.root.key)
                self = self.root.left
                # print(self.root.key)
                return True
            # 情况3：被删除的节点有两个子节点,则寻找右子树最小值
            else:
                # print('dddd')
                print('remove success --' + self.root.value)
                # print(self.root.left is None)
                # print(getMin(self.root.right).key)
                # print(deleteMin(self.root.right).root.key)
                tempkey = getMin(self.root.right).key
                tempvalue = getMin(self.root.right).value
                self.root.key = tempkey
                self.root.value = tempvalue
                self.root.right = deleteMin(self.root.right)
                # print(self.root.left is None)
                return True
        elif self.root.left is not None and key < self.root.key:
            self.root.left.remove(key)
        elif self.root.right is not None and key > self.root.key:
            self.root.right.remove(key)
        else:
            print('remove unsuccessful --' + key)
            return


def getMin(self):
    if self is None or self.root is None:
        return
    if self.root.left is None:
        return self.root
    else:
        return getMin(self.root.left)


def deleteMin(self):
    if self is None or self.root is None:
        return
    if self.root.left is None:
        return self.root.right
    else:
        self.root.left = deleteMin(self.root.left)
        return self


t = BST()
t.insert('great', 'adj. 极好的')
t.insert('abstract', 'adj. 抽象的')
t.insert('absolute', 'adj. 绝对的')
t.insert('solution', 'n. 解决方案')
t.insert('allow', 'v. 允许')
t.insert('clear', 'v. 清除')
t.insert('hello', 'int. 你好')
t.update('hello', 'int. 你好!')
# t.search('hello')
# t.search('hi')
# for i in range(0, len(t.printInOrder()) - 1, 2):
#     print(t.printInOrder()[i] + ' ' + t.printInOrder()[i + 1])
# print(t.showStructure())
# a = ['absolute', 'abstract', 'allow', 'clear', 'hello', 'solution']
# for i in range(6):
#     print("删除" + a[i])
#     t.remove(a[i])
# print(t.printInOrder())
