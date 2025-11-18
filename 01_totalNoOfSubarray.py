def total_subarrays(N):
    return N * (N + 1) // 2

N = int(input())
print(total_subarrays(N))
