# 1
# 2019/05/26

s=input()
if s=='a':
	print(-1)
	exit()
elif s[:2]=='aa':
	print('a')
else:print(chr(ord(s[0])-1))

# 2
# 2019/05/26

s=input()
if s=='a':
	print(-1)
else:print('a')

# 3
# 2019/05/26

print(-1 if input()=='a' else 'a')