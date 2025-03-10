def ulam_spiral_coordinates(n):
    """
    Calculates the x, y coordinates for numbers up to n in the Ulam spiral.

    Args:
        n: The upper limit of numbers to generate coordinates for.

    Returns:
        A dictionary where keys are numbers and values are (x, y) tuples.
    """
    coordinates = {1: (0, 0)}
    x, y = 0, 0
    dx, dy = 1, 0
    for i in range(2, n + 1):
        x += dx
        y += dy
        coordinates[i] = (x, y)
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
    return coordinates

# Example usage:
n = 120  # Calculate coordinates up to 25
spiral_coords = ulam_spiral_coordinates(n)
for num, coord in spiral_coords.items():
    print(f"Number: {num}, Coordinates: {coord}")