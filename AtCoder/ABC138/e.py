from bisect import bisect_right

s=input()
t=input()

arr=[[] for _ in range(26)]

for idx,e in enumerate(s):
    arr[ord(e)-97].append(idx)

for i in range(26):
    if arr[i]==[]:continue
    arr[i].sort()
print(arr)

cnt=[]

pre=0
for e in t:
    e=ord(e)-97
    if arr[e] is None:
        print(-1)
        exit()
    idx=bisect_right(arr[e],pre)
    pre=arr[e][idx]
    cnt.append(pre)
print(*cnt)