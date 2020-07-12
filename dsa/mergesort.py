def merge_sort(list): 
  
    if len(list)>1: 
        m = len(list)//2
        left = list[:m] 
        right = list[m:] 
        left = merge_sort(left) 
        right = merge_sort(right) 
  
        list =[] 
  
        while len(left)>0 and len(right)>0: 
            if left[0]<right[0]: 
                list.append(left[0]) 
                left.pop(0) 
            else: 
                list.append(right[0]) 
                right.pop(0) 
  
        for i in left: 
            list.append(i) 
        for i in right: 
            list.append(i) 
                  
    return list 
  

a = [9,6,8,4,7,2,1]  
a = merge_sort(a) 
print("Sorted values: ",*a) 

  
