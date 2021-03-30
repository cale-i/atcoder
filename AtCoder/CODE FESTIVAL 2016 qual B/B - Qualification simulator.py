# 2019/12/09

n,a,b=map(int,input().split())
s=input()

cnt=0
cnt_b=0
for i in range(n):
    if cnt>=(a+b):
        print('No')
        continue
    else:
        if s[i]=='c' or cnt>a+b:
            print('No')
            continue
        else:
            if s[i]=='b':
                cnt_b+=1
                if cnt_b>b:
                    print('No')
                    continue
                else:
                    print('Yes')
                    cnt+=1
            else:
                print('Yes')
                cnt+=1