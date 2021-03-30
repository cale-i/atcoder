n=int(input())
s=list(input())+[None]
cnt=0
for i in range(n):
    if s[i]==s[i+1]:continue
    cnt+=1
print(cnt)