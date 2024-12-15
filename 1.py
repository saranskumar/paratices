def rotate(L, k):
    for i in range(k):
        L.insert(0, L[-1])  # Insert the last element at the front
        L.pop()             # Remove the last element
    return L

L = [1, 2, 3, 4, 5]
k = 5
print(rotate(L, k))  # Output: [4, 5, 1, 2, 3]

