n=int(input())
k=int(input())

def k1(nn):
    ans=0
    for i in range(1,nn+1):
        if i<nn:
            ans+=9
        else:
            ans+=int(str(k)[0])
    return ans


def k2(nn):
    ans=0
    for i in range(2,nn+1):
        if i<nn:
            ans+=9**i
        else:
            tmp=int(str(n)[0])
            for j in range(1,len(str(n))):
                ans+=tmp*int(str(n)[j])

    return ans

if k==1:
    ans=k1(len(str(n)))

elif k==2:
    ans=k2(len(str(n)))
else:
    pass
print(ans)
