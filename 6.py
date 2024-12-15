
def tuple_input():
    L = []
    for i in range(int(input("Enter number of items in tuple: "))):
        L.append(int(input(f"Enter element no.{i + 1} :")))
    return tuple(L)

tuple =tuple_input()
print("The elements of the tuple are:")
for element in tuple:
    print(element)

# Display the maximum and minimum values of the tuple
print(f"Maximum value in the tuple: {max(tuple)}")
print(f"Minimum value in the tuple: {min(tuple)}")