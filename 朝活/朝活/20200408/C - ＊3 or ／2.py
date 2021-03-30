# https://atcoder.jp/contests/abc100/tasks/abc100_c

n = int(input())
a = list(map(int,input().split()))
cnt = 0
for e in a:
    tmp = e
    while tmp % 2 == 0:
        tmp //= 2
        cnt += 1
print(cnt)