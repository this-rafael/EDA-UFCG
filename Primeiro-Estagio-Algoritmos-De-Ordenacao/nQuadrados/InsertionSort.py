import Util


def ordenedInsertion(array, start, end, index):
    for i in range(end, start - 1, -1):
        if array[index] < array[i]:
            Util.swapInArray(array, index, i)
            index = i# update index




def insertionSort(array):
    for i in range(0,len(array) - 1):
        ordenedInsertion(array, 0, i, i + 1)


l = [44, 43, 21, 4, 62, 29, 60, 11, 40, 51, 99,-1]
insertionSort(l)
print(l)