#bubble sort
def bubble_sort(arr):

    len_arr = len(arr)

    for i in range(len_arr-1):
        for j in range(len_arr-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]



arr = [4, 3, 3, -1, 1000]

bubble_sort(arr)

print(arr)


            
