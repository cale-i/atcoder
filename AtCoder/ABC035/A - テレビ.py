w,h=map(int,input().split())
if w%16==0 and h%9==0:ans='16:9'
else: ans='4:3'
print(ans)