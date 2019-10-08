n=int(input())
h=list(map(int,input().split()))
h[0]-=1
for i in range(1,n-1):
    if h[i-1]<h[i]:
        h[i]-=1
    if h[i]>h[i+1]:
        print('No')    
        exit()
else:
    print('Yes')