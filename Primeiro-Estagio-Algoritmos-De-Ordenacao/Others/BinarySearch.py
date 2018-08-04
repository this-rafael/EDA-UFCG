def recursiveBinarySearch(array, element):  # for correct running of this function the array must be ordered
    return  __recursiveBinarySearch__(array, element, 0, len(array) - 1)


def __recursiveBinarySearch__(array, element, firstIndex, lastIndex):
    if firstIndex <= lastIndex:
        middle = (firstIndex + lastIndex) // 2
        if array[middle] == element:
            return middle
        else:
            if  element > array[middle]:
                return __recursiveBinarySearch__(array, element, middle + 1, lastIndex)
            else:
                return __recursiveBinarySearch__(array, element, firstIndex, middle - 1)
    else:
        return


