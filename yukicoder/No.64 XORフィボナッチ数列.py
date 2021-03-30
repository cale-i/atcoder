# yukicoder No.64 XORフィボナッチ数列 2020/03/03

*f,n=map(int,input().split())
f.append(f[0]^f[1])
print(f[n%3])