# ===============================================================

# Name: Tyler Jackson

# Date: 4/8/2024

# Course: CSC 120 NLE01

# Algorithm:Import the FootMeasure class from the foot_measure module.
# Create instances of FootMeasure with various initialization parameters:
# meas1 initialized with default values,
# meas2 initialized with feet only,
# meas3 initialized with feet and inches,
# meas4 initialized with inches only,
# meas5 initialized with a single argument (feet),
# meas6 initialized with both arguments (feet and inches).
# Print the measurement for each instance,
# Test addition by adding meas7 and meas8.
# Test relational operators:
# Check if meas7 is equal to meas8,
# Check if meas7 is not equal to meas8,
# Check if meas7 is less than meas8,
# Check if meas7 is less than or equal to meas8,
# Check if meas7 is greater than meas8,
# Check if meas7 is greater than or equal to meas8.


# References: in class

# ===============================================================
from foot_measure import FootMeasure

# Default initialization
meas1 = FootMeasure()
print("Default:", meas1)

# Initialization with feet only
meas2 = FootMeasure(feet=5)
print("Feet only:", meas2)

# Initialization with feet and inches
meas3 = FootMeasure(feet=5, inches=8)
print("Feet and inches:", meas3)

# Initialization with inches only
meas4 = FootMeasure(inches=58)
print("Inches only:", meas4)

# Initialization with single argument (feet)
meas5 = FootMeasure(6)
print("Single argument (feet):", meas5)

# Initialization with both arguments (feet and inches)
meas6 = FootMeasure(6, 3)
print("Both arguments (feet and inches):", meas6)

# Testing addition
print("\nTesting addition:")
meas7 = FootMeasure(5, 8)
meas8 = FootMeasure(2, 6)
print(f"{meas7} + {meas8} should be 8 ft. 2 in.: {meas7 + meas8}")

# Testing relational operators
print("\nTesting relational operators:")
print(f"{meas7} == {meas8}:", meas7 == meas8)
print(f"{meas7} != {meas8}:", meas7 != meas8)
print(f"{meas7} < {meas8}:", meas7 < meas8)
print(f"{meas7} <= {meas8}:", meas7 <= meas8)
print(f"{meas7} > {meas8}:", meas7 > meas8)
print(f"{meas7} >= {meas8}:", meas7 >= meas8)
