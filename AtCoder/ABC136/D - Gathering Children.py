
# 2019/09/12

s=list(input())
n=len(s)
res=[1]*n


def rle():
    RLE=[]
    l=0
    r=1
    while l<n:
        while r<n:
            if s[l]==s[r]:
                r+=1
            else:
                break
        RLE.append((s[l],r-l))
        l=r
        r+=1
    return RLE


RLE=rle()

ans=[]

for i in range(0,len(RLE),2):
    r=RLE[i][1]
    l=RLE[i+1][1]
    ans+=[0]*(r-1)

    a=r//2+(-(-l//2))   
    b=l//2+(-(-r//2))
    if (r+l)%2:
        a,b=b,a


    ans.append(a)
    ans.append(b)
    ans+=[0]*(l-1)
    
print(*ans)


# だめだったやつ
""" 
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
"""    