#selection sort
#at every iteration find min or max and place it correctly

def selection_sort(arr):
    '''
        At every iteration find min or max
        and place it correctly
    '''

    l = len(arr)

    for i in range(l):
        for j in range(i+1,l):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

        

arr = [3,4,1,-2,-9,1000]
selection_sort(arr)
print(arr)
