 
def integerlist(List):
    
    newlist = []
    for value in List: 
        if isinstance(value, int):
            newlist.append(value)
    
    return newlist
def find_mode(lst):
    max_count = 0   
    mode = None    
    for i in range(len(lst)):  
        count = 0
        for j in range(len(lst)):  
            if lst[i] == lst[j]:   
                count += 1
        if count > max_count:  
            max_count = count
            mode = lst[i]

    return mode

List = [25, 30, '32', 'N/A', 40, '50', 30, 25, 'abc', 35, 40, 25]
 
newlist = integerlist(List)
 
print("Filtered list (only integers):", newlist)
print(f"Yound{min(newlist)} And oldest {max(newlist)} and average{sum(newlist)/len(newlist)} and commom age is{find_mode(newlist)}")
