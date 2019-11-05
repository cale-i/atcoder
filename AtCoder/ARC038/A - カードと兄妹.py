# 2019/11/6

input()
print(sum([e for i,e in enumerate(sorted(map(int,input().split()))[::-1]) if i%2==0]))