import BST.BST
from BasicNode.Node import Node
from Functions.Util import swap

class AVL(BST):

    def balance(self, node: Node):
        return self.__height__(node.left) - self.__height__(node.right)

    def rotationLeft(self, node: Node):
        pivot = node.right
        pivotRS = pivot.left

        # Perform rotation
        pivot.left = node
        node.right = pivotRS

        pivot.parent = node.parent
        node.parent = pivot

    def rotationRigh(self, node: Node):

        pivot = node.left
        pivotOS = pivot.right

        pivot.right = node
        node.right = pivotOS

        pivot.parent = node.parent
        node.parent = pivot

    def rebalance(self, node: Node):
        if self.balance(node) >= 2:  # node is unbalanced for left
            if self.balance(node.left) <= -1:  # pivot pending for right
                self.rotationLeft(node.left)  # fix
            self.rotationRigh(node)

        elif self.balance(node) <= -2:  # node is unbalanced for right
            if self.balance(node.right) >= 1:  # pivot pending for left
                self.rotationRigh(node.right)
            self.rotationLeft(node)

    def rebalanceUp(self, node: Node):


        if not (node is None or node.isNIL()):
            self.rebalance(node)
            self.rebalanceUp(node.parent)

    def insert(self, element):
        super(AVL,self).insert(element)
        self.rebalanceUp(self.search(element))

    def remove(self, element):
        node = self.search(element)
        if not (node.isNIL()):
            return self.__remove__(node)
        else:
            return None

    def __remove__(self, node: Node):
        aux = node.value
        if node.isLeaf():
            node.makeNIL()
            if not node.parent.isNIL():
                self.rebalanceUp(node.parent)

        elif not (node.left.isNIL() and node.right.isNIL()):
            sucessor = self.__sucessor__(node)
            swap(node, sucessor)
            self.__remove__(sucessor)

        return aux
