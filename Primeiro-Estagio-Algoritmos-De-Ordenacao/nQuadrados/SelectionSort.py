import Util


def selectMin(array, i, j):
    min = i

    for k in range(i,j):
        if array[k] < array[min]:
            min = k
    return min


def SelectionSort(array):
    for i in range(len(array)):
        min = selectMin(array, i, len(array))
        Util.swapInArray(array,i,min)

l = [44, 43, 21, 4, 62, 29, 60, 11, 40, 51]
SelectionSort(l)
print(l)