# 2020/01/05
# 累積和

from itertools import accumulate

n=int(input())
a=list(map(int,input().split()))
A=list(accumulate(a))
sum_a=A[-1]
max_a=max(a)

def divisors(n):
    div=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            div.append(i)
            if i!=n//i:
                div.append(n//i)
    div.sort()
    return div


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
        

div=divisors(sum_a)
res=[i for i in div if i>=max_a]


for r in res:
    div=sum_a//r
    for d in range(r,sum_a+1,r):
        ret=search(A,d,0,len(A))
        if ret<0:break
    else:
        print(div)
        exit()