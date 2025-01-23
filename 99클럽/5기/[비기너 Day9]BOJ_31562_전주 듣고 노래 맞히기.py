N, M = map(int, input().split(' '))

name = []
melody = []

for _ in range(N):
    song = list(input().split(' '))
    name.append(song[1])
    melody.append(''.join(song[2:5]))

# 동일한 노래 -> 제목, 두 개 이상 -> ?, 없으면 !
for _ in range(M):
    q = ''.join(input().split(' '))
    a = melody.count(q)
    
    if a > 1:
        print("?")
    elif a == 1:
        print(name[melody.index(q)])
    else:
        print("!")