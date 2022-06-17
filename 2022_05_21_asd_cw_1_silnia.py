def silnia(n):
    if n > 1:
        return n * silnia(n - 1)
    else:
        return n


n = 5
print("n:", n)
print("!n:", silnia(n))
