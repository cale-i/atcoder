# yukicocer No.717 ファッションへのこだわり 2020/01/24

n,m=map(int,input().split())
s=list(input())
t=list(input())

ans=min(s.count('A'),t.count('A'))
ans+=min(s.count('B'),t.count('B'))
print(ans)