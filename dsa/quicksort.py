
def partition(list, low, high):
    pivot = list[high]
    i = low - 1
    for j in range(low, high):
        if list[j] <= pivot:
            i = i + 1
            (list[i], list[j]) = (list[j], list[i])

    (list[i + 1], list[high]) = (list[high], list[i + 1])

    return i + 1


def quickSort(list, low, high):
    if low < high:
        pi = partition(list, low, high)
        quickSort(list, low, pi - 1)
        quickSort(list, pi + 1, high)


list_data = [9,6,8,4,7,2,1]
size = len(list_data)
quickSort(list_data, 0, size - 1)
print('Sorted list using quick sort:',list_data)
