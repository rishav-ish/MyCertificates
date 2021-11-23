#Delete middle in stack using recursion

#middle is defined as
#middle = size/2 + 1


def middleStack(stack,size):
    if size == 1:
        stack.pop()
        return

    temp = stack.pop()
    middleStack(stack,size-1)
    stack.append(temp)
    

arr = [1,2]
middleStack(arr,len(arr)//2 + 1)
print(arr)
print("hello")