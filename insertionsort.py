#insertion sort

def insertion_sort(arr):

    l = len(arr)

    for i in range(1,l):
        hole = i
        value = arr[i]

        while(hole > 0 and arr[hole-1] > value):
            arr[hole] = arr[hole-1]
            hole -= 1

        arr[hole] = value


arr = [1,5,7,9,8]
insertion_sort(arr)
print(arr)

        
