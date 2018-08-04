class Node:

    def __init__(self, value):
        if(value == "NIL"):
            self.value = "NIL"
        else:
            self.value = value
            self.parent = Node("NIL")
            self.left = Node("NIL")
            self.right = Node("NIL")



    def isNIL(self):
        return self.value == "NIL"

    def __str__(self):
        if not(self.value is None): return str(self.value)
        else : return ""

    def __eq__(self, other):
        return self.value == other.value and self.left__eq__(other.left) and self.right__eq__(
            other.right) and self.parent__eq__(other.parent)

    def makeNIL(self):
        self.value = "NIL"
        self.left = None
        self.right = None

    def isLeaf(self):
        return self.right.isNIL() and self.left.isNIL()
