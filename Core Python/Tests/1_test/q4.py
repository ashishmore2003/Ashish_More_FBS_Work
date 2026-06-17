### 4. Calculate the cost of painting the following building’s walls (both interior and exterior).
# You need to accept area (one wall) and cost of both interior and exterior wall.
#(Note: 1. Below diagram is of two joint rooms.
#       2. It is upper view of building.)

# Input area of one wall
area = float(input("Enter area of one wall: "))

# Input interior and exterior painting cost
interior_cost = float(input("Enter Interior cost per sq unit: "))
exterior_cost = float(input("Enter Exterior cost per sq unit: "))

# Calculate total interior cost
interior = area * 8 * interior_cost

# Calculate total exterior cost
exterior = area * 7 * exterior_cost

# Display result
print("Interior Painting Cost =", interior)
print("Exterior Painting Cost =", exterior)
print("Total Painting Cost =", interior + exterior)
