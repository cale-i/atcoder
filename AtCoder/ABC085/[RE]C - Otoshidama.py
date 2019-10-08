# 2019/07/17

n,y=map(int,input().split())

def solve():

    for i in range((y//10000)+1):
        for j in range((y//5000)+1):
            k=(y-i*10000-j*5000)//1000
            if k<0:break
            if i+j+k==n:
                return [i,j,k]
                
    else:
        return [-1]*3


print(*solve())

        