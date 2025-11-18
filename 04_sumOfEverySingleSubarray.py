def print_subarray_sums(A):
    N = len(A)
    i = 0
    while i < N:
        j = i
        total = 0
        while j < N:
            total = total + A[j]
            print(total)
            j = j + 1
        i = i + 1

N = int(input())
A = list(map(int, input().split()))
print_subarray_sums(A)
