import sys

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        return None

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    N_list = list(map(int, sys.stdin.readline().split()))
    N_list.sort()

    M = int(sys.stdin.readline())
    M_list = list(map(int, sys.stdin.readline().split()))

    for i in M_list:
        result = binary_search(N_list, i, 0, N-1)
        if result != None:
            print("yes",end=' ')
        else:
            print("no", end=' ')