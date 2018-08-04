import Util


def partition(array, start, end): #Lomuto Partition
    pivot = start
    
    for i in range(start, end):
        if array[i] <= array[end]:
            Util.swapInArray(array, pivot, i)
            pivot += 1
    Util.swapInArray(array, pivot, end)
    return pivot

def Quick(array, start, end):
    if start < end:
        pivot = partition(array, start, end)
        Quick(array, start, pivot - 1)
        Quick(array, pivot + 1, end)


def QuickSort(array):
    Quick(array, 0, len(array) - 1)

l = [44, 43, 21, 4, 62, 29, 60, 11, 40, 51]
QuickSort(l)
print(l)