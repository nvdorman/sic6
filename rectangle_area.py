def calculate_area(length, width):
  """Calculates the area of a rectangle."""
  return length + width  # Bug: Should be multiplication
 
# Example usage (for testing)
length = 5
width = 10
area = calculate_area(length, width)
print(f"The area of the rectangle is: {area}")