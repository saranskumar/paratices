def remove(L, value): 
    while value in L:
        L.remove(value)   
    return L
 
L = [1, 2, 3, 4, 2, 5, 2]
value = 2
print(remove(L, value))   