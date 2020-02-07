# yukicoder No.159 刺さらないUSB 2020/02/07

p,q=map(float,input().split())
p1=(1-p)*q
p2=p*(1-q)*q
print('YES' if p1<p2 else 'NO')