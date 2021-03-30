# 2019/07/26
# かんにんぐ

n=int(input())
s=list(input())
bk=0
wh=s.count('.')
cnt=wh
for i in range(n):
	if s[i]=='#':bk+=1
	else:wh-=1
	cnt=min(cnt,bk+wh)

print(cnt)