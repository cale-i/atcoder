n=int(input())
s=input()

nn=n//2
ans=0


def solve(nn):
    r=nn
    for l in range(n+1-(nn*2)):
        a=s[l:r]
        b=s[r:]
        if a in b:
            print(nn)
            exit()
        r+=1
    return 0



while nn:

    solve(nn)
    nn-=1

print(ans)
