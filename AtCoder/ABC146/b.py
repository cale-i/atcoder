# 2019/11/24

n=int(input())
s=input()
ans=[chr((ord(e)-65+n)%26+65) for e in s]
print(''.join(ans))    
