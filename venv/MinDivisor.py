def MinDivisor(n):
    k = 2
    while n % k != 0:
        if k > n ** 0.5:
            return n
        k += 1
    return k
n = int(input())
print(MinDivisor(n))
