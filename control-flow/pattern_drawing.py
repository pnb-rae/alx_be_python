# pattern_drawing.py

# Ask user for size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop for each row
while row < size:
    # Inner for loop to print stars in the row
    for col in range(size):
        print("*", end="")  # Print on the same line
    print()  # Move to next line after each row
    row += 1
