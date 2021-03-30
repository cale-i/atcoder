# 2019/10/14
import sys
input=sys.stdin.readline

n=int(input())
cnt=0
b_a=0
a=0
b=0
for i in range(n):
    s=input().rstrip('\n')
    cnt+=s.count('AB')
    is_b=s[0]=='B'
    is_a=s[-1]=='A'
    if is_b or is_a:
        if is_b and is_a:b_a+=1
        elif is_b:b+=1
        else:a+=1
    


if b_a:
    cnt+=b_a-1
    if a==b and a>0:
        a-=1;b-=1
        cnt+=2
    else:
        if abs(a-b)>0:
            cnt+=1
cnt+=min(a,b)

print(cnt)