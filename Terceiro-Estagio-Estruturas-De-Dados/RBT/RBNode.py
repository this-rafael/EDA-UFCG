from BasicNode.Node import Node

class RBNode(Node):

    __COLORS__ = ("BLACK", "RED")


    def __init__(self, value):
        super.__init__(value)
        self.color = self.__COLORS__[0]

    def __eq__(self, other):
        if not isinstance(other, RBNode):
            return False
        else:
            return super.__eq__(other) and other.color == self.color

    def __str__(self):
        retorno = ""

        retorno += super.__str__()

        if(self.color == "RED"):
            retorno += " COLOR: RED"
        else:
            retorno += " COLOR; BLACK"

        return retorno