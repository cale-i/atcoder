# yukicoder No.785 色食い虫 2020/01/22

HEX=16
R=list(input().split(','))
G=list(input().split(','))
B=list(input().split(','))

r=pow(HEX-len(R) if R[0]!='NONE' else HEX, 2)
g=pow(HEX-len(G) if G[0]!='NONE' else HEX, 2)
b=pow(HEX-len(B) if B[0]!='NONE' else HEX, 2)

print(r*g*b)