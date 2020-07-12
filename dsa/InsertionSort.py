def insertionSort(list):
    for step in range(1, len(list)):
        key = list[step]
        j = step - 1      
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = key

list_data = [9,6,8,4,7,2,1]
insertionSort(list_data)
print('Sorted using insertion sort:',list_data)
