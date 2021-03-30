# https://atcoder.jp/contests/arc068/tasks/arc068_a

x = int(input())
d,m = divmod(x,11)
ans = d*2
ans += 1

if m > 6:
    ans += 1
elif m == 0:
    ans -= 1
print(ans)