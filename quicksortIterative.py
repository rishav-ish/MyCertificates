#quick sort iterative approach
from collections import deque

def partition(arr, start, end):

    pivot = arr[end]
    pIndex = start

    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[pIndex] = arr[pIndex], arr[i]
            pIndex += 1

    arr[pIndex], arr[end] = arr[end], arr[pIndex]
    return pIndex


def quick_sort_iterative(arr, start, end):

    stack = deque()
    stack.append((start,end))

    while(stack):
        start, end = stack.pop()

        pIndex = partition(arr,start,end)
        
        if pIndex - 1 > start:
            stack.append((start,pIndex-1))

        if pIndex + 1 < end:
            stack.append((pIndex + 1, end))



arr = [2,3,1,4,-8]
quick_sort_iterative(arr,0,len(arr)-1)
print(arr)
