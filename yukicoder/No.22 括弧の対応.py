# yukicoder No.22 括弧の対応 2020/03/06

n,k=map(int,input().split())
s=input()

def search(bracket):
    idx=0
    cnt=0
    flag = False
    if bracket=='(':
        for i in range(n):
            if i==k-1:
                idx=cnt
                flag = True

            if s[i]==bracket: cnt+=1
            else: cnt-=1

            if flag and idx==cnt:            
                return i+1
            
    else:
        for i in reversed(range(n)):
            if i==k-1:
                idx=cnt
                flag = True

            if s[i]==bracket: cnt+=1
            else: cnt-=1

            if flag and idx==cnt:            
                return i+1

    return ret

ret=search(s[k-1])
print(ret)