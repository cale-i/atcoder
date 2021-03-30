# yukicoder No.201 yukicoderじゃんけん 2020/02/03

sa,pa,xa=input().split()
sb,pb,xb=input().split()
pa,pb=int(pa),int(pb)

if pa==pb:
    print(-1)
else:
    print(sa if pa>pb else sb)