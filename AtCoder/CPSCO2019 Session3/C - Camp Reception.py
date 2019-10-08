# 2019/07/23
# 区間スケジューリング

n=int(input())
st=[(0,0)]*n
for i in range(n):
    st[i]=tuple(map(int,input().split()))

st.sort()

l=st[0][0]
r=st[0][1]
cnt=1
for i in range(n):
    s,t=st[i]
    if l<=s<=r:r=max(r,t)
    elif r<s:
        l=s
        r=t
        cnt+=1

print(cnt)

# 別解
# いもす法