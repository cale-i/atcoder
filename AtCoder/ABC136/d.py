s=list(input())
res=[0]*len(s)
cnt=0
a=0
b=0
for i in range(1,len(s)):
    if s[i]=='L':continue
    else:
        cnt+=1
        if s[i+1]=='L':
            if cnt%2:
                res[i]+=cnt//2
                res[i+1]+=cnt//2+1
            else:
                res[i+1]+=cnt//2+1
                res[i]+=cnt//2
            cnt=0
print(res)           
    