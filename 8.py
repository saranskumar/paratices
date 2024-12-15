# Function to generate the Fibonacci sequence up to n terms
def fibonacci_sequence(n):
    # Create a list to store Fibonacci numbers
    fib_sequence = []
    
    # First two Fibonacci numbers
    a, b = 0, 1
    
    # Generate Fibonacci sequence
    for i in range(n):
        fib_sequence.append(a)
        a, b = b, a + b  # Update a and b for next Fibonacci numbers
    
    return fib_sequence

# Input: number of terms in Fibonacci sequence
n = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Get the Fibonacci sequence
fib_sequence = fibonacci_sequence(n)

# Print the Fibonacci sequence
print(f"Fibonacci sequence:{fib_sequence}")
 
