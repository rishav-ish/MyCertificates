#Reverse Stack using recursion

def insert(stack,temp):
    
    if not stack:
        stack.append(temp)
        return

    temp2 = stack.pop()
    insert(stack,temp)
    stack.append(temp2)

def reverse(stack):
    if not stack:
        return

    temp = stack.pop()
    reverse(stack)
    
    insert(stack,temp)




arr = [1,2,3,45,6,7,1]
reverse(arr)
print(arr)

