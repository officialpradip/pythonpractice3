
def bubbleSort(list):
    for i in range(len(list)):
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                (list[j], list[j + 1]) = (list[j + 1], list[j])
list_data= [9,6,8,4,7,2,1]
bubbleSort(list_data)
print('Sorted list:',list_data)
