# 2019/07/14

n=int(input())
a=list(map(int,input().split()))
A=set(a[1:])
res=[-1]*n

dct={}
for e in a:
    dct[e]=dct.get(e,0)+1
tmp=a[0]
res[0]=tmp
dct[tmp]-=1

for i in range(1,n):
    tmp=res[0]^a[i]
    if  dct.get(tmp,0)>0:
        res[1]=a[i]
        res[-1]=res[0]^a[i]
        dct[res[1]]-=1
        dct[res[-1]]-=1
        break
else:
    print('No')
    exit()


for i in range(1,n-2):
    x=res[i]
    y=res[i-1]
    tmp=x^y
    if dct.get(tmp,0)>0:
        res[i+1]=tmp
        dct[tmp]-=1
    else:
        print('No')
        exit()

if res[-2]^res[-3]==res[-1]:
    print('Yes')
else:
    print('No')

# 2019/07/15
# ACするけど不正解のやつ

n=int(input())
a=list(map(int,input().split()))
ans=a[0]
for i in range(1,n):
    ans=ans^a[i]

print('No' if ans else 'Yes')