def if_heap(K):
    length = len(K)

    result = True

    for i in range (0,length):
        left = i * 2 + 1
        right = left + 1

        if left < length and K[left] > K[i]:
            result = False
        elif right < length and K[right] > K[i]:
            result = False

    return result

# arr = [12,6,33,4,6,11]
# arr = [33,6,12,4,6,11]
# arr = [7,2,1,4,9,8,7,4]
# arr = [50,9,8,7,2,1,7,4,4]
arr = [50,9,8,7,2,1,7,4,8]
# arr = [50,9,8,7,2,1,7,4,4,2]


print("Tablica:")
print(arr)
print("\n* * *\n")

# print(max_heapify(arr, 0))

# for i in range (0,len(arr)-1):
#     if_arr_heap = if_heap(arr,i)
#     if not if_arr_heap:
#         break

print(if_heap(arr))

