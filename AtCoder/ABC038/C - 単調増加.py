# 2019/06/19
# 尺取法 しゃくとり法

n=int(input())
a=list(map(int,input().split()))

r,res=0,0

for l in range(n):
	if l==r:r+=1
	while r<n and a[r-1]<a[r]:
		r+=1
	res+=r-l
	if r==l:r+=1
print(res)