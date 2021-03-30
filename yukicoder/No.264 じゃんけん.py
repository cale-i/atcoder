# 2019/12/28

n,k=map(int,input().split())
result=['Drew','Lost','Won']
print(result[(n-k+3)%3])