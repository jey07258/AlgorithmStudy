S = list(input())
T = list(input())

for i in range(len(T)-1, len(S)-1, -1):
    if T[i] == 'A':
        T.pop()
    else:
        T.pop()
        T.reverse()

if S == T:
    print('1')
else:
    print('0')