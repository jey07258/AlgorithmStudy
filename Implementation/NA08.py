import sys

N = list(sys.stdin.readline().rstrip())

#리스트에서 특정 요소만 제거하고자 할때 -> 리스트 컴프리헨션 이용
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
alph = [i for i in N if i not in numbers]
num = [i for i in N if i in numbers]

alph.sort()
result = 0
for i in num:
    result += int(i)

print(''.join(alph)+str(result))