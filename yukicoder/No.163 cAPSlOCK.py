# 2019/12/28

s=input()
ans=[]
for i in s:
    if ord(i) in range(ord('A'),ord('Z')+1):
        tmp=chr(ord(i)+32)
    else:tmp=chr(ord(i)-32)
    ans.append(tmp)
print(*ans,sep='')

