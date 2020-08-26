"""


"""


def merge(arr1,arr2,arr):
    i = 0
    j =0
    k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            k = k + 1
        else:
            arr.append(arr2[j])
            k = k + 1
    if i == len(arr1):
        arr.append(arr1[i])
        k = k + 1
    else:
        arr.append(arr2[i])
        k = k + 1
    print(arr)

def mergesort(arr):
    l = 0
    h = len(arr)
    mid = int((l + h)/2)
    arr1 = []
    arr2 = []
    if h > 1:
        arr1.extend(arr[l:mid])
        arr2.extend(arr[mid:h])
        mergesort(arr1)
        mergesort(arr2)
        merge(arr1,arr2,arr)




# if __name__ ==  '__main__':
arr = [5, 2, 6, 1]
mergesort(arr)
# print(arr)