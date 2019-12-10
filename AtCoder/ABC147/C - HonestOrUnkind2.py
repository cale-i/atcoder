# 2019/12/09

n=int(input())
xy=[]
for i in range(n):
    a=int(input())
    lst=['1']*n
    for j in range(a):
        x,y=input().split()
        lst[int(x)-1]=y
    lst=int(''.join(lst),2)
    xy.append(lst)

ans=0

def search(bit):
    BIT=bit+(2**n-1)-(len(bin(bit))-2)
    for idx in range(n):
        if bit&(1<<idx):
            for j in range(n):
                if (1<<j&BIT)&(1<<j&xy[idx]):
                    continue
                else:
                    return 0
    return BIT


for bit in range(1,2**n):
    ret=search(bit)
    if ret:
        ans=max(ans,bin(ret).count('1'))
print(ans)