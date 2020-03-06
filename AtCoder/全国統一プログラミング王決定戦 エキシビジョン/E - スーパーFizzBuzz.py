# atcoder E - スーパーFizzBuzz 2020/03/06

n=int(input())
for i in range(1,n+1):
    tmp=''
    if i%2==0:tmp+='a'
    if i%3==0:tmp+='b'
    if i%4==0:tmp+='c'
    if i%5==0:tmp+='d'
    if i%6==0:tmp+='e'
    if tmp=='':tmp=i
    print(tmp)