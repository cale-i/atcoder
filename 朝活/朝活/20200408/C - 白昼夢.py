# https://atcoder.jp/contests/abc049/tasks/arc065_a

s = list(input())
words = ['dream','dreamer','erase','eraser']

def check(w):
    return word in words

while s:
    word = ''.join([s.pop() for _ in range(5)][::-1])
    if check(word): continue
    
    for _ in range(2):
        word = s.pop() + word
        if check(word): break
    else:
        print('NO')
        exit()
print('YES')