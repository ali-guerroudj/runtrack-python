def print_custom_triangle(height):
    for i in range(height - 1):
        spaces = " " * (height - i - 1)
        if i == 0:
            print(spaces + " /\\")
        else:
            inner_spaces = " " * (2 * (i - 1))
            print(spaces + "/" + inner_spaces + "\\")

    bottom_line = "/" + "_" * (2 * (height - 1)) + "\\"
    print(bottom_line)

# Get the height as input from the user
try:
    triangle_height = int(input("Enter the height of the triangle: "))
    if triangle_height < 1:
        raise ValueError("Height must be a positive integer.")
    print_custom_triangle(triangle_height)
except ValueError as ve:
    print(f"Error: {ve}. Please enter a valid positive integer for the height.")






