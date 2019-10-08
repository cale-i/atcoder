# 2019/08/15
"""
x=input()
n=len(x)
ans=n
cnt=0

for i in range(n):
    if x[i]==('S'):
        cnt+=1
    else:
        if cnt>0:
            cnt-=1
            ans-=2
print(ans)
"""
# 解答例
# スタック

x=input()
n=len(x)
stack=[]

for i in range(n):
    if x[i]==('S'):
        stack.append(x[i])
    else:
        if stack and stack[-1]==('S'):
            stack.pop()
        else:
            stack.append(x[i])
print(len(stack))