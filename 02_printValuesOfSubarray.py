def print_subarrays(A):
    N = len(A)
    i = 0
    while i < N:
        j = i
        while j < N:
            k = i
            while k <= j:
                print(A[k], end=" ")
                k = k + 1
            print()
            j = j + 1
        i = i + 1

N = int(input())
A = list(map(int, input().split()))
print_subarrays(A)
