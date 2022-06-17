n1, n2, n3 = 0, 1, 42
count = 0

while count <= n3:
    if count >= 40:
        print(count, ":", n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1


