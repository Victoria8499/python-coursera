n = int(input())
m = int(input())


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def ReduceFraction(n, m):
    p = n / gcd(n, m)
    q = m / gcd(n, m)
    return int(p), int(q)


print(*ReduceFraction(n, m))
