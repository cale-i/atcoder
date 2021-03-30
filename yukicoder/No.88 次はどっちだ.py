# yukicoder No.88 次はどっちだ 2020/03/02

s=input()
fst=s
snd='yukiko' if s=='oda' else 'oda'

cnt=0
for _ in range(8):
    b=input()
    cnt+=len(b)-b.count('.')
print(snd if cnt%2 else fst)