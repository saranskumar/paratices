def add(a, b):
     
    if b == 0:
        return a
    return add(a + 1, b - 1)
def pro(a, b): 
    if b == 0:
        return 0
    return a + pro(a, b - 1)
def gcd(a, b): 
    if b == 0:
        return a
    return gcd(b, a % b)
 
a = 5
b = 3
print("Addition:", add(a, b))  
 
print("Multiplication:", pro(a, b))  
 
print("GCD:", gcd(a, b))   
