# Create a 2D array (list of lists)
rows, cols = 3, 4
array_2d = [[0 for _ in range(cols)] for _ in range(rows)]

# Print the 2D array
for row in array_2d:
    print(row)

# Update an element in the 2D array
array_2d[1][2] = 5

# Print the updated 2D array
print("\nUpdated 2D array:")
for row in array_2d:
    print(row)