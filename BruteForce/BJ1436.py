N = int(input())
i = 666
count = 0
while True:
    if '666' in str(i):
        count = count+1
        if count==N:
            break
    i = i+1
print(i)