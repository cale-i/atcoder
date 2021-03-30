# yukicoder No.395 永遠の17歳 2020/01/31

a=int(input())
div=a-7
print(div if divmod(a,div)==(1,7) else -1)