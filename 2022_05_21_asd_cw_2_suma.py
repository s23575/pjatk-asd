def suma(n):
    if n > 1:
        if n % 3 == 0:
            return n + suma(n - 1)
        else:
            return suma(n - 1)
    else:
        return 0


n = 12
print("n:", n)
print("Suma elementów podzielnych przez 3 z liczb od 1 do n:", suma(n))
