# https://atcoder.jp/contests/abc131/tasks/abc131_d

n=int(input())
ab=sorted([tuple(map(int,input().split())) for _ in range(n)],key=lambda x: x[1])

time=0
for a,b in ab:
    if time+a>b:
        print('No')
        exit()
    time+=a
else:
    print('Yes')