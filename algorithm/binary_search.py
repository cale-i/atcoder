def search(arr,key,low,high):
    
    while True:
        mid=(high+low)//2
        if mid>=len(arr) or high<0 or low>high:
            return -1

        if arr[mid]==key:
            return mid

        elif arr[mid]>key:
            high=mid-1
        else:
            low=mid+1
        


arr=[3,4,8,11,200]
key=int(input())

res=search(arr,key,0,len(arr))
print(res)