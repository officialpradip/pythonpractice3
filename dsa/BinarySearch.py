def binarySearch(list, x, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if list[mid] == x:
            return mid
        elif list[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

list = [9,6,8,4,7,2,1]
x = 4
result = binarySearch(list, x, 0, len(list)-1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")