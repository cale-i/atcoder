n=int(input())
v=list(map(int,input().split()))

v.sort(reverse=True)

while len(v)!=1:
    tmp=(v.pop()+v.pop())/2
    v.append(tmp)
print(*v)