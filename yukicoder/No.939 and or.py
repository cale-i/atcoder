# 2020/01/02
# コーナーケース1 : any(論理積==1 and 論理和==0)
# コーナーケース2 : a==b

a,b=map(int,input().split())
if a&b!=a:
    print(0)
    exit()
bit=bin(a^b).count('1')
print(pow(2,max(bit-1,0)))