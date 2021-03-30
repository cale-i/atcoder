n=int(input())
d=sorted(map(int,input().split()))

mid=n//2

print(d[mid]-d[mid-1])