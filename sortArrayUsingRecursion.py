#Sort Array Using Recursion
#We will be using Base Hypothesis Induction Method

def insert(arr,temp):
    if len(arr) == 0 or arr[-1] <= temp:
        arr.append(temp)
        return

    temp2 = arr.pop()
    insert(arr, temp)
    arr.append(temp2)

def sort(arr):
    if len(arr) <= 0:
        return

    temp = arr.pop()
    sort(arr)

    insert(arr,temp)

arr = [4,2,1,3,-1,-10,1000,2000,0,5,9,8,17,19,22,21,12]
sort(arr)
print(arr)

