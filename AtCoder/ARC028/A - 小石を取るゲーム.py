# 2019/11/4

n,a,b=map(int,input().split())
turn=1
while True:
    if turn:n-=a
    else:n-=b
    if n<1:break
    turn=1-turn
print('Ant' if turn else 'Bug')