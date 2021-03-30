# 2020/01/07
# 解説カンニング
# 数字根の性質を利用する
#  n==0のとき => 0
#  n%9==0のとき => 9
#  else => n%9

n=int(input())
p=list(map(int,input().split()))

cnt=1
for e in p:
    tmp=e%9
    if tmp:
        cnt*=tmp
    else:
        if e:
            cnt*=9
        else:
            print(0)
            exit()
ans=cnt%9 if cnt%9 else 9

print(ans)