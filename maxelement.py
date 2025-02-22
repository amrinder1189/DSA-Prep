arr = [2,9,4,3,1,0]
n = len(arr)
answer = arr[0]

for i in range(n):
    if(arr[i] > answer):
        answer = arr[i]
        
print(answer)


// space complexity  -1 
// time ""   - o(n)