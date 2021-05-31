def IsPrime(n):
    k = 2
    while n % k != 0 or k == n:
        if k > n ** 0.5:
            return "YES"
        k += 1
    return "NO"
print(IsPrime(int(input())))
