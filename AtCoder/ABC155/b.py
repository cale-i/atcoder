n=int(input())
a=list(map(int,input().split()))

for e in a:
    if e%2:continue
    if e%3 and e%5:
        print('DENIED')
        exit()
else:
    print('APPROVED')