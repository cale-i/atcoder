n=int(input())

cnt=0
for i in range(1,(n+1)):
    if i%10==0:continue
    j=0
    a=b=str(i)

    if int(a)<10:
        a_f=a
        a_l=a
    else:
        a_f=a[0]
        a_l=a[-1]
    b_f=a_l
    b_l=a_f
    if a_f==a_l:
        b=a_f
    else:
        b=int(b_f+b_l)
    if len(str(b))==1:
        cnt+=1
        b=int(str(b)+str(b))
    
    while b<=n:
        if len(str(b))==2:
            cnt+=1
            j+=1
            b=int(b_f+'0'*j+b_l)
            continue

        elif len(str(n))>j+2:
            cnt+=10*j
            j+=1
            b=int(b_f+'0'*j+b_l)
            continue

        elif len(str(n))==j+2:
            cnt+=(n-b)//10+1
            j+=1
            b=int(b_f+'0'*j+b_l)
print(cnt)        