arr = []
for k in range(10000,0,-1):
        arr.append(k)
lid = 0 
hid = 0 
mid = 0 

arrlen = len(arr) 
for x in range(1,arrlen): 
        hid = x        
        lid = 0
        mid = x//2     
        while True: 
                if (arr[x] <= arr[mid]) and (mid == lid): 
                        arr.insert(mid,arr.pop(x)) 
                        break 
                elif arr[x] < arr[mid] and mid != lid: 
                        hid = mid 
                        mid = lid + (hid - lid)//2                         
                elif arr[x] >= arr[mid] and (mid != hid and mid != lid): 
                        lid = mid   
                        mid = lid + (hid - lid)//2    
                elif arr[x] > arr[mid] and (mid == hid or mid == lid): 
                        arr.insert(mid+1,arr.pop(x)) 
                        break 
print(arr) 
