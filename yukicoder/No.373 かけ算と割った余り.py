# yukicoder No.373 かけ算と割った余り 2020/01/31

a,b,c,d=map(int,input().split())
a,b,c=a%d,b%d,c%d
ans=(a*b)%d*c%d
print(ans)