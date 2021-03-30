# 2019/12/27
# atcoderだとRE

import numpy as np

M=5
n=int(input())
dp_r=[0]*(n+1)
dp_b=[0]*(n+1)
dp_w=[0]*(n+1)

s=np.array([list(input()) for _ in range(5)])

r=M-(np.count_nonzero(s=='R',axis=0))
b=M-(np.count_nonzero(s=='B',axis=0))
w=M-(np.count_nonzero(s=='W',axis=0))

for i in range(1,n+1):
    dp_r[i]=min(dp_b[i-1],dp_w[i-1])+(r[i-1])
    dp_b[i]=min(dp_r[i-1],dp_w[i-1])+(b[i-1])
    dp_w[i]=min(dp_r[i-1],dp_b[i-1])+(w[i-1])

print(min(dp_r[-1],dp_b[-1],dp_w[-1]))