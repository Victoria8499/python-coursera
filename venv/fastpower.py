def power(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    if n % 2 == 0:
        return power(a ** 2, n / 2)
    return power(a, n - 1) * power(a, 1)

a = float(input())
n = int(input())
print(power(a, n))
