def subarray_sum(A, L, R):
    total = 0
    i = L - 1
    while i <= R - 1:
        total = total + A[i]
        i = i + 1
    return total

N = int(input())
A = list(map(int, input().split()))
L, R = map(int, input().split())
print(subarray_sum(A, L, R))
