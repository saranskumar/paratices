def newlist(L):
    for i in range(len(L)):
        if L[i] % 2 == 0:    
            L[i] = L[i] / 2   
        else:  
            L[i] = L[i] * 2   
    return L   
L = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))  
    L.append(element)
 
print(newlist(L))
