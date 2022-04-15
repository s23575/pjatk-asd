def heapify(kopiec, i):
    lewy = 2 * i + 1
    prawy = 2 * i + 2
    dl = len(kopiec)
    najw = i;
    if lewy < dl and kopiec[lewy] > kopiec[i]:
        najw = lewy
    if prawy < dl and kopiec[prawy] > kopiec[najw]:
        najw = prawy
    if najw != i:
        kopiec[najw], kopiec[i] = kopiec[i], kopiec[najw]
        przywracanie(kopiec, najw)
    return kopiec

arr = [4,1,3,2,16,9,10,14,8,7]
print("Tablica:")
print(arr)
print("\n* * *\n")

kopiec = arr
for i in range (2,len(kopiec)):
    kopiec = przywracanie(kopiec, i)

print(kopiec)

