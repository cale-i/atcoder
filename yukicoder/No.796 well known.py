# yukicoder No.796 well known 2020/01/22

n=int(input())
ans=[3]+[1]*(n-2)
_sum=sum(ans)
rest=4-_sum%3
ans.append(rest)
print(*ans)