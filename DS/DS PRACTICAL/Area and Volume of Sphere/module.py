import math

# Function to calculate area and volume of sphere
def sphere_properties(diameter):
    radius = diameter / 2
    area = 4 * math.pi * radius ** 2
    volume = (4/3) * math.pi * radius ** 3
    return area, volume

# Diameter of the sphere
diameter = 12

# Calculate area and volume using the function
area, volume = sphere_properties(diameter)

# Print the results
print("Area of the sphere:", area)
print("Volume of the sphere:", volume)