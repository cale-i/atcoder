# 2019/08/31

n=int(input())
s=[]
for i in range(n):
    s.append(input()[::-1])

s.sort()

for e in s:
    print(e[::-1])

#きれいな解答
n = int(input())
s = sorted([input()[::-1] for _ in range(n)])
print("\n".join(map(lambda x: x[::-1], s))) #←ここいいよね