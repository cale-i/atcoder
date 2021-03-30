# 2019/10/23

n=int(input())%30
arr=list(range(1,7))
mod=5
for i in range(n):
    idx=i%mod
    fst=arr[idx]
    snd=arr[idx+1]
    arr[idx],arr[idx+1]=snd,fst
print(*arr,sep='')