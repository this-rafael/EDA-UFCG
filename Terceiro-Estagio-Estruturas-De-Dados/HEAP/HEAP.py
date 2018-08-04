from Util import swapElementsInArray


def parent(i):
    return i // 2


def right(i):
    return (2 * i) + 1


def left(i):
    return 2 * i


class HEAP:
    INITIAL_SIZE = 20
    index = -1

    def __init__(self):
        self.heap = [None] * self.INITIAL_SIZE

    def toArray(self):
        array = [None] * (self.index + 1)

        i = self.index;
        while i >= 0:
            array[i] = self.heap[i]
            i -= 1

    def insert(self, element):
        self.index += 1  # Cresce o indice do heap

        i = self.index  # Define uma variavel para caminha na lista

        self.insereOrdenado(element, i)

        self.heap[i] = element  # Insert a new element

    """
    Insert a new element in "tail" of heap, and swap your value for up, the value. if this is a bigger of you parent
    """

    def insereOrdenado(self, element, i):
        while i >= 0 and self.heap[parent(i)] < element:
            swapElementsInArray(self.heap, parent(i), element)
            i = parent(i)

    def remove(self):
        max = self.heap[0] # function return

        self.heap[0] = self.heap[self.index]  # swap the smaller element in heap for a a postion zero
        self.index -= 1

        self.heapify(0)  # swap down a smaller element in heap  arranging the heap

        return max;  # Return ever the bigger  element in heap

    def heapify(self, index):
        l = left(index)
        r = right(index)
        maxPOSITION = index


        if l <= len(self.heap) and self.heap[l] > self.heap[index]:
            maxPOSITION = l
        elif r <= len(self.heap) and self.heap[r] > self.heap[index]:
            maxPOSITION = r


        if maxPOSITION != index:
            swapElementsInArray(self.heap, index, maxPOSITION)
            self.heap(maxPOSITION)
