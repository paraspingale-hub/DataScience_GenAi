x, y, z = 11, 10, 21

# Simple math
sqtr = lambda x: x**2
print(f"Square of {x}:", sqtr(x))

cube = lambda x: x**3
print(f"Cube of {x}:", cube(x))

# Comparison (Renamed to avoid overwriting built-ins)
find_max = lambda x, y: max(x, y)
print(f"Max of {x}, {y}:", find_max(x, y))

find_min = lambda x, y: min(x, y)
print(f"Min of {x}, {y}:", find_min(x, y))

# Boolean checks
even = lambda x: x % 2 == 0
print(f"Is {x} even?", even(x))

odd = lambda x: x % 2 != 0
print(f"Is {x} odd?", odd(x))

div5 = lambda x: x % 5 == 0
print(f"Is {x} div by 5?", div5(x))

# Arithmetic
add = lambda x, y: x + y
print(f"Sum of {x}, {y}:", add(x, y))

mul = lambda x, y: x * y
print(f"Product of {x}, {y}:", mul(x, y))

# Three arguments
max3 = lambda x, y, z: max(x, y, z)
print(f"Max of {x}, {y}, {z}:", max3(x, y, z))
