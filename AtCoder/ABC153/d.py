h=int(input())
i=0
cnt=0
while h:
    cnt+=2**i
    h//=2
    i+=1
print(cnt)