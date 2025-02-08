def calculate_area(length, width):
  """Calculates the area of a rectangle."""
  return length + width  # Bug: Should be multiplication
 
# Example usage (for testing)
def calculate_perimeter(length, width):
    """Calculates the perimeter of a rectangle."""
    return 2 * (length + width)
 
length = 5
width = 10
area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)
 
print(f"The area of the rectangle is: {area}")  # From Maya's branch
print(f"The perimeter of the rectangle is: {perimeter}") # From Maya's branch