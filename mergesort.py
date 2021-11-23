#merge sort

def merge_sort(arr):

    l = len(arr)

    if l < 2:
        return

    mid = l // 2

    left = arr[0:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(arr,left,right)

def merge(arr,left,right):
    nL = len(left)
    nR = len(right)

    i,j,k = 0,0,0

    while(i < nL and j < nR):
        if(left[i] <= right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    #left overs
    while(i < nL):
        arr[k] = left[i]
        k += 1
        i += 1

    while(j < nR):
        arr[k] = right[j]
        j += 1
        k += 1


arr = [4,32,1,-100,-56,32,12,4,-9000]
merge_sort(arr)
print(arr)
