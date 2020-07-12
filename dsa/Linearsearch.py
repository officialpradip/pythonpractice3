def linearSearch(list, n, x):
    for i in range(0, n):
        if (list[i] == x):
            return i
    return -1
list = [9,6,8,4,7,2,1]
x = 1
n = len(list)
result = linearSearch(list, n, x)
if(result == -1):
    print("Not found")
else:
    print("Found at index: ", result)