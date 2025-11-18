def kadane(A):
    max_sum = A[0]
    current_sum = A[0]
    i = 1
    while i < len(A):
        current_sum = max(A[i], current_sum + A[i])
        if current_sum > max_sum:
            max_sum = current_sum
        i = i + 1
    return max_sum

N = int(input())
A = list(map(int, input().split()))
print(kadane(A))
