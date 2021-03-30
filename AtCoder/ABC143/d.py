from bisect import bisect_left,bisect_right

n=int(input())
l=sorted(list(map(int,input().split())))
cnt=0
for i in range(n):
    lim=False
    for j in range(i+1,n):
        MIN=abs(l[i]-l[j])
        MAX=l[i]+l[j]
        min_idx=max(bisect_right(l,MIN),j+1)
        if not lim:
            max_idx=bisect_left(l,MAX)
            if max_idx==n:lim=True
        res=max_idx-min_idx
        if min_idx<=i<=max_idx:res-=1
        if min_idx<=j<=max_idx:res-=1
        cnt+=max(res,0)
print(cnt)