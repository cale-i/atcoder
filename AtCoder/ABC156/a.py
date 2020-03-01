n,r=map(int,input().split())

rate=r+(100*(10-n)) if n<10 else r
print(rate)