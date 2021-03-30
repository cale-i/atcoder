m,d=map(int,input().split())
if d<22 or m<4 :
    print(0)
    exit()

cnt=0

for i in range(4,m+1):
    for j in range(2,i+1):
        if i%j==0 and i%(i//j)==0 and i>1 and i//j>1:
            tmp=int(str(j)+str(i//j))
            if tmp<=d:
                cnt+=1
print(cnt)