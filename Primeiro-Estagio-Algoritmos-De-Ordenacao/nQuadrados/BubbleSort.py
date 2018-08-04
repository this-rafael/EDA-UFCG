import Util


def BubbleSort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array) -1):
            if array[j] > array[j + 1]:
                Util.swapInArray(array, j, j+1)


l = [44, 43, 21, 4, 62, 29, 60, 11, 40, 51]
BubbleSort(l)
print(l)