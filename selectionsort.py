
# ---------------- selection sort ----------------


arr = [4,3,6,1,0]
n = len(arr)


for i in range(n):
    min = i
    for j in range(i+1,n):
        if(arr[min] > arr[j]):
            min = j
        
        arr[min],arr[i] = arr[i],arr[min]
        
print(arr)