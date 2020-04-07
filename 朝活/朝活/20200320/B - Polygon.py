# https://atcoder.jp/contests/abc117/tasks/abc117_b

n=int(input())
l=list(map(int,input().split()))
mx=max(l)
sum_l=sum(l)-mx
print('Yes' if mx<sum_l else 'No')