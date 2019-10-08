# 2019/08/10

n,m=map(int,input().split())
x=sorted(list(map(int,input().split())))

diff=[]
for i in range(m-1):
    diff.append(abs(x[i]-x[i+1]))

diff.sort(reverse=True)
print(sum(diff[n-1:]))
