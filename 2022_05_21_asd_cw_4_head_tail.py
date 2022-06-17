def head(arr):
    return arr[0]

def tail(arr):
    arr.pop(0)
    return arr

def isEmpty(arr):
    if not arr:
        return True
    else:
        return False

def reverse(arr):
    if not isEmpty(arr):
        h = head(arr)
        tail(arr)
        arr = reverse(arr)
        if arr == None:
            return h
        else:
            return arr, h

arr = list("kot")
print(arr)
print(reverse(arr))