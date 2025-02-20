
# ------------- bubble sort -----------------

arr = [4,3,6,1,0]
n = len(arr)

print(arr)
print("array before the array is sorted :")



for i in range(n):
    swapped = False
    for j in range(0,n-i-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]
            swapped = True
        
    if swapped == False:
        break
        
        
        
print("before that:")
print(arr)

