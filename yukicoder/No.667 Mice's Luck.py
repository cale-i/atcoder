# yukicoder No.667 Mice's Luck 2020/01/25

s=input()
n=len(s)
safe=s.count('o')
trap=n-safe
for i in range(n):
    print(100*(safe/n))
    if s[i]=='o':
        safe-=1
    else:
        trap-=1
    n-=1