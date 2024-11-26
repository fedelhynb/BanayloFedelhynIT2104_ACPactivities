# Ask the user to input the size of the array
size = int(input("Enter the size of the array: "))

# Create an array of the specified size with default values of 0.0
arr = [0.0] * size

# Prompt for the elements of the array
print("Enter the element of the array:")
for i in range(size):
    arr[i] = int(input())  # Use int since the example expects integers

# Ask for an index to access
try:
    x = int(input("Enter the index of the element to print: "))
    
    # Attempt to access the element at index x and print it
    print(f"Element at index {x}: {arr[x]:.2f}")
except IndexError:
    print(f"Index {x} is invalid.")
