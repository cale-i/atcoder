# yukicoder No.722 100×100=1000 2020/01/24

A,B=map(int,input().split())

def chk(a,b):
    a=list(str(abs(a)))
    b=list(str(abs(b)))
    for x in [a,b]:
        cnt=0
        while x:
            tmp=x.pop()
            if int(tmp):
                x.append(tmp)
                break
            cnt+=1
        
        len_x=len(x)
        
        if cnt<2 or len_x>1:
            return False
    else:
        return True

ret=chk(A,B)
if ret:
    print(A*B//10)
    exit()

ans=A*B
MIN=-99999999
MAX=99999999
print(ans if MIN<=ans<=MAX else 'E')