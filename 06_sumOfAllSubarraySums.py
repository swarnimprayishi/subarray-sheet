def sum_of_all_subarray_sums(A):
    total = 0
    N = len(A)
    i = 0
    while i < N:
        contribution = A[i] * (i + 1) * (N - i)
        total = total + contribution
        i = i + 1
    return total

N = int(input())
A = list(map(int, input().split()))
print(sum_of_all_subarray_sums(A))
