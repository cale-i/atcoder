# 2019/10/18

s=input()
a,b,c,d=map(int,input().split())
b+=1;c+=2;d+=3
n=len(s)
ans=[]
cnt=0
for i in range(n+4):
    if i in (a,b,c,d):
        ans.append('"')
        cnt+=1
    else:
        ans.append(s[i-cnt])    
print(''.join(ans))