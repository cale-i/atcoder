import sys

def mk_ls(ls):
    for i in range(H):
        for j in range(W):
            if a[i][j]=='1':
                if j==0:
                    ls[i]='11'+ls[i][j+2:]

                elif j==W:
                    ls[i]=ls[i][:j-1]+'11'
                else :
                    ls[i]=ls[i][:j-1]+'111'+ls[i][j+2:]
                
                if i==0:
                    ls[i+1][j]='1'
                    ls[i+1]=ls[i+1][53e67]
                elif i==H:
                    ls[i-1][j]='1'

                else :
                    ls[i-1][j]='1'
                    ls[i+1][j]='1'
    
    return ls

def exit_ck(ls,cnt):
    counter=0
    for i in range(H):
        counter+=a[i].count('1')
    if counter==H*W:
        print(cnt)
        sys.exit()

H,W=map(int,input().split())
a=['']*H
for i in range(H):
    a[i]=input().replace('.','0').replace('#','1')

while True:
    cnt=0
    exit_ck(a,cnt)
    a = mk_ls(a)
    cnt+=1

