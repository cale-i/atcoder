s=list(input())
odd=['R','U','D']
even=['L','U','D']

for i in range(len(s)):
    if (i+1)%2:
        if s[i] not in odd:
            print('No')
            exit()
    else:
        if s[i] not in even:
            print('No')
            exit()
print('Yes')