"""
this method exchanges the value of two nodes
"""
def swap(node, otherNode):
    node.value, otherNode.value = otherNode.value, node.value

def swapElementsInArray(array, i, j):
        array[i], array[j] = array[j], array[i]