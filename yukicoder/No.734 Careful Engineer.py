# yukicoder No.734 Careful Engineer 2020/01/24

a,b,c=map(int,input().split())
x=-(-(3600*c)//(60*a-b))
print(x if x>0 else -1)