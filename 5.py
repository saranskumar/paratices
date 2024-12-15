def long(strings: list):
    # Find the longest word
    longest_word = max(strings)
    
    # Replace the longest word with "found"
    index = strings.index(longest_word)
    strings[index] = "found"
    
    return strings

# Example usage
strings = ["apple", "banana", "grape", "watermelon", "kiwi"]
 
print(long(strings))
