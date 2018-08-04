from BasicNode.Node import Node
from Functions.Util import swap


class BST:

    def __init__(self):
        self.root = Node("NIL")

    """
    check if the root's node is a NIL object
    """

    def isEmpty(self):
        return self.root.isNIL()

    """
    :return the difference between the root and a deeper leaf
    """

    def height(self):
        return self.__height__(self.root)

    """
    :return compares the height of the left and right, and returns the largest of them, and adds one more to the current
     node
    """

    def __height__(self, node: Node):
        if not node.value is None and not node.isNIL():
            left = self.__height__(node.left)
            right = self.__height__(node.right)
            return 1 + max(left, right)
        else:
            return -1

    """
    :return the bigger element in BST. the element at the right end.
    """

    def max(self):
        return self.__max__(self.root)

    """
    :return the lower element in BST. the element at the left end.
    """

    def min(self):
        return self.__min__(self.root)

    def __max__(self, node):
        aux = node

        while not aux.right.isNIL():
            aux = aux.right
        return aux

    def __min__(self, node):
        aux = node

        while not aux.left.isNIL():
            aux = aux.left
        return aux

    """
    insert a new Node in BST
    """

    def insert(self, element):
        if self.isEmpty():  # configure a root element
            self.root.value = element
            self.root.left = Node("NIL")
            self.root.right = Node("NIL")
            self.root.parent = Node("NIL")

            # set parent for NIL NODES
            self.root.left.parent = self.root
            self.root.right.parent = self.root
        else:
            self.__insert__(self.root, element)

    def __insert__(self, node, element):

        if node.isNIL():

            # Set the value for the current node if isNIL
            node.value = element

            # Make NIL nodes
            node.left = Node("NIL")
            node.right = Node("NIL")

            # set parent for NIL NODES
            node.left.parent = node
            node.right.parent = node

        elif element > node.value:
            self.__insert__(node.right, element)

        elif element < node.value:
            self.__insert__(node.left, element)

    """
    find a node, for your data (element) and
    :returns  
        * None if the element do not exist in BST
        * The node that contains the date that is equal to the element   
    """

    def search(self, element):
        return self.__search__(self.root, element)

    def __search__(self, node, element):
        if node.value == element:
            return node

        elif node.isNIL():
            return None

        elif element > node.value:
            return self.__search__(node.right, element)

        elif element < node.value:
            return self.__search__(node.left, element)

    """
    :return a number immediately previous of node
    """
    def predecessor(self, element):

        node = self.search(element)

        if not (node is None) and node.value != self.min().value:
            return self.__predecessor__(node)

    def __predecessor__(self, node):
        answer = None

        if not (node.left.isNIL()):  # if exists a left, the predecessor of the node,
            #  will be the max element in the left
            answer = self.__max__(node.left)
        else:
            parent = node.parent

            while not parent.isNIL() and parent.left.value == node.value:
                node = node.parent
                parent = parent.parent

            answer = parent

        return answer

    """
    :return a number immediately successor of node
    """
    def sucessor(self, element):
        node = self.search(element)
        if not (node is None) and node.value != self.max().value:
            return self.__sucessor__(node)

    def __sucessor__(self, node):
        answer = None

        if not (node.right.isNIL()):
            answer = self.__min__(node.right)
        else:

            parent = node.parent

            while not parent.isNIL() and parent.right.value == node.value:
                node = node.parent
                parent = parent.parent

            answer = parent
        return answer

    '''
    removes a node from bst with a value equal to the parameter (element)
    '''
    def remove(self, element):
        node = self.search(element)
        if not (node.isNIL()):
            self.__remove__(node)

    def __remove__(self, node: Node):

        if node.isLeaf():
            node.makeNIL()

        elif not node.right.isNIL():
            successor = self.__sucessor__(node)
            swap(node, successor)
            self.__remove__(successor)
        else: # if not is left and the right don't exist, is the case, to remove with the predecessor.
            predecessor = self.__predecessor__(node)
            swap(node, predecessor)
            self.__remove__(predecessor)
    
    def __eq__(self, other):
        if isinstance(self, other, ):
            return self.root.__eq__(other.root)

    def size(self):
        return self.__size__(self.root)

    def __size__(self, node):
        answer = 0
        if not (node is None or node.isNIL()):
            answer += 1
            answer += self.__size__(node.left)
            answer += self.__size__(node.right)

        return  answer

    def preOrder(self):
        return self.__preOrder__(self.root)

    def __preOrder__(self, node) -> list:
        answer: list = []
        if not node is None and not node.isNIL():
            answer.append(node.__str__())
            answer += self.__preOrder__(node.left)
            answer += self.__preOrder__(node.right)
        return answer
    def order(self):
        return self.__order__(self.root)

    def __order__(self, node) -> list:
        answer: list = []
        if not(node is None or node.isNIL()):
            answer += self.__preOrder__(node.left)
            answer.append(node)
            answer += self.__preOrder__(node.right)
    def postOrder(self):
        return self.__postOrder__(self.root)

    def __postOrder__(self, node) -> list:
        answer: list = []
        if not(node is None or node.isNIL()):
            answer += self.__preOrder__(node.left)
            answer += self.__preOrder__(node.right)
            answer.append(node)





